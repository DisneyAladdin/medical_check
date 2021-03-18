#coding:utf-8
import random

dict_manual = {}
a = open("manual.txt","r")
for i in a:
    key = i.rstrip().split(",")[0]
    value = i.rstrip().split(",")[1]
    dict_manual[key] = value
a.close()

visit = 3
checkup = 3

for i in range(1,visit+1):
    checkup_list = []
    random_keys = list(dict_manual.keys())
    checkup_list = random.sample(random_keys, checkup) 
    print(i,"回目の来訪手順")
    for n in checkup_list:
        print ("検査項目：", n , "手順：", dict_manual[n])
    print("---------------------------------------")
