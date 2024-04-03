
# Private lessons app simulator using RabbitMQ

from consumer import consumer
import threading
from constants import *


def main():
    thread_a = threading.Thread(target=consumer, args=('Teacher A', 'MORNING', 'MATH', 'BASIC'))
    thread_b = threading.Thread(target=consumer, args=('Teacher B', 'EVENING', 'MATH', 'ADVANCED'))

    thread_a.start()
    thread_b.start()

    thread_a.join()
    thread_b.join()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e} ")
