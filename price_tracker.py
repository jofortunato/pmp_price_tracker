#!/home/joaofortunato/.virtualenvs/pmp_price_tracker/bin/python3

def get_input_data(file_name, var_name):
    f = open(file_name, "r")
    for line in f:
        words = line.split(sep="=")
        if words[0].strip() == var_name:
            return words[1].strip()
    return -1
