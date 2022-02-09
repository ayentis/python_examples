#!python
# Файл listinherited.ру (Python 2.Х + З.Х)

from shutil import copy


class ListInherited:
    def attrnames(self):
        result = ''
        for attr in dir (self) :
            if attr[:2] == '__' and attr[-2:] == '__':
                result += '\t%s\n' % attr
            else:
                result += '\t%s=%s\n' % (attr, getattr(self, attr))
        return result

    def __str__(self):
        return 'cinstance of %s, address %s:\n%s>' % (
            self.__class__ .__name__,
            id(self) ,
            self.__attrnames())

    def __attrnames(self, indent=' ' * 4):
        result = 'Unders%s\n%s%%s\nOthers%s\n' % ('-' * 77, indent, '-' * 77)
        unders = []
        for attr in dir(self):
            # dir() экземпляра
            if attr[: 2] == '__' and attr[-2:] == '__':
                unders.append(attr)
            else:
                display = str(getattr(self, attr))[:82 - (len(indent) + len(attr))]
                result += '%s%s=%s\n' % (indent, attr, display)
        return result % ', '.join(unders)


if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInherited)