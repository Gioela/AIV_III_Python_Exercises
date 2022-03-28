class GegUtils:
    '''
    Geg's utility class
    '''

    def __str__(self) -> str:
        return 'GegUtils is an utility class with static methods'

    @staticmethod
    def is_numeric(value):
        '''
        Check if value is number or not
        '''
        val = str(value)
        if val.startswith('-'):
            val = val[1:]
        return val.strip().replace('.','',1).isnumeric()
    
    @staticmethod
    def is_alpha_value(value):
        '''
        Check if all chars in value are alphabetical char
        '''
        return str(value).isalpha() and type(value) is not bool
    
    @staticmethod
    def is_float_value(value):
        '''
        Check if value could be cast to float
        '''
        try:
            if float(value):
                return True
            else:
                return False
        except ValueError:
            raise ValueError(f"could not convert {type(value)} to float: {value}")
    
    @staticmethod
    def is_int_value(value):
        '''
        Check if value could be cast to int
        '''
        try:
            if int(value):
                return True
            else:
                return False
        except ValueError:
            raise ValueError(f"could not convert {type(value)} to int: {value}")

    @staticmethod
    def is_value_type(value, typ):
        '''
        Check if value could be cast to given type
        '''
        try:
            if typ(value):
                return True
            else:
                return False
        except ValueError:
            raise ValueError(f"could not convert {type(value)} to {typ}. Value: {value}")
        except AssertionError:
            raise AssertionError("could not convert {type(value)} to {typ}. Value: {value}")
