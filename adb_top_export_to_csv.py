# -*- coding:utf-8 -*- 

import sys
import re
import os
from datetime import datetime
import pandas as pd


def create_cpu_summary_csv(num_of_args): 
    current_time = datetime.now()
    file_name = os.getcwd() + r"/top_result.txt"
    # file_name = os.getcwd() + r"/top_result_error.txt"

    lines = [line.rstrip('\n') for line in open(file_name)]
    
    # num_of_args = 2
    index_num = 1

    for line in lines:
        if line.find("Mem:") != -1:
            need_index = index_num * num_of_args #need to create the number of pandas's index.
            index_num += 1
    print("Total index number of pandas is {}".format(need_index))
    
    df = pd.DataFrame(index = [i for i in range(need_index)], columns = ["times_from_start", "total_memory", "used_memory", "free_memory", "buffers_memory", "total_swap", "used_swap", "free_swap", "cached_swap", "PID", "USER", "VIRT", "RES", "SHR", "S", "CPU", "MEM", "TIME", "ARGS"])

    times_frst = 0

    df_index_times_frst = 0
    df_index_total_mem = 0
    df_index_used_mem = 0
    df_index_free_mem = 0
    df_index_buff_mem = 0
    df_index_total_sw = 0
    df_index_used_sw = 0
    df_index_free_sw = 0
    df_index_cached_sw = 0
    df_index_PID = 0
    df_index_USER = 0
    df_index_VIRT = 0
    df_index_RES = 0
    df_index_SHR = 0
    df_index_S = 0
    df_index_CPU = 0
    df_index_MEM = 0
    df_index_TIME = 0
    df_index_ARGS = 0

    for line in lines: #line is not 'list'. ".find" only use "abcde", can not use in list.
        if line.find("Mem:") != -1:
            
            for i in range(df_index_times_frst, df_index_times_frst + num_of_args, 1):
                df.times_from_start[df_index_times_frst] = times_frst
                df_index_times_frst += 1
            times_frst += 1
            
            words = re.split(",", line)
            if words == ['']: pass
            else:
                # print(line.find("Mem:")) #if "Mem:" is returned "2". else "-1". This mean of "2" is the start position of "Mem:". e.g.['  Mem:  3775284K total...'].
                # print(line.find("used")) #if "used" is returned "34". else "-1". ['  Mem:  3775284K total,  3124440K used...']

                for word in words:
                    features = word.split(" ")

                    if word.find("total") != -1:
                        for i in range(df_index_total_mem, df_index_total_mem + num_of_args, 1):
                            df.total_memory[df_index_total_mem] = features[-2]
                            df_index_total_mem += 1

                    elif word.find("used") != -1:
                        for i in range(df_index_used_mem, df_index_used_mem + num_of_args, 1):
                            df.used_memory[df_index_used_mem] = features[-2]
                            df_index_used_mem += 1

                    elif word.find("free") != -1:
                        for i in range(df_index_free_mem, df_index_free_mem + num_of_args, 1):
                            df.free_memory[df_index_free_mem] = features[-2]
                            df_index_free_mem += 1
            
                    elif word.find("buffers") != -1:
                        for i in range(df_index_buff_mem, df_index_buff_mem + num_of_args, 1):
                            df.buffers_memory[df_index_buff_mem] = features[-2]
                            df_index_buff_mem += 1

        elif line.find("Swap:") != -1:
            words = re.split(",", line)
            if words == ['']: pass
            else:
                for word in words:
                    features = word.split(" ")

                    if word.find("total") != -1:
                        for i in range(df_index_total_sw, df_index_total_sw + num_of_args, 1):
                            df.total_swap[df_index_total_sw] = features[-2]
                            df_index_total_sw += 1
        
                    elif word.find("used") != -1:
                        for i in range(df_index_used_sw, df_index_used_sw + num_of_args, 1):
                            df.used_swap[df_index_used_sw] = features[-2]
                            df_index_used_sw += 1

                    elif word.find("free") != -1:
                        for i in range(df_index_free_sw, df_index_free_sw + num_of_args, 1):
                            df.free_swap[df_index_free_sw] = features[-2]
                            df_index_free_sw += 1
            
                    elif word.find("cached") != -1:
                        for i in range(df_index_cached_sw, df_index_cached_sw + num_of_args, 1):
                            df.cached_swap[df_index_cached_sw] = features[-2]
                            df_index_cached_sw += 1
        
        elif line.find("com.honda") != -1:
            words = re.split(" ", line)

            temp = []
            for word in words:
                if word == "": pass
                else:
                    temp.append(word)

            if temp[-1].find("smar") != -1:
                print("ARGS of 'smar+' is existed.")
                df.PID[df_index_PID] = temp[-12]
                df_index_PID += 1
                df.USER[df_index_USER] = temp[-11]
                df_index_USER += 1
                df.VIRT[df_index_VIRT] = temp[-8]
                df_index_VIRT += 1
                df.RES[df_index_RES] = temp[-7]
                df_index_RES += 1
                df.SHR[df_index_SHR] = temp[-6]
                df_index_SHR += 1
                df.S[df_index_S] = temp[-5]
                df_index_S += 1
                df.CPU[df_index_CPU] = temp[-4]
                df_index_CPU += 1
                df.MEM[df_index_MEM] = temp[-3]
                df_index_MEM += 1
                df.TIME[df_index_TIME] = temp[-2]
                df_index_TIME += 1
                df.ARGS[df_index_ARGS] = temp[-1]
                df_index_ARGS += 1
            
            elif temp[-1].find("intu") != -1:
                print("ARGS of 'intu+' is existed.")
                df.PID[df_index_PID] = temp[-12]
                df_index_PID += 1
                df.USER[df_index_USER] = temp[-11]
                df_index_USER += 1
                df.VIRT[df_index_VIRT] = temp[-8]
                df_index_VIRT += 1
                df.RES[df_index_RES] = temp[-7]
                df_index_RES += 1
                df.SHR[df_index_SHR] = temp[-6]
                df_index_SHR += 1
                df.S[df_index_S] = temp[-5]
                df_index_S += 1
                df.CPU[df_index_CPU] = temp[-4]
                df_index_CPU += 1
                df.MEM[df_index_MEM] = temp[-3]
                df_index_MEM += 1
                df.TIME[df_index_TIME] = temp[-2]
                df_index_TIME += 1
                df.ARGS[df_index_ARGS] = temp[-1]
                df_index_ARGS += 1

            else: print("All ARGS is not existed...")

    #to create csv file from df(dataframe) we made.
    df.to_csv(file_name + '_{0:0>4}-{1:0>2}-{2:0>2}_{3:0>2}-{4:0>2}-{5:0>2}_summary.csv'.format(current_time.year, current_time.month, current_time.day, current_time.hour, current_time.minute, current_time.second),index=False)


if __name__ == '__main__':
    create_cpu_summary_csv(2)