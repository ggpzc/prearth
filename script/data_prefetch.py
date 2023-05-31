import pandas as pd
import os

path_to_datadir = "data/"

target_file_list = {
    "ipre" : [
        "ipre99.xlsx",
        "ipre01.xlsx",
        "ipre03.xlsx",
        "ipre05.xlsx",
        "ipre07.xlsx",
        "ipre09.xlsx",
        "ipre11.xlsx",
        "ipre13.xlsx",
        "ipre15.xlsx",
        "ipre17.xlsx",
        "ipre19.xlsx",        
    ],

    "iartpre" : [
        "iartypre99.xlsx",
        "iartypre01.xlsx",
        "iartypre03.xlsx",
        "iartypre05.xlsx",
        "iartypre07.xlsx",
        "iartypre09.xlsx",
        "iartypre11.xlsx",
        "iartypre13.xlsx",
        "iartypre15.xlsx",
        "iartypre17.xlsx",
        "iartypre19.xlsx",     
    ]
}


def ipre_fecth(filepath):
    if not os.path.exists(filepath):
        print("{} not exists".format(filepath))
        return 
    df = pd.read_excel(io=filepath)
    print(df.columns)


if __name__ == "__main__":
    # ipre_fecth(path_to_datadir + target_file_list["ipre"][0])
    pass
