def grammer_check(text):
    print("Inside grammer...")
    if text == " ":
        print("Inside the exception...")
        raise Exception("No sentense is given")
    
    
    if (text[0].isupper() == True):
        if (text[-1] == '.' or text[-1] == '.'):
            return True
        else:
            return False
    else:
        return False