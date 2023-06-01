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
    df = pd.read_excel(io=filepath,header=None)
    data = {}

    data["sex"] = {}
    data["sex"]["male"] = [df.iloc[0,2],[df.iloc[4,2],df.iloc[5,2]]]
    data["sex"]["female"] = [df.iloc[0,3],[df.iloc[4,3],df.iloc[5,3]]]

    data["age"] = {}
    data["age"]["18-44yrs"] = [df.iloc[10,3],[df.iloc[14,3],df.iloc[15,3]]]
    data["age"]["44-65yrs"] = [df.iloc[10,4],[df.iloc[14,4],df.iloc[15,4]]]
    data["age"][">65yrs"] = [df.iloc[10,5],[df.iloc[14,5],df.iloc[15,5]]]

    data["race"] = {}
    
    # check if nan 
    if df.iloc[20,10]==df.iloc[20,10]:
        data["race"]["MA"] = [df.iloc[20,6],[df.iloc[24,6],df.iloc[25,6]]]
        data["race"]["OH"] = [df.iloc[20,7],[df.iloc[24,7],df.iloc[25,7]]]
        data["race"]["NHW"] = [df.iloc[20,8],[df.iloc[24,8],df.iloc[25,8]]]
        data["race"]["NHB"] = [df.iloc[20,9],[df.iloc[24,9],df.iloc[25,9]]]
        data["race"]["NHS"] = [df.iloc[20,10],[df.iloc[24,10],df.iloc[25,10]]]
        data["race"]["OR"] = [df.iloc[20,11],[df.iloc[24,11],df.iloc[25,11]]]
    else:
        data["race"]["MA"] = [df.iloc[20,5],[df.iloc[24,5],df.iloc[25,5]]]
        data["race"]["OH"] = [df.iloc[20,6],[df.iloc[24,6],df.iloc[25,6]]]
        data["race"]["NHW"] = [df.iloc[20,7],[df.iloc[24,7],df.iloc[25,7]]]
        data["race"]["NHB"] = [df.iloc[20,8],[df.iloc[24,8],df.iloc[25,8]]]
        data["race"]["NHS"] = [None]
        data["race"]["OR"] = [df.iloc[20,9],[df.iloc[24,9],df.iloc[25,9]]]


    data["edu"] = {}
    data["edu"]["<high school"] = [df.iloc[30,3],[df.iloc[34,3],df.iloc[35,3]]]
    data["edu"]["high school graduate and some college"] = [df.iloc[34,4],[df.iloc[30,4],df.iloc[35,4]]]
    data["edu"]["college graduate"] = [df.iloc[30,5],[df.iloc[34,5],df.iloc[35,5]]]

    data["bmi"] = {}
    data["bmi"]["bmi<18.5"] = [df.iloc[40,6],[df.iloc[44,6],df.iloc[45,6]]]
    data["bmi"]["bmi18.5-25.0"] = [df.iloc[40,7],[df.iloc[44,7],df.iloc[45,7]]]
    data["bmi"]["bmi25.0-30.0"] = [df.iloc[40,8],[df.iloc[44,8],df.iloc[45,8]]]
    data["bmi"]["bmi30.0-35.0"] = [df.iloc[40,9],[df.iloc[44,9],df.iloc[45,9]]]
    data["bmi"]["bmi35.0-40.0"] = [df.iloc[40,10],[df.iloc[44,10],df.iloc[45,10]]]
    data["bmi"]["bmi>=40"] = [df.iloc[40,11],[df.iloc[44,11],df.iloc[45, 11]]]

    data["wai"] = {}
    data["wai"]["wai-no"] = [df.iloc[50,2],[df.iloc[54,2],df.iloc[55,2]]]
    data["wai"]["wai-yes"] = [df.iloc[50,3],[df.iloc[54,3],df.iloc[55,3]]]

    data["insu"] = {}
    data["insu"]["insu-no"] = [df.iloc[60,2],[df.iloc[64,2],df.iloc[65,2]]]
    data["insu"]["insu-yes"] = [df.iloc[60,3],[df.iloc[64,3],df.iloc[65,3]]]

    data["pov"] = {}
    data["pov"]["pov-no"] = [df.iloc[70,2],[df.iloc[74,2],df.iloc[75,2]]]
    data["pov"]["pov-yes"] = [df.iloc[70,3],[df.iloc[74,3],df.iloc[75,3]]]

    data["smok"] = {}
    data["smok"]["smok-yes"] = [df.iloc[80,3],[df.iloc[84,3],df.iloc[85,3]]]
    data["smok"]["smok-no"] = [df.iloc[80,4],[df.iloc[84,4],df.iloc[85,5]]]
    data["smok"]["smok-unknown"] = [df.iloc[80,5],[df.iloc[84,5],df.iloc[85,5]]]

    data["phys"] = {}
    data["phys"]["phys-vigorous"] = [df.iloc[90,3],[df.iloc[94,3],df.iloc[95,3]]]
    data["phys"]["phys-moderate"] = [df.iloc[90,4],[df.iloc[94,4],df.iloc[95,5]]]
    data["phys"]["phys-no"] = [df.iloc[90,5],[df.iloc[94,5],df.iloc[95,5]]]

    data["overall"] = {}
    data["overall"]["overall"] = [df.iloc[100,1],[df.iloc[104,1],df.iloc[105,1]]]


    # for key in data.keys():
    #     print(key)
    #     for key1 in data[key].keys():
    #         print(key1,end="  ")
    #         print(data[key][key1])
    return data

if __name__ == "__main__":
    data_ipre = {}
    for filepath in target_file_list["ipre"]:
        data = ipre_fecth(path_to_datadir + filepath)
        for key in data.keys():
            if key in data_ipre.keys():
                for key1 in data[key].keys():
                    data_ipre[key][key1] += data[key][key1]
            else:
                data_ipre[key] = data[key]

    for key in data_ipre.keys():
        print(key)
        for key1 in data_ipre[key].keys():
            print(key1,end="  ")
            print(data_ipre[key][key1])


