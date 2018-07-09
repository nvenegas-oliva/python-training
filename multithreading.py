
import threading


def simple_count(factor_limit=1):
    counter = 0
    while counter < 10000 * factor_limit:
        counter += 1
        print("thread.name=%s\tid=%d\tfactor_limit=%d\tcounter=%d" % (
            threading.current_thread().getName(),
            threading.current_thread().ident,
            factor_limit,
            counter)
        )


N_THREADS = 5
for n_thread in range(N_THREADS):
    thread = threading.Thread(name="thread_%d" % n_thread, target=simple_count, args=(n_thread))
    thread.start()
