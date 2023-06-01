import pandas as pd
import os

path_to_datadir = "data/"



def save_to_json(raw_data,filepath):
    import json
    new_data = {
        "years": [],
        "keys": [],
        "data": [],
    }
    for key in raw_data.keys():
        new_data["keys"].append(key)
        new_data["data"].append([])
        data = raw_data[key]
        print(data)
        years = ["{}-{}".format(1999+i*2,2000+i*2) for i in range(int(len(data)/2))]
        miss_cnt = 0
        for i in range(int(len(data)/2)):
            if data[2*i]:
                new_data["data"][-1].append([data[2*i], data[2*i+1][0], data[2*i+1][1]])
            else:
                miss_cnt += 1
        new_data["years"] = years[miss_cnt:]
    with open(filepath,"w") as f:
        json.dump(new_data,f)


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
    # data["bmi"]["bmi<18.5"] = [df.iloc[40,6],[df.iloc[44,6],df.iloc[45,6]]]
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


def iartypre_fetch_99_07(filepath):
    if not os.path.exists(filepath):
        print("{} not exists".format(filepath))
        return 
    df = pd.read_excel(io=filepath,header=None)

    data_RA = {}
    data_OA = {}
    data_OT = {}


    data_RA["sex"] = {}
    data_RA["sex"]["male"] = [df.iloc[3*0,2],[df.iloc[3*0+4,2],df.iloc[3*0+5,2]]]
    data_RA["sex"]["female"] = [df.iloc[3*0,3],[df.iloc[3*0+4,3],df.iloc[3*0+5,3]]]

    data_RA["age"] = {}
    data_RA["age"]["18-44yrs"] = [df.iloc[3*10,3],[df.iloc[3*10+4,3],df.iloc[3*10+5,3]]]
    data_RA["age"]["44-65yrs"] = [df.iloc[3*10,4],[df.iloc[3*10+4,4],df.iloc[3*10+5,4]]]
    data_RA["age"][">65yrs"] = [df.iloc[3*10,5],[df.iloc[3*10+4,5],df.iloc[3*10+5,5]]]

    data_RA["race"] = {}
    
    # check if nan 
    if df.iloc[3*20,10]==df.iloc[3*20,10]:
        data_RA["race"]["MA"] = [df.iloc[3*20,6],[df.iloc[3*20+4,6],df.iloc[3*20+5,6]]]
        data_RA["race"]["OH"] = [df.iloc[3*20,7],[df.iloc[3*20+4,7],df.iloc[3*20+5,7]]]
        data_RA["race"]["NHW"] = [df.iloc[3*20,8],[df.iloc[3*20+4,8],df.iloc[3*20+5,8]]]
        data_RA["race"]["NHB"] = [df.iloc[3*20,9],[df.iloc[3*20+4,9],df.iloc[3*20+5,9]]]
        data_RA["race"]["NHS"] = [df.iloc[3*20,10],[df.iloc[3*20+4,10],df.iloc[3*20+5,10]]]
        data_RA["race"]["OR"] = [df.iloc[3*20,11],[df.iloc[3*20+4,11],df.iloc[3*20+5,11]]]
    else:
        data_RA["race"]["MA"] = [df.iloc[3*20,5],[df.iloc[3*20+4,5],df.iloc[3*20+5,5]]]
        data_RA["race"]["OH"] = [df.iloc[3*20,6],[df.iloc[3*20+4,6],df.iloc[3*20+5,6]]]
        data_RA["race"]["NHW"] = [df.iloc[3*20,7],[df.iloc[3*20+4,7],df.iloc[3*20+5,7]]]
        data_RA["race"]["NHB"] = [df.iloc[3*20,8],[df.iloc[3*20+4,8],df.iloc[3*20+5,8]]]
        data_RA["race"]["NHS"] = [None]
        data_RA["race"]["OR"] = [df.iloc[3*20,9],[df.iloc[3*20+4,9],df.iloc[3*20+5,9]]]


    data_RA["edu"] = {}
    data_RA["edu"]["<high school"] = [df.iloc[3*30,3],[df.iloc[3*30+4,3],df.iloc[3*30+5,3]]]
    data_RA["edu"]["high school graduate and some college"] = [df.iloc[3*30+4,4],[df.iloc[3*30,4],df.iloc[3*30+5,4]]]
    data_RA["edu"]["college graduate"] = [df.iloc[3*30,5],[df.iloc[3*30+4,5],df.iloc[3*30+5,5]]]

    data_RA["bmi"] = {}
    # data_RA["bmi"]["bmi<18.5"] = [df.iloc[3*40,6],[df.iloc[3*40+4,6],df.iloc[3*40+5,6]]]
    data_RA["bmi"]["bmi18.5-25.0"] = [df.iloc[3*40,7],[df.iloc[3*40+4,7],df.iloc[3*40+5,7]]]
    data_RA["bmi"]["bmi25.0-30.0"] = [df.iloc[3*40,8],[df.iloc[3*40+4,8],df.iloc[3*40+5,8]]]
    data_RA["bmi"]["bmi30.0-35.0"] = [df.iloc[3*40,9],[df.iloc[3*40+4,9],df.iloc[3*40+5,9]]]
    data_RA["bmi"]["bmi35.0-40.0"] = [df.iloc[3*40,10],[df.iloc[3*40+4,10],df.iloc[3*40+5,10]]]
    data_RA["bmi"]["bmi>=40"] = [df.iloc[3*40,11],[df.iloc[3*40+4,11],df.iloc[3*40+5, 11]]]

    data_RA["wai"] = {}
    data_RA["wai"]["wai-no"] = [df.iloc[3*50,2],[df.iloc[3*50+4,2],df.iloc[3*50+5,2]]]
    data_RA["wai"]["wai-yes"] = [df.iloc[3*50,3],[df.iloc[3*50+4,3],df.iloc[3*50+5,3]]]

    data_RA["insu"] = {}
    data_RA["insu"]["insu-no"] = [df.iloc[3*60,2],[df.iloc[3*60+4,2],df.iloc[3*60+5,2]]]
    data_RA["insu"]["insu-yes"] = [df.iloc[3*60,3],[df.iloc[3*60+4,3],df.iloc[3*60+5,3]]]

    data_RA["pov"] = {}
    data_RA["pov"]["pov-no"] = [df.iloc[3*70,2],[df.iloc[3*70+4,2],df.iloc[3*70+5,2]]]
    data_RA["pov"]["pov-yes"] = [df.iloc[3*70,3],[df.iloc[3*70+4,3],df.iloc[3*70+5,3]]]

    data_RA["smok"] = {}
    data_RA["smok"]["smok-yes"] = [df.iloc[3*80,3],[df.iloc[3*80+4,3],df.iloc[3*80+5,3]]]
    data_RA["smok"]["smok-no"] = [df.iloc[3*80,4],[df.iloc[3*80+4,4],df.iloc[3*80+5,5]]]
    data_RA["smok"]["smok-unknown"] = [df.iloc[3*80,5],[df.iloc[3*80+4,5],df.iloc[3*80+5,5]]]

    data_RA["phys"] = {}
    data_RA["phys"]["phys-vigorous"] = [df.iloc[3*90,3],[df.iloc[3*90+4,3],df.iloc[3*90+5,3]]]
    data_RA["phys"]["phys-moderate"] = [df.iloc[3*90,4],[df.iloc[3*90+4,4],df.iloc[3*90+5,5]]]
    data_RA["phys"]["phys-no"] = [df.iloc[3*90,5],[df.iloc[3*90+4,5],df.iloc[3*90+5,5]]]

    data_RA["overall"] = {}
    data_RA["overall"]["overall"] = [df.iloc[3*100,1],[df.iloc[3*100+4,1],df.iloc[3*100+5,1]]]



    data_OA["sex"] = {}
    data_OA["sex"]["male"] = [df.iloc[10+3*0,2],[df.iloc[10+3*0+4,2],df.iloc[10+3*0+5,2]]]
    data_OA["sex"]["female"] = [df.iloc[10+3*0,3],[df.iloc[10+3*0+4,3],df.iloc[10+3*0+5,3]]]

    data_OA["age"] = {}
    data_OA["age"]["18-44yrs"] = [df.iloc[10+3*10,3],[df.iloc[10+3*10+4,3],df.iloc[10+3*10+5,3]]]
    data_OA["age"]["44-65yrs"] = [df.iloc[10+3*10,4],[df.iloc[10+3*10+4,4],df.iloc[10+3*10+5,4]]]
    data_OA["age"][">65yrs"] = [df.iloc[10+3*10,5],[df.iloc[10+3*10+4,5],df.iloc[10+3*10+5,5]]]

    data_OA["race"] = {}
    
    # check if nan 
    if df.iloc[10+3*20,10]==df.iloc[10+3*20,10]:
        data_OA["race"]["MA"] = [df.iloc[10+3*20,6],[df.iloc[10+3*20+4,6],df.iloc[10+3*20+5,6]]]
        data_OA["race"]["OH"] = [df.iloc[10+3*20,7],[df.iloc[10+3*20+4,7],df.iloc[10+3*20+5,7]]]
        data_OA["race"]["NHW"] = [df.iloc[10+3*20,8],[df.iloc[10+3*20+4,8],df.iloc[10+3*20+5,8]]]
        data_OA["race"]["NHB"] = [df.iloc[10+3*20,9],[df.iloc[10+3*20+4,9],df.iloc[10+3*20+5,9]]]
        data_OA["race"]["NHS"] = [df.iloc[10+3*20,10],[df.iloc[10+3*20+4,10],df.iloc[10+3*20+5,10]]]
        data_OA["race"]["OR"] = [df.iloc[10+3*20,11],[df.iloc[10+3*20+4,11],df.iloc[10+3*20+5,11]]]
    else:
        data_OA["race"]["MA"] = [df.iloc[10+3*20,5],[df.iloc[10+3*20+4,5],df.iloc[10+3*20+5,5]]]
        data_OA["race"]["OH"] = [df.iloc[10+3*20,6],[df.iloc[10+3*20+4,6],df.iloc[10+3*20+5,6]]]
        data_OA["race"]["NHW"] = [df.iloc[10+3*20,7],[df.iloc[10+3*20+4,7],df.iloc[10+3*20+5,7]]]
        data_OA["race"]["NHB"] = [df.iloc[10+3*20,8],[df.iloc[10+3*20+4,8],df.iloc[10+3*20+5,8]]]
        data_OA["race"]["NHS"] = [None]
        data_OA["race"]["OR"] = [df.iloc[10+3*20,9],[df.iloc[10+3*20+4,9],df.iloc[10+3*20+5,9]]]


    data_OA["edu"] = {}
    data_OA["edu"]["<high school"] = [df.iloc[10+3*30,3],[df.iloc[10+3*30+4,3],df.iloc[10+3*30+5,3]]]
    data_OA["edu"]["high school graduate and some college"] = [df.iloc[10+3*30+4,4],[df.iloc[10+3*30,4],df.iloc[10+3*30+5,4]]]
    data_OA["edu"]["college graduate"] = [df.iloc[10+3*30,5],[df.iloc[10+3*30+4,5],df.iloc[10+3*30+5,5]]]

    data_OA["bmi"] = {}
    # data_OA["bmi"]["bmi<18.5"] = [df.iloc[10+3*40,6],[df.iloc[10+3*40+4,6],df.iloc[10+3*40+5,6]]]
    data_OA["bmi"]["bmi18.5-25.0"] = [df.iloc[10+3*40,7],[df.iloc[10+3*40+4,7],df.iloc[10+3*40+5,7]]]
    data_OA["bmi"]["bmi25.0-30.0"] = [df.iloc[10+3*40,8],[df.iloc[10+3*40+4,8],df.iloc[10+3*40+5,8]]]
    data_OA["bmi"]["bmi30.0-35.0"] = [df.iloc[10+3*40,9],[df.iloc[10+3*40+4,9],df.iloc[10+3*40+5,9]]]
    data_OA["bmi"]["bmi35.0-40.0"] = [df.iloc[10+3*40,10],[df.iloc[10+3*40+4,10],df.iloc[10+3*40+5,10]]]
    data_OA["bmi"]["bmi>=40"] = [df.iloc[10+3*40,11],[df.iloc[10+3*40+4,11],df.iloc[10+3*40+5, 11]]]

    data_OA["wai"] = {}
    data_OA["wai"]["wai-no"] = [df.iloc[10+3*50,2],[df.iloc[10+3*50+4,2],df.iloc[10+3*50+5,2]]]
    data_OA["wai"]["wai-yes"] = [df.iloc[10+3*50,3],[df.iloc[10+3*50+4,3],df.iloc[10+3*50+5,3]]]

    data_OA["insu"] = {}
    data_OA["insu"]["insu-no"] = [df.iloc[10+3*60,2],[df.iloc[10+3*60+4,2],df.iloc[10+3*60+5,2]]]
    data_OA["insu"]["insu-yes"] = [df.iloc[10+3*60,3],[df.iloc[10+3*60+4,3],df.iloc[10+3*60+5,3]]]

    data_OA["pov"] = {}
    data_OA["pov"]["pov-no"] = [df.iloc[10+3*70,2],[df.iloc[10+3*70+4,2],df.iloc[10+3*70+5,2]]]
    data_OA["pov"]["pov-yes"] = [df.iloc[10+3*70,3],[df.iloc[10+3*70+4,3],df.iloc[10+3*70+5,3]]]

    data_OA["smok"] = {}
    data_OA["smok"]["smok-yes"] = [df.iloc[10+3*80,3],[df.iloc[10+3*80+4,3],df.iloc[10+3*80+5,3]]]
    data_OA["smok"]["smok-no"] = [df.iloc[10+3*80,4],[df.iloc[10+3*80+4,4],df.iloc[10+3*80+5,5]]]
    data_OA["smok"]["smok-unknown"] = [df.iloc[10+3*80,5],[df.iloc[10+3*80+4,5],df.iloc[10+3*80+5,5]]]

    data_OA["phys"] = {}
    data_OA["phys"]["phys-vigorous"] = [df.iloc[10+3*90,3],[df.iloc[10+3*90+4,3],df.iloc[10+3*90+5,3]]]
    data_OA["phys"]["phys-moderate"] = [df.iloc[10+3*90,4],[df.iloc[10+3*90+4,4],df.iloc[10+3*90+5,5]]]
    data_OA["phys"]["phys-no"] = [df.iloc[10+3*90,5],[df.iloc[10+3*90+4,5],df.iloc[10+3*90+5,5]]]

    data_OA["overall"] = {}
    data_OA["overall"]["overall"] = [df.iloc[10+3*100,1],[df.iloc[10+3*100+4,1],df.iloc[10+3*100+5,1]]]




    data_OT["sex"] = {}
    data_OT["sex"]["male"] = [df.iloc[20+3*0,2],[df.iloc[20+3*0+4,2],df.iloc[20+3*0+5,2]]]
    data_OT["sex"]["female"] = [df.iloc[20+3*0,3],[df.iloc[20+3*0+4,3],df.iloc[20+3*0+5,3]]]

    data_OT["age"] = {}
    data_OT["age"]["18-44yrs"] = [df.iloc[20+3*10,3],[df.iloc[20+3*10+4,3],df.iloc[20+3*10+5,3]]]
    data_OT["age"]["44-65yrs"] = [df.iloc[20+3*10,4],[df.iloc[20+3*10+4,4],df.iloc[20+3*10+5,4]]]
    data_OT["age"][">65yrs"] = [df.iloc[20+3*10,5],[df.iloc[20+3*10+4,5],df.iloc[20+3*10+5,5]]]

    data_OT["race"] = {}
    
    # check if nan 
    if df.iloc[20+3*20,10]==df.iloc[20+3*20,10]:
        data_OT["race"]["MA"] = [df.iloc[20+3*20,6],[df.iloc[20+3*20+4,6],df.iloc[20+3*20+5,6]]]
        data_OT["race"]["OH"] = [df.iloc[20+3*20,7],[df.iloc[20+3*20+4,7],df.iloc[20+3*20+5,7]]]
        data_OT["race"]["NHW"] = [df.iloc[20+3*20,8],[df.iloc[20+3*20+4,8],df.iloc[20+3*20+5,8]]]
        data_OT["race"]["NHB"] = [df.iloc[20+3*20,9],[df.iloc[20+3*20+4,9],df.iloc[20+3*20+5,9]]]
        data_OT["race"]["NHS"] = [df.iloc[20+3*20,10],[df.iloc[20+3*20+4,10],df.iloc[20+3*20+5,10]]]
        data_OT["race"]["OR"] = [df.iloc[20+3*20,11],[df.iloc[20+3*20+4,11],df.iloc[20+3*20+5,11]]]
    else:
        data_OT["race"]["MA"] = [df.iloc[20+3*20,5],[df.iloc[20+3*20+4,5],df.iloc[20+3*20+5,5]]]
        data_OT["race"]["OH"] = [df.iloc[20+3*20,6],[df.iloc[20+3*20+4,6],df.iloc[20+3*20+5,6]]]
        data_OT["race"]["NHW"] = [df.iloc[20+3*20,7],[df.iloc[20+3*20+4,7],df.iloc[20+3*20+5,7]]]
        data_OT["race"]["NHB"] = [df.iloc[20+3*20,8],[df.iloc[20+3*20+4,8],df.iloc[20+3*20+5,8]]]
        data_OT["race"]["NHS"] = [None]
        data_OT["race"]["OR"] = [df.iloc[20+3*20,9],[df.iloc[20+3*20+4,9],df.iloc[20+3*20+5,9]]]


    data_OT["edu"] = {}
    data_OT["edu"]["<high school"] = [df.iloc[20+3*30,3],[df.iloc[20+3*30+4,3],df.iloc[20+3*30+5,3]]]
    data_OT["edu"]["high school graduate and some college"] = [df.iloc[20+3*30+4,4],[df.iloc[20+3*30,4],df.iloc[20+3*30+5,4]]]
    data_OT["edu"]["college graduate"] = [df.iloc[20+3*30,5],[df.iloc[20+3*30+4,5],df.iloc[20+3*30+5,5]]]

    data_OT["bmi"] = {}
    # data_OT["bmi"]["bmi<18.5"] = [df.iloc[20+3*40,6],[df.iloc[20+3*40+4,6],df.iloc[20+3*40+5,6]]]
    data_OT["bmi"]["bmi18.5-25.0"] = [df.iloc[20+3*40,7],[df.iloc[20+3*40+4,7],df.iloc[20+3*40+5,7]]]
    data_OT["bmi"]["bmi25.0-30.0"] = [df.iloc[20+3*40,8],[df.iloc[20+3*40+4,8],df.iloc[20+3*40+5,8]]]
    data_OT["bmi"]["bmi30.0-35.0"] = [df.iloc[20+3*40,9],[df.iloc[20+3*40+4,9],df.iloc[20+3*40+5,9]]]
    data_OT["bmi"]["bmi35.0-40.0"] = [df.iloc[20+3*40,10],[df.iloc[20+3*40+4,10],df.iloc[20+3*40+5,10]]]
    data_OT["bmi"]["bmi>=40"] = [df.iloc[20+3*40,11],[df.iloc[20+3*40+4,11],df.iloc[20+3*40+5, 11]]]

    data_OT["wai"] = {}
    data_OT["wai"]["wai-no"] = [df.iloc[20+3*50,2],[df.iloc[20+3*50+4,2],df.iloc[20+3*50+5,2]]]
    data_OT["wai"]["wai-yes"] = [df.iloc[20+3*50,3],[df.iloc[20+3*50+4,3],df.iloc[20+3*50+5,3]]]

    data_OT["insu"] = {}
    data_OT["insu"]["insu-no"] = [df.iloc[20+3*60,2],[df.iloc[20+3*60+4,2],df.iloc[20+3*60+5,2]]]
    data_OT["insu"]["insu-yes"] = [df.iloc[20+3*60,3],[df.iloc[20+3*60+4,3],df.iloc[20+3*60+5,3]]]

    data_OT["pov"] = {}
    data_OT["pov"]["pov-no"] = [df.iloc[20+3*70,2],[df.iloc[20+3*70+4,2],df.iloc[20+3*70+5,2]]]
    data_OT["pov"]["pov-yes"] = [df.iloc[20+3*70,3],[df.iloc[20+3*70+4,3],df.iloc[20+3*70+5,3]]]

    data_OT["smok"] = {}
    data_OT["smok"]["smok-yes"] = [df.iloc[20+3*80,3],[df.iloc[20+3*80+4,3],df.iloc[20+3*80+5,3]]]
    data_OT["smok"]["smok-no"] = [df.iloc[20+3*80,4],[df.iloc[20+3*80+4,4],df.iloc[20+3*80+5,5]]]
    data_OT["smok"]["smok-unknown"] = [df.iloc[20+3*80,5],[df.iloc[20+3*80+4,5],df.iloc[20+3*80+5,5]]]

    data_OT["phys"] = {}
    data_OT["phys"]["phys-vigorous"] = [df.iloc[20+3*90,3],[df.iloc[20+3*90+4,3],df.iloc[20+3*90+5,3]]]
    data_OT["phys"]["phys-moderate"] = [df.iloc[20+3*90,4],[df.iloc[20+3*90+4,4],df.iloc[20+3*90+5,5]]]
    data_OT["phys"]["phys-no"] = [df.iloc[20+3*90,5],[df.iloc[20+3*90+4,5],df.iloc[20+3*90+5,5]]]

    data_OT["overall"] = {}
    data_OT["overall"]["overall"] = [df.iloc[20+3*100,1],[df.iloc[20+3*100+4,1],df.iloc[20+3*100+5,1]]]


    # for key in data_OT.keys():
    #     print(key)
    #     for key1 in data_OT[key].keys():
    #         print(key1,end="  ")
    #         print(data_OT[key][key1])

    return data_RA,data_OA,data_OT


