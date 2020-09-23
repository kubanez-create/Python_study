import csv
import os

class CarBase:
    def __init__(self, car_type = None, brand=None, photo_file_name=None, carrying=None):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        ty = os.path.splitext(self.photo_file_name)
        return ty[1]



class Car(CarBase):
    def __init__(self, passenger_seats_count, car_type=None, brand=None, photo_file_name=None, carrying=None):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, car_type=None, brand=None, photo_file_name=None, carrying=None, body_whl=None):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.body_whl = body_whl
        if not self.body_whl == 0:
            self._body_length = 0
            self._body_width = 0
            self._body_height = 0    
        else:
            dim = [float(d) for d in self.body_whl.split('x')]
            self._body_length = dim[0]
            self._body_width = dim[1]
            self._body_height = dim[2]

    def get_body_volume(self):
        return round(self._body_length * self._body_width * self._body_height, 1)


class SpecMachine(CarBase):
    def __init__(self, car_type=None, brand=None, photo_file_name=None, carrying=None, extra=None):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra


def parser(row, ty_car):
    if ty_car == 'car':
        return row[2], row[1], row[3], row[5]
    elif ty_car == 'truck':
        return row[1], row[3], row[5], row[4]
    elif ty_car == 'spec_machine':
        return row[1], row[3], row[5], row[6]


def get_car_list(csv_filename):
    car_list = []
    try:
        with open(csv_filename) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)  # пропускаем заголовок
            for row in reader:
                if len(row[0]) != 0:
                    if row[0] == 'car':
                        car = Car(parser(row, 'car'))
                        car_list.append(car)
                    elif row[0] == 'truck':
                        truck = Truck(parser(row, 'truck'))
                        car_list.append(truck)
                    elif row[0] == 'spec_machine':
                        sp = SpecMachine(parser(row, 'spec_machine'))
                        car_list.append(sp)
    except IndexError:
       pass        
    return car_list