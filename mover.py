import shutil
import os
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
# "python3 -m pip install watchdog" to install the library required to run this program

"""
A program developed in python using the 'watchdog' library event listeners and 'shutil' library file operations to detect any school assignment files being added to a specific folder and moving them to their designated folders organised according to each subject and date of creation automatically and efficiently so as to reduce file clutter.
"""

config = {
    "Directory_To": "/Users/kavyupadhyay/Desktop/OWIS/Subjects",
    "Directory_From": "/Users/kavyupadhyay/Documents"
# switch with directories that you have in your pc
}

class Handler(FileSystemEventHandler):

    def on_modified(self,event):

        for filename in os.listdir(config["Directory_From"]):
            newname = filename
            extsplit = newname.split(".")
            split = newname.split(" ")

            if "Assignment" in split:
                if "Physics" in split:
                    subject = "Physics"
                elif "Chemistry" in split:
                    subject = "Chemistry"
                elif "Maths" in split:
                    subject = "Maths"
                elif "English" in split:
                    subject = "English"
                elif "Spanish" in split:
                    subject = "Spanish"
                elif "Economics" in split:
                    subject = "Economics"
                else:
                    continue
            else:
                continue

            if "pdf" in extsplit:
                ext = "pdf"
            elif "pages" in extsplit:
                ext = "pages"
            elif "numbers" in extsplit:
                ext = "numbers"
            elif "docx" in extsplit:
                ext = "docx"
            elif "xlsx" in extsplit:
                ext = "xlsx"
            else:
                continue

            subject_exist = os.path.isdir(config["Directory_To"]+"/"+subject)
            if subject_exist == False:
                try:
                    os.makedirs(config["Directory_To"]+"/"+subject+"/Solved Assignments")
                except:
                    print("could not make directory")
                    continue
                    
            else:
                solved_exists = os.path.isdir(config["Directory_To"]+"/"+subject+"/Solved Assignments")
                if solved_exists == False:
                    try:
                        os.mkdir(config["Directory_To"]+"/"+subject+"/Solved Assignments")
                    except:
                        print("could not make directory")
                        continue
                    
            pathfrom = config["Directory_From"]+"/"+newname
            pathto = config["Directory_To"]+"/"+subject+"/Solved Assignments"

            file_exists = os.path.isfile(pathto+"/"+newname)
            """
            i=1
            while file_exists == True:
                newname = extsplit[0]+str(i)+extsplit[1]
                file_exists = os.path.isfile(pathto+"/"+newname)
            """
            if file_exists == True:
                continue

            shutil.move(src=pathfrom,dst=pathto)
            print(f"moved {newname} to {pathto}")

events = Handler()
observer = Observer()
observer.schedule(events,config["Directory_From"],recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
