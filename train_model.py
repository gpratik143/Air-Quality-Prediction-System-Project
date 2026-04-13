import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pickle
import os

# Load the data
try:
    df = pd.read_csv('Data/Real-Data/Real_Combine.csv')
    print("Data loaded successfully")
except:
    print("Could not load data - using dummy data for demonstration")
    # Create dummy data for testing if real data doesn't exist
    np.random.seed(42)
    df = pd.DataFrame({
        'T': np.random.uniform(15, 35, 100),
        'TM': np.random.uniform(20, 40, 100),
        'Tm': np.random.uniform(10, 30, 100),
        'SLP': np.random.uniform(1000, 1020, 100),
        'H': np.random.uniform(30, 90, 100),
        'VV': np.random.uniform(5, 20, 100),
        'V': np.random.uniform(1, 10, 100),
        'VM': np.random.uniform(10, 30, 100),
        'PM25': np.random.uniform(20, 150, 100)
    })

# Prepare features and target
# Remove rows with NaN values
df = df.dropna()

X = df.iloc[:, :-1]  # All columns except last
y = df.iloc[:, -1]   # Last column as target

print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")

# Train Random Forest model
print("Training Random Forest model...")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the model
filename = 'random_forest_regression_model.pkl'
pickle.dump(model, open(filename, 'wb'))
print(f"Model saved to {filename}")

# Verify the model works
test_data = np.array([[20, 30, 10, 1010, 60, 10, 5, 15]])
prediction = model.predict(test_data)
print(f"Test prediction: {prediction[0]:.2f}")
