from flask import Flask, render_template, request, session, redirect, url_for

import random

app = Flask(__name__)

app.secret_key = "your_secret_key"

@app.route("/", methods=["GET", "POST"])

def index():
    if "number" not in session:

        session["number"] = random.randint(1, 100)
        session["attempts"] = 0
        session["max_attempts"] = 10

    message = ""

    if request.method == "POST":

        guess = int(request.form["guess"])
        session["attempts"] += 1

        if guess < session["number"]:
            message = "🔻 Too low!"

        elif guess > session["number"]:
            message = "🔺 Too high!"

        else:
            message = f"🎉 Correct! The number was {session['number']}."
            session.pop("number", None)

            return render_template("index.html", message=message, win=True)
        

        if session["attempts"] >= session["max_attempts"]:

            message = f"😢 You've used all attempts. The number was {session['number']}."
            session.pop("number", None)

            return render_template("index.html", message=message, win=False)

    return render_template("index.html", message=message)



if __name__ == "__main__":

    app.run(debug=True)