import pandas as pd
import joblib
from models.plot_helper import generate_plot

# Load model & test dataset once on startup
model = joblib.load("models/strength_model.joblib")
test_df = pd.read_csv("models/test_set.csv")




def predict_strength(data):
    # Convert request to DataFrame
    row = pd.DataFrame([data.dict()])

    # Make prediction
    pred_value = model.predict(row)[0]

    # Generate graph
    graph_base64 = generate_plot(pred_value, model, test_df)

    return {
        "predicted_strength": round(float(pred_value), 2),
        "graph": graph_base64
    }