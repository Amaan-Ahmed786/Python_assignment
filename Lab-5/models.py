# codefiles/models.py
from dataclasses import dataclass, field
import pandas as pd
from datetime import datetime

@dataclass
class MeterReading:
    timestamp: datetime
    kwh: float

@dataclass
class Building:
    name: str
    readings: list = field(default_factory=list)

    def add_reading(self, ts, kwh):
        self.readings.append(MeterReading(ts, float(kwh)))

    def df(self):
        return pd.DataFrame({
            "timestamp": [r.timestamp for r in self.readings],
            "kwh": [r.kwh for r in self.readings]
        })

    def report(self):
        df = self.df()
        if df.empty:
            return {}
        return {
            "building": self.name,
            "total_kwh": df["kwh"].sum(),
            "mean_kwh": df["kwh"].mean(),
            "min_kwh": df["kwh"].min(),
            "max_kwh": df["kwh"].max(),
        }

class BuildingManager:
    def __init__(self):
        self.buildings = {}

    def get(self, name):
        if name not in self.buildings:
            self.buildings[name] = Building(name)
        return self.buildings[name]

    def load_from_dataframe(self, df):
        for _, row in df.iterrows():
            b = self.get(row["building"])
            b.add_reading(row["timestamp"], row["kwh"])

    def summary(self):
        return pd.DataFrame([b.report() for b in self.buildings.values()])
