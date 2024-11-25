import pandas as pd
import yfinance as yf

from research.config import DATA_DIR
from research.datasets.dataset import Dataset

RAW_FILE_PATH = DATA_DIR + "/iwv_daily_raw.csv"
CLEAN_FILE_PATH = DATA_DIR + "/iwv_daily_clean.parquet"


class RussellDaily(Dataset):
    """
    Daily dataset for IWV Russell 3000 ETF. This class handles the downloading, and cleaning in order to improve the reproducibility of our research.
    """

    def __init__(self, RAW_FILE_PATH=RAW_FILE_PATH, CLEAN_FILE_PATH=CLEAN_FILE_PATH) -> None:
        super().__init__(RAW_FILE_PATH, CLEAN_FILE_PATH)

    def download(self):
        df = yf.download(tickers="IWV", start="1925-12-31", end="2024-12-31").stack().reset_index()

        df.to_csv(RAW_FILE_PATH, index=False)

    def clean(self):
        # Raw file
        df = pd.read_csv(RAW_FILE_PATH)

        # Rename columns
        df = df.rename(columns={"Date": "date", "Adj Close": "prc"})

        # Compute daily return column
        df["ret"] = df["prc"].pct_change()

        # Keep columns
        df = df[["date", "prc", "ret"]].copy()

        # Cast types
        df["date"] = pd.to_datetime(df["date"])

        df.to_parquet(CLEAN_FILE_PATH)
