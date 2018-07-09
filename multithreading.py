
import threading


def simple_count():
    counter = 0
    while counter < 100:
        counter += 1
        print("thread.name=%s\tid=%d\tcounter=%d" % (
            threading.current_thread().getName(),
            threading.current_thread().ident,
            counter)
        )


th1 = threading.Thread(target=simple_count)
th2 = threading.Thread(target=simple_count)

th1.start()
th2.start()
