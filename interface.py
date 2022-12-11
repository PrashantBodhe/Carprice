from flask import Flask,jsonify,render_template,request
import utils

app = Flask(__name__)

@app.route('/')
def home():
    print('Testing home API')
    return render_template('home.html')

@app.route('/predict',methods = ["POST"])
def prediction():
    print("Testing prediction API")
    data = request.form
    if request.method == "POST":
        print('Input data is:',data)
        x1 = int(data["Year"])
        x2 = float(data["Present_Price"])
        x3 = int(data["Kms_Driven"])
        x4 = int(data["Seller_Type"])
        x5 = int(data["Transmission"])
        x6 = int(data["Owner"])
        x7 = int(data["Fuel_Diesel"])
        x8 = int(data["Fuel_Petrol"])

        prediction = utils.predict_class(x1,x2,x3,x4,x5,x6,x7,x8)

        return render_template('after.html', price = prediction)
    
    else:
        return jsonify({'Message':"Unsuccessful"})


if __name__ == "__main__":
    app.run()