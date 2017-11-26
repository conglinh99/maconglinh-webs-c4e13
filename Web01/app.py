from flask import Flask, render_template
app = Flask(__name__)


# @app.route('/')
# def index():
#     return "Hello C4E13"
#
# @app.route('/hello-me')
# def hello_me():
#     return "Hello mai phờ den =))"
# # cách đặt tên ngay trong loop
# @app.route('/<lastname>/<firstname>')
# def hello(lastname, firstname):
#     return "Hello " + lastname + " " + firstname
#
# @app.route('/sum/<int:x>/<int:y>')
# def calc(x, y):
#     total = x + y
#     # int(x, y)
#     # return int("Sum: " + int(x+y))
#     return str(total)
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
  app.run(debug=True)
