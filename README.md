# budou_file_output
Python script I wrote for writing Budou Japanese output to file. Note, this works on my Windows machine-- you might need to tweak files for other OS, e.g. make case_sensitive = True in the watchdog event listener.

Requires python and Budou. See https://github.com/google/budou for more information

Watchdog event listener script requires Watchdog. https://pypi.org/project/watchdog/ 

Pyperclip requires pyperclip (https://pypi.org/project/pyperclip/) This automatically copies the 

Out of the box, Budou CLI only prints to terminal. This script prints to an output file + copies output to clipboard.

NOTE: My project uses Tinysegmenter, but you can specify a different segmenter. Also, make sure you have already created an output.txt file in your working directory because input.py needs that file to write to. 
