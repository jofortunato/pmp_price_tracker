import re

def get_input_data(file_name, input_name):
    f = open(file_name, "r")
    for line in f:
        words = re.split(r"[=]", line)
    return input_data
