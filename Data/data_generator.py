# The below code generates random data for 1000+ indian medicinal plants

import time
import json
from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.random_data
collection = db['information']

# function to generate random number between two numbers(numbers inclusive)
def random_num(beg,end):
    div = end - beg + 1
    sysTime = time.clock() # seeder(current processor time as a floating point number expressed in seconds)
    num = (sysTime*1000000)
    digits = (int(num))%100 # extracting last two digits which range from 00 to 99

    rn = (digits*div)/100  # rn is used to scale the random number between lower and upper limit values

    if rn < beg:
        return (rn + beg)
    elif rn > end:
        return (rn - end)
    else:
        return rn


states_list = []
with open('states.txt', 'r') as states:
    for s in states:
        states_list.append(s.strip("\n").split('|')[0])

states.close()


disease_list = []
with open('diseases.txt', 'r') as diseases:
    for d in diseases:
        disease_list.append(d.strip("\n"))

diseases.close()

cnt = 0
data = []
with open('plants.txt', 'r') as plants:
    for p in plants:
        data_object = {}
        data_object['botanical_name'] = p.strip("\n")
        data_object['family'] = p.strip("\n").split(" ")[0]
        #data_object['english_name'] = p.strip("\n").split(" ")[0]

        data_object['places'] = []
        num = []
        for i in range(5):
            n = random_num(0,32)
            if n not in num:
                num.append(n)
                data_object['places'].append(states_list[n])

        data_object['properties'] = []
        num = []
        for j in range(5):
            n = random_num(0,92)
            if n not in num:
                num.append(n)
                data_object['properties'].append(disease_list[n])

        data.append(data_object)
        collection.insert_one(data_object)
        cnt+=1
        print cnt

plants.close()

'''
# printing data of first 6 plants
with open('data.json', 'w') as data_json:
    data_json.write(json.dumps(data))

data_json.close()
'''
