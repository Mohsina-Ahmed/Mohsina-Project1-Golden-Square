def calculate_reading_time(word):
    if word == " ":
        raise Exception("No word is given")
    else:
        str = word.split(' ')
        return len(str)/200
 
