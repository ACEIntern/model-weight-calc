import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def train_and_save_model():
    try:
        # Load Excel
        df = pd.read_excel("File-Calculator.xlsx")
        print("Excel loaded successfully")

        # Map material to density
        material_map = {'Al': 2700, 'MS': 7850}
        df['Density'] = df['Material'].map(material_map)

        if df['Density'].isnull().any():
            raise ValueError("Unknown material in data.")

        df.drop(columns=["Material"], inplace=True)

        # Check if all required columns are there
        print("Columns:", df.columns.tolist())

        X = df.drop(columns=["Weight","Actual Volume"])
        print("Training features used:", X.columns.tolist())
        y = df["Weight"]

        # Train model
        model = RandomForestRegressor()
        model.fit(X, y)
        print("Model trained ")

        # Save model
        joblib.dump(model, "model_pipeline.pkl")
        print("Model saved as model_pipeline.pkl")

    except Exception as e:
        print(f"Error during training: {e}")

if __name__ == "__main__":
    train_and_save_model()



