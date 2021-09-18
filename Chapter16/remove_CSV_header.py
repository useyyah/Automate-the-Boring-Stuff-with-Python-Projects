import csv
import os

os.makedirs("header_removed", exist_ok=True)

# Loop through every file in the current working directory.
for csvFilename in os.listdir("."):
    if not csvFilename.endswith(".csv"):
        continue  # skip non-csv files

    print(f"Removing header from {csvFilename}...")

    # Read the CSV file in (skipping first row).
    csv_rows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue  # skip first row
        csv_rows.append(row)
    csvFileObj.close()

    # Write out the CSV file.
    csvFileObj = open(os.path.join("header_removed", csvFilename), "w", newline="")
    csvWriter = csv.writer(csvFileObj)
    for row in csv_rows:
        csvWriter.writerow(row)
    csvFileObj.close()
