# this file serves as the data / model layer
def generate_keylist():
    """[summary]

    Returns:
        [list]: [orderkeys]
        generates complete dataset:
        - number range 1-999
        - alphanumeric prefix concatenated with a number 1-99
        - follows sequential order
        - max number of characters: 3
        - returns results-list in json format
    """
# define alphanumeric prefix
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'
    orderkeys = []
    # numeric up to 999
    for _ in range (1,1000):
        if len(str(_)) == 1:
            x = "00" + str(_)
        elif len(str(_)) == 2: 
            x = "0" + str(_)
        else:
            x = str(_)
        orderkeys.append(x)
# loop though the characters
    for c in abc:
        # loop through the number range 1 - 99
        for _ in range(1,100):
            if len(str(_))==1:
                x = "0" + str(_)
            else:
                x = str(_)
            orderkeys.append(c + x)
    return orderkeys