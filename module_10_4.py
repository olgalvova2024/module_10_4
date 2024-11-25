from threading import Thread
from time import sleep
from random import randint
import queue

class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *args, **kwargs):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for i in range(len(guests)):
            if i < len(self.tables):
                self.tables[i].guest = guests[i].name
                Guest(guests[i]).start()
                print(f'{self.tables[i].guest} сел(а) за стол {self.tables[i].number}.')
            else:
                print(f'{guests[i].name} в очереди')
                self.queue.put(guests[i].name)


    def discuss_guests(self):
        while not self.queue.empty():
            for i in range(len(self.tables)):
                if self.tables[i].guest and not Guest(guests[i]).is_alive():
                    print(f'{tables[i].guest} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {i+1} свободен')
                    tables[i].guest = None
                if not self.queue.empty() and tables[i].guest is None:
                    next_guest = self.queue.get()
                    self.tables[i].guest = next_guest
                    Guest(next_guest).start()
                    print(f'{tables[i].guest} вышел(-ла) из очереди и сел(-а) за стол номер {i+1}')



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
            'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
