# Private lessons app simulator using RabbitMQ

from publisher import publisher
import sys


from constants import *


def inputs():
    time_of_day = input(f"Type the time of day: {TIME_OF_DAY}\n")
    subject = input(f"Type the subject: {SUBJECTS}\n")
    level = input(f"Type the level: {LEVEL}\n")

    return time_of_day, subject, level


def main():
    if len(sys.argv) == 5:
        client_name, time_of_day, subject, level = sys.argv[1:5]
    else:
        client_name = "Client A"
        time_of_day, subject, level = inputs()

    publisher(client=client_name, time_of_day=time_of_day, subject=subject, level=level)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e} ")
