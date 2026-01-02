import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Setting a seed for reproducibility
SEED = 42
np.random.seed(SEED)

# Location of data to access and where to store the built model
train_path = "/work_env/cleandata/taxi_train.csv"
model_path = "/work_env/cleandata/xgb_model_best_features.joblib"

# Load data
df = pd.read_csv(train_path)

# Selecting on identified in EDAly the best features
selected_features = [
    "trip_distance",
    "trip_duration_min",
    "is_airport_trip",
    "has_toll",
    "RatecodeID",
    "DO_Borough",
    "PU_Borough"
]

X = df[selected_features]
y = df["fare_amount"]

#Transformation of categorical variables (One hot encoding)
categorical_cols = ["DO_Borough", "PU_Borough"]
numeric_cols = [c for c in X.columns if c not in categorical_cols]

# Column transformer
transform = ColumnTransformer(
    transformers=[
        ("num", "passthrough", numeric_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
    ]
)

# XGB Pipeline
pipeline = Pipeline([
    ("preprocessor", transform),
    ("model", XGBRegressor(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.1,
        subsample=0.8,
        random_state=SEED,
        n_jobs=-1
    ))
])

# Training the model
pipeline.fit(X, y)
print("XGBoost model trained successfully.")

# Metrics on training data
y_pred = pipeline.predict(X)
mae = mean_absolute_error(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))
r2 = r2_score(y, y_pred)
print(f"Training Metrics - MAE: {mae:.2f}, RMSE: {rmse:.2f}, R²: {r2:.4f}")

# Saving the trained model
joblib.dump(pipeline, model_path)
print(f"Model saved to: {model_path}")