# -*- coding:utf-8 -*- 

import subprocess
import os

monitor_period = 1
smart_shortcuts_app_id_connected = True
intuition_engine_id_connected = True

print(">> 測定を開始します。")
smart_shortcuts_app_id = subprocess.Popen('adb shell "ps | grep com.honda.smartdash"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
print(">> smart_shortcuts_app_id, 取得準備OK!!")
os.system('cmd /c "pause"')
intuition_engine_id = subprocess.Popen('adb shell "ps | grep com.honda.intuitionengine"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
print(">> intuition_engine_id, 取得準備OK!!")
os.system('cmd /c "pause"')
smart_shortcuts_app_id = smart_shortcuts_app_id.decode('ascii')
intuition_engine_id = intuition_engine_id.decode('ascii')
if smart_shortcuts_app_id == "":
    print(">> usbケーブルが接続されていないか、SmartShortcuts Appが起動されていません。")
    smart_shortcuts_app_id_connected = False
else:
    smart_shortcuts_app_id_connected = True

if intuition_engine_id == "":
    print(">> usbケーブルが接続されていないか、IntuitionEngineが起動されていません。")
    intuition_engine_id_connected = False
else:
    intuition_engine_id_connected = True

if smart_shortcuts_app_id_connected and intuition_engine_id_connected == True:
    smart_shortcuts_app_id = smart_shortcuts_app_id.split()
    intuition_engine_id = intuition_engine_id.split()

    # ['Android', 'Debug', 'Bridge', 'version', '1.0.41', 'Version', '29.0.1-5644136', 'Installed', 'as', 'C:\\Program', 'Files\\platform-tools\\adb.exe']
    print(">> smart_shortcuts_app_id : {}".format(smart_shortcuts_app_id[1]))
    print(">> intuition_engine_id : {}".format(intuition_engine_id[1]))
    print(">> 実行中。測定を終了したい場合は「ctrl + C」を押した後、「N」キーを押して頂き、「Enter」キーを押してください。")
    start_command = 'adb shell "top -p {},{} -d {}" >> top_result.txt'.format(smart_shortcuts_app_id[1], intuition_engine_id[1], monitor_period)
    # print("このコマンドをコピーし、入力してください。")
    # print(start_command)
    # os.system('cmd /c "{}"'.format(start_command)

    # batchファイル作成
    file_name = os.getcwd() + r"/make_to_csv.bat"
    delete_file_name = "top_result.txt"
    sleep_time = 1

    my_bat = open(file_name,'w+')
    # top_result.txtを削除するコマンド入れる。
    my_bat.write("del {0}".format(delete_file_name) + "\n")
    # 1秒待機
    my_bat.write("timeout {0}".format(sleep_time) + "\n")
    my_bat.write(start_command + "\n")
    # 1秒待機
    my_bat.write("timeout {0}".format(sleep_time) + "\n")
    my_bat.write("python adb_top_to_csv_pandas.py")
    # my_bat.write("pause")
    my_bat.close()
