"""
The flask application package.
"""

from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app, title="Api números primos", version="1.0.0", doc="/doc/")

def genPrimes(max_num): # valid to 2^32
    def isPrime(n):
        def isSpsp(n, a):
            d, s = n-1, 0
            while d % 2 == 0:
                d //= 2; s += 1
            t = pow(a,d,n)
            if t == 1: return True
            while s > 0:
                if t == n-1: return True
                t = (t*t) % n; s -= 1
            return False
        for p in [2, 7, 61]:
            if n % p == 0: return n == p
            if not isSpsp(n, p): return False
        return True
    w, wheel = 0, [1,2,2,4,2,4,2,4,6,2,6,4,2,4,\
        6,6,2,6,4,2,6,4,6,8,4,2,4,2,4,8,6,4,6,\
        2,4,6,2,6,6,4,2,4,6,2,6,4,2,4,2,10,2,10]
    p = 2 
    yield p
    while p < max_num:
        p = p + wheel[w]
        w = 4 if w == 51 else w + 1
        if isPrime(p) and p <= max_num: 
            yield p

@api.route("/prime/<int:number>/json")
@api.param("number", description="Returns a list of numbers from 2 to the number passed as parameter as a json", _in="path", required=True, type="Integer")
class Prime(Resource):
    def get(self, number):
        return list(genPrimes(number))  # Flask-restplus assumes json so it tries to convert what I return here to json.

import segundoparcial.views
