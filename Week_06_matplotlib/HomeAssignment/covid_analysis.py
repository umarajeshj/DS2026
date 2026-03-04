import pandas as pd

class CovidAnalysis:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        print("File loaded successfully!")

    def get_top_n(self, column, n=10):
        """Returns top N rows based on a specific column."""
        return self.df.nlargest(n, column)
