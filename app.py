from flask import Flask
import mlab
from model.task import Task
from flask_restful import *
from resources.task_resource import *

mlab.connect()
app = Flask(__name__)

api = Api(app)


# task = Task(name="Quyet", local_id="ashiahsid", done= False)
# task.save()
#

# all_tasks = Task.objects()
#
# for task in all_tasks :
#     print(mlab.item2json(task))
#
# my_task = Task.objects(name="Quyet").first()
# print(mlab.item2json(my_task))

# my_task.update(set__done=True)
# my_task.delete()
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#

api.add_resource(TaskListRes, "/tasks")
api.add_resource(TaskRes, "/tasks/<task_id>")
if __name__ == '__main__':
    app.run()
