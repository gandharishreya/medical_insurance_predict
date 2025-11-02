import pandas as pd

def transform_data(df):
    print(" Step 2: Transforming data...")

    df = df.drop_duplicates()

    if 'bmi' in df.columns:
        df['bmi'] = df['bmi'].fillna(df['bmi'].mean())
    if 'age' in df.columns:
        df['age'] = df['age'].fillna(df['age'].median())

    categorical_cols = [col for col in ['sex', 'smoker', 'region'] if col in df.columns]
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    if 'age' in df.columns and 'bmi' in df.columns:
        df['age_bmi_interaction'] = df['age'] * df['bmi']

    print(f" Transformation complete — {df.shape}")
    return df
