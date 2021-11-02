# app.py
from flask import Flask, request, jsonify
from flask.helpers import make_response
from flask.wrappers import Response
from werkzeug.exceptions import Unauthorized, abort



app = Flask(__name__)

#api = Api(
#    app=app,
#    version=1.0,
#    title="New Itemkeys",
#    description="Generate n new itemkeys of 3 characters starting form the last \
#         one as input. Max: 3474, keys are distributed 1-999, A01-Z99 sequentially ")

#@app.get("/keys") - removed this resource because it is also used internally
# to provide the list 
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
    

def last_key(oldkeys=list):
    oldkeys.sort() # check if it provides good result, else check keys. 
    n = len(oldkeys)
    values = oldkeys[n-1:n] # get the last value from a list 
    newstr = ''.join(item for item in values) # convert list value to string 
    return newstr

#@api.route("/newitemkeys/<n>")
@app.route("/newitemkeys/<n>")
def itemkeys(n, lastkey=None):
    try:
        lk = request.args.get('lastkey', None)
        """[summary]
        Returns:
        [list]: [itemkeys]
            # generates list of new keys, input: list of keys. number of required new keys
            # call the numeric, and the string function in a loop, output a list
        """
        orderkeys = []
        newkeys = []
        orderkeys = generate_keylist()
        if lk in orderkeys:
            i1 = orderkeys.index(lk)
        elif lk is None:
            i1 = 0
        for _ in range(int(n)):
            i1 = i1 + 1 
            newkey = orderkeys[i1]
            newkeys.append(newkey)
        return jsonify(newkeys)
    except IndexError as e:
        #abort(404)
        abort(Response('Indexerror: response out of range',404))


assert(['A01', 'A02' ,'B12'])

#@app.errorhandler(404)
#def not_found(error):
#    resp = make_response(render_template('error.html'),404)
#    resp.headers['X-something'] = 'A-value'
#    return resp

@app.errorhandler(IndexError)
def index_error(e):
    resp = make_response(" An index error occured", 404)
    return " An index error occured"


if __name__ == "__main__": 
    pass

