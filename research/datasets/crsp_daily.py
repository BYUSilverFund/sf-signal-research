import gdown
import pandas as pd

from research.config import DATA_DIR
from research.datasets.dataset import Dataset

RAW_FILE_PATH = DATA_DIR + "/dsf.parquet"
CLEAN_FILE_PATH = DATA_DIR + "/crsp_daily_clean.parquet"


class CRSPDaily(Dataset):
    """
    Monthly dataset for CRSP. This class handles the downloading, and cleaning in order to improve the reproducibility of our research.
    """

    def __init__(self, RAW_FILE_PATH=RAW_FILE_PATH, CLEAN_FILE_PATH=CLEAN_FILE_PATH) -> None:
        super().__init__(RAW_FILE_PATH, CLEAN_FILE_PATH)

    def download(self):
        file_id = "1Zfj5XiBnf87zvYwM-l944AFRaWKfXJbo"
        url = f"https://drive.google.com/uc?id={file_id}"

        gdown.download(url, RAW_FILE_PATH, quiet=False)

    def clean(self):
        # Raw file
        df = pd.read_parquet(RAW_FILE_PATH)

        # Filters
        df = df.query("10 <= shrcd <= 11")  # Stocks
        df = df.query("1 <= exchcd <= 3")  # NYSE, AMEX, NASDAQ

        # Keep only necessary columns
        keep_columns = [
            "permno",
            "date",
            "shrcd",
            "exchcd",
            "ticker",
            "shrout",
            "vol",
            "prc",
            "ret",
        ]
        df = df[keep_columns]

        # Fix ret and prc variables
        df["prc"] = abs(df["prc"])  # Stocks with unavailable prc data are negated (bid-ask spread)

        # Cast types
        df["ret"] = pd.to_numeric(df["ret"])
        df["date"] = pd.to_datetime(df["date"])

        # Sort values
        df = df.sort_values(by=["permno", "date"])

        # Drop duplicates
        df = df.drop_duplicates(subset=["permno", "date"])

        # Reset index
        df = df.reset_index(drop=True)

        df.to_parquet(CLEAN_FILE_PATH)
