from time import sleep
from termcolor import colored


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый', 'Желтый']

    def running(self):
        i = 0
        while True:
            if i % 4 == 0:
                print(colored(TrafficLight.__color[i], 'red'))
                sleep(7)
            elif (i % 4 == 1) or (i % 4 == 3):
                print(colored(TrafficLight.__color[i], 'yellow'))
                sleep(2)
            elif i % 4 == 2:
                print(colored(TrafficLight.__color[i], 'green'))
                sleep(7)
            i += 1
            if i == 4:
                i = 0


t = TrafficLight()
t.running()
