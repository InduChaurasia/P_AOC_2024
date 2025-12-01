'''file to handle common utilities like file reading and year enumeration'''
import os
import stat
from enum import Enum

class Year(Enum):
    y2024 = '__2024__'
    y2025 = '__2025__'
    leet = 'leet'

def read_file(year: Year,file_name):
    file_path = os.path.abspath('data\\'+year.value+'\\'+file_name)
    os.chmod(file_path, stat.S_IRWXU)
    lines = []
    with open(file_path) as file:
        for line in file:
            lines.append(line.rstrip())
    file.close()
    return lines    
