import matplotlib
matplotlib.use("Agg")    # 👈 VERY IMPORTANT — prevents macOS GUI crash

import matplotlib.pyplot as plt
import base64
from io import BytesIO
import pandas as pd


def generate_plot(pred_value, model, test_df):
    # Create a new figure using the non-GUI Agg backend
    plt.figure(figsize=(7, 7))

    # Predict test dataset
    X_test = test_df.drop("Strength", axis=1)
    y_pred_test = model.predict(X_test)

    # Scatter plot: actual vs predicted
    plt.scatter(test_df["Strength"], y_pred_test, alpha=0.6, label="Test Data")

    # Perfect prediction diagonal
    mn = min(test_df["Strength"].min(), pred_value)
    mx = max(test_df["Strength"].max(), pred_value)
    plt.plot([mn, mx], [mn, mx], "r", label="Perfect Prediction Line")

    # Highlight NEW prediction point
    plt.scatter(pred_value, pred_value,
                s=200,
                color="yellow",
                edgecolor="black",
                linewidth=1.5,
                label="New Prediction")

    plt.xlabel("Actual Strength (MPa)")
    plt.ylabel("Predicted Strength (MPa)")
    plt.title("Actual vs Predicted Strength")
    plt.legend()
    plt.grid(True)

    # Convert matplotlib plot → base64 string for frontend
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close()
    buffer.seek(0)

    # Return encoded PNG image
    return base64.b64encode(buffer.read()).decode("utf-8")