from flask import Flask, render_template
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
def object_list():
    data = Item.objects()
    return render_template('index.html', items=data)

if __name__ == '__main__':
  app.run(debug=True)
