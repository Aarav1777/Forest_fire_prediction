# Forest Fire Prediction – End-to-End ML Project

## Team Members
- Aarav kumar  

## Project Overview
Forest fires are a major environmental hazard, causing significant loss of life, property, and biodiversity. This project aims to predict the likelihood of forest fires using machine learning techniques by analyzing environmental factors such as humidity, temperature, wind speed, rainfall, and other relevant parameters.  

By building an end-to-end ML pipeline, we provide insights to prevent and manage forest fires efficiently.  

## Features
- Predict the probability of forest fires based on environmental data.  
- Uses multiple parameters including:
  - Humidity
  - Temperature
  - Wind speed
  - Rainfall
  - Vegetation and other environmental factors  
- Exploratory Data Analysis (EDA) for feature insights.  
- Data preprocessing including handling missing values, normalization, and encoding.  
- End-to-end Machine Learning pipeline:
  - Model selection
  - Training & testing
  - Evaluation metrics (accuracy, precision, recall, F1-score, etc.)
- Optional visualization of predicted fire-prone areas.  

## Dataset
The dataset contains environmental measurements such as:

- **Temperature** (°C) – the ambient temperature of the area  
- **Humidity** (%) – the relative humidity in the atmosphere  
- **Wind Speed** (km/h) – the speed of wind at the location  
- **Rainfall** (mm) – amount of rainfall recorded  
- **Area** – the geographic area of measurement  
- **Region** – the larger region or zone the area belongs to  
- **Month** – month of observation  
- **Day** – day of observation  
- **FFMC** – Fine Fuel Moisture Code  
- **DMC** – Duff Moisture Code  
- **DC** – Drought Code  
- **ISI** – Initial Spread Index 

## Technology Stack
- Python  
- Pandas, NumPy (Data handling)  
- Matplotlib, Seaborn (Data visualization)  
- Scikit-learn (Machine Learning)
- Flask (web app devlopment)
- Jupyter Notebook (Experimentation & EDA)
  
## Model Training 
-The dataset is used to train a predictive model for environmental analysis. The steps include:
 Data Preprocessing
 Handle missing values (if any)
 Convert categorical variables (Area, Region, Month, Day) into numerical form using encoding
 Normalize or standardize numerical features (Temperature, Humidity, Wind Speed, Rainfall, FFMC, DMC, DC, ISI)

-Feature Selection
 All environmental parameters are used as features: Temperature, Humidity, Wind Speed, Rainfall, Area, Region, Month, Day, FFMC, DMC, DC, ISI
-Train-Test Split
 Split the dataset into training and testing sets (e.g., 80% training, 20% testing)
-Model Choice
 A regression/classification model (e.g., Linear Regression, Random Forest, or Decision Tree) is trained to predict the target variable
-Model Training
 Fit the model on the training data: model.fit(X_train, y_train)
-Evaluation
 Evaluate the model on the test data using metrics like Mean Squared Error (MSE), R² score (for regression), or accuracy (for classification)

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Aarav1777/Forest_fire_prediction.git
