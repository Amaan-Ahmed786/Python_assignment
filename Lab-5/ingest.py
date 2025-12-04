# codefiles/ingest.py
from pathlib import Path
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def infer_building_name(path: Path):
    return path.stem.split("_")[0]

def read_and_merge(input_folder="meter_inputs"):
    folder = Path(input_folder)
    files = list(folder.glob("*.csv"))

    if not files:
        logging.error("No CSV files found in meter_inputs folder.")
        return pd.DataFrame()

    frames = []
    for f in files:
        try:
            df = pd.read_csv(f, parse_dates=["timestamp"])
            df["building"] = infer_building_name(f)
            df["month"] = df["timestamp"].dt.to_period("M").astype(str)
            frames.append(df)
            logging.info(f"Loaded {f.name} ({len(df)} rows)")
        except Exception as e:
            logging.error(f"Error reading {f.name}: {e}")

    if not frames:
        return pd.DataFrame()

    combined = pd.concat(frames, ignore_index=True)
    combined.dropna(subset=["timestamp", "kwh"], inplace=True)
    combined["kwh"] = pd.to_numeric(combined["kwh"], errors="coerce")
    combined.dropna(subset=["kwh"], inplace=True)

    combined.sort_values("timestamp", inplace=True)
    combined.reset_index(drop=True, inplace=True)

    return combined
