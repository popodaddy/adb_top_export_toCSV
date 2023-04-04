# What is this?
Batch &amp; Python script using Pandas for export android top content(adb top -p) data to csv format in Windows.

# How to use?
1. To use <code>adb command</code>, install the <code>Android Debug Bridge(adb) tool</code>,first.
2. Enable <code>Developer options</code> on the device & Connecting to the device in usb cable or otherwise.
3. You just should run the <code>top_export_to_csv.cmd</code>.
4. That's all!

# Output
We will use two <code>.py</code> files. 
1. The first file, <code>get_process_id.py</code>, is to get the id of the process you want to observe and to create bacth file for executing <code>.py</code> that processes csv converting.
2. The second file, <code>adb_top_export_to_csv.py</code>, is a file that uses the <code>Pandas library</code> to make the data of <code>adb top -p</code> into a DataFrame and csv format.
