import random
import datetime
import os

with open('Events.txt', 'r') as f :
    event_list = f.readlines()
    id_dict = {}
    id_max = random.randint(0,24)
    while 1:
        now_id = random.randint(0,24)
        if now_id in id_dict:
            continue
        while 1:
            now_value = random.choice(event_list)
            if now_value not in id_dict.values():
                id_dict[now_id] = now_value
                break
        if len(id_dict) > id_max:
            break
    log_array = sorted(id_dict.items(),key=lambda x:x[0])
    now_time = datetime.datetime.now()
    log_path = os.path.join('log',str(now_time.year) + '-' + str(now_time.month) + '-' + str(now_time.day))
    with open(log_path,'w') as log_file:
        for now_id,now_log in log_array:
            log_file.write(str(now_id) + ':' + now_log)
