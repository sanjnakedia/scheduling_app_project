from flask import Flask, render_template, request, redirect, session, json, url_for
app = Flask(__name__)
app.secret_key = 'your_secret_key'

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
    return render_template("base2.html")


@app.route('/rankings', methods=['POST'])
def rankings():
    selected_time_blocks_str = request.form.get('selectedTimeBlocks', '[]')  # Default to an empty list as a string if not found
    selected_time_blocks = json.loads(selected_time_blocks_str)  # Parse the JSON string into a Python list

    return render_template('rank.html', selected_time_blocks=selected_time_blocks)

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