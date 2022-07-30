class Tomato:
    # Стадии созревания помидора
    states = {1: 'соцветие', 2: 'зеленый, несозревший', 3: 'красный,сочный и наливной'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    # Переход к следующей стадии созревания
    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    # Узнаем стадию созревания помидоров
    def print_state(self):
        if self.state < 3:
            print(f'Томат {self.index+1} еще {Tomato.states[self.state]}')
        else:
            print(f'Томат {self.index+1} уже {Tomato.states[self.state]}, пора собирать урожай')

    # Проверка, созрел ли томат
    def tomato_is_ripe(self):
        if self.state == 3:
            return True
        return False

    # Защищенные(protected) методы

    def change_state(self):
        if self.state < 3:
            self.state += 1
        self.print_state()


class TomatoBush():

    # Создаем список из объектов класса Tomato
    def __init__(self, num):
        arr = []
        self.tomatoes = arr
        for stage in range(num):
            arr.append(Tomato(stage))

    # Переводим все томаты из списка на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяем, все ли помидоры созрели
    def all_are_ripe(self):
        for tomato in self.tomatoes:
            if tomato.tomato_is_ripe():
                return True


class Gardener():

    # Выдаем садовнику растение для ухода
    def __init__(self, name, plant):
        self.name = name
        self.plant = plant

    # Ухаживаем за растением
    def work(self):
        print(f'{self.name} тяжело работает в саду...')
        self.plant.grow_all()
        print(f'{self.name} закончил работать')

    # Собираем урожай
    def harvest(self):
        if self.plant.all_are_ripe():
            print('Сбор урожая завершен')
        else:
            print('Слишком рано. Урожай еще не созрел!')


great_harvest = TomatoBush(3)
gardener = Gardener('Vova', great_harvest)
gardener.work()
gardener.work()
gardener.work()
gardener.harvest()
