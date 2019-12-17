import csv
import sys
import getopt
import re
import json

def usage():
    print(' -h help')
    print(' -f open file_name')

def read_file(file_name):
    data = []
    with open(file_name, newline='', encoding='utf-8-sig') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            # TODO : decide peak
            time_str = re.findall(r"\d+", row['發生時間'])
            if len(time_str) < 5 :
                continue
            hour = int(time_str[3])
            minute = int(time_str[4])
            time_peak = ""
            if hour >=5 and hour <17 : # morning : 5:00~16:59
                if (hour == 8 ) or (hour==7 and minute>=30) : # peak morning : 7:30~8:59
                    time_peak = "peak morning"
                else:
                    time_peak = "off-peak morning"
            else: # evening : 17:00~4:59
                if hour ==17 or hour==18 : # peak evening : 17:00~18:59
                    time_peak = "peak evening"
                else:
                    time_peak = "off-peak evening"

            # TODO : decide place
            place_str = row['發生地點'][:3]
            place_city = ""
            place_county = ""
            if place_str[2] == "市":
                place_city = place_str
            else:
                place_county = place_str

            # TODO : died and injured people count
            died = 0
            # died = int(row['死亡人數'][2:])
            injured = int(row['受傷人數'][2:])

            # TODO: car type
            cars = []
            cars.append(row['車種1'].split('-', 1))
            cars.append(row['車種2'].split('-', 1))
            cars.append(row['車種3'].split('-', 1))

            for index, value in enumerate(cars):
                cars[index] = 0
                if len(value) == 2 :
                    if value[1][:1] == "人" :
                        cars[index] = 1
                    elif value[1] == "慢車" :
                        cars[index] = 2
                    elif value[0][:4] == "普通重型" :
                        cars[index] = 3
                    elif value[0][:4] == "大型重型" : 
                        cars[index] = 4
                    elif value[1][:3] == "小客車" or value[1][:3] == "小貨車" :
                        cars[index] = 5
                    elif value[1][:3] == "大客車" or value[1][:3] == "大貨車" :
                        cars[index] = 6
                    else:
                        cars[index] = 7

            dic_temp = {'month':     int(time_str[1]), 
                        'time peak': time_peak,
                        'place':     place_str, 
                        'city':      place_city, 
                        'county':    place_county,
                        'died':      died,
                        'injured':   injured,
                        'car':      cars}
            data.append(dic_temp) 
    
    save_file = file_name.split('.',1)[0]+".json"
    with open(save_file,'w') as file_object:
        json.dump(data, file_object)
    # with open(save_file,'r') as file_object:
    #     contents = json.load(file_object)
    #     for one_data in contents:
    #         print(one_data)
    # for r in data:
    #     print(r['month'],r['time peak'],r['place'],r['city'],r['county'],r['died'],r['injured'],r['car1'],r['car2'],r['car3'])
            
        

if __name__ == '__main__':
    try:
        options, args = getopt.getopt(sys.argv[1:], "hf:",[])

        for name,value in options:
            if name in ('-h'):
                usage()
            elif name in ('-f'):
                read_file(value)

    except getopt.GetoptError:
        usage()