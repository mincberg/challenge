class IllegalCarError(Exception):
    def __init__(self, kind):
        self.kind = kind

    def __str__(self):
        return '{}'.format(self.kind)

class Car():
    def __init__(self, pax_count, car_mass, gear_count):
        self.pax_count = pax_count
        self.car_mass = car_mass
        self.gear_count = gear_count

        try:
            pax_count in range(1,5)
            raise IllegalCarError('Pax count nust be greater than 1 and less than 5!')
        except IllegalCarError as e:
            print('Error: {}'.format(e))
        try:
            car_mass <= 2000
            raise IllegalCarError('Car mass cannot be greater than 2000kg.')
        except IllegalCarError as e:
            print('Error: {}'.format(e))

        self.total_mass = pax_count * 70 + car_mass

    def getInfo(self):
        print('Pax count:  {}'.format(self.pax_count))
        print('Car mass:   {}'.format(self.car_mass))
        print('Gear count: {}'.format(self.gear_count))


if __name__ == '__main__':
    c1 = Car(3,1600,5)
    c1.getInfo()
    print(c1.total_mass)
    c2 = Car(3,2001,5)