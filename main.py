# Uber app simulator using RabbitMQ
import string
import os

from consumer import consumer
from publisher import publisher
import threading
import random
import time


def main():
    # car_type_a = ask_question(f"Tipo de veículo", car_types)
    # origem_a = ask_question(f"Bairro em que se encontra", neighborhoods)
    # destination_a = ask_question(f"Bairro destino", neighborhoods)
    # car_type_b = ask_question(f"Tipo de veículo", car_types)
    # origem_b = ask_question(f"Bairro em que se encontra", neighborhoods)
    # destination_b = ask_question(f"Bairro destino", neighborhoods)

    # p1 = threading.Thread(target=publisher, args=("João", "*", "centro", "batel"))
    # c1 = threading.Thread(target=consumer, args=("Zezão", "normal", "*", "*"))
    #
    # c1.start()
    # time.sleep(2)
    # p1.start()
    # c1.join()
    # p1.join()
    pass


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e} ")
