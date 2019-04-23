# Budou write output to file / clipboard 

NOTE: These files work only with tinysegmenter for Japanese. To use Chinese or Korean, you'll need to follow the directions on https://github.com/google/budou and create a Google Cloud account to use the Cloud Natural language API. Follow those directions, set the parser declaration as `parser = budou.authenticate('budou-api-key.json')` and create a `/tmp` directory with a `budou-cache.pickle` file and you're good to go.

Python script I put together for writing Budou Japanese/Chinese/Korean output to file. This would be useful for content editors who are dealing with the notorious linebreak issue when copy/pasting Japanese text into CMS like Wordpress, Sitefinity, Drupal, etc., and who want a more streamlined, automated process for dealing with a large amount of Japenese/Chinese/Korean content. 

Requires python and Budou. See https://github.com/google/budou for more information 

Watchdog event listener script requires Watchdog. https://pypi.org/project/watchdog/

Pyperclip requires pyperclip (https://pypi.org/project/pyperclip/) This automatically copies the output to the clipboard. Optional. 

Hotkey file requires autohotkey: totally optional option, in case you wanted to bind `python input.py` to a key...

## Out of the box, Budou CLI only prints to terminal. This script prints to an output file + copies output to clipboard.

### GETTING STARTED
1) Install python on your machine (python comes standard on most Macs)
2) Run `pip install budou`, `pip install watchdog`, and then `pip install pyperclip` on the terminal of your choice
3) Create new project folder, name it whatever you want. Git clone or download the files in this repository to that folder.
4) Navigate to the project folder in your terminal and run `python monitor_changes.py` This runs in the background and listens for changes to the "input.py" file.
5) Open "input.py" in IDE/text editor of your choice, and drop in Japanese text to line 4 `result= parser.parse('japanese/chinese/korean characters go here')` Save file (ctrl+s)
6) The watchdog automatically executes "input.py" after you save it, which prints the segmented japanese characters into "output.txt" and copies them to your clipboard, as well, so you don't have to copy the text from "output.txt"

NOTE: this was developed on Windows 10-- you might need to tweak files for other OS, e.g. make case_sensitive = True in the watchdog event listener for other OS. Also, make sure you have already created an output.txt file in your working directory because input.py needs that file to write to. 

AGAIN: My project uses Tinysegmenter, which is an opensource parser for Japanese only. For Chinese and/or Korean, just follow directions on https://github.com/google/budou, replace line 3 in `input.py` with `parser = budou.authenticate('/path/to/api-key.json')` and create a pickle file under /tmp like so `budou_file_output/tmp/budou-cache.pickle` 
