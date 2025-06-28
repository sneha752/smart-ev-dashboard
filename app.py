from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the new CSV file with predicted power usage
df = pd.read_csv("ev_station_with_predictions.csv")

@app.route("/")
def index():
    stations = df.to_dict(orient='records')
    return render_template("index.html", stations=stations)

if __name__ == "__main__":
    app.run(debug=True)
