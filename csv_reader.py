import csv

class CSVLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> list[dict]:
        rows = []
        with open(self.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)
        return rows
