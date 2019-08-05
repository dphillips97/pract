#!python3
'''What did I learn?
1. squaring is ** not ^
2. how to uses 'pop': find index place then pop(index)
'''


def eval():

    # Get all 3 sides
    side_1 = int(input("Side 1 = "))
    side_2 = int(input("Side 2 = "))
    side_3 = int(input("Side 3 = "))
    
    # create list from tuple
    sides_tuple = (side_1, side_2, side_3)
    sides_list = list(sides_tuple)
    
    # find max value
    c = max(sides_list)
    
    # remove max value from list by pop (need index)
    c_index = sides_list.index(c)
    sides_list.pop(c_index)
    
    # assign a and b randomly (2 remaining in list)
    a = sides_list[0]
    b = sides_list[1]

    if a ** 2 + b ** 2 == c ** 2:
        print("Triples confirmed!")
        
    else:
        print("Not a triple :(")
            
    play_again()
    
def play_again():
    again = str(input("Try again? (y/n): "))
    if again.strip().lower() == 'y':
        eval()
    else:
        print("Bye!")

eval()