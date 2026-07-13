import sys
import os 
import pandas as pd

def main():
    filename = sys.argv[1]
    if filename.endswith(".p"):
        filepath_without_ext = os.path.splitext(filename)[0]
        csv_filepath = filepath_without_ext + ".csv"
        pd.read_pickle(filename).to_csv(csv_filepath, index=False)
        print(f"Created: {csv_filepath}")
    else:
        print("Input pickle file with extensions .p")

if __name__ == "__main__":
    main()
