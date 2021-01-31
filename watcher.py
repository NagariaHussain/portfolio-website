# External lib
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler, FileModifiedEvent, FileCreatedEvent

# Internal Lib
from utils import process_sass_files
from site_generator import SiteGenerator

def on_modified(event: FileModifiedEvent):
    modified_file = Path(event.src_path)

    if modified_file.parent == Path("sass"):
        print("SCSS files modified. recompiling...")
        process_sass_files()

    if modified_file.parent in (Path("blogs"), Path("projects"), Path("partials")):
        site_gen = SiteGenerator()
        site_gen.generate()

def on_created(event: FileCreatedEvent):
    created_file = Path(event.src_path)

    if created_file.parent in (Path("blogs"), Path("projects"), Path("partials")):
        print("Changes detected. Regenerating site...")
        site_gen = SiteGenerator()
        site_gen.generate()

def start_watching():
    '''start watchdog, watching to file modifications'''
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    my_event_handler.on_modified = on_modified
    my_event_handler.on_created = on_created

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