def make_snippet(sentense):
    print("Make snippet is being called...")
    # if sentense == None:
    #     print("Exception is being raised...")
    #     raise Exception("No argument given!")
    # else:
    str= sentense.split()
    if len(str) <= 5:
        return (' '.join(str))
    else:
        return (' '.join(str[:5]) + '...')
        
#make_snippet("This is clear")

#count words
def count_words(sentense):
    if sentense == " ":
        return 0
    count = 1
    for letter in sentense:
        if(letter == ' '):
            count+=1
    return count
#print(count_words("This is my test"))
    