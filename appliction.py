from flask import Flask, render_template, request
import pickle
import numpy as np

appliction = Flask(__name__)

# Load your trained model and scaler
scaler = pickle.load(open("model/scaler.pkl", "rb"))
ridge = pickle.load(open("model/ridge.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    try:
        temp = float(request.form['temp'])
        humidity = float(request.form['humidity'])
        wind = float(request.form['wind'])
        rain = float(request.form['rain'])
        area = float(request.form['area'])
        region = float(request.form['region'])
        month = float(request.form['month'])
        day = float(request.form['day'])
        FFMC = float(request.form['FFMC'])
        DMC = float(request.form['DMC'])
        DC = float(request.form['DC'])
        ISI = float(request.form['ISI'])

        # Create full feature vector
        input_data = np.array([[temp, humidity, wind, rain, area, region, month, day, FFMC, DMC, DC, ISI]])
        input_scaled = scaler.transform(input_data)
        prediction = ridge.predict(input_scaled)

        return render_template('index.html', prediction_text=f"🔥 Fire intensity: {prediction[0]:.2f}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")


if __name__ == "__main__":
    app.run(debug=True)
