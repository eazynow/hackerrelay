from flask import Flask
from flask import render_template, request, redirect

from httplib2 import Http
from urllib import urlencode

import sys
 
app = Flask(__name__)

# update this list of hosts with everones ngrok addresses
hosts = ['http://localhost:8000/ngrokpost',
         'http://localhost:8001/ngrokpost']

# run app and pass a port number (to simulate on one machine..)
 
@app.route("/", methods=['GET'])
def ngrok_input():
    """Display input form"""

    return render_template('ngrok_input.html')
 
@app.route("/ngrokpost", methods=['POST'])
def ngrok_post():
    """receive string"""
    # Get the digit pressed by the user
    print "Request received."
    print request.values
    ngrok_string = request.values.get('ngrok_string', None)
    char_index = int(request.values.get('char_index', 0))

    print "String received:" + ngrok_string

    replace_char = ngrok_string[char_index]
    replace_with = chr(ord(replace_char)+1)

    changed_string = ngrok_string.replace(replace_char,replace_with ,1)

    print "Changed string:" + changed_string
    
    # move no next host
    char_index +=1
    
    if char_index>=len(hosts):
        # all hosts passed
        return changed_string
    else:
        return call_next(changed_string,char_index)
        
def call_next(changed_string, char_index):
    h = Http()
    url = hosts[char_index]
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    post_data = dict(ngrok_string=changed_string, char_index=char_index)
    print "Calling next host:" + url
    params = urlencode(post_data)
    print "With params:" + params
    resp, content = h.request(url, "POST", params, headers)
    print "String received:" + str(resp.values())
    return content

if __name__ == "__main__":

    port = int(sys.argv[1])
    app.run(debug=True,port=port)