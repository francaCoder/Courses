from csv import DictReader
with open("csv_exemplo (2).csv") as file:
    class DictReader:
        reader_csv = DictReader(file)
        for line in reader_csv:
            print(line["oderID"] + line["First Name"])