from flask import Flask, render_template, request
import mlab
from mongoengine import *
app = Flask(__name__)

mlab.connect()

class Item(Document):

    title = StringField()
    author = StringField()
    image = StringField()
    description = StringField()
    price = IntField()

@app.route('/')
def index():
    items = Item.objects()
    return render_template('index.html', items=items)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method =="GET":
        return render_template('add_item.html')
    elif request.method == "POST":
        form = request.form
        title = form['title']
        author = form['author']
        image = form['image']
        description = form['description']
        price = form['price']
        new_item = Item(title=title, author=author, image=image, description=description, price=price)
        return "Thêm sách thành công!"
if __name__ == '__main__':
  app.run(debug=True)
