# Requires Watchdog
# This script listens for any change in input.py i.e. if the file is changed and then saved, and then executes input.py.
# This saves time by eliminating the need to run input.py in the terminal.
# Whenever new JP text is inputted to input.py and then input.py is saved, this automatically runs input.py.
# There are several uneccessary arguments in this script, however, I'm keeping them in case I want to re-use Watchdog for anothe project ;) 
import time
import os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

if __name__ == "__main__":
    patterns = ["*/input.py"]
    ignore_patterns = ""
    ignore_directories = True
    case_sensitive = False
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def on_created(event):
    print(f"hey, {event.src_path} has been created!")

def on_deleted(event):
    print(f"what the f**k! Someone deleted {event.src_path}!")

def on_modified(event):
    os.system('python input.py')

def on_moved(event):
    print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")

my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved

path = "."
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
