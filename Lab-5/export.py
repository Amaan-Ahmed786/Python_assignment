# codefiles/export.py
from pathlib import Path

def save_cleaned(df, folder="output"):
    p = Path(folder)
    p.mkdir(exist_ok=True)
    df.to_csv(p / "cleaned_meter_data.csv", index=False)

def save_summary(df, folder="output"):
    p = Path(folder)
    p.mkdir(exist_ok=True)
    df.to_csv(p / "building_summary.csv", index=False)

def write_summary_text(df, summary_df, folder="output"):
    p = Path(folder)
    p.mkdir(exist_ok=True)

    total = df["kwh"].sum()
    top = summary_df.sort_values("total_kwh", ascending=False).iloc[0]

    peak_df = df.groupby("timestamp")["kwh"].sum().reset_index()
    peak = peak_df.loc[peak_df["kwh"].idxmax()]

    text = f"""
Total Campus Consumption: {total:.2f} kWh
Highest Consuming Building: {top['building']} ({top['total_kwh']:.2f} kWh)
Peak Load Time: {peak['timestamp']} — {peak['kwh']:.2f} kWh
"""

    (p / "summary.txt").write_text(text.strip())
