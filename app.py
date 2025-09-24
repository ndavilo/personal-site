from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    # Load CSV data
    df = pd.read_csv("data/projects.csv")
    projects = df.to_dict(orient="records")
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
