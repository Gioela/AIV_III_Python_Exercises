from math import pi, pow
from utils.geg_utils import GegUtils

class GegCircle:

    def __init__(self, *, radius = None, diameter = None, name='C'):

        if self._validate_input_value(radius, diameter):
            self.name = name
            self._radius = float(radius) if radius is not None else float(diameter) / 2
            self._diameter = float(diameter) if diameter is not None else self.radius * 2
            self._circle_area()
            self._circle_circumference()

    def _validate_input_value(self, r, d):
        '''
        Returns True if the input radius and diameter are validated.
        Otherwise will raise an exception
        '''
        if r is None and d is None:
            raise ValueError('Missing arguments')

        if not (GegUtils.is_numeric(r) or GegUtils.is_numeric(d)):
            raise ValueError('One or more init arguments are not numeric')
        
        if r is None:
            d = float(d)
            r = d / 2
        # elif d is None:
        else:
            r = float(r)
            d = r * 2
        
        if r <= 0 or d <= 0:
            raise ValueError('Init arguments must be positive numbers')
        if r * 2 != d:
            raise TypeError(f'Init values r:\'{r}\' and d:\'{d}\' are incompatible')

        return True

    @classmethod
    def from_radius(cls, *, radius, name='C'):
        return GegCircle(radius=radius, name=name)

    @classmethod
    def from_diameter(cls, *, diameter, name='C'):
        return GegCircle(diameter=diameter, name=name)

    def __str__(self) -> str:
        return f'Circle {self.name} has attributes: Radius={self.radius} | Diameter={self.diameter}'

    def __repr__(self) -> str:
        return f'GegCircle(radius={self.radius}, diameter={self.diameter}, name={self.name})'

    def __add__(self, other):
        if isinstance(other, GegCircle):
            new_name = '{0}+{1}'.format(self.name, other.name)
            return GegCircle(radius=(self.radius + other.radius), name=new_name )
        elif GegUtils.is_numeric(other):
            return GegCircle(radius=(self.radius + other), name=self.name )
        elif GegUtils.is_alpha_value(other):
            return GegCircle(radius=self.radius, name=self.name + other )
        return None
    
    def __radd__(self, other):
        if GegUtils.is_alpha_value(other) :
            return GegCircle(radius=self.radius, name=(other + self.name) )
        return self.__add__(other)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, GegCircle):
            return self.radius == __o.radius
        return False
    
    def __lt__(self, __o: object ) -> bool:
        if isinstance(__o, GegCircle):
            return self.radius < __o.radius
        raise TypeError(f"operator '<' not supported between instances of 'GegCircle' and '{type(__o)}'")

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, r):
        self._radius = r
    
    @property
    def diameter(self):
        return self._diameter
    
    @diameter.setter
    def diameter(self, d):
        self._diameter = d
    
    @property
    def area(self):
        return self._area

    def _circle_area(self):
        # self.area = self.radius * self.radius * pi
        self._area = pow(self.radius, 2) * pi
    
    @property
    def circumference(self):
        return self._circumference
    
    def _circle_circumference(self):
        self._circumference = self.radius * 2 * pi

    @staticmethod
    def get_area_with_radius(radius):
        '''
        Returns the area of circle with given radius
        '''
        return pow(radius, 2) * pi
    
    @staticmethod
    def get_area_with_diameter(diameter):
        '''
        Returns the area of circle with given diameter
        '''
        return pow(diameter, 2) * pi / 4