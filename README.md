# budou_file_output
Python script I wrote for writing Budou Japanese output to file

Requires python and Budou. See https://github.com/google/budou for more information

Watchdog event listener script requires Watchdog. https://pypi.org/project/watchdog/ 

Out of the box, Budou CLI only prints to terminal. This script prints to an output file. 

NOTE: My project uses Tinysegmenter, but you can specify a different segmenter. Also, make sure you have already created an output.txt file in your working directory; input.py needs that file to write to. 
