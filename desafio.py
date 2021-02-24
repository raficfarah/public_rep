import datetime
import re
import sys

def unix_time_value(value):
    if value != 'TRAILER RE':
        dt = datetime.datetime(int(value[:4]), int(value[4:6]), int(value[6:8]), int(value[8:]))
        return dt.timestamp()

def dicting(data):
    mpe_dicts = {
    'effective_timestamp': data[0:10],
    'active': data[10:11],
    'table_id': data[11:19],
    'subject_table_id': data[19:27],
    'subject_table_name': data[28:55],
    'subject_table_key_length': data[55:60],
    'subject_table_key_start': data[60:64],
    'subject_table_record_length_min': data[64:69],
    'subject_table_record_length_max': data[69:74],
    'vision_number': data[74:82],
    'central_update': data[82:94],
    'member_update': data[94:106],
    'table_row_count': data[106:114],
    'full_table_build_indicator': data[224:225],
    'table_sub_indicator': data[243:246]
    }


    for key, value in mpe_dicts.items():
        if re.search('[a-zA-Z]*', value) == None:
            mpe_dicts.update({key: int(value)})
        elif key == 'effective_timestamp':
            mpe_dicts.update({key: unix_time_value(value)})

    return mpe_dicts


# opening the file and printing each record a dictionary.
def open_file(file):
    f = open(file)
    f_lines = f.readlines()
    for line in f_lines:
        temp = dicting(line)
        if temp['effective_timestamp'] != None:
            print(temp, '\n')

    f.close()

def load(filename):
    open_file(filename)


def show():
    return


def main():
    if len(sys.argv) != 3:
        print('How to use it: ./desafio.py {load | show} filename output.json')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    #output = sys.argv[3]

    if option == 'load':
        load(filename)
    elif option == 'show':
        show(filename)
    else:
        print(f'Unknow command: {option}')
        sys.exit(1)


if __name__ == '__main__':
    main()
