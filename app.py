from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# this will load the model
model = pickle.load(open("model.pkl", "rb"))

# for loading feature names
df = pd.read_csv("BostonHousing.csv")
feature_names = df.drop("price", axis=1).columns.tolist()

@app.route('/')
def index():
    return render_template('index.html', features=feature_names)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_values = [float(request.form[feature]) for feature in feature_names]
        prediction = model.predict([input_values])[0]
        return render_template('index.html', features=feature_names,
                               prediction_text=f"Predicted House Price: ${prediction:.2f}")
    except:
        return render_template('index.html', features=feature_names,
                               prediction_text="Invalid input. Please check your values.")# with error handeling if the field is blank

if __name__ == "__main__":
    app.run(debug=True)

