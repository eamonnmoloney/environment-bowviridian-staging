import sqlite3
import os.path
from bottle import route, run, debug, template, request

basedir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(basedir, 'todo.db')


@route('/todo')
def todo_list():
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
        result = c.fetchall()
        c.close()
    template_path = os.path.join(basedir, 'make_table.tpl')
    return template(template_path, rows=result)


@route('/new', method='GET')
def new_item():
    if request.GET.save:

        new = request.GET.task.strip()
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, 1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new task was inserted into the database, the IDs is %s</p>' % new_id
    else:
        template_path = os.path.join(basedir, 'new_task.tpl')
        return template(template_path)


debug(True)
run(host='0.0.0.0', port=6080, reloader=True)
