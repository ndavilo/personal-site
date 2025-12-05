from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Helper: load a CSV file safely
def load_csv(path):
    try:
        df = pd.read_csv(path)
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"Error loading {path}: {e}")
        return []

@app.route("/")
def index():
    # Load all CSV files
    projects = load_csv("data/projects.csv")
    education = load_csv("data/education.csv")
    certifications = load_csv("data/certifications.csv")

    return render_template(
        "index.html",
        projects=projects,
        education=education,
        certifications=certifications
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
