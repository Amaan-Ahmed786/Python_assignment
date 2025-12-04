# codefiles/aggregation.py
import pandas as pd

def calculate_daily_totals(df):
    df = df.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.set_index("timestamp")
    return df.groupby("building").resample("D")["kwh"].sum().reset_index()

def calculate_weekly_aggregates(df):
    df = df.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.set_index("timestamp")
    return df.groupby("building").resample("W")["kwh"].sum().reset_index()

def building_wise_summary(df):
    return df.groupby("building")["kwh"].agg(
        mean_kwh="mean",
        min_kwh="min",
        max_kwh="max",
        total_kwh="sum"
    ).reset_index()
