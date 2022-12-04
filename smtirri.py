from flask import Flask, render_template , request
import machinelearning
app = Flask(__name__)
server = app.server
wateramount =0
@app.route("/", methods = ["GET","POST"])
def predict():
    global wateramount
    if request.method == "POST":
        cpday   = request.form['cpday']
        sm      = request.form['sm']
        temp    = request.form['temp']
        humi    = request.form['humi']
        tempmax = request.form['tempmax']
        tempmin = request.form['tempmin']
        evapo   = request.form['evapo']
        cpfactor = request.form['cpfactor']

        env_values = [[cpday,sm,temp,humi,tempmax,tempmin,evapo,cpfactor]]

        wateramt = machinelearning.WateramountPrediction(env_values)
        print(wateramt)
        wateramount = wateramt
    return render_template("index.html", n= wateramount )


# @app.route("/sub", methods = ["POST"])
# def submit():
#     if request.method == "POST":
#         name = request.form["username"]
#
#         return render_template("sub.html", n=name)



if __name__  == "__main__":
    app.run(debug= "True")