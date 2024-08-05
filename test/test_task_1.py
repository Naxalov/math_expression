try:
    from task_1 import fn
except ImportError:
    fn = None
# Create a test to check if function exists
def test_fn_exists():
    assert hasattr(fn, '__call__'), 'Function not found'

def test_fn():
    assert fn(8) == 2.0, 'Wrong answer'