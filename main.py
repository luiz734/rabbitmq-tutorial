# Uber app simulator using RabbitMQ
import string

from consumer import consumer
from publisher import publisher
import threading
import random
import time


def main():
    car_type_a = input(f"Digite o tipo do seu veículo['normal', 'utilitario', 'luxo']\n")

    origem_a = input(f"Digite o bairro em que se encontra: \n ['centro', 'aguaverde', 'batel']\n")
    destination_a = input(f"Digite o bairro de destino: \n ['centro', 'aguaverde', 'batel']\n")

    car_type_b = input(f"Digite o tipo do seu veículo['normal', 'utilitario', 'luxo']\n")

    origem_b = input(f"Digite o bairro em que se encontra: \n ['centro', 'aguaverde', 'batel']\n")
    destination_b = input(f"Digite o bairro de destino: \n ['centro', 'aguaverde', 'batel']\n")

    car_type = ['normal', 'utilitario', 'luxo']
    origem_destination = ['centro', 'aguaverde', 'batel']
    thread_client_a = threading.Thread(target=publisher, args=(random.choice(string.ascii_uppercase), 'normal',
                                                                   'centro', 'centro'))
    thread_client_b = threading.Thread(target=publisher, args=(random.choice(string.ascii_uppercase), random.choice(car_type),
                                                                   random.choice(origem_destination), random.choice(origem_destination)))
    thread_uber_a = threading.Thread(target=consumer, args=(car_type_a, origem_a, destination_a, "Uber A"))
    thread_uber_b = threading.Thread(target=consumer, args=(car_type_b, origem_b, destination_b, "Uber B"))

    thread_client_a.start()
    thread_client_b.start()
    thread_uber_a.start()
    thread_uber_b.start()

    # thread_uber_a.join()
    # thread_uber_b.join()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e} ")
