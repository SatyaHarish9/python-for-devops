import os
import datetime

file_age = 15
today_date = datetime.datetime.now()

for dirpath, dirname, filename in os.walk('/Users/sgumpall/Documents/nutanix'):
    for file in filename:
        complete_path = os.path.join(dirpath,file)
        file_creation_time = datetime.datetime.fromtimestamp(os.path.getctime(complete_path))
        time_diff = (today_date - file_creation_time).days
        if time_diff > file_age:
            print(complete_path, time_diff)
            os.remove(complete_path)