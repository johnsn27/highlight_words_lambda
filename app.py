# app.py

from flask import Flask, jsonify, make_response, request
from response import response
app = Flask(__name__)
# most extreme words method not working. Potentially doesn't like calling get_list_of_most_extreme_words so get it into one function
@app.route('/sentiment')
def sentiment_analysis():
    """"method that outputs a response"""
    if request.method == 'GET':
        text = request.args.get('text')
        return response(text)
    return make_response(jsonify({'error': 'sorry! unable to parse', 'status_code': 500}), 500)

# We only need this for local development.
if __name__ == '__main__':
 app.run()
