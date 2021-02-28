""" Transform exported contact list 
from Google contacts to Outlook.
"""

import pandas as pd
import argparse

def parse_arguments():
    """ Argument Parser
    """
    parser = argparse.ArgumentParser(description='Get file name.')
    parser.add_argument('--file', type=str,
                    help='Path to file that is to be processed.')
    args = parser.parse_args()

    return args

def import_file(filename):
    """ File Importer
    """
    try:
        df = pd.read_csv(filename ,sep=",",index_col=False, encoding="utf-8",dtype=str)

        return df
    except FileNotFoundError:
        print(f"File not found: {filename}")
        exit()

def split_timestamp(string):
    """ Split timestamp in German form
    """
    year = int(string.split(".")[2])
    month = int(string.split(".")[1])
    day =int(string.split(".")[0])

    return year, month, day

def convert_timestamp(timestamp_str):
    """ Convert timestamp in string format to 
    American style timestamp in string format
    """
    try:
        year, month, day = split_timestamp(timestamp_str)
        timestamp = pd.Timestamp(day=day, month=month, year=year)
        timestamp = timestamp.strftime(format = "%Y-%m-%d")
    except:
        timestamp = float("nan")

    return timestamp

def transform_timestamp(df):
    """ Apply functions to transform the timestamps
    """
    df["Birthday"] = df["Birthday"].apply(convert_timestamp)
    df["Anniversary"] = df["Anniversary"].apply(convert_timestamp)
    
    return df

def transform_address(df):
    """  Remove fields with full address and also 
    notes when there is an address available
    """
    df["Home Address"] = float("nan")
    df["Other Address"] = float("nan")
    df["Notes"] = df.loc[df.isna()["Home Street"] == False,"Notes"] = float("nan")

    return df

def rem_double_label_delimiters(label):
    """ Remove double delimiters due to label removal
    """
    if label != "":
        if label[-1] == ";":
            label = label[:-1]


def remove_mycontacts_label(df):
    """ Remove the label 'myContacts' that is added 
    to every contact during export.
    """
    df["Categories"] = df["Categories"].str.replace("myContacts", "").replace(";;", ";")
    df["Categories"] = df["Categories"].apply(rem_double_label_delimiters)

    return df

def main():
    """ Main function
    """
    args = parse_arguments()
    df = import_file(args.file)
    df = transform_timestamp(df)
    df = transform_address(df)
    df = remove_mycontacts_label(df)

    # New filename = old_filename + "_outlook"
    new_filename = f"{args.file.split('.')[-2]}_outlook.{args.file.split('.')[-1]}"
    df.to_csv(new_filename,sep=",", encoding="utf-8",index=False)

    print(f"New file: '{new_filename}' was created successfully!")


if __name__ == "__main__":
    main()