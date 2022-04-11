from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add(): 
    """Add a and b parameters."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = add(a, b)
    
    return str(result)

@app.route('/sub')
def sub():
    """Subtract a parameter from b parameter."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = sub(a, b)
    
    return str(result)

@app.route('/mult')
def mult():
    """Multiply a and b parameters."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = mult(a, b)
    
    return str(result)

@app.route('/div')
def div():
    """Divide parameter a by parameter b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = div(a, b)
    
    return str(result)
 