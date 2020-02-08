"""Initial tasks to be invoked after containers up.

Tasks are defined with ``invoke`` package.
See details at http://www.pyinvoke.org/.
"""
import os
import time

from invoke import task


def wait_port_is_open(host, port):
    import socket
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((host, port))
            sock.close()
            if result == 0:
                return
        except socket.gaierror:
            pass
        time.sleep(1)


@task
def init_db(ctx):
    wait_port_is_open(os.getenv('DB_HOST', 'db'), 5432)
    ctx.run('python sandbox/manage.py makemigrations')
    ctx.run('python sandbox/manage.py migrate')


@task
def start_celery(ctx):
    ctx.run('cp /code/celery.conf /etc/supervisor/conf.d/ && '
            'service supervisor start && '
            'supervisorctl start celery')


@task
def run(ctx):
    init_db(ctx)
    start_celery(ctx)

    ctx.run('python sandbox/manage.py runserver 0.0.0.0:8990')
