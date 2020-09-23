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
    def __init__(self, passenger_seats_count=None, brand=None, photo_file_name=None, carrying=None):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count
        self.car_type = 'car'


class Truck(CarBase):
    def __init__(self, brand=None, photo_file_name=None, carrying=None, body_whl=None):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        self.car_type = 'truck'
        print("Body_whl before if equal", self.body_whl)
        if type(body_whl) != type(''):
            print("Body_whl now equal", body_whl)
            self.body_length = 0
            self.body_width = 0
            self.body_height = 0    
        else:
            dim = [float(d) for d in self.body_whl.split('x')]
            print(dim)
            self.body_length = dim[0]
            self.body_width = dim[1]
            self.body_height = dim[2]

    def get_body_volume(self):
        return round(self.body_length * self.body_width * self.body_height, 1)


class SpecMachine(CarBase):
    def __init__(self, brand=None, photo_file_name=None, carrying=None, extra=None):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'



def setter(row, obj):
    if row[0] == 'car':
        obj.car_type = row[0]
        obj.passenger_seats_count = row[2]
        obj.brand = row[1]
        obj.photo_file_name = row[3]
        obj.carrying = row[5]
        return obj
    elif row[0] == 'truck':
        obj.car_type = row[0]
        obj.brand = row[1]
        obj.photo_file_name = row[3]
        obj.carrying = row[5]
        obj.body_whl = row[4]
        return obj
    elif row[0] == 'spec_machine':
        obj.car_type = row[0]
        obj.brand = row[1]
        obj.photo_file_name = row[3]
        obj.carrying = row[5]
        obj.extra = row[6]
        return obj


def get_car_list(csv_filename):
    car_list = []
    try:
        with open(csv_filename) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)  # пропускаем заголовок
            for row in reader:
                if len(row[0]) != 0:
                    if row[0] == 'car':
                        car = Car()
                        car_list.append(setter(row,car))
                    elif row[0] == 'truck':
                        truck = Truck()
                        car_list.append(setter(row, truck))
                    elif row[0] == 'spec_machine':
                        sp = SpecMachine()
                        car_list.append(setter(row, sp))
    except IndexError:
       pass        
    return car_list