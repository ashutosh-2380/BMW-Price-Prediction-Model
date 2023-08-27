from flask import Flask, render_template, request
import joblib

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load your pre-trained model
model = joblib.load('bmw_price_model')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        mileage = float(request.form['mileage'])
        age = float(request.form['age'])
        prediction = model.predict([[mileage, age]])[0]
        return render_template('index.html', prediction=f'${prediction:.2f}')
    except Exception as e:
        error_message = f"Error: {str(e)}"
        return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
