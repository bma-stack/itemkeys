# service.py this serves as the service layer that contains the request response
from flask import Flask, request, jsonify, render_template
from werkzeug.exceptions import HTTPException


from app import itemkeys

#api = Api(
#    app=app,
#    version=1.0,
#    title="New Itemkeys",
#    description="Generate n new itemkeys of 3 characters starting form the last \
#         one as input. Max: 3474, keys are distributed 1-999, A01-Z99 sequentially ")

app = Flask(__name__)

@app.route("/newitemkeys/<n>")
def newkeys(n, lastkey=None):
    lastkey = request.args.get('lastkey', None)
 
    return jsonify(itemkeys(n,lastkey)), 200

assert(5,100)

@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e

    # handling non-HTTP exceptions only
    return render_template("500_generic.html", e=e), 500

if __name__== ("__main__"):
    print(newkeys(5,100))