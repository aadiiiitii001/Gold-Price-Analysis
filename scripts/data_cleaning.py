import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/gold_historical_data.csv")
PROCESSED_PATH = Path("data/processed/gold_cleaned.csv")


def load_raw_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Raw data not found at {path}")
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # enforce date parsing
    if "date" not in df.columns:
        raise KeyError("Expected 'date' column not found")

    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # drop invalid rows
    df = df.dropna()
    df = df.drop_duplicates()

    # sort for time-series integrity
    df = df.sort_values("date")

    return df


def validate_data(df: pd.DataFrame):
    if df.isna().sum().sum() != 0:
        raise ValueError("Data still contains missing values")

    if not df["date"].is_monotonic_increasing:
        raise ValueError("Date column is not sorted")

    if df.empty:
        raise ValueError("Cleaned dataset is empty")


def save_processed_data(df: pd.DataFrame, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def main():
    df_raw = load_raw_data(RAW_PATH)
    df_cleaned = clean_data(df_raw)
    validate_data(df_cleaned)
    save_processed_data(df_cleaned, PROCESSED_PATH)

    print("Data cleaning completed successfully")
    print(f"Rows: {df_cleaned.shape[0]}")
    print(f"Columns: {df_cleaned.shape[1]}")


if __name__ == "__main__":
    main()
