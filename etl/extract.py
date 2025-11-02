import pandas as pd

def extract_data(filepath):
    print("🔹 Step 1: Extracting data...")
    df = pd.read_csv(filepath)
    print(f" Extracted {df.shape[0]} rows and {df.shape[1]} columns.")
    return df
