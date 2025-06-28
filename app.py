from flask import Flask, render_template, request,redirect, url_for
from joblib import load
from flask_mysqldb import MySQL
import pandas as pd 

app = Flask(__name__)
mysql=MySQL(app)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='YOUR_PASSWORD'
app.config['MYSQL_DB']='YOUR_DB'

model = load(r"D:\ITVedant\ML\Energy_Consumption_prediction\joblib\model.joblib")

@app.route("/",methods=['GET','POST'])
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact",methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']
        subject=request.form['Subject']
        message=request.form['message']
        cur=mysql.connection.cursor()
        cur.execute("insert into response(name,email,subject,message) values(%s,%s,%s,%s)",(name,email,subject,message))
        mysql.connection.commit()
        cur.close()
        return render_template("response.html")
    return render_template("contact.html")

@app.route("/response",methods=["POST"])
def response():
    return render_template("response.html")

@app.route("/home", methods=["GET", "POST"])
def predict_energy():
    prediction = None
    breakdown = None  # NEW: to hold breakdown percentages
    threshold = 6.0  # kWh
    percentage_increase = None
    if request.method == "POST":
        try:
            # Extract form values
            house_age = float(request.form.get("house_age", 0))
            num_occupants = int(request.form.get("num_occupants", 0))
            temperature = float(request.form.get("temperature", 0))
            humidity = float(request.form.get("humidity", 0))
            day_of_week = int(request.form.get("day_of_week", 0))
            is_holiday = int(request.form.get("is_holiday", 0))
            window_open = int(request.form.get("window_open", 0))
            hour = int(request.form.get("hour", 0))
            appliance_usage = float(request.form.get("appliance_usage", 0))
            ac_usage = float(request.form.get("ac_usage", 0))
            heater_usage = float(request.form.get("heater_usage", 0))

            # Prepare input for prediction
            feature_names = [
            "House_Age", "Number_of_Occupants", "Temperature", "Humidity",
            "Day_of_Week", "Is_Holiday", "Window_Open", "Hour_of_Day",
            "Appliance_Usage", "AC_Usage", "Heater_Usage"
            ]
            
            features = pd.DataFrame([[  # 2D list for one sample
                house_age,
                num_occupants,
                temperature,
                humidity,
                day_of_week,
                is_holiday,
                window_open,
                hour,
                appliance_usage,
                ac_usage,
                heater_usage
            ]], columns=feature_names)

            prediction = round(float(model.predict(features)[0]), 2)

            # --- Calculate breakdown (percentage-based) ---
            total_usage = appliance_usage + ac_usage + heater_usage
            if total_usage > 0:
                appliance_pct = round((appliance_usage / total_usage) * 100, 1)
                ac_pct = round((ac_usage / total_usage) * 100, 1)
                heater_pct = round((heater_usage / total_usage) * 100, 1)
                other_pct = round(100 - (appliance_pct + ac_pct + heater_pct), 1)  # To sum to 100
            else:
                appliance_pct = ac_pct = heater_pct = other_pct = 0

            breakdown = {
                "appliance_pct": appliance_pct,
                "ac_pct": ac_pct,
                "heater_pct": heater_pct,
                "other_pct": other_pct,
            }

        except Exception as e:
            prediction = f"Error: {e}"
        
        if prediction > threshold:
            percentage_increase = round(((prediction - threshold) / threshold) * 100, 2)

    return render_template("index.html", prediction=prediction, breakdown=breakdown,percentage_increase=percentage_increase)

if __name__ == "__main__":
    app.run(debug=True)
