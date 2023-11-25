from flask import Flask,render_template
import datetime

app = Flask(__name__)

@app.route("/")
def main():
    now = datetime.datetime.now()
    current_year = now.year
    return render_template("index.html",year = current_year)



if __name__=="__main__":
    app.run(debug=False,host='0.0.0.0')
