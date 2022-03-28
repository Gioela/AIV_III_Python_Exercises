from turtle import circle
import pytest
from core.ex_circle import GegCircle

'''
Test the GegCircle initialization with diameter input parameter
'''

@pytest.fixture
def circle_01():
    return GegCircle(diameter=6, name='A')

def test_geg_circle_init_with_default_name():
    circle = GegCircle(diameter=7.2)
    assert circle is not None
    assert isinstance(circle, GegCircle)
    assert circle.name == 'C'
    assert circle.radius == 3.6
    assert circle.diameter == 7.2

def test_geg_circle_init(circle_01):
    assert circle_01 is not None
    assert isinstance(circle_01, GegCircle)

def test_geg_circle_properties_int_radius(circle_01):
    assert circle_01.name == 'A'
    assert circle_01.radius == 3.0
    assert circle_01.diameter == 6.0

def test_geg_circle_area(circle_01):
    area = GegCircle.get_area_with_diameter(circle_01.diameter)
    assert circle_01.area == 28.274333882308138
    assert area == 28.274333882308138

# __str__
def test_geg_circle_str(circle_01):
    assert str(circle_01) == 'Circle A has attributes: Radius=3.0 | Diameter=6.0'

# __add__
def test__add__2_geg_circle(circle_01):
    circle_B = GegCircle(diameter=2, name='B')
    circle_AB = circle_01 + circle_B
    assert str(circle_AB) == 'Circle A+B has attributes: Radius=4.0 | Diameter=8.0'

def test__add__geg_circle_with_int_number(circle_01):
    circle_B = circle_01 + 10
    assert circle_B.name == 'A'
    assert circle_B.radius == 13
    assert circle_B.diameter == 26
    assert str(circle_B) == 'Circle A has attributes: Radius=13.0 | Diameter=26.0'

def test__add__geg_circle_with_float_number(circle_01):
    circle_B = circle_01 + 10.5
    assert circle_B.name == 'A'
    assert circle_B.radius == 13.5
    assert circle_B.diameter == 27
    assert str(circle_B) == 'Circle A has attributes: Radius=13.5 | Diameter=27.0'

def test__add__geg_circle_with_chars(circle_01):
    circle_B = circle_01 + 'Pippo'
    assert circle_B.name == 'APippo'
    assert circle_B.radius == 3
    assert circle_B.diameter == 6
    assert str(circle_B) == 'Circle APippo has attributes: Radius=3.0 | Diameter=6.0'

def test__add__geg_circle_failure(circle_01):
    no_obj = circle_01 + True
    assert no_obj == None

# __radd__
def test__radd__geg_circle_with_int_number(circle_01):
    circle_B = 10 + circle_01
    assert circle_B.name == 'A'
    assert circle_B.radius == 13
    assert circle_B.diameter == 26
    assert str(circle_B) == 'Circle A has attributes: Radius=13.0 | Diameter=26.0'

def test__radd__geg_circle_with_float_number(circle_01):
    circle_B = 10.5 + circle_01
    assert circle_B.name == 'A'
    assert circle_B.radius == 13.5
    assert circle_B.diameter == 27
    assert str(circle_B) == 'Circle A has attributes: Radius=13.5 | Diameter=27.0'

def test__radd__geg_circle_with_chars(circle_01):
    circle_B = 'Bell' + circle_01
    assert circle_B.name == 'BellA'
    assert circle_B.radius == 3
    assert circle_B.diameter == 6
    assert str(circle_B) == 'Circle BellA has attributes: Radius=3.0 | Diameter=6.0'

def test__radd__geg_circle_failure(circle_01):
    no_obj = True + circle_01
    assert no_obj == None

# __eq__
def test__eq__geg_circle_are_equals(circle_01):
    circle_B = GegCircle(diameter=6, name='B')
    assert circle_01 == circle_B

def test__eq__geg_circle_are_not_equals(circle_01):
    circle_B = GegCircle(diameter=4, name='B')
    assert circle_01 != circle_B

def test__eq__geg_circle_with_other_obj(circle_01):
    assert circle_01 != 'Pippo'

# __lt__
def test__lt__geg_circle(circle_01):
    circle_B = GegCircle(diameter=8, name='B')
    assert circle_01 < circle_B
    assert circle_B > circle_01

def test__lt__geg_circle_with_other_obj(circle_01):
    text = 'Pippo'
    with pytest.raises(TypeError) as lt_exception:
        circle_01 < text
        assert lt_exception == f"operator '<' not supported between instances of 'GegCircle' and '{type(text)}'"