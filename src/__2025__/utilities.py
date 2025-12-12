'''file to handle common utilities like file reading and year enumeration'''
import os
import stat
from enum import Enum


class Year(Enum):
    y2024 = '__2024__'
    y2025 = '__2025__'
    leet = 'leet'


def read_file(year: Year, file_name, is_r_strip: bool = True) -> list[str]:
    file_path = os.path.abspath('data\\'+year.value+'\\'+file_name)
    os.chmod(file_path, stat.S_IRWXU)
    lines = []
    with open(file_path) as file:
        for line in file:
            if is_r_strip:
                lines.append(line.rstrip())
            else:
                lines.append(line)
    file.close()
    return lines
