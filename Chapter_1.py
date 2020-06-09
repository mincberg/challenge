class Car():
    def __init__(self, pax_count, car_mass, gear_count):
        self.pax_count = pax_count
        self.car_mass = car_mass
        self.gear_count = gear_count

        if not pax_count in range(1,5):
            raise IllegalCarError("Pax count nust be greater than 1 and less than 5!")
        if car_mass >2000:
            raise ValueError("Car mass cannot be greater than 2000kg.")

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