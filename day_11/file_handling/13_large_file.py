import csv

file_path = (
    r"C:\Users\ronin\Documents\Codes\python_teaching\day_11\data\people-2000000.csv"
)


def read_csv_data():
    with open(file_path, "r", encoding="utf-8") as f_obj:
        yield from csv.DictReader(f_obj)


gen = read_csv_data()
print(next(gen))
print(next(gen))
print(next(gen))
