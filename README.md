# 🌍 Air Quality Prediction System

> **👨‍💻 Developed by Pratik**

---

## 📌 Overview

**Air Quality Prediction System** is a Machine Learning-based project that predicts the **Air Quality Index (AQI)** using environmental parameters such as temperature, humidity, pressure, and wind conditions.

This project helps in understanding pollution trends and enables early forecasting for better environmental awareness and decision-making.

---

## 🎯 Objective

- Predict AQI using historical environmental data
- Apply Machine Learning models for accurate forecasting
- Build a user-friendly interface using **Flask**
- Provide real-time AQI prediction based on user input

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| 📊 Data Preprocessing | Feature engineering on raw environmental data |
| 🤖 Multiple ML Models | Linear Regression, Random Forest, and more |
| 🌐 Web Interface | User-friendly interface built with Flask |
| 📈 Visualization | AQI trend charts and graphs |
| ⚡ Real-time Prediction | Instant AQI prediction from user inputs |

---

## 🧠 Machine Learning Models Used

| Model | Type |
|-------|------|
| Linear Regression | Regression |
| Decision Tree | Tree-based |
| Random Forest | Ensemble |
| Ridge Regression | Regularized |
| Lasso Regression | Regularized |
| KNN | Instance-based |
| XGBoost | Gradient Boosting |

---

## 🛠️ Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)

- **Python** — Core programming language
- **Pandas & NumPy** — Data manipulation and numerical computing
- **Scikit-learn** — Machine learning model training & evaluation
- **Flask** — Web application framework
- **Matplotlib / Visualization Libraries** — Data visualization

---

## 📂 Project Structure

```
Air-Quality-Prediction/
│
├── app.py                              # Flask web application
├── train_model.py                      # Model training script
├── requirements.txt                    # Python dependencies
├── templates/                          # HTML templates
├── static/                             # CSS, JS, images
├── Data/                               # Dataset files
├── *.ipynb                             # Jupyter Notebooks (model training)
└── random_forest_regression_model.pkl  # Saved ML model
```

---

## ⚙️ Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/gpratik143/Air-Quality-Prediction-System-Project.git
cd Air-Quality-Prediction
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

```bash
python app.py
```

> The application will start on `http://localhost:5000` by default.

---

## 📊 Input Parameters

| Parameter | Description |
|-----------|-------------|
| 🌡️ Average Temperature | Mean daily temperature |
| 🔺 Max Temperature | Maximum recorded temperature |
| 🔻 Min Temperature | Minimum recorded temperature |
| 🔵 Pressure | Atmospheric pressure |
| 💧 Humidity | Relative humidity percentage |
| 👁️ Visibility | Atmospheric visibility |
| 💨 Wind Speed | Average wind speed |
| 🌬️ Max Wind Speed | Maximum recorded wind speed |

---

## 📈 Output

```
✅ Predicted Air Quality Index (AQI)
```

The model returns a numerical AQI value which can be mapped to standard air quality categories:

| AQI Range | Category |
|-----------|----------|
| 0 – 50 | 🟢 Good |
| 51 – 100 | 🟡 Moderate |
| 101 – 150 | 🟠 Unhealthy for Sensitive Groups |
| 151 – 200 | 🔴 Unhealthy |
| 201 – 300 | 🟣 Very Unhealthy |
| 301+ | 🔵 Hazardous |

---

## 🔮 Future Enhancements

- [ ] Improve model accuracy using **Deep Learning**
- [ ] Add **real-time API integration**
- [ ] Enhance **UI/UX design**
- [ ] Deploy on cloud platforms (**AWS / Azure**)

---

## 📬 Contact

If you have any queries or suggestions, feel free to connect:

🔗 **LinkedIn:** [Connect with Pratik](https://www.linkedin.com/in/pratikgupta999)

---

## ⭐ Conclusion

This project demonstrates the application of **Machine Learning** in solving real-world environmental problems and showcases practical skills in:

- ✅ Data Analysis
- ✅ Model Building
- ✅ Web Deployment

---

> 💡 *If you found this project useful, consider giving it a ⭐ star on GitHub!*