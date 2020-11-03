

def quotes(string):
    if type(string) != "str":
        strval = str(string)
    else:
        strval = string
    return strval.replace('"', '\"').replace("'", "\'")