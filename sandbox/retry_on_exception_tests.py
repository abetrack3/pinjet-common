from pinjet.common.decorators.retry_on_exception import retry_on_exception


@retry_on_exception
def my_function():
    print('my_function')
    raise RuntimeError


@retry_on_exception(exception_type=ValueError)
def another_function():
    print('another_function')
    raise ValueError


@retry_on_exception(retries=3)
def yet_another_function():
    print('yet another')
    raise TimeoutError('yet another')


@retry_on_exception(retries=5, exception_type=IOError)
def one_more_function():
    print('one more')
    raise IOError('one more')


