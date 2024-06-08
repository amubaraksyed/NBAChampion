# README.md

# Predicting the 2024 NBA Champion With Machine Learning (Group 27)

**Zareb Islam | Aadhil Mubarak Syed | Jaynor Singson | Dylan Tran**  
**ECS 171: Machine Learning | Professor Setareh Rafatirad**  
**Department of Computer Science | University of California, Davis**

## Introduction

This repository contains the code and data used for our project on predicting the 2024 NBA Champion using machine learning techniques. Our project employs a deep neural network (DNN) model to forecast the NBA Championship outcomes based on historical team statistics, performance metrics, and advanced analytics.

## Repository Structure

- **Documents/**: Folder containing documentation related to the project.
- **data/**: Folder containing the cleaned and processed data used for model training and testing.
- **model/**: Folder containing the saved DNN model.
- **raw_data/**: Folder containing the raw data extracted from Basketball-Reference.
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

This project aims to develop a predictive model for forecasting the NBA Championship outcomes using deep neural networks. The model integrates historical team statistics, performance metrics, and advanced analytics to accurately predict the likelihood of an NBA team winning the championship. The model's performance was evaluated using cross-validation and achieved a high accuracy rate, demonstrating its robustness.

### Introduction and Background

Accurately predicting the NBA Championship outcome is a complex challenge that has intrigued analysts, fans, and stakeholders. With the rise of machine learning techniques, particularly deep neural networks, new avenues have opened for tackling such predictive tasks with enhanced accuracy and depth.

### Methodology

Our methodology involves the following steps:

1. **Data Collection and Cleaning**: Data was sourced from Basketball-Reference, covering team statistics and advanced metrics from the last 30 years.
2. **Exploratory Data Analysis (EDA)**: Identified key trends and significant predictors of championship success.
3. **Model Selection and Training**: A deep neural network (DNN) was chosen for its ability to handle complex patterns in the data. The model was trained using TensorFlow with an input layer, three hidden layers with ReLU activation, and an output layer with sigmoid activation.
4. **Model Evaluation**: The model was evaluated using cross-validation and tested on historical data from 1994 to 2023, achieving a 90% accuracy rate.

### Key Findings

- The model predicted 27 out of 30 historical NBA champions correctly.
- Important predictors included win percentage, offensive and defensive ratings, effective field goal percentage, and more.
- The model predicted the Boston Celtics as the 2024 NBA Champions with a 37.86% chance.

## Usage

### Data Extraction and Cleaning

To extract and clean the data, run the `Data_Extraction.ipynb` notebook. This will collect the data from Basketball-Reference and preprocess it for analysis.

### Exploratory Data Analysis

Explore the data and identify key trends using the EDA notebooks (`EDA_Aadhil.ipynb`, `EDA_Dylan.ipynb`, `EDA_Final.ipynb`, `EDA_Jaynor.ipynb`, `EDA_Zareb.ipynb`).

### Model Training

Train the deep neural network model using the `Model_Training.ipynb` notebook. This notebook will preprocess the data, define the model architecture, and train the model using the specified parameters.

### Model Testing

Test the trained model using the `Model_Testing.ipynb` notebook. This notebook will evaluate the model's performance on the test data and provide the accuracy metrics.

## Contributions

All team members contributed to the brainstorming of project topics and goals, the mid-quarter progress report, and the exploratory data analysis. Specific contributions are as follows:

- **Aadhil Mubarak Syed**: Data extraction, initial cleaning, model training, and evaluation.
- **Jaynor Singson**: Development of the front-end HTML interface.
- **Dylan Tran and Zareb Islam**: Literature review, project report, and cleanup of exploratory data analysis.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
