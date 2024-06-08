# Predicting the 2024 NBA Champion With Machine Learning (Group 27)

**Zareb Islam | Aadhil Mubarak Syed | Jaynor Singson | Dylan Tran**  
**ECS 171: Machine Learning | Professor Setareh Rafatirad**  
**Department of Computer Science | University of California, Davis**

## Introduction

Welcome to our project repository for predicting the 2024 NBA Champion using advanced machine learning techniques. This project leverages a deep neural network (DNN) model to forecast the outcomes of the NBA Championship based on a comprehensive set of historical team statistics, performance metrics, and advanced analytics.

## Repository Structure

- **Documents/**: Contains documents related to the project submission
- **data/**: Contains cleaned and processed data used for model training and testing.
- **model/**: Contains the saved DNN model.
- **raw_data/**: Contains raw data extracted from Basketball-Reference.
- **Data_Extraction.ipynb**: Jupyter notebook for extracting and cleaning data.
- **EDA_Aadhil.ipynb**: Exploratory Data Analysis by Aadhil.
- **EDA_Dylan.ipynb**: Exploratory Data Analysis by Dylan.
- **EDA_Final.ipynb**: Final Exploratory Data Analysis for championship frequency.
- **EDA_Jaynor.ipynb**: Exploratory Data Analysis by Jaynor.
- **EDA_Skeleton.ipynb**: Renamed notebook for initial data analysis.
- **EDA_Zareb.ipynb**: Exploratory Data Analysis by Zareb.
- **LICENSE**: Project license file.
- **Model_Testing.ipynb**: Jupyter notebook for testing the trained model.
- **Model_Training.ipynb**: Jupyter notebook for training the DNN model.
- **README.md**: This README file.

## Project Overview

### Abstract

Our project aims to develop a predictive model to forecast the NBA Championship outcomes using deep neural networks. The model integrates historical team statistics, performance metrics, and advanced analytics to accurately predict the likelihood of an NBA team winning the championship. The model's performance was evaluated using cross-validation and achieved a high accuracy rate, demonstrating its robustness.

### Introduction and Background

Predicting the outcome of the NBA Championship is a complex challenge that has intrigued analysts, fans, and stakeholders. With the advent of machine learning techniques, particularly deep neural networks, new avenues have opened for tackling such predictive tasks with enhanced accuracy and depth. This project explores these techniques to build a reliable predictive model.

## Methodology

Our methodology involves several key steps:

1. **Data Collection and Cleaning**: Data was sourced from Basketball-Reference, covering team statistics and advanced metrics from the last 30 years. Initial data extraction faced complexities, and manual extraction methods were employed to ensure data accuracy.
2. **Exploratory Data Analysis (EDA)**: Key trends and significant predictors of championship success were identified. This analysis helped in understanding the data and selecting features for the model.
3. **Model Selection and Training**: A deep neural network (DNN) was chosen due to its ability to handle complex patterns in the data. The model was built using TensorFlow, with an architecture consisting of an input layer, three hidden layers with ReLU activation, and an output layer with sigmoid activation.
4. **Model Evaluation**: The model was evaluated using cross-validation and tested on historical data from 1994 to 2023, achieving a 90% accuracy rate. 

### Key Findings

- The model correctly predicted 27 out of 30 historical NBA champions.
- Significant predictors included win percentage, offensive and defensive ratings, and effective field goal percentage.
- The model predicted the Boston Celtics as the 2024 NBA Champions with a 37.86% likelihood.

## Usage

### Data Extraction and Cleaning

To extract and clean the data, run the `Data_Extraction.ipynb` notebook. This will gather the data from Basketball-Reference and preprocess it for analysis.

### Exploratory Data Analysis

Use the EDA notebooks (`EDA_Aadhil.ipynb`, `EDA_Dylan.ipynb`, `EDA_Final.ipynb`, `EDA_Jaynor.ipynb`, `EDA_Zareb.ipynb`) to explore the data and identify key trends.

### Model Training

Train the DNN model using the `Model_Training.ipynb` notebook. This notebook includes data preprocessing, model architecture definition, and the training process.

### Model Testing

Test the trained model using the `Model_Testing.ipynb` notebook. This notebook evaluates the model's performance on test data and provides accuracy metrics.

## Contributions

Our project was a collaborative effort with specific contributions from each team member:

- **Aadhil Mubarak Syed**: Data extraction, initial cleaning, model training, and evaluation.
- **Jaynor Singson**: Development of the front-end HTML interface for deploying our machine learning model.
- **Dylan Tran and Zareb Islam**: Literature review, project report, and cleanup of exploratory data analysis.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
