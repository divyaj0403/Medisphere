from flask import Flask, render_Medisphere, request
import sqlite3

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    msg = None
    if request.method == "POST":
        name = request.form["Name"]
        email = request.form["Email"]
        password = request.form["password"]

        if name != "" and email != "" and password != "":
            conn = sqlite3.connect("loginfo.db")
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS PERSON (Name TEXT, Email VARCHAR, Password TEXT)")
            c.execute("INSERT INTO PERSON VALUES (?, ?, ?)", (name, email, password))
            msg = "You have successfully logged in"
            conn.commit()
            conn.close()
        else:
            msg = "Please fill all the entries"

    return render_Medisphere("login.html", msg=msg)

if __name__ == "__main__":
    app.run(debug=True)
