import preprocess
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

scaler = joblib.load('scaler.h5')
model = joblib.load('model.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'POST':
        temp = request.form['temp']
        humidity = request.form['humidity']
        hour = request.form['hour']
        month = request.form['month']
        day = request.form['day']
        weather = request.form['weather']

        data = {'temp':temp, 'humidity':humidity, 'hour':hour, 'month':month, 'day':day, 'weather':weather}
        Final_Data  = preprocess.User(data)
        print((Final_Data))
        print()
        print(len(Final_Data))

        model = joblib.load('model.h5')
        scaler = joblib.load('scaler.h5')
        Final_Data = scaler.transform([Final_Data])

        print()
        print(Final_Data)
        prediction  = model.predict(Final_Data)[0]
        print(prediction )

        return render_template('prediction.html', prediction_text=f"COUNT BIKES RENTED ARE:  {int((prediction))}")

    else:
        return render_template("prediction.html")

if __name__ == "__main__":
    app.run(debug=True)