import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

fromdir = "C:/Users/shlok/Downloads"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f" !! The file {event.src_path} has been created =D" )
    
    def on_deleted(self, event):
        print(f" !! The file {event.src_path} has been deleted! =(" )

    def on_modified(self, event):
        print(f" !! The file {event.src_path} has been changed =)" )

    def on_moved(self, event):
        print(f" !! The file {event.src_path} has been moved =)" )

event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, fromdir, recursive=True)

observer.start()
try: 
    while True:
        time.sleep(1)
        print("Running")
except KeyboardInterrupt:
    print("Stopped! =D")
    observer.stop()
    