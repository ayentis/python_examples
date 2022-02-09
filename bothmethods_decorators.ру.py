class Methods (object):
    def imeth(self, х) :
        print([self, х])


    @staticmethod
    def smeth (x) :
        print([x]) # Статический метод: экземпляр не передается


    @classmethod
    def cmeth(cls, x):
        print([cls, x]) # Метод класса: получает класс, не экземпляр


    @property
    def name(self):
        return 'Bob ' + self.__class__ .__name__

obj = Methods()
obj.imeth(1)
obj.smeth(2)
obj.cmeth(3)
obj.name