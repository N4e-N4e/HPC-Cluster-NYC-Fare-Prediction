import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Setting a seed for reproducibility
SEED = 42
np.random.seed(SEED)

# Location of data to access and where to store the build models
train_path = "/work_env/cleandata/taxi_train.csv"
model_path = "/work_env/cleandata/lasso_model.joblib"

# Load data
df = pd.read_csv(train_path)
X = df.drop(columns=["fare_amount"])
y = df["fare_amount"]

# Transformation of categorical variables (One hot encoding)
categorical_cols = ["day_of_week", "month", "time_of_day", "PU_Borough", "DO_Borough"]
numeric_cols = [c for c in X.columns if c not in categorical_cols]

transform = ColumnTransformer(
    transformers=[
        ("num", "passthrough", numeric_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)])

# Lass - Regression pipeline
pipeline = Pipeline([
    ("preprocessor", transform),
    ("model", Lasso(alpha=0.1, random_state=SEED))
])

# Training the model
pipeline.fit(X, y)
print("Lasso model trained successfully.")

# Metrics
y_pred = pipeline.predict(X)
mae = mean_absolute_error(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))
r2 = r2_score(y, y_pred)
print(f"Training Metrics - MAE: {mae:.2f}, RMSE: {rmse:.2f}, R²: {r2:.4f}")

# Saving the trained model
joblib.dump(pipeline, model_path)
print(f"Model saved to: {model_path}")