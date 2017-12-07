import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds133136.mlab.com:33136/oldstuff

host = "ds133136.mlab.com"
port = 33136
db_name = "oldstuff"
user_name = "kaizennnn"
password = "maconglinh"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
