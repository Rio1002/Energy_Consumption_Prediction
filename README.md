<h1 align="center">⚡️ Energy Consumption Prediction</h1>
<p align="center">
  <img src="https://github.com/Rio1002/Energy_Consumption_Prediction/blob/main/static/banner.png?raw=true" alt="Banner" width="100%"/>
</p>

<p align="center">
  <b>Smarter Energy, Greener Future</b><br/>
  Predict and analyze energy usage using machine learning, visualization, and real-time web deployment.
</p>

---

## ✨ Project Highlights

- 🔍 In-depth **EDA** on household energy patterns  
- 🤖 ML-based prediction (Random Forest, Linear Regression)  
- 🌐 Deployed with a **Flask web app**  
- 📊 **Power BI** dashboard for business insights  
- 🧠 Model saved using `joblib` for real-time prediction

---

## 🧰 Tech Stack

| Area              | Tools & Libraries                                                |
|-------------------|------------------------------------------------------------------|
| Programming       | ![Python](https://img.shields.io/badge/Python-3.8-blue?logo=python) |
| Web Development   | ![Flask](https://img.shields.io/badge/Flask-Web_App-lightgrey?logo=flask) |
| ML & Data Science | ![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikit-learn) ![Pandas](https://img.shields.io/badge/Pandas-Data-yellowgreen?logo=pandas) |
| Visualization     | ![Matplotlib](https://img.shields.io/badge/Matplotlib-Graphs-blueviolet?logo=matplotlib) ![PowerBI](https://img.shields.io/badge/PowerBI-Insights-yellow?logo=powerbi) |

---

## 📁 Folder Structure

```bash
Energy_Consumption_prediction/
├── app.py                    # Flask web application
├── requirements.txt          # Dependencies
├── Data Insights.pbix        # Power BI Dashboard
├── data/
│   └── house_energy_consumption.csv
├── joblib/
│   └── model.joblib          # Trained ML model
├── notebooks/
│   ├── eda.ipynb             # Exploratory Data Analysis
│   └── model.ipynb           # Model training and evaluation
├── templates/
│   ├── index.html            # Main form
│   ├── response.html         # Prediction result
│   ├── about.html
│   └── contact.html
```

---

## 🚀 Getting Started

> Follow these steps to get the project up and running locally.

### 1. 🔽 Clone the Repository

```bash
git clone https://github.com/Rio1002/Energy_Consumption_Prediction.git
cd Energy_Consumption_Prediction
```

### 2. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. ▶️ Run the Flask App

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser to test the prediction app.

---

## 📈 Model Performance

## 📈 Updated Model Performance

| Model                      | R² Score | RMSE     | MAE      |
|---------------------------|----------|----------|----------|
| Linear Regression         | 0.951893 | 0.088766 | 0.237367 |
| Gradient Boosting         | 0.945040 | 0.101410 | 0.252460 |
| Random Forest             | 0.936746 | 0.116714 | 0.270190 |
| XGBoost                   | 0.933014 | 0.123600 | 0.280856 |
| Support Vector Regressor | 0.932147 | 0.125199 | 0.278390 |
| Decision Tree             | 0.853033 | 0.271178 | 0.409091 |
| KNN Regressor             | 0.188651 | 1.497070 | 0.981463 |

> 📌 Detailed training code available in [`notebooks/model.ipynb`](notebooks/model.ipynb)

---

## 🧪 Demo Snapshot

| Input Form                            | Prediction Output                      |
|--------------------------------------|----------------------------------------|
| ![form](https://github.com/Rio1002/Energy_Consumption_Prediction/blob/main/input1.png) | ![output](https://github.com/Rio1002/Energy_Consumption_Prediction/blob/main/output.png) |

---

## 📊 Power BI Dashboard

The file `Data Insights.pbix` provides an interactive energy dashboard built with Power BI:

- Time-based consumption patterns  
- Comparative regional usage  
- Predictive insights and visual KPIs  V

> 🔸 Open with **Power BI Desktop** to explore

---

## 🤝 Contributing

We welcome contributions of all kinds!

```bash
# Fork, clone, and contribute!
git checkout -b feature/YourFeature
git commit -m "Add your feature"
git push origin feature/YourFeature
```

Submit a Pull Request and let’s build smarter energy systems together.

---

## 🙋‍♂️ Author

Made with ❤️ by **[Rio1002](https://github.com/Rio1002)**

---

## 📬 Contact & Feedback

Feel free to reach out via [GitHub](https://github.com/Rio1002)  
Have suggestions? Open an issue or submit a PR!

---

<p align="center"><i>"Powering tomorrow with data-driven energy insights."</i></p>
