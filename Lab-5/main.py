# codefiles/main.py
from ingest import read_and_merge
from aggregation import calculate_daily_totals, calculate_weekly_aggregates, building_wise_summary
from models import BuildingManager
from visualize import create_dashboard
from export import save_cleaned, save_summary, write_summary_text

def run():
    df = read_and_merge("meter_inputs")
    if df.empty:
        print("No meter files found.")
        return

    daily = calculate_daily_totals(df)
    weekly = calculate_weekly_aggregates(df)
    summary = building_wise_summary(df)

    bm = BuildingManager()
    bm.load_from_dataframe(df)

    create_dashboard(daily, weekly, df)
    save_cleaned(df)
    save_summary(summary)
    write_summary_text(df, summary)

    print("Pipeline completed! Check the output folder.")

if __name__ == "__main__":
    run()
