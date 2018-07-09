import contextlib
from threading import local

_local = local()


def get_current_context():
    return _local.stack[-1];


@contextlib.contextmanager
def context():
    ctx = {}
    _local.__dict__.setdefault('stack', []).append(ctx)
    yield ctx
    _local.stack.pop()
