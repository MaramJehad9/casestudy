'''
Rubik cube microservice

This is the entry point for a microservice that enumerates the face rotations
needed to transform the input cube to a solved state.
'''
import os
import json
from flask import Flask, request
from rubik.view.solve import solve
from rubik.view.rotate import rotate
import unittest
import random

app = Flask(__name__)

#-----------------------------------
#  The following code is invoked with the path portion of the URL matches
#         /
#  It returns a welcome string
#
@app.route('/')
def default():
    '''Return welcome information'''
    return 'welcome to secure software process'

#-----------------------------------
#  The following code is invoked with the path portion of the URL matches
#         /about
#  It returns the author identifier
#
@app.route('/about')
def about():
    '''Return author information'''
    return str(_getAuthor())

#-----------------------------------
#  The following code is invoked when the path portion of the URL matches
#         /rubik/solve
#
#  The cube is passed as a URL query:
#        /rubik/solve?cube=<value>
#
@app.route('/rubik/solve')
def solveServer():
    '''Return face rotation solution set'''
    try:
        userParms = _parseParms(request.args)
        result = solve(userParms)
        print("Response -->", str(result))
        return str(result)
    except Exception as anyException:
        return str(anyException)
#-----------------------------------
#  The following code is invoked when the path portion of the URL matches
#         /rubik/rotate
#
#  The cube and the face rotation(s) are passed as a URL query:
#        /rubik/rotate?cube=<value>&rotation=<value>
#
@app.route('/rubik/rotate')
def rotateServer():
    '''Return rotated cube'''
    try:
        userParms = _parseParms(request.args)
        result = rotate(userParms)
        print("Response -->", str(result))
        return str(result)
    except Exception as anyException:
        return str(anyException)

#-----------------------------------
#  URL parsing support code
def _parseParms(queryString):
    '''Convert URL query string items into dictionary form'''
    userParms = {}
    for key in queryString:
        userParms[key] = str(queryString.get(key,''))
    print(userParms)
    return userParms

#-----------------------------------
#  SBOM support code
#
def _getAuthor(sbomDirectory = ''):
    '''Return author information from SBOM'''
    with open(os.path.join(sbomDirectory,"sbom.json"), encoding="utf-8") as sbomFile:
        parsedSbom = json.load(sbomFile)
    sbomComponents = parsedSbom["components"]
    author = "unknown"
    for component in sbomComponents:
        if 'rubik' in component.get('name'):
            author = component.get('author', author)
            continue
    return {'author': author}
 
#-----------------------------------
if __name__ == "__main__":
    port = os.getenv('PORT', '8080')
    app.run(debug=False, host = '0.0.0.0', port = int(port))




class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_default(self):
        for i in range(0, 1000):
            charset = 'gybnmf'
            
            # Generate a list of characters with 9 occurrences of each character
            char_list = [char for char in charset for _ in range(9)]
            
            # Shuffle the list to get a random order of the characters
            random.shuffle(char_list)
            
            # Join the shuffled list into a string of length 54
            random_string = ''.join(char_list[:54])
            response = self.client.get('/rubik/rotate/?dir=fLUF&cube='+random_string)
            #self.assertEqual('ok', response['status'])

if __name__ == '__main__':
    unittest.main()