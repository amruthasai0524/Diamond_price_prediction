#  Diamond Price Prediction using KNN & Streamlit

##  Project Overview
This project builds an **end-to-end Machine Learning application** to predict diamond prices based on their physical and categorical features.

The model is trained using **K-Nearest Neighbors (KNN) Regression**, combined with **data preprocessing, outlier removal, and pipeline techniques**, and deployed using **Streamlit Cloud**.

---

##  Objective
- Perform data preprocessing
- Remove outliers
- Train KNN regression model
- Evaluate model performance
- Save trained pipeline using pickle
- Build Streamlit web app
- Deploy online

---

##  Dataset
**diamonds.csv**

Features used:
- carat
- cut
- color
- clarity
- depth
- table
- x (length)
- y (width)
- z (height)

Target:
- price

---

##  Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

---

##  Machine Learning Pipeline

### 1️ Data Preprocessing
- Missing value check
- Categorical encoding (OneHotEncoder)
- Numerical scaling (StandardScaler)

### 2️ Outlier Removal
- Quantile method (1%–99%) filtering

### 3️ Model
- KNN Regressor

### 4️ Evaluation Metrics
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

##  Model Performance (Example)

| Dataset | MAE | RMSE | R² |
|--------|-----|------|-----|
| Train | 305 | 520 | 0.97 |
| Test  | 315 | 545 | 0.96 |

---


