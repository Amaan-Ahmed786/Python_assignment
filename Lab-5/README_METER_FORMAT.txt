# Meter File Format Guide

This folder contains all the raw energy meter CSV files used by the Campus Energy Dashboard project. 
Each file represents energy readings for one building for one month.

## File Naming Format:
<buildingName>_<YYYY-MM>.csv

Examples:
buildingA_2024-11.csv
buildingB_2024-11.csv

## CSV Structure:
Each file must contain the following two columns:

1. timestamp  → Date & time of the reading (ISO format)
2. kwh        → Energy consumed during that hour (float)

## Sample Format:

timestamp,kwh
2024-11-01 00:00:00,12.5
2024-11-01 01:00:00,14.2
2024-11-01 02:00:00,10.8

## Rules:
- The timestamp must be in "YYYY-MM-DD HH:MM:SS" format.
- kwh values should be numeric (float or integer).
- Each CSV file contains readings for only one building.
- No blank columns or extra spaces.
- No merged cells (plain CSV text only).

## Purpose:
These files are automatically read by the program. 
The ingest.py module extracts:
- Building name (from filename)
- Month (from timestamp)
- All meter readings (timestamp + kwh)

Ensure the format is consistent so the pipeline can run without errors.
