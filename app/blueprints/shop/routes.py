from flask import Blueprint, render_template

shop = Blueprint('shop', __name__)

@shop.route('/')
def shop_home():
    return render_template('shop.html')
