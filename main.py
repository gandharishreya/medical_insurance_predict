from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_to_postgres

def main():
    raw_file = 'data/insurance.csv'

    # Step 1: Extract
    df = extract_data(raw_file)

    # Step 2: Transform
    transformed_df = transform_data(df)

    # Step 3: Load to PostgreSQL
    load_to_postgres(
        df=transformed_df,
        db_name='insurance',
        user='postgres',
        password='root',
        host='localhost',
        port=5432,
        table_name='cleaned_insurance'
    )

    print("\n🎯 ETL pipeline completed successfully and data stored in PostgreSQL!")

if __name__ == "__main__":
    main()
