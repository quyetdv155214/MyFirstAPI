import mongoengine


# mongodb://<dbuser>:<dbpassword>@ds121980.mlab.com:21980/myfirstapi
host = "ds121980.mlab.com"
port = 21980
db_name = "myfirstapi"
username = "quyetdv155214"
password = "ba@3athuong"
def connect():
    mongoengine.connect(db_name, host=host, port=port, username=username, password=password)
def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]
def item2json(item):
    import json
    return json.loads(item.to_json())