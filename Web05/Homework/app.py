from flask import Flask, render_template, request, flash
import mlab
from mongoengine import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qjadngjjtuvnagsajrt'

#1. Connect to database
mlab.connect()

#2. Design collection
class Item(Document):
    title = StringField()
    author = StringField()
    image = StringField()
    description = StringField()
    price = IntField()


@app.route('/')
def index():
    items = Item.objects() # Get ALL items
    return render_template('index.html', items=items)
@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'GET':
        return render_template('add_item.html')
    elif request.method == 'POST':
        form = request.form
        title = form['title']
        author = form['author']
        image = form['image']
        description = form['description']
        price = form['price']
        new_item = Item(title=title, author=author, image=image, description=description, price=price)
        new_item.save()
        return "Thêm sách thành công!"
@app.route('/admin')
def admin():
    return render_template('admin.html', items=Item.objects())

@app.route('/edit_item/<item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = Item.objects().with_id(item_id)
    if request.method == "GET":
        return render_template('edit_item.html', item=item)
    elif request.method == "POST":
        form = request.form
        title = form['title']
        author = form['author']
        description = form['description']
        image = form['image']
        price = form['price']
        item.update(title=title, author=author, description=description, image=image, price=price)

        flash("Cập nhật thành công!")
        return render_template('edit_item.html', item=Item.objects().with_id(item_id))
        # return "Updated"

@app.route('/delete_item/<item_id>', methods=['GET', 'POST'])
def delete_item(item_id):
    item = Item.objects().with_id(item_id)
    if request.method == "GET":
        return render_template('delete_item.html', item=item)
    elif request.method == "POST":
        form = request.form
        item.delete()
        flash("Xóa thành công!")
        return render_template('delete_item.html', item=Item.objects().with_id(item_id))



if __name__ == '__main__':
  app.run(debug=True)
