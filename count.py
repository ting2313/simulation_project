import sys
import getopt
import json

def usage():
    print(' -h help')
    print(' -p open file_name')

def read_place(file_name):
    city_dict = {}
    with open(file_name,'r') as file_object:
        contents = json.load(file_object)
        for one_data in contents:
            if one_data['county'] == "":
                if one_data['city'] in city_dict:
                    city_dict[one_data['city']] += 1
                else :
                    city_dict[one_data['city']] = 1    
            else :
                if one_data['county'] in city_dict:
                    city_dict[one_data['county']] += 1
                else :
                    city_dict[one_data['county']] = 1  
        print(sorted(city_dict.items(), key=lambda x: x[1]))

def read_car(file_name):
    car_list = [0,0,0,0,0,0]
    with open(file_name,'r') as file_object:
        contents = json.load(file_object)
        for one_data in contents:
            if 1 in one_data['car']:
                car_list[0] += 1
            if 2 in one_data['car']:
                car_list[1] += 1
            if 3 in one_data['car']:
                car_list[2] += 1
            if 4 in one_data['car']:
                car_list[3] += 1
            if 5 in one_data['car']:
                car_list[4] += 1
            if 6 in one_data['car']:
                car_list[5] += 1
        print(car_list)

def read_time(file_name):
    time_list = [0,0,0,0]
    with open(file_name,'r') as file_object:
        contents = json.load(file_object)
        for one_data in contents:
            if one_data['time peak'][0]=='o':
                if one_data['time peak'][9]=='m':
                    time_list[1] += 1
                else:
                    time_list[3] += 1
            else :
                if one_data['time peak'][5]=='m':
                    time_list[0] += 1
                else:
                    time_list[2] += 1
        print(time_list)
            
if __name__ == '__main__':
    try:
        options, args = getopt.getopt(sys.argv[1:], "hp:c:t:",[])

        for name,value in options:
            if name in ('-h'):
                usage()
            elif name in ('-p'):
                read_place(value)
            elif name in ('-c'):
                read_car(value)
            elif name in ('-t'):
                read_time(value)

    except getopt.GetoptError:
        usage()