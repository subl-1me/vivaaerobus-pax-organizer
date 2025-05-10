import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pyfiglet

# --- Configuration ---
FOLDER_TO_MONITOR = "./documents" # file to monitor

# --- make sure folder exits ---
if not os.path.exists(FOLDER_TO_MONITOR):
    print(f"Creating monitoring folder...: {FOLDER_TO_MONITOR}")
    os.makedirs(FOLDER_TO_MONITOR)
    print(f"Folder created: {FOLDER_TO_MONITOR}")

# --- Event class handler ---
class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"\n[NEW_FILE] {event.src_path}")


if __name__ == "__main__":
    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, FOLDER_TO_MONITOR, recursive=False) 
    observer.start()
    
    title = pyfiglet.figlet_format('VIVA AEROBUS PAX ORGANIZER')
    print(title)

    print(f"Monitoring '{FOLDER_TO_MONITOR}'...")
    print("Press Ctrl+C to stop the application.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:

        observer.stop()
        print("\nExiting...")

    # wait for the observer to finish
    observer.join()