import os
from subprocess import Popen, check_call, PIPE
import time
from contextlib import contextmanager

example_root = os.path.join(os.path.dirname(__file__), '..')

@contextmanager
def pushd(path):
    prev = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(prev)

@contextmanager
def run_server(*proc):
    server = Popen(proc, stdout=PIPE, stderr=PIPE)
    try:
        time.sleep(1)
        if server.poll():
            raise Exception('Cannot run server: %s' % (' '.join(proc)))

        yield
    finally:
        if server.poll():
            print(server.stdout.read())
            print(server.stderr.read())
            raise Exception('Server is terminated unexpectedly.')
        server.kill()
        server.wait()

@contextmanager
def run(*args, **kwargs):
    p = Popen(args, stdin=PIPE)
    if 'input' in kwargs:
        p.stdin.write(kwargs['input'].encode('utf-8'))
        p.stdin.close()
    ret = p.wait()
    if ret != 0:
        raise Exception('terminated with error: %d' % ret)
