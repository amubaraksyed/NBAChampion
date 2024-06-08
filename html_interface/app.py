from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np


app = Flask(__name__)

# Load pre-trained machine learning model here
path = "../model/DNN_Model.h5"
model = load_model(path)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index", methods=["POST"])
def predict2024():
    if request.method == "POST":
        # load data
        df = pd.read_csv(f"../data/2024.csv")

        # preprocess data
        new_df = df.drop(columns=["Champion", "Arena", "Team", "Year", "G"])
        X = StandardScaler().fit_transform(new_df)

        # extract prediction
        y = model.predict(X)
        predicted_team = df.iloc[np.argmax(y)]["Team"]

        # get all championship probabilites
        championship_probs = []
        for i in range(len(y)):
            team = df.iloc[i]["Team"]
            probability = round(y[i][0] * 100, 2)
            championship_probs.append({"team": team, "probability": probability})
        return render_template("index.html", pred_champion=predicted_team, probabilities=championship_probs)
    

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        year_input = int(request.form.get("input"))
        # load data
        if year_input < 1994 or year_input >= 2024:
            return "Something went wrong. Please try again."
        df = pd.read_csv(f"../data/{year_input}.csv")

        # get actual champion
        champion = df[df["Champion"] == 1]["Team"].values[0]

        # preprocess data
        new_df = df.drop(columns=["Champion", "Arena", "Team", "Year", "G"])
        X = StandardScaler().fit_transform(new_df)

        # extract prediction
        y = model.predict(X)
        predicted_team = df.iloc[np.argmax(y)]["Team"]

        # get all championship probabilites
        championship_probs = []
        for i in range(len(y)):
            team = df.iloc[i]["Team"]
            probability = round(y[i][0] * 100, 2)
            championship_probs.append({"team": team, "probability": probability})
        return render_template("result.html", pred_champion=predicted_team, probabilities=championship_probs, year=year_input, actual_champion=champion)

    else:
        return "Something went wrong. Please try again."

if __name__ == "__main__":
    app.run(debug=True)

# visit link http://localhost:5000
