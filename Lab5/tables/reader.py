import os
import sys
import pandas as pd


def read_file(link):
    if not (os.path.exists(link)):
        sys.exit("No such file exists")
    if not(os.path.isfile(link)):
        sys.exit("No such file")
    return pd.read_csv(link)

