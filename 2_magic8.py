import random
import time

while True:
    
    # create list of canned responses
    responses = ['It is certain', 'Better not tell you now', 'Outlook not so good', 'Definitely!', 'Cannot predict now', 'Very doubtful']
    
    # user inputs a string that's not used for anything
    user_input = input("What is your question? Type Q to quit. > ")
    if user_input.strip().lower() == 'q':
        break
    
    else:
    
        # upgrade: make dots appear one by one?
        print("Consulting...")
        time.sleep(.5)
        
        # get randint up to length of responses list
        # both are included in randint
        rand = random.randint(0, len(responses)-1)
        
        # get response at position [rand]
        message = responses[rand]
        print(message)
