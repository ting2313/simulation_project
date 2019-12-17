import sys
import getopt
import json

def usage():
    print(' -h help')
    print(' -f open file_name')

def read_file(file_name):
    with open(file_name,'r') as file_object:
        contents = json.load(file_object)
        for one_data in contents:
            print(one_data)
            
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