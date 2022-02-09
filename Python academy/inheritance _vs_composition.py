class PropertyChangeException(Exception):
    pass


class Tiers:

    def __init__(self, size):
        self.__pressure = 0
        self.__size = size

    def get_pressure(self):
        return self.__pressure

    def pump(self, new_pressure):
        self.__pressure = new_pressure

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self):
        raise PropertyChangeException("Can't change protected attribute")

    @size.deleter
    def size(self):
        raise PropertyChangeException("Can't change protected attribute")


class Engine:

    def __init__(self, fuel_type):
        self.__fuel_type = fuel_type
        self.__status = "off"

    def get_fuel_type(self):
        return self.__fuel_type

    @property
    def fuel_type(self):
        return self.__fuel_type

    @fuel_type.setter
    def fuel_type(self):
        raise PropertyChangeException("Can't change protected attribute")

    @fuel_type.deleter
    def fuel_type(self):
        raise PropertyChangeException("Can't change protected attribute")

    def start(self):
        self.__status = "on"

    def stop(self):
        self.__status = "off"

    def get_status(self):
        return self.__status


class Vehicle:

    def __init__(self, VIN, engine, tires):
        self.__VIN = VIN
        self.engine = engine
        self.tiers = tires


city_tires = Tiers(15)
off_road_tires = Tiers(18)

electric_engine = Engine("Electric")
petrol_engine = Engine("Petrol")

city_car = Vehicle("1234", electric_engine, city_tires)
all_terrain_car = Vehicle("5678", petrol_engine, off_road_tires)

city_car.engine.start()
city_car.tiers.pump(2)
print(city_car.engine.get_status(), city_car.tiers.get_pressure())