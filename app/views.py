from flask import Flask, url_for, render_template, redirect, request

from . import app, db
from .forms import NewsForm
from .models import Category, News


@app.route('/')
def index():
    news_list = News.query.order_by(News.created_date).all()
    categories = Category.query.all()
    return render_template(
        'index.html',
        news=news_list[::-1],
        categories=categories)


@app.route('/news_detail/<int:id>')
def news_detail(id):
    news = News.query.get(id)
    categories = Category.query.all()
    return render_template(
        'news_detail.html',
        news = news,
        categories=categories)


@app.route('/category/<int:id>')
def news_in_category(id):
    category = Category.query.get(id)
    news = Category.news
    category_name = category.title
    categories = Category.query.all()
    return render_template('category.html',
                           news=news,
                           category_name=category_name,
                           categories=categories
                           )


@app.route('/add_news', methods=['GET', 'POST'])
def add_news():
    form = NewsForm()
    categories = Category.query.all()
    if form.validate_on_submit():
        news = News()
        news.title = form.title.data
        news.text = form.text.data
        news.category_id = form.category.data
        if not news.category_id:
            news.category_id = None
        db.session.add(news)
        db.session.commit()
        return redirect(url_for('news_detail', id=news.id))
    return render_template('add_news.html',
                           form=form,
                           categories=categories)