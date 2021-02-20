from flask import Flask, render_template, redirect, jsonify, request
import retrievedata
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index1.html")

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
        print(predictions)

    return redirect("/")


if __name__ == '__main__':
    port = int(os.environ.get('Port', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
