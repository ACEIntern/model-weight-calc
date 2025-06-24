import joblib
import pandas as pd


def predict_weight(inputs):
    # Map 'Material' to density
    material_density = {'Al': 2700, 'MS': 7850}

    if 'Material' not in inputs:
        raise ValueError("Material input is missing")

    density = material_density.get(inputs['Material'])
    if density is None:
        raise ValueError("Material must be 'Al' or 'MS'")

    # Replace 'Material' with 'Density'
    inputs['Density'] = density
    del inputs['Material']

    # Create DataFrame and predict
    df = pd.DataFrame([inputs])
    model = joblib.load("model_pipeline.pkl")
    prediction = model.predict(df)[0]
    return prediction
