from datetime import datetime

import requests


def test_testcase_get():
    testcase_url = 'http://127.0.0.1:5000/testcase'
    r = requests.post(
        testcase_url,
        json={
            'name': f"case1 {datetime.now().isoformat()}",
            'description': 'desc1',
            'steps': ['1', '2', '3']

        }

    )
    assert r.status_code == 200
    r = requests.get(testcase_url)
    print(r.json())
    assert r.json()['body']


def test_task_post():
    task_url = 'http://127.0.0.1:5000/task'
    r = requests.post(
        task_url,
        json={

            'testcases': ['1', '2', '3']

        }

    )
    assert r.status_code == 200
    assert r.json()['msg'] == 'ok'

def test_task_delete():
    task_url = 'http://127.0.0.1:5000/task'
    r = requests.delete(
        task_url,
        json={
            'id': 5
        }

    )
    assert r.status_code == 200
    # assert r.json()['msg'] == 'ok'
    print(r.json()['msg'])

