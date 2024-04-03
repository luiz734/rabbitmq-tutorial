
# Private lessons app simulator using RabbitMQ

from publisher import publisher


from constants import *

def inputs():
    time_of_day = input(f"Type the time of day: {TIME_OF_DAY}\n")
    subject = input(f"Type the subject: {SUBJECTS}\n")
    level = input(f"Type the level: {LEVEL}\n")

    return time_of_day, subject, level

def main():
    time_of_day, subject, level = inputs()
    time_of_day2, subject2, level2 = inputs()

    publisher(client='Client A', time_of_day=time_of_day, subject=subject, level=level)
    publisher(client='Client B', time_of_day=time_of_day2, subject=subject2, level=level2)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e} ")
