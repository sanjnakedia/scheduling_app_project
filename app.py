#Necessary imports for the app 
from flask import Flask, render_template, request, redirect, session, json, url_for
app = Flask(__name__)

#Homepage which contains form for user to input their name and time_zone 
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST": 
        name = request.form.get("name")
        time_zone = request.form.get("time_zone")  
        #Once form is filled out and submitted, page redirects to schedule page
        return redirect("/schedule") 
    else: 
        return render_template("home3.html")
    
#Schedule page --> Main page of the app 
@app.route("/schedule")
def scheduler():
    return render_template("base8.html")

#Intermediary structure to save the preferred times inputted by user to display them on the thank you page at the end 
@app.route('/save-preferred-times', methods=['POST'])
def save_preferred_times():
    data = request.get_json()
    preferred_times = data['preferredTimes']
    #Redirects to the thank you template 
    return jsonify(redirect_url=url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    # Preferred times are transferred to the thank you template 
    return render_template('thank_you.html', preferred_times=session.get('preferred_times'))



#@app.route('/rankings', methods=['POST'])
#def rankings():
    selected_time_blocks_str = request.form.get('selectedTimeBlocks', '[]')  # Default to an empty list as a string if not found
    selected_time_blocks = json.loads(selected_time_blocks_str)  # Parse the JSON string into a Python list

    return render_template('rank.html', selected_time_blocks=selected_time_blocks)

#@app.route('/rank')
#def rank():
#    return render_template('rank.html')

#@app.route('/results')
#def results():
    # This route would handle displaying the rankings.
    # You might retrieve the rankings from localStorage or wherever they are stored.
    return render_template('results.html')
    
#@app.route('/submit-rankings', methods=['POST'])
#def submit_rankings():
    print("Form data:", request.form)
    # Example data structure to hold the sorted time blocks
    time_blocks = {
        '1': [],  # Most preferred times
        '2': [],  # If needed times
        '3': []   # Please don't schedule times
    }
    
    # Assuming the number of time blocks is passed in some form field
    num_blocks = int(request.form.get('num_time_blocks', 0))
    
    for i in range(1, num_blocks + 1):
        time_block = request.form.get(f'time_block_{i}')
        ranking = request.form.get(f'ranking_{i}')
        if ranking in time_blocks:
            time_blocks[ranking].append(time_block)
    
    # Pass the sorted time blocks to the template
    return render_template('sorted_times.html', time_blocks=time_blocks)