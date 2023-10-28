from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("disease.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final = [np.array(int_features)]
    prediction = model.predict_proba(final)
    output = '{0:.{1}f}'.format(prediction[0][1], 2)

    # Assuming 'area_prediction' is the variable that holds the demographic area prediction
    area_prediction = "AREA(D=DOMBIVLI/V=VASAI)_VASAI"

    if prediction[0][1] >= 0.5:
        area_prediction = "High probability of Demographic Area A"
    else:
        area_prediction = "High probability of Demographic Area B"

    result_message = f"According to the analysis, the demographic area is: {area_prediction}"


    
        

if __name__ == '__main__':
    app.run(debug=True)