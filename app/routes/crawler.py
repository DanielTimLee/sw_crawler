from app import app
from app.forms.crawler import CrawlerForm
from crawler.crawler_init import smtm_crawler
from flask import jsonify, Response, render_template, redirect, url_for


@app.route('/crawler', methods=['GET', 'POST'])
def crawler():
    form = CrawlerForm()
    if form.validate_on_submit():
        return redirect(url_for('crawler_active',target=form.target.data))

    return render_template('crawler.html',form=form)

@app.route('/crawler/<string:target>')
def crawler_active(target):
    a = smtm_crawler(app.config['CRAWLER_EMAIL'],
                     app.config['CRAWLER_PWD'],
                     target)
    a.init()

    return Response(a.start(), mimetype='text/html')

