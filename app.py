from flask import Flask, render_template, redirect, jsonify, request
import retrievedata
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predictor")
def predictor():
    return render_template("index1.html")

@app.route("/graphs")
def graphs():
    return render_template("index2.html")

@app.route("/datainfo")
def datainfo():
    return render_template("index3.html")

@app.route("/collaborators")
def collaborators():
    return render_template("index4.html")

@app.route("/predictor/nostrokerisk")
def nostroke():
    return render_template("index5.html")

@app.route("/predictor/strokerisk")
def yesstroke():
    return render_template("index6.html")

@app.route("/retrieve", methods=['GET', 'POST'])
def retrieve():

    if request.method == "POST":
        gender = request.form["gender"]
        age = request.form["age"]
        hypertension = request.form["hypertension"]
        heartdisease = request.form["heartdisease"]
        married = request.form["married"]
        worktype = request.form["worktype"]
        residencetype = request.form["residencetype"]
        bmi = request.form["bmi"]
        smokingstatus = request.form["smokingstatus"]

        predictions = retrievedata.entrylist(gender,age,hypertension,heartdisease,married,worktype,residencetype,bmi,smokingstatus)
        
        if predictions[0]==0:
            return redirect("/predictor/nostrokerisk")
        else:
            return redirect("/predictor/strokerisk")


if __name__ == '__main__':
    port = int(os.environ.get('Port', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
