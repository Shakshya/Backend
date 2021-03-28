from flask import Flask, abort, jsonify, request, render_template
import joblib
from feature import *
from scraping import *
import json
from flask_cors import CORS, cross_origin

pipeline = joblib.load('pipeline.sav')

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/api',methods=['POST'])
# def get_delay():
#     result = request.get_json()
#     query_title = result['title']
#     query_text = result['maintext']
#     query_author = " "
#     query = get_all_query(query_title, query_author , query_text)
#     user_input = {'query':query}
#     pred = pipeline.predict(query)
#     dic = {1:'real',0:'fake'}
#     return jsonify(dic[pred[0]])

# @app.route('/api',methods=['GET'])
# @cross_origin()
# def get_url():
#     result=request.args.get("link")
#     url = result
#     query_text = scrap_url(url)
#     query = get_all_query(query_text)
#     pred = pipeline.predict(query)
#     dic = {1:'real',0:'fake'}
#     return jsonify(dic[pred[0]])


@app.route('/api', methods=['GET', 'POST'])
@cross_origin()
def register():
    if request.method == 'POST':
        result = request.get_json()
        query_title = result['title']
        query_text = result['maintext']
        query_author = " "
        query = get_all_query(query_title, query_author , query_text)
        user_input = {'query':query}
        pred = pipeline.predict(query)
        dic = {1:'real',0:'fake'}
        return jsonify(res=dic[pred[0]])
    else:
        result=request.args.get("link")
        url = result
        query_text = scrap_url(url)
        query = get_all_query(query_text)
        pred = pipeline.predict(query)
        dic = {1:'real',0:'fake'}
        return jsonify(res=dic[pred[0]])


if __name__ == '__main__':
    app.run(debug=True)
