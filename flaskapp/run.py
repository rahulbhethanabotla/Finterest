from flask import Flask, request
from flaskapp.utils.summarizer import create_summary
from flaskapp.utils.definition_scraper import get_definitions
from flaskapp.utils.blackrock import get_analysis
app = Flask(__name__)

@app.route('/summary')
def get_summary():
    article = request.headers['Article']
    summary = create_summary(article)
    return summary

@app.route('/keywords')
def get_keywords():
    '''

    :return: Json response of keywords, as well as what other features should be assocated with them
    example:
    {
        "GDP": {
            "type": "definition",
            "definition": definition
        },
        "AMZN": {
            "type": stock,
            "currentPrice": price,
            "blackrockData": blackrockdata
        }
    }
    '''
    article = request.headers['Article']
    return

@app.route('/blackrock/<ticker>')
def get_blackrock_analysis(ticker):
    return get_analysis(ticker)