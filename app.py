from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    stats = {
        "atendidos": 25,
        "preparados": 50,
        "restantes": 25
    }

    return render_template("dashboard.html", stats=stats)

if __name__ == "__main__":
    app.run(debug=True)
    