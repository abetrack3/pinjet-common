import time
from typing import NoReturn

from pinjet.common.decorators.function_timer import timeit


@timeit
def time_consuming_function() -> NoReturn:

    print('Consuming function start')

    time.sleep(5)

    print('Consuming function end')


time_consuming_function()
