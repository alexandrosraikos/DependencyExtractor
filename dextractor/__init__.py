import re
import os

def analyze(path):
    if os.path.isdir(path):  
        print("\nIt is a directory")
        return "Directory!"
    elif os.path.isfile(path):  
        print("\nIt is a normal file")  
        return "File!"
    else:  
        print("It is a special file (socket, FIFO, device file)" )
        return "Wrong!"