import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

# Sample dataset (mock)
data = {
    "crop_type": ["Wheat", "Wheat", "Rice", "Rice", "Maize", "Maize"],
    "region_code": [101, 102, 101, 103, 102, 103],
    "day_of_year": [120, 150, 160, 170, 180, 200],
    "rainfall_mm": [50, 60, 55, 70, 40, 90],
    "price": [1500, 1600, 1400, 1550, 1300, 1650]
}
df = pd.DataFrame(data)

# One-hot encoding for crop types
df = pd.get_dummies(df, columns=["crop_type"])

# Prepare features and target
X = df.drop("price", axis=1)
y = df["price"]

# Train a basic model
model = RandomForestRegressor(n_estimators=10, random_state=42)
model.fit(X, y)

# Save the model
with open("crop_price_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Sample crop_price_model.pkl created!")