def iartypre_fetch_09_19(filepath):
    if not os.path.exists(filepath):
        print("{} not exists".format(filepath))
        return 
    df = pd.read_excel(io=filepath,header=None)

    data_RA = {}
    data_OA = {}
    data_PA = {}
    data_OT = {}


    data_RA["sex"] = {}
    data_RA["sex"]["male"] = [df.iloc[10+4*0,2],[df.iloc[10+4*0+4,2],df.iloc[10+4*0+5,2]]]
    data_RA["sex"]["female"] = [df.iloc[10+4*0,3],[df.iloc[10+4*0+4,3],df.iloc[10+4*0+5,3]]]

    data_RA["age"] = {}
    data_RA["age"]["18-44yrs"] = [df.iloc[10+4*10,3],[df.iloc[10+4*10+4,3],df.iloc[10+4*10+5,3]]]
    data_RA["age"]["44-65yrs"] = [df.iloc[10+4*10,4],[df.iloc[10+4*10+4,4],df.iloc[10+4*10+5,4]]]
    data_RA["age"][">65yrs"] = [df.iloc[10+4*10,5],[df.iloc[10+4*10+4,5],df.iloc[10+4*10+5,5]]]

    data_RA["race"] = {}
    
    # check if nan 
    if df.iloc[10+4*20,10]==df.iloc[10+4*20,10]:
        data_RA["race"]["MA"] = [df.iloc[10+4*20,6],[df.iloc[10+4*20+4,6],df.iloc[10+4*20+5,6]]]
        data_RA["race"]["OH"] = [df.iloc[10+4*20,7],[df.iloc[10+4*20+4,7],df.iloc[10+4*20+5,7]]]
        data_RA["race"]["NHW"] = [df.iloc[10+4*20,8],[df.iloc[10+4*20+4,8],df.iloc[10+4*20+5,8]]]
        data_RA["race"]["NHB"] = [df.iloc[10+4*20,9],[df.iloc[10+4*20+4,9],df.iloc[10+4*20+5,9]]]
        data_RA["race"]["NHS"] = [df.iloc[10+4*20,10],[df.iloc[10+4*20+4,10],df.iloc[10+4*20+5,10]]]
        data_RA["race"]["OR"] = [df.iloc[10+4*20,11],[df.iloc[10+4*20+4,11],df.iloc[10+4*20+5,11]]]
    else:
        data_RA["race"]["MA"] = [df.iloc[10+4*20,5],[df.iloc[10+4*20+4,5],df.iloc[10+4*20+5,5]]]
        data_RA["race"]["OH"] = [df.iloc[10+4*20,6],[df.iloc[10+4*20+4,6],df.iloc[10+4*20+5,6]]]
        data_RA["race"]["NHW"] = [df.iloc[10+4*20,7],[df.iloc[10+4*20+4,7],df.iloc[10+4*20+5,7]]]
        data_RA["race"]["NHB"] = [df.iloc[10+4*20,8],[df.iloc[10+4*20+4,8],df.iloc[10+4*20+5,8]]]
        data_RA["race"]["NHS"] = [None]
        data_RA["race"]["OR"] = [df.iloc[10+4*20,9],[df.iloc[10+4*20+4,9],df.iloc[10+4*20+5,9]]]


    data_RA["edu"] = {}
    data_RA["edu"]["<high school"] = [df.iloc[10+4*30,3],[df.iloc[10+4*30+4,3],df.iloc[10+4*30+5,3]]]
    data_RA["edu"]["high school graduate and some college"] = [df.iloc[10+4*30+4,4],[df.iloc[10+4*30,4],df.iloc[10+4*30+5,4]]]
    data_RA["edu"]["college graduate"] = [df.iloc[10+4*30,5],[df.iloc[10+4*30+4,5],df.iloc[10+4*30+5,5]]]

    data_RA["bmi"] = {}
    # data_RA["bmi"]["bmi<18.5"] = [df.iloc[10+4*40,6],[df.iloc[10+4*40+4,6],df.iloc[10+4*40+5,6]]]
    data_RA["bmi"]["bmi18.5-25.0"] = [df.iloc[10+4*40,7],[df.iloc[10+4*40+4,7],df.iloc[10+4*40+5,7]]]
    data_RA["bmi"]["bmi25.0-30.0"] = [df.iloc[10+4*40,8],[df.iloc[10+4*40+4,8],df.iloc[10+4*40+5,8]]]
    data_RA["bmi"]["bmi30.0-35.0"] = [df.iloc[10+4*40,9],[df.iloc[10+4*40+4,9],df.iloc[10+4*40+5,9]]]
    data_RA["bmi"]["bmi35.0-40.0"] = [df.iloc[10+4*40,10],[df.iloc[10+4*40+4,10],df.iloc[10+4*40+5,10]]]
    data_RA["bmi"]["bmi>=40"] = [df.iloc[10+4*40,11],[df.iloc[10+4*40+4,11],df.iloc[10+4*40+5, 11]]]

    data_RA["wai"] = {}
    data_RA["wai"]["wai-no"] = [df.iloc[10+4*50,2],[df.iloc[10+4*50+4,2],df.iloc[10+4*50+5,2]]]
    data_RA["wai"]["wai-yes"] = [df.iloc[10+4*50,3],[df.iloc[10+4*50+4,3],df.iloc[10+4*50+5,3]]]

    data_RA["insu"] = {}
    data_RA["insu"]["insu-no"] = [df.iloc[10+4*60,2],[df.iloc[10+4*60+4,2],df.iloc[10+4*60+5,2]]]
    data_RA["insu"]["insu-yes"] = [df.iloc[10+4*60,3],[df.iloc[10+4*60+4,3],df.iloc[10+4*60+5,3]]]

    data_RA["pov"] = {}
    data_RA["pov"]["pov-no"] = [df.iloc[10+4*70,2],[df.iloc[10+4*70+4,2],df.iloc[10+4*70+5,2]]]
    data_RA["pov"]["pov-yes"] = [df.iloc[10+4*70,3],[df.iloc[10+4*70+4,3],df.iloc[10+4*70+5,3]]]

    data_RA["smok"] = {}
    data_RA["smok"]["smok-yes"] = [df.iloc[10+4*80,3],[df.iloc[10+4*80+4,3],df.iloc[10+4*80+5,3]]]
    data_RA["smok"]["smok-no"] = [df.iloc[10+4*80,4],[df.iloc[10+4*80+4,4],df.iloc[10+4*80+5,5]]]
    data_RA["smok"]["smok-unknown"] = [df.iloc[10+4*80,5],[df.iloc[10+4*80+4,5],df.iloc[10+4*80+5,5]]]

    data_RA["phys"] = {}
    data_RA["phys"]["phys-vigorous"] = [df.iloc[10+4*90,3],[df.iloc[10+4*90+4,3],df.iloc[10+4*90+5,3]]]
    data_RA["phys"]["phys-moderate"] = [df.iloc[10+4*90,4],[df.iloc[10+4*90+4,4],df.iloc[10+4*90+5,5]]]
    data_RA["phys"]["phys-no"] = [df.iloc[10+4*90,5],[df.iloc[10+4*90+4,5],df.iloc[10+4*90+5,5]]]

    data_RA["overall"] = {}
    data_RA["overall"]["overall"] = [df.iloc[10+4*100,1],[df.iloc[10+4*100+4,1],df.iloc[10+4*100+5,1]]]



    data_OA["sex"] = {}
    data_OA["sex"]["male"] = [df.iloc[20+4*0,2],[df.iloc[20+4*0+4,2],df.iloc[20+4*0+5,2]]]
    data_OA["sex"]["female"] = [df.iloc[20+4*0,3],[df.iloc[20+4*0+4,3],df.iloc[20+4*0+5,3]]]

    data_OA["age"] = {}
    data_OA["age"]["18-44yrs"] = [df.iloc[20+4*10,3],[df.iloc[20+4*10+4,3],df.iloc[20+4*10+5,3]]]
    data_OA["age"]["44-65yrs"] = [df.iloc[20+4*10,4],[df.iloc[20+4*10+4,4],df.iloc[20+4*10+5,4]]]
    data_OA["age"][">65yrs"] = [df.iloc[20+4*10,5],[df.iloc[20+4*10+4,5],df.iloc[20+4*10+5,5]]]

    data_OA["race"] = {}
    
    # check if nan 
    if df.iloc[20+4*20,10]==df.iloc[20+4*20,10]:
        data_OA["race"]["MA"] = [df.iloc[20+4*20,6],[df.iloc[20+4*20+4,6],df.iloc[20+4*20+5,6]]]
        data_OA["race"]["OH"] = [df.iloc[20+4*20,7],[df.iloc[20+4*20+4,7],df.iloc[20+4*20+5,7]]]
        data_OA["race"]["NHW"] = [df.iloc[20+4*20,8],[df.iloc[20+4*20+4,8],df.iloc[20+4*20+5,8]]]
        data_OA["race"]["NHB"] = [df.iloc[20+4*20,9],[df.iloc[20+4*20+4,9],df.iloc[20+4*20+5,9]]]
        data_OA["race"]["NHS"] = [df.iloc[20+4*20,10],[df.iloc[20+4*20+4,10],df.iloc[20+4*20+5,10]]]
        data_OA["race"]["OR"] = [df.iloc[20+4*20,11],[df.iloc[20+4*20+4,11],df.iloc[20+4*20+5,11]]]
    else:
        data_OA["race"]["MA"] = [df.iloc[20+4*20,5],[df.iloc[20+4*20+4,5],df.iloc[20+4*20+5,5]]]
        data_OA["race"]["OH"] = [df.iloc[20+4*20,6],[df.iloc[20+4*20+4,6],df.iloc[20+4*20+5,6]]]
        data_OA["race"]["NHW"] = [df.iloc[20+4*20,7],[df.iloc[20+4*20+4,7],df.iloc[20+4*20+5,7]]]
        data_OA["race"]["NHB"] = [df.iloc[20+4*20,8],[df.iloc[20+4*20+4,8],df.iloc[20+4*20+5,8]]]
        data_OA["race"]["NHS"] = [None]
        data_OA["race"]["OR"] = [df.iloc[20+4*20,9],[df.iloc[20+4*20+4,9],df.iloc[20+4*20+5,9]]]


    data_OA["edu"] = {}
    data_OA["edu"]["<high school"] = [df.iloc[20+4*30,3],[df.iloc[20+4*30+4,3],df.iloc[20+4*30+5,3]]]
    data_OA["edu"]["high school graduate and some college"] = [df.iloc[20+4*30+4,4],[df.iloc[20+4*30,4],df.iloc[20+4*30+5,4]]]
    data_OA["edu"]["college graduate"] = [df.iloc[20+4*30,5],[df.iloc[20+4*30+4,5],df.iloc[20+4*30+5,5]]]

    data_OA["bmi"] = {}
    # data_OA["bmi"]["bmi<18.5"] = [df.iloc[20+4*40,6],[df.iloc[20+4*40+4,6],df.iloc[20+4*40+5,6]]]
    data_OA["bmi"]["bmi18.5-25.0"] = [df.iloc[20+4*40,7],[df.iloc[20+4*40+4,7],df.iloc[20+4*40+5,7]]]
    data_OA["bmi"]["bmi25.0-30.0"] = [df.iloc[20+4*40,8],[df.iloc[20+4*40+4,8],df.iloc[20+4*40+5,8]]]
    data_OA["bmi"]["bmi30.0-35.0"] = [df.iloc[20+4*40,9],[df.iloc[20+4*40+4,9],df.iloc[20+4*40+5,9]]]
    data_OA["bmi"]["bmi35.0-40.0"] = [df.iloc[20+4*40,10],[df.iloc[20+4*40+4,10],df.iloc[20+4*40+5,10]]]
    data_OA["bmi"]["bmi>=40"] = [df.iloc[20+4*40,11],[df.iloc[20+4*40+4,11],df.iloc[20+4*40+5, 11]]]

    data_OA["wai"] = {}
    data_OA["wai"]["wai-no"] = [df.iloc[20+4*50,2],[df.iloc[20+4*50+4,2],df.iloc[20+4*50+5,2]]]
    data_OA["wai"]["wai-yes"] = [df.iloc[20+4*50,3],[df.iloc[20+4*50+4,3],df.iloc[20+4*50+5,3]]]

    data_OA["insu"] = {}
    data_OA["insu"]["insu-no"] = [df.iloc[20+4*60,2],[df.iloc[20+4*60+4,2],df.iloc[20+4*60+5,2]]]
    data_OA["insu"]["insu-yes"] = [df.iloc[20+4*60,3],[df.iloc[20+4*60+4,3],df.iloc[20+4*60+5,3]]]

    data_OA["pov"] = {}
    data_OA["pov"]["pov-no"] = [df.iloc[20+4*70,2],[df.iloc[20+4*70+4,2],df.iloc[20+4*70+5,2]]]
    data_OA["pov"]["pov-yes"] = [df.iloc[20+4*70,3],[df.iloc[20+4*70+4,3],df.iloc[20+4*70+5,3]]]

    data_OA["smok"] = {}
    data_OA["smok"]["smok-yes"] = [df.iloc[20+4*80,3],[df.iloc[20+4*80+4,3],df.iloc[20+4*80+5,3]]]
    data_OA["smok"]["smok-no"] = [df.iloc[20+4*80,4],[df.iloc[20+4*80+4,4],df.iloc[20+4*80+5,5]]]
    data_OA["smok"]["smok-unknown"] = [df.iloc[20+4*80,5],[df.iloc[20+4*80+4,5],df.iloc[20+4*80+5,5]]]

    data_OA["phys"] = {}
    data_OA["phys"]["phys-vigorous"] = [df.iloc[20+4*90,3],[df.iloc[20+4*90+4,3],df.iloc[20+4*90+5,3]]]
    data_OA["phys"]["phys-moderate"] = [df.iloc[20+4*90,4],[df.iloc[20+4*90+4,4],df.iloc[20+4*90+5,5]]]
    data_OA["phys"]["phys-no"] = [df.iloc[20+4*90,5],[df.iloc[20+4*90+4,5],df.iloc[20+4*90+5,5]]]

    data_OA["overall"] = {}
    data_OA["overall"]["overall"] = [df.iloc[20+4*100,1],[df.iloc[20+4*100+4,1],df.iloc[20+4*100+5,1]]]




    data_PA["sex"] = {}
    data_PA["sex"]["male"] = [df.iloc[30+4*0,2],[df.iloc[30+4*0+4,2],df.iloc[30+4*0+5,2]]]
    data_PA["sex"]["female"] = [df.iloc[30+4*0,3],[df.iloc[30+4*0+4,3],df.iloc[30+4*0+5,3]]]

    data_PA["age"] = {}
    data_PA["age"]["18-44yrs"] = [df.iloc[30+4*10,3],[df.iloc[30+4*10+4,3],df.iloc[30+4*10+5,3]]]
    data_PA["age"]["44-65yrs"] = [df.iloc[30+4*10,4],[df.iloc[30+4*10+4,4],df.iloc[30+4*10+5,4]]]
    data_PA["age"][">65yrs"] = [df.iloc[30+4*10,5],[df.iloc[30+4*10+4,5],df.iloc[30+4*10+5,5]]]

    data_PA["race"] = {}
    
    # check if nan 
    if df.iloc[30+4*20,10]==df.iloc[30+4*20,10]:
        data_PA["race"]["MA"] = [df.iloc[30+4*20,6],[df.iloc[30+4*20+4,6],df.iloc[30+4*20+5,6]]]
        data_PA["race"]["OH"] = [df.iloc[30+4*20,7],[df.iloc[30+4*20+4,7],df.iloc[30+4*20+5,7]]]
        data_PA["race"]["NHW"] = [df.iloc[30+4*20,8],[df.iloc[30+4*20+4,8],df.iloc[30+4*20+5,8]]]
        data_PA["race"]["NHB"] = [df.iloc[30+4*20,9],[df.iloc[30+4*20+4,9],df.iloc[30+4*20+5,9]]]
        data_PA["race"]["NHS"] = [df.iloc[30+4*20,10],[df.iloc[30+4*20+4,10],df.iloc[30+4*20+5,10]]]
        data_PA["race"]["OR"] = [df.iloc[30+4*20,11],[df.iloc[30+4*20+4,11],df.iloc[30+4*20+5,11]]]
    else:
        data_PA["race"]["MA"] = [df.iloc[30+4*20,5],[df.iloc[30+4*20+4,5],df.iloc[30+4*20+5,5]]]
        data_PA["race"]["OH"] = [df.iloc[30+4*20,6],[df.iloc[30+4*20+4,6],df.iloc[30+4*20+5,6]]]
        data_PA["race"]["NHW"] = [df.iloc[30+4*20,7],[df.iloc[30+4*20+4,7],df.iloc[30+4*20+5,7]]]
        data_PA["race"]["NHB"] = [df.iloc[30+4*20,8],[df.iloc[30+4*20+4,8],df.iloc[30+4*20+5,8]]]
        data_PA["race"]["NHS"] = [None]
        data_PA["race"]["OR"] = [df.iloc[30+4*20,9],[df.iloc[30+4*20+4,9],df.iloc[30+4*20+5,9]]]


    data_PA["edu"] = {}
    data_PA["edu"]["<high school"] = [df.iloc[30+4*30,3],[df.iloc[30+4*30+4,3],df.iloc[30+4*30+5,3]]]
    data_PA["edu"]["high school graduate and some college"] = [df.iloc[30+4*30+4,4],[df.iloc[30+4*30,4],df.iloc[30+4*30+5,4]]]
    data_PA["edu"]["college graduate"] = [df.iloc[30+4*30,5],[df.iloc[30+4*30+4,5],df.iloc[30+4*30+5,5]]]

    data_PA["bmi"] = {}
    # data_PA["bmi"]["bmi<18.5"] = [df.iloc[30+4*40,6],[df.iloc[30+4*40+4,6],df.iloc[30+4*40+5,6]]]
    data_PA["bmi"]["bmi18.5-25.0"] = [df.iloc[30+4*40,7],[df.iloc[30+4*40+4,7],df.iloc[30+4*40+5,7]]]
    data_PA["bmi"]["bmi25.0-30.0"] = [df.iloc[30+4*40,8],[df.iloc[30+4*40+4,8],df.iloc[30+4*40+5,8]]]
    data_PA["bmi"]["bmi30.0-35.0"] = [df.iloc[30+4*40,9],[df.iloc[30+4*40+4,9],df.iloc[30+4*40+5,9]]]
    data_PA["bmi"]["bmi35.0-40.0"] = [df.iloc[30+4*40,10],[df.iloc[30+4*40+4,10],df.iloc[30+4*40+5,10]]]
    data_PA["bmi"]["bmi>=40"] = [df.iloc[30+4*40,11],[df.iloc[30+4*40+4,11],df.iloc[30+4*40+5, 11]]]

    data_PA["wai"] = {}
    data_PA["wai"]["wai-no"] = [df.iloc[30+4*50,2],[df.iloc[30+4*50+4,2],df.iloc[30+4*50+5,2]]]
    data_PA["wai"]["wai-yes"] = [df.iloc[30+4*50,3],[df.iloc[30+4*50+4,3],df.iloc[30+4*50+5,3]]]

    data_PA["insu"] = {}
    data_PA["insu"]["insu-no"] = [df.iloc[30+4*60,2],[df.iloc[30+4*60+4,2],df.iloc[30+4*60+5,2]]]
    data_PA["insu"]["insu-yes"] = [df.iloc[30+4*60,3],[df.iloc[30+4*60+4,3],df.iloc[30+4*60+5,3]]]

    data_PA["pov"] = {}
    data_PA["pov"]["pov-no"] = [df.iloc[30+4*70,2],[df.iloc[30+4*70+4,2],df.iloc[30+4*70+5,2]]]
    data_PA["pov"]["pov-yes"] = [df.iloc[30+4*70,3],[df.iloc[30+4*70+4,3],df.iloc[30+4*70+5,3]]]

    data_PA["smok"] = {}
    data_PA["smok"]["smok-yes"] = [df.iloc[30+4*80,3],[df.iloc[30+4*80+4,3],df.iloc[30+4*80+5,3]]]
    data_PA["smok"]["smok-no"] = [df.iloc[30+4*80,4],[df.iloc[30+4*80+4,4],df.iloc[30+4*80+5,5]]]
    data_PA["smok"]["smok-unknown"] = [df.iloc[30+4*80,5],[df.iloc[30+4*80+4,5],df.iloc[30+4*80+5,5]]]

    data_PA["phys"] = {}
    data_PA["phys"]["phys-vigorous"] = [df.iloc[30+4*90,3],[df.iloc[30+4*90+4,3],df.iloc[30+4*90+5,3]]]
    data_PA["phys"]["phys-moderate"] = [df.iloc[30+4*90,4],[df.iloc[30+4*90+4,4],df.iloc[30+4*90+5,5]]]
    data_PA["phys"]["phys-no"] = [df.iloc[30+4*90,5],[df.iloc[30+4*90+4,5],df.iloc[30+4*90+5,5]]]

    data_PA["overall"] = {}
    data_PA["overall"]["overall"] = [df.iloc[30+4*100,1],[df.iloc[30+4*100+4,1],df.iloc[30+4*100+5,1]]]



    data_OT["sex"] = {}
    data_OT["sex"]["male"] = [df.iloc[40+4*0,2],[df.iloc[40+4*0+4,2],df.iloc[40+4*0+5,2]]]
    data_OT["sex"]["female"] = [df.iloc[40+4*0,3],[df.iloc[40+4*0+4,3],df.iloc[40+4*0+5,3]]]

    data_OT["age"] = {}
    data_OT["age"]["18-44yrs"] = [df.iloc[40+4*10,3],[df.iloc[40+4*10+4,3],df.iloc[40+4*10+5,3]]]
    data_OT["age"]["44-65yrs"] = [df.iloc[40+4*10,4],[df.iloc[40+4*10+4,4],df.iloc[40+4*10+5,4]]]
    data_OT["age"][">65yrs"] = [df.iloc[40+4*10,5],[df.iloc[40+4*10+4,5],df.iloc[40+4*10+5,5]]]

    data_OT["race"] = {}
    
    # check if nan 
    if df.iloc[40+4*20,10]==df.iloc[40+4*20,10]:
        data_OT["race"]["MA"] = [df.iloc[40+4*20,6],[df.iloc[40+4*20+4,6],df.iloc[40+4*20+5,6]]]
        data_OT["race"]["OH"] = [df.iloc[40+4*20,7],[df.iloc[40+4*20+4,7],df.iloc[40+4*20+5,7]]]
        data_OT["race"]["NHW"] = [df.iloc[40+4*20,8],[df.iloc[40+4*20+4,8],df.iloc[40+4*20+5,8]]]
        data_OT["race"]["NHB"] = [df.iloc[40+4*20,9],[df.iloc[40+4*20+4,9],df.iloc[40+4*20+5,9]]]
        data_OT["race"]["NHS"] = [df.iloc[40+4*20,10],[df.iloc[40+4*20+4,10],df.iloc[40+4*20+5,10]]]
        data_OT["race"]["OR"] = [df.iloc[40+4*20,11],[df.iloc[40+4*20+4,11],df.iloc[40+4*20+5,11]]]
    else:
        data_OT["race"]["MA"] = [df.iloc[40+4*20,5],[df.iloc[40+4*20+4,5],df.iloc[40+4*20+5,5]]]
        data_OT["race"]["OH"] = [df.iloc[40+4*20,6],[df.iloc[40+4*20+4,6],df.iloc[40+4*20+5,6]]]
        data_OT["race"]["NHW"] = [df.iloc[40+4*20,7],[df.iloc[40+4*20+4,7],df.iloc[40+4*20+5,7]]]
        data_OT["race"]["NHB"] = [df.iloc[40+4*20,8],[df.iloc[40+4*20+4,8],df.iloc[40+4*20+5,8]]]
        data_OT["race"]["NHS"] = [None]
        data_OT["race"]["OR"] = [df.iloc[40+4*20,9],[df.iloc[40+4*20+4,9],df.iloc[40+4*20+5,9]]]


    data_OT["edu"] = {}
    data_OT["edu"]["<high school"] = [df.iloc[40+4*30,3],[df.iloc[40+4*30+4,3],df.iloc[40+4*30+5,3]]]
    data_OT["edu"]["high school graduate and some college"] = [df.iloc[40+4*30+4,4],[df.iloc[40+4*30,4],df.iloc[40+4*30+5,4]]]
    data_OT["edu"]["college graduate"] = [df.iloc[40+4*30,5],[df.iloc[40+4*30+4,5],df.iloc[40+4*30+5,5]]]

    data_OT["bmi"] = {}
    # data_OT["bmi"]["bmi<18.5"] = [df.iloc[40+4*40,6],[df.iloc[40+4*40+4,6],df.iloc[40+4*40+5,6]]]
    data_OT["bmi"]["bmi18.5-25.0"] = [df.iloc[40+4*40,7],[df.iloc[40+4*40+4,7],df.iloc[40+4*40+5,7]]]
    data_OT["bmi"]["bmi25.0-30.0"] = [df.iloc[40+4*40,8],[df.iloc[40+4*40+4,8],df.iloc[40+4*40+5,8]]]
    data_OT["bmi"]["bmi30.0-35.0"] = [df.iloc[40+4*40,9],[df.iloc[40+4*40+4,9],df.iloc[40+4*40+5,9]]]
    data_OT["bmi"]["bmi35.0-40.0"] = [df.iloc[40+4*40,10],[df.iloc[40+4*40+4,10],df.iloc[40+4*40+5,10]]]
    data_OT["bmi"]["bmi>=40"] = [df.iloc[40+4*40,11],[df.iloc[40+4*40+4,11],df.iloc[40+4*40+5, 11]]]

    data_OT["wai"] = {}
    data_OT["wai"]["wai-no"] = [df.iloc[40+4*50,2],[df.iloc[40+4*50+4,2],df.iloc[40+4*50+5,2]]]
    data_OT["wai"]["wai-yes"] = [df.iloc[40+4*50,3],[df.iloc[40+4*50+4,3],df.iloc[40+4*50+5,3]]]

    data_OT["insu"] = {}
    data_OT["insu"]["insu-no"] = [df.iloc[40+4*60,2],[df.iloc[40+4*60+4,2],df.iloc[40+4*60+5,2]]]
    data_OT["insu"]["insu-yes"] = [df.iloc[40+4*60,3],[df.iloc[40+4*60+4,3],df.iloc[40+4*60+5,3]]]

    data_OT["pov"] = {}
    data_OT["pov"]["pov-no"] = [df.iloc[40+4*70,2],[df.iloc[40+4*70+4,2],df.iloc[40+4*70+5,2]]]
    data_OT["pov"]["pov-yes"] = [df.iloc[40+4*70,3],[df.iloc[40+4*70+4,3],df.iloc[40+4*70+5,3]]]

    data_OT["smok"] = {}
    data_OT["smok"]["smok-yes"] = [df.iloc[40+4*80,3],[df.iloc[40+4*80+4,3],df.iloc[40+4*80+5,3]]]
    data_OT["smok"]["smok-no"] = [df.iloc[40+4*80,4],[df.iloc[40+4*80+4,4],df.iloc[40+4*80+5,5]]]
    data_OT["smok"]["smok-unknown"] = [df.iloc[40+4*80,5],[df.iloc[40+4*80+4,5],df.iloc[40+4*80+5,5]]]

    data_OT["phys"] = {}
    data_OT["phys"]["phys-vigorous"] = [df.iloc[40+4*90,3],[df.iloc[40+4*90+4,3],df.iloc[40+4*90+5,3]]]
    data_OT["phys"]["phys-moderate"] = [df.iloc[40+4*90,4],[df.iloc[40+4*90+4,4],df.iloc[40+4*90+5,5]]]
    data_OT["phys"]["phys-no"] = [df.iloc[40+4*90,5],[df.iloc[40+4*90+4,5],df.iloc[40+4*90+5,5]]]

    data_OT["overall"] = {}
    data_OT["overall"]["overall"] = [df.iloc[40+4*100,1],[df.iloc[40+4*100+4,1],df.iloc[40+4*100+5,1]]]


    # for key in data_RA.keys():
    #     print(key)
    #     for key1 in data_RA[key].keys():
    #         print(key1,end="  ")
    #         print(data_RA[key][key1])

    return data_RA,data_OA,data_PA,data_OT



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

    # for key in data_ipre.keys():
    #     print(key)
    #     for key1 in data_ipre[key].keys():
    #         print(key1,end="  ")
    #         print(data_ipre[key][key1])

    data_iartypre_RA = {}
    data_iartypre_OA = {}
    data_iartypre_PA = {}
    data_iartypre_OT = {}

    for filepath in target_file_list["iartpre"][:5]:
        data_RA,data_OA,data_OT = iartypre_fetch_99_07(path_to_datadir + filepath)
        for key in data_RA.keys():
            if key in data_iartypre_RA.keys():
                for key1 in data_RA[key].keys():
                    data_iartypre_RA[key][key1] += data_RA[key][key1]
                    data_iartypre_OA[key][key1] += data_OA[key][key1]
                    data_iartypre_OT[key][key1] += data_OT[key][key1]
                    data_iartypre_PA[key][key1] += [None,[None,None]]
            else:
                data_iartypre_RA[key] = data_RA[key]
                data_iartypre_OA[key] = data_OA[key]
                data_iartypre_OT[key] = data_OT[key]
                data_iartypre_PA[key] = {}
                for key1 in data_RA[key].keys():
                    data_iartypre_PA[key][key1] = [None,[None,None]]


    for filepath in target_file_list["iartpre"][5:]:
        data_RA,data_OA,data_PA,data_OT = iartypre_fetch_09_19(path_to_datadir + filepath)
        for key in data_RA.keys():
            if key in data_iartypre_RA.keys():
                for key1 in data_RA[key].keys():
                    data_iartypre_RA[key][key1] += data_RA[key][key1]
                    data_iartypre_OA[key][key1] += data_OA[key][key1]
                    data_iartypre_PA[key][key1] += data_PA[key][key1]       
                    data_iartypre_OT[key][key1] += data_OT[key][key1]

    for key in data_ipre.keys():
        save_to_json(data_ipre[key],"data_preprocessed/ipre/{}.json".format(key))

    for key in data_ipre.keys():
        save_to_json(data_iartypre_RA[key],"data_preprocessed/iartypre_RA/{}.json".format(key))

    for key in data_ipre.keys():
        save_to_json(data_iartypre_OA[key],"data_preprocessed/iartypre_OA/{}.json".format(key))
    
    # for key in data_ipre.keys():
    #     save_to_json(data_iartypre_PA[key],"data_preprocessed/iartypre_PA/{}.json".format(key))

    # for key in data_ipre.keys():
    #     save_to_json(data_iartypre_OT[key],"data_preprocessed/iartypre_OT/{}.json".format(key))

    # for key in data_iartypre_PA.keys():
    #     print(key)
    #     for key1 in data_iartypre_PA[key].keys():
    #         print(key1,end="  ")
    #         print(data_iartypre_PA[key][key1])