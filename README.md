# What is this?
Batch &amp; Python script using Pandas library for export android top contents(adb top -p) data to csv format in Windows OS.

# How to use?
1. To use <code>adb command</code>, you need to install the <code>Android Debug Bridge(adb) tool</code>, first.
2. You need to enable <code>Developer options</code> on the device & connecting to the device in usb cable or otherwise.
3. When you're all set(1 & 2), you just need to run the <code>top_export_to_csv.cmd</code>!

# Output
We will use two <code>.py</code> files. 
1. The first file, <code>get_process_id.py</code>, is to get the id of the process you want to observe on Android device and to create bacth file <code>make_to_csv.bat</code> for executing <code>.py</code> that processes csv format converting.
2. The second file, <code>adb_top_export_to_csv.py</code>, is a file that uses the <code>Pandas library</code> to make the data of <code>adb top -p</code> into a DataFrame and csv format.
3. 
