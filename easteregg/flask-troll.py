@web.route('/troll', methods=['POST', 'GET']) # change endpoint to where you want to troll
def flask_troll():
    if request.method == "POST":
        #do something
        pass
    else:
        if 'visit' in session:
            session["visit"] += 1
        else:
            session["visit"] = 1
        if session["visit"] > 0 and session["visit"] < 6:
            return render_template('troll.html', image_src="image"+str(session["visit"])+".png")
        else:
            session["visit"] = 0
            return render_template("troll.html", image_src="image6.png")
