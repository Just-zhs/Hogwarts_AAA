import json
from typing import List

from flask import app, Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

# fake
# app.config['db'] = []
# sqlite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lagou4:lagou4password@stuq.ceshiren.com:23306/lagou4'


db = SQLAlchemy(app)


@app.route('/')
def hello():
    return 'hello world'


class TestCase(db.Model):
    __tablename__ = 'Testcase_zhs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=True)
    steps = db.Column(db.String(1024), nullable=True)

    # task_id = db.Column(db.Integer, db.ForeignKey('Task_zhs.id'),
    #                     nullable=False)
    # task = db.relationship('Task',
    #                        backref=db.backref('testcases', lazy=True))

    def __repr__(self):
        return '<TestCase %r>' % self.username


class Task(db.Model):
    __tablename__ = 'Task_zhs'
    id = db.Column(db.Integer, primary_key=True)
    testcases = db.Column(db.String(1024), nullable=True)

    def __repr__(self):
        return '<Task %r>' % self.username


class TestCaseService(Resource):
    def get(self):
        """
        测试用例的浏览获取/testcase.json /testcase.json?id=1
        :return:
        """
        testcases: List[TestCase] = TestCase.query.all()
        res = [{'id': testcase.id,
                'name': testcase.name,
                'description': testcase.description,
                'steps': json.loads(testcase.steps)} for testcase in testcases]
        return {
            'body': res
        }

    def post(self):
        """
        上传用例，更新用例
        /testcase.json {'name':'xx','description':'xx','steps':[]}
        :return:
        """
        testcase = TestCase(
            name=request.json.get('name'),
            description=request.json.get('descripion'),
            steps=json.dumps(request.json.get('steps'))
        )
        db.session.add(testcase)
        db.session.commit()

        return 'ok'


class TaskService(Resource):
    def get(self):
        id = request.args.get('id')
        if id:
            task = Task.query.filter_by(id=id).first()
            return {
                'msg': "ok",
                'body': [json.loads(task.testcases)]
            }

        else:

            tasks = Task.query.all()
            return {
                'msg': "ok",
                'body': [json.loads(task.testcases) for task in tasks]
            }

    def post(self):
        """
       上传用例，更新用例
       /task.json {'testcases':[1,2,3,4]}
       :return:
       """
        testcases_id = request.json.get('testcases')
        task = Task(
            testcases=json.dumps(testcases_id),
        )
        db.session.add(task)
        db.session.commit()

        return {
            'msg': "ok",
        }

    def delete(self):
        """
        删除数据
        :return:
        """
        id = request.json.get('id')
        # print(id)
        if id and Task.query.get(id):
            task = Task.query.get(id)
            db.session.delete(task)
            db.session.commit()
            return {
                'msg': "ok",
            }
        else:
            return {
                'msg':'no such record'
            }



class ReportService(Resource):
    def get(self):
        pass


api.add_resource(TestCaseService, '/testcase')
api.add_resource(TaskService, '/task')
api.add_resource(ReportService, '/report')

if __name__ == '__main__':
    app.run(debug=True)
