import json
import csv
from pathlib import Path

def run(args):
    report = ReportGenerator()
    report.generate_txt_report()
    print("Reports module selected")

class ReportGenerator:
    def __init__(self):
        self.report_dir = Path("reports")

        self.txt_dir = self.report_dir / "txt"
        self.csv_dir = self.report_dir / "csv"
        self.json_dir = self.report_dir / "json"

        self.create_directories()

    def create_directories(self):
        self.txt_dir.mkdir(parents=True, exist_ok=True)
        self.csv_dir.mkdir(parents=True, exist_ok=True)
        self.json_dir.mkdir(parents=True, exist_ok=True)

    def generate_txt_report(self, filename, content):
        # creates report path, ex: reports/txt/system_report.txt
        report_file = self.txt_dir/filename
        # opens the file, "w" = write mode, creates the file if it doesn't exist, overwrites the file if it already exits
        with open(report_file, "w") as file:
            # writes the content
            file.write(content)
            # display success message
            print(f"TXT report generated: {report_file}")

    def generate_csv_report(self, filename, data):
            # creates report path, ex: reports/csv/system_report.csv
            report_file = self.csv_dir/filename
            # opens the file, "w" = write mode, newline="" = prevents blank lines between rows, the writer object is responsible for writing rows into the csv file, creates the file if it doesn't exist, overwrites the file if it already exits
            with open(report_file, "w", newline="") as file:
                # creates the csv writer
                writer = csv.writer(file)
                # writes each row
                for row in data:
                    writer.writerow(row)
                # display success message
                print(f"CSV report generated: {report_file}")

    def generate_json_report(self, filename, data):
            # creates report path, ex: reports/json/system_report.json
            report_file = self.json_dir/filename
            # opens the file, "w" = write mode, creates the file if it doesn't exist, overwrites the file if it already exits
            with open(report_file, "w") as file:
                # writes the json data, indent=4 parameter formats the json nicely for readability
                json.dump(data, file, indent=4)
                # display success message
                print(f"JSON report generated: {report_file}")

    
