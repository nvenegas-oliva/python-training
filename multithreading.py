
import threading
import time


def simple_count(factor_limit=1):
    counter = 0
    while counter < 100000 * factor_limit:
        counter += 1
        print("thread.name=%s\tid=%d\tfactor_limit=%d\tcounter=%d" % (
            threading.current_thread().getName(),
            threading.current_thread().ident,
            factor_limit,
            counter)
        )


N_THREADS = 5
for n_thread in range(N_THREADS):
    thread = threading.Thread(name="thread_%d" % n_thread, target=simple_count, args=(n_thread,))
    thread.start()


vmax_threads = {}


def count_seconds(seconds):
    """Count until time limit"""
    global vmax_threads
    counter = 0
    start = time.time()
    limit = start + seconds
    name = threading.current_thread().getName()
    while start <= limit:
        counter += 1
        start = time.time()
        print(name, counter)

    vmax_threads[name] = counter
    if threading.active_count() == 2:
        print(vmax_threads)
        print(threading.enumerate())


seconds = 2
for n_thread in range(5):
    thread = threading.Thread(name='thread%s' % n_thread,
                              target=contar,
                              args=(seconds,))
    thread.start()
