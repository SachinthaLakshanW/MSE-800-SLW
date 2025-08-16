import pandas as pd

class CusProcessing:
    def __init__(self, input_file, parquet_file="output.parquet"):
        self.input_file = input_file
        self.parquet_file = parquet_file
        self.df = None

    def read_csv(self):
        """Read CSV file into DataFrame"""
        self.df = pd.read_csv(self.input_file)

    def save_parquet(self):
        """Save DataFrame as Parquet"""
        self.df.to_parquet(self.parquet_file, index=False)

    def compute_stats_table(self):
        """Compute max, min, mean, and absolute max for numeric columns and display as table"""
        numeric_cols = self.df.select_dtypes(include='number')
        stats_df = pd.DataFrame({
            'Max': numeric_cols.max(),
            'Min': numeric_cols.min(),
            'Mean': numeric_cols.mean(),
            'Abs Max': numeric_cols.abs().max()
        })
        print(stats_df)

def main():
    processor = CusProcessing("Wholesale_customers_data.csv")
    processor.read_csv()
    processor.save_parquet()
    processor.compute_stats_table()

if __name__ == "__main__":
    main()
