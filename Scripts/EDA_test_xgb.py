import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import matplotlib.pyplot as plt
import numpy as np

# Loading the trained model and test data
test_path = "/work_env/cleandata/taxi_test.csv"
model_path = "/work_env/cleandata/xgb_model_best_features.joblib"
save_path = "/work_env/result/actual_vs_pred_XGB_best_features.png"

# Load test data
df_test = pd.read_csv(test_path)

# Select only the features used in the model
selected_features = [
    "trip_distance",
    "trip_duration_min",
    "is_airport_trip",
    "has_toll",
    "RatecodeID",
    "DO_Borough",
    "PU_Borough"
]

X_test = df_test[selected_features]
y_test = df_test["fare_amount"]

# Load trained model
pipeline = joblib.load(model_path)
print("XGBoost model (best features) loaded successfully.")

# Predicting on test data
y_pred = pipeline.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("XGBoost Model (Best Features) Performance on Test Data:")
print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²: {r2:.4f}")

# Plotting and saving visual
subset_size = 10000
idx = np.random.RandomState(42).choice(len(y_test), subset_size, replace=False)

plt.figure(figsize=(8, 6))
plt.scatter(y_test.iloc[idx], y_pred[idx], alpha=0.3, s=10)
max_val = max(y_test.iloc[idx].max(), y_pred[idx].max())
plt.plot([0, max_val], [0, max_val], linestyle="--", color="red")
plt.xlabel("Actual Fare")
plt.ylabel("Predicted Fare")
plt.title("Actual vs Predicted - XGBoost (Best Features)")
plt.tight_layout()

plt.savefig(save_path, dpi=300)
print(f"Scatter plot saved at: {save_path}")