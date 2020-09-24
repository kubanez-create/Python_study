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
    car_type = 'car'
    def __init__(self, passenger_seats_count=None, brand=None, photo_file_name=None, carrying=None):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count
    
    @staticmethod
    def is_data_valid(row):
        l = []
        ind = 0
        for i in row:
            if ind != 4:
                existance = bool(len(i)) #true if string is not blank
                form = bool(type(i)==type('')) #true if type is str
                l.append(bool(existance and form))
            ind += 1
        if sum(l) == (len(row) - 2):
            return True
        


class Truck(CarBase):
    car_type = 'truck'
    def __init__(self, brand=None, photo_file_name=None, carrying=None, body_whl=None):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl

    def splitter(self, bw):
        if bool(len(bw)):
            dim = [float(d) for d in bw.split('x')]
            print('classmethod splitter working', bw)
            print(dim[0], dim[1], dim[2])
            return (dim[0], dim[1], dim[2])
        else:
            bw = '0.0x0.0x0.0'
            dim = [float(d) for d in bw.split('x')]
            print('classmethod splitter working', bw)
            print(dim[0], dim[1], dim[2])
            return (dim[0], dim[1], dim[2])


    def get_body_volume(self):
        return round(self.body_length * self.body_width * self.body_height, 1)
    
    @staticmethod
    def is_data_valid(row):
        l = []
        ind = 0
        for i in row:
            if ind != 2:
                existance = bool(len(i)) #true if string is not blank
                form = bool(type(i)==type('')) #true if type is str
                l.append(bool(existance and form))
            ind += 1
        if sum(l) == (len(row) - 2):
            return True
        else:
            return False


class SpecMachine(CarBase):
    car_type = 'spec_machine'
    def __init__(self, brand=None, photo_file_name=None, carrying=None, extra=None):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        
    @staticmethod
    def is_data_valid(row):
        l = []
        ind = 0
        for i in row:
            if ind != 4:
                existance = bool(len(i)) #true if string is not blank
                form = bool(type(i)==type('')) #true if type is str
                l.append(bool(existance and form))
            ind += 1
        if sum(l) == (len(row) - 2):
            return True
        



def setter(row, obj):
    if row[0] == 'car':
        if Car.is_data_valid(row):
            obj.car_type = row[0]
            obj.passenger_seats_count = int(row[2])
            obj.brand = row[1]
            obj.photo_file_name = row[3]
            obj.carrying = float(row[5])
        return obj
    elif row[0] == 'truck':
        obj.car_type = row[0]
        obj.brand = row[1]
        obj.photo_file_name = row[3]
        obj.carrying = int(row[5])
        obj.body_whl = row[4]
        return obj
    elif row[0] == 'spec_machine':
        if SpecMachine.is_data_valid(row):
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
                        obj = Truck()
                        truck = Truck(setter(row, obj))
                        print(setter(row, truck).__dict__)
                        truck.body_length, truck.body_width, truck.body_height = truck.splitter(truck.body_whl)
                        if Truck.is_data_valid(row):
                            car_list.append(truck)
                    elif row[0] == 'spec_machine':
                        sp = SpecMachine()
                        car_list.append(setter(row, sp))
    except IndexError:
       pass        
    return car_list