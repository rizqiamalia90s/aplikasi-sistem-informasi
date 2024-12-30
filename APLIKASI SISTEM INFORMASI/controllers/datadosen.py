import csv
import os

class DataDosen:
    def __init__(self):
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.csv_file = os.path.join(current_dir, 'assets', 'datadosen.csv')
        
    def get_all_dosen(self):
        try:
            with open(self.csv_file, mode='r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                return list(csv_reader)
        except Exception as e:
            print(f"Error: {str(e)}")
            return []
    
    def get_dosen_by_nidn(self, nidn):
        try:
            with open(self.csv_file, mode='r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    if row['nidn'] == nidn:
                        return row
                return None
        except Exception as e:
            print(f"Error: {str(e)}")
            return None 