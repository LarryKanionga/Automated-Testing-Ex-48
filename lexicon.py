# convert a string to number    
def convert_number(usr_input):
    try:
        return int(usr_input) 
    except ValueError:
        return None

# check if a word is support in the game 
# and return the type of the supported value
def scan(word):
    list_word = word.split() 
    scan = []
    # dic with all the supported 'key' words
    types = {'north' : 'direction', 
            'south' : 'direction',
            'east' : 'direction',
            'go' : 'verb',
            'kill' : 'verb',
            'eat' : 'verb',
            'bear' : 'noun',
            'princess' : 'noun',
            'player' : 'noun',
            'the' : 'stop'
            }
       
    i = 0
    for usr_input in list_word: 
        # trying to convert all words in number
        num = convert_number(usr_input)

        if num == None: # if a num is a string
            if types.has_key(usr_input): 
                tuples = (types.get(usr_input), usr_input)
                scan.insert(i, tuples)
            else: # if a word is not supported by 'types' dict
                err_tuples = ('error', usr_input)
                scan.insert(i, err_tuples)            

        else: # if a num is number
            num_tuples = ('number', num)
            scan.insert(i, num_tuples)

        i += 1
    return scan
