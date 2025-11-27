import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib

df = pd.read_csv("../dataset/Concrete_Data_Yeh.csv")

df.columns = [
    "Cement", "Slag", "FlyAsh", "Water",
    "Superplasticizer", "CoarseAggregate",
    "FineAggregate", "Age", "Strength"
]

X = df.drop("Strength", axis=1)
y = df["Strength"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "strength_model.joblib")

# Save test set
test_df = pd.concat([X_test, y_test], axis=1)
test_df.to_csv("test_set.csv", index=False)

print("Model + test set saved!")