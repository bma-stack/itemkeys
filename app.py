# app.py this serves as the application layer that contains the app logic

from flask.wrappers import Response
from werkzeug.exceptions import abort

from model import generate_keylist

def last_key(oldkeys=list):
    oldkeys.sort() # check if it provides good result, else check keys. 
    n = len(oldkeys)
    values = oldkeys[n-1:n] # get the last value from a list 
    newstr = ''.join(item for item in values) # convert list value to string 
    return newstr

#@api.route("/newitemkeys/<n>")

def itemkeys(n, lastkey=None):
    try:
        #lk = request.args.get('lastkey', None)
        lk = str(lastkey)
        """[summary]
        Returns:
        [list]: [itemkeys]
            # generates list of new keys in a dictionary format, input:
            # list of keys. number of required new keys
            # call the numeric, and the string function in a loop, output a
            dictionary that can be used in the json response
        """
        orderkeys = []
        newkeys = []
        i1 = 0
        newkeysdict = {}
        orderkeys = generate_keylist()
        if lk in orderkeys:
            i1 = orderkeys.index(lk)
        elif lk is None:
            i1 = 0
        for _ in range(int(n)):
            i1 = i1 + 1 
            newkey = orderkeys[i1]
            newkeys.append(newkey)
            newkeysdict["keys"] = newkeys
        return newkeysdict
    except IndexError as e:
        abort(Response('IndexError: response out of range',404))
    except ValueError as e: 
        abort(Response('ValueError : incorrect input parameter',400))


assert(['A01', 'A02' ,'B12'])


if __name__ == "__main__": 
    pass