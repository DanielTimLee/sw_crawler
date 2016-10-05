from app import app
from crawler.crawler_init import smtm_crawler


@app.route('/crawler/<string:target>')
def crawler(target):
    a = smtm_crawler(app.config['CRAWLER_EMAIL'],
                     app.config['CRAWLER_PWD'],
                     target)
    a.init()
    a.signin()
    a.start()

    return "hi"
