import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

print("Step 1: Loading dataset...")

# Load dataset
data = pd.read_csv("data/Cleaned_District_Level_Crops_Merged.csv")

print("Dataset Loaded Successfully!")
print("\nColumns Available:")
print(data.columns)

print("\nStep 2: Cleaning dataset...")

# Remove missing values
data = data.dropna()

print("Dataset Shape After Cleaning:", data.shape)

# ---------------------------------------------------
# IMPORTANT: CHECK COLUMN NAMES BELOW
# ---------------------------------------------------

# Update these names after seeing printed columns
X = data[
    [
        'Area_Hectare_Veg',
        'Yield_MT_per_Hectare_Veg',
        'Area_Hectare_Fruit',
        'Yield_MT_per_Hectare_Fruit'
    ]
]

y = data['Production_MT_Veg']



print("\nStep 3: Splitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Step 4: Training Random Forest model...")

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Model Training Completed!")

print("\nStep 5: Evaluating model...")

predictions = model.predict(X_test)

r2 = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)

print("R2 Score:", round(r2, 4))
print("Mean Absolute Error:", round(mae, 2))

print("\nStep 6: Saving model...")

pickle.dump(model, open("models/crop_model.pkl", "wb"))

print("Model Saved Successfully!")
