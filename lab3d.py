#!/usr/bin/env python3
# Author ID: 146631213

import os

def free_space():
    command = os.popen("df -h | grep '/$' | awk '{print $4}'")
    output = command.read()
    command.close()

    return output.strip()

if __name__ == '__main__':
    print(free_space())



    



