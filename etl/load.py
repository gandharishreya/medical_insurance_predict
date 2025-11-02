from sqlalchemy import create_engine

def load_to_postgres(df, db_name, user, password, host, port, table_name):
    print("🔹 Step 3: Loading data into PostgreSQL...")

    try:
        # Create SQLAlchemy engine
        engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")

        # Load DataFrame to PostgreSQL table
        df.to_sql(table_name, engine, index=False, if_exists='replace')

        print(f" Successfully loaded data into table: {table_name}")
    except Exception as e:
        print(" Error loading data to PostgreSQL:", e)
