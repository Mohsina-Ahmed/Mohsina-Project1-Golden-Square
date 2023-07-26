# Exercise One

## 1. Describe the problem

> As a user
> So that I can manage my own time
> I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## Design the Method Signature
def calculate_reading_time(text):
    #parameter:
        #text: a string contain words
    #return:
        #float: reading time
## 3.Create Example as Test:
'''
given a text of 200 words string then
it will return the reading time of 1 min
'''
calculate_reading_time(200 words)
# => 1
'''
given a text of 400 words string then
it will return the reading time of 1 min
'''
calculate_reading_time(400 words)
# => 2

'''
given a text of 500 words string then
it will return the reading time of 1 min
'''
calculate_reading_time(500 words)
# => 2.5

'''
given a text of 0 word string then
it will return the reading time of 1 min
'''
calculate_reading_time("")
# => exception message "Can't calculate the reading time for an empty text

## 4. Implement the behaviour
Implement the test file and see what errors we got then go to the python file add the function put pass and run the pytest. See what errors you got and carry on from there


# Exercise Two

## 1. Describe the problem

> As a user
> So that I can improve my grammer
> I want to verify that a text starts with a capital letter and ends with a suitable sentense-ending punctuation mark.

## Design the Method Signature
def grammer_check(text):
    #parameter:
        #text: a string contain words
    #return:
        #True if the sentense starts with a capital letter and ends with a suitable sentence endign punctuation mark. 
## 3.Create Example as Test:
'''
given a text check if it starts with a capital letter and ends with suitable ending punctuation mark.
'''
grammer_check_capital_punct(sentence)
# => True
'''
given a text check if it does not start with a capital letter and ends with suitable ending punctuation mark.
'''
grammer_check_no_capital_punct(sentence)
# => False

'''
given a text check if it does not start with a capital letter and does not end with suitable ending punctuation mark.
'''
grammer_check_no_capital_no_punct(sentence)
# => False

'''
given an empty string it gives an exception
'''
calculate_reading_time_empty("")
# => exception message "Can't validate an empty text

## 4. Implement the behaviour
Implement the test file and see what errors we got then go to the python file add the function put pass and run the pytest. See what errors you got and carry on from there




    
