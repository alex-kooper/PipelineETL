class RecordFormatError:
    pass

class Record(object):
    __slots__ = ()
    
    def __init__(self, values):
        if len(self.__class__.__slots__) != len(values):
            raise RecordFormatError()

        for i, v in enumerate(values):
            setattr(self, self.__class__.__slots__[i], v)

    def __iter__(self):
        for name in self.__class__.__slots__:
            yield getattr(self, name)
