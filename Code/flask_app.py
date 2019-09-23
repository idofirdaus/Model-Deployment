# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
from flask import Flask, request, jsonify
import numpy as np
import pickle
from sklearn.externals import joblib

app = Flask(__name__)

# Load the model
model = joblib.load(open('/home/idofirdaus/mysite/forest.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    datas = request.get_json(force=True)
    output=[]
    for data in datas:
    # Make prediction using model loaded from disk as per the data.
        prediction = model.predict([np.array([data['EDUCATION'],data['AGE'], data['PAY_1'], data['PAY_2'],data['PAY_3']])])

        if prediction==0:
            output.append('Prediction Result: '+ str(prediction)+', Artinya pelanggan diprediksi tidak akan terlambat bayar')
        else:
            output.append('Prediction Result: '+ str(prediction)+', Artinya pelanggan diprediksi akan terlambat bayar')

    # Take the first value of prediction
    return jsonify(output)

#if __name__ == '__main__':
#    app.run(port=5000, debug=True)