import sys
import os
import re

import pandas as pd

def get_csv_filepath(filepath:str):
    filepath_without_ext = os.path.splitext(filepath)[0]
    return filepath_without_ext + ".csv"

def remove_list_braces_quotes(list_str:str):
    return re.sub(r"[\[\]\']", "", list_str)    

def convert_pickle_to_csv(filepath:str):
    csv_filepath= get_csv_filepath(filepath)
    pd.read_pickle(filepath).to_csv(csv_filepath, index=False)

def print_conversion_message(created_files: list[str],failed_created_files:list[str]):
    created_files_count = len(created_files)
    failed_conversions_count = len(failed_created_files)
    has_created_files = created_files_count > 0
    has_failed_conversions = failed_conversions_count > 0

    if created_files_count == 0 and failed_conversions_count == 0:
        print("No files have already been converted")
        return

    message = "\n"
    if has_created_files:
        message += f"\033[1mConverted Files\033[0m: {created_files_count}\n"
    if has_failed_conversions:
        message += f"\033[1mFailed Conversions\033[0m: {failed_conversions_count}\n"
    if has_created_files and has_failed_conversions:
        message += "\n"
    if has_created_files:
        message += f"\033[1mCreated Files\033[0m: {remove_list_braces_quotes(f"{created_files}")}\n"
    if has_failed_conversions:
        message += f"\033[1mFailed Files\033[0m: {remove_list_braces_quotes(f"{failed_created_files}")}"
    print(message)

def main():
    files_agv = sys.argv[1:]
    created_files = []
    failed_created_files = []
    print("Attempting... file conversion\n")
    for filepath in files_agv:
        csv_filepath= get_csv_filepath(filepath)
        file_exists = os.path.isfile(csv_filepath)

        if file_exists:
            continue
        elif filepath.endswith(".p"):
            try:
                convert_pickle_to_csv(filepath)
                created_files.append(csv_filepath)
            except IOError as e:
                print(f"An I/O error occurred: {e}")
                print(f"Failed to convert {filepath} to {csv_filepath}")
                failed_created_files.append(filepath)
    print_conversion_message(created_files, failed_created_files)

if __name__ == "__main__":
    main()
