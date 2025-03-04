import os
import stat
def read_file(file_path):
    os.chmod(file_path, stat.S_IRWXU)
    lines = []
    with open(file_path) as file:
        for line in file:
            lines.append(line.rstrip())
    file.close()
    return lines    
