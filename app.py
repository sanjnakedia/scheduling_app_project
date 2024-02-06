from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST": 
        name = request.form.get("name")
        calendar = request.form.get("calendar")
        time_zone = request.form.get("time_zone")  
    #schedule_times = schedule_times.query.all()
        return redirect("/schedule") 
    else: 
        return render_template("home2.html")
    

@app.route("/schedule")
def scheduler():
    return render_template("base.html")

@app.route('/rank')
def rank():
    return render_template('rank.html')

@app.route('/results')
def results():
    # This route would handle displaying the rankings.
    # You might retrieve the rankings from localStorage or wherever they are stored.
    return render_template('results.html')

#class Schedule


#class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


#class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)