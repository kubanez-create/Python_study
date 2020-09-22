import csv
import os

class CarBase:
    def __init__(self, brand=None, photo_file_name=None, carrying=None):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        ty = os.path.splitext(self.photo_file_name)
        return ty[1]



class Car(CarBase):
    def __init__(self, brand=None, photo_file_name=None, carrying=None, passenger_seats_count=None):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand=None, photo_file_name=None, carrying=None, body_whl=None):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        if len(self.body_whl) == 0:
            self._body_length = 0
            self._body_width = 0
            self._body_height = 0    
        dim = [float(d) for d in self.body_whl.split('x')]
        self._body_length = dim[0]
        self._body_width = dim[1]
        self._body_height = dim[2]

    def get_body_volume(self):
        return round(self._body_length * self._body_width * self._body_height, 1)


class SpecMachine(CarBase):
    def __init__(self, brand=None, photo_file_name=None, carrying=None, extra=None):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def parser(row):
    return tuple(row[1], row[2], row[3], row[4])


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if row[0] == 'car':
                car = Car(parser(row))
                car_list.append(car)
            elif row[0] == 'truck':
                truck = Truck(parser(row))
                car_list.append(truck)
            elif row[0] == 'spec_machine':
                sp = SpecMachine(parser(row))
                car_list.append(sp)
            
    return car_list