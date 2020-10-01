import csv
import os

class CarBase:

    def __new__(cls, *args):
        if len(args) >= 3:
            ch = []
            for i in range(len(args)):
                if len(args[i]) > 0:
                    ch.append(1)
            if sum(ch) == len(args):    
                return object.__new__(cls)

    def __init__(self, brand=None, photo_file_name=None, carrying=None):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
    

    def get_photo_file_ext(self):
        if self.photo_file_name:
            ty = os.path.splitext(self.photo_file_name)
        if ty[1] in ('.jpg', '.jpeg', '.png', '.gif'):
            return ty[1]

    @property
    def carrying(self):
        return self.__carrying
    
    @carrying.setter
    def carrying(self, value):
            try:
                if len(value) > 0 and type(float(value)) == type(0.):
                    self.__carrying = float(value)
            except (ValueError, TypeError):
                return None

class Car(CarBase):
    car_type = 'car'
    def __new__(cls, *args):
        if len(args) >= 4:
            ch = []
            for i in range(len(args)):
                if len(args[i]) > 0:
                    ch.append(1)
            if sum(ch) == len(args):
                try:
                    if len(args[3]) > 0 and isinstance(int(args[3]), int):
                        return object.__new__(cls)
                except ValueError:
                    return None

    def __init__(self, brand=None, photo_file_name=None, carrying=None,
    passenger_seats_count=None):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count
    
    @property
    def passenger_seats_count(self):
        return self.__passenger_seats_count

    @passenger_seats_count.setter
    def passenger_seats_count(self, value):
        if len(value) > 0 and isinstance(int(value), int):
            self.__passenger_seats_count = int(value)
        


class Truck(CarBase):
    car_type = 'truck'
    def __new__(cls, *args):
        if len(args) == 4:
            return object.__new__(cls)


    def __init__(self, brand=None, photo_file_name=None, carrying=None, body_whl=None):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        inf = [float(d) for d in self.body_whl.split('x')]
        self.body_length = inf[0]
        self.body_width = inf[1]
        self.body_height = inf[2]
    

    @property
    def body_whl(self):
        return self.__body_whl
    
    @body_whl.setter
    def body_whl(self, value):
        if isinstance(value, str) and len(value) >= 5:
            try:
                if len([float(p) for p in value.split('x')])>3:
                    self.__body_whl = '0.0x0.0x0.0'
                elif isinstance(float(value.split('x')[0]), float):
                    self.__body_whl = value
                else:
                    self.__body_whl = '0.0x0.0x0.0'
            except ValueError:
                self.__body_whl = '0.0x0.0x0.0'
        else:
            self.__body_whl = '0.0x0.0x0.0'
            


    def splitter(self, bw):
        dim = [float(d) for d in bw.split('x')]
        print('classmethod splitter working', bw)
        print(dim[0], dim[1], dim[2])
        return (dim[0], dim[1], dim[2])


    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height
    

class SpecMachine(CarBase):
    car_type = 'spec_machine'
    def __new__(cls, *args):
        if len(args) >= 4:
            ch = []
            for i in range(len(args)):
                if len(args[i]) > 0:
                    ch.append(1)
            if sum(ch) == len(args):
                try:
                    if len(args[3]) > 0 and isinstance(args[3], str):
                        return object.__new__(cls)
                except ValueError:
                    return None

    def __init__(self, brand=None, photo_file_name=None, carrying=None, extra=None):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

    @property
    def extra(self):
        return self.__extra

    @extra.setter
    def extra(self, value):
        try:
            if len(value) > 0 and isinstance(value, str):
                self.__extra = value
        except (ValueError,TypeError):
            return None        



def setter(row):
    if row[0] == 'car':
        brand = row[1]
        photo_file_name = row[3]
        carrying = row[5]
        passenger_seats_count = row[2]
        #print('we printing car attributes', brand, photo_file_name, carrying, passenger_seats_count)
        return brand, photo_file_name, carrying, passenger_seats_count
    elif row[0] == 'truck':
        brand = row[1]
        photo_file_name = row[3]
        carrying = row[5]
        body_whl = row[4]
        return brand, photo_file_name, carrying, body_whl
    elif row[0] == 'spec_machine':
        brand = row[1]
        photo_file_name = row[3]
        carrying = row[5]
        extra = row[6]
        return brand, photo_file_name, carrying, extra


def get_car_list(csv_filename):
    car_list = []
    try:
        with open(csv_filename) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)  # пропускаем заголовок
            for row in reader:
                if len(row[0]) != 0:
                    if row[0] == 'car':
                        car = Car(row[1], row[3], row[5], row[2])
                        car_list.append(car)
                    elif row[0] == 'truck':
                        truck = Truck(row[1], row[3], row[5], row[4])
                        car_list.append(truck)
                    elif row[0] == 'spec_machine':
                        sp = SpecMachine(row[1], row[3], row[5], row[6])
                        car_list.append(sp)
    except IndexError:
       pass        
    if car_list.count(None) == len(car_list):
        return []
    else:
        return car_list