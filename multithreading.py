
import threading


def simple_count():
    counter = 0
    while counter < 1000000:
        counter += 1
        print("thread.name=%s\tid=%d\tcounter=%d" % (
            threading.current_thread().getName(),
            threading.current_thread().ident,
            counter)
        )


N_THREADS = 5
for n_thread in range(N_THREADS):
    thread = threading.Thread(name="thread_%d" % n_thread, target=simple_count)
    thread.start()
