import py
import pytest
from core.ex_circle import GegCircle

'''
Test the GegCircle initialization with radius input parameter
'''

@pytest.fixture
def circle_01_f():
    return GegCircle(radius=3.5)

@pytest.fixture
def circle_01_i():
    return GegCircle(radius=3, name='A')


def test_geg_circle_init_float_radius(circle_01_f):
    assert circle_01_f is not None
    assert isinstance(circle_01_f, GegCircle)

def test_geg_circle_properties_float_radius(circle_01_f):
    assert circle_01_f.name == 'C'
    assert circle_01_f.radius == 3.5
    assert circle_01_f.diameter == 7.0

def test_geg_circle_init_int_radius(circle_01_i):
    assert circle_01_i is not None
    assert isinstance(circle_01_i, GegCircle)

def test_geg_circle_properties_int_radius(circle_01_i):
    assert circle_01_i.name == 'A'
    assert circle_01_i.radius == 3.0
    assert circle_01_i.diameter == 6.0

def test_geg_circle_area(circle_01_i):
    area = GegCircle.get_area_with_radius(circle_01_i.radius)
    assert circle_01_i.area == 28.274333882308138
    assert area == 28.274333882308138

# __str__
def test_geg_circle_str(circle_01_f):
    assert str(circle_01_f) == 'Circle C has attributes: Radius=3.5 | Diameter=7.0'

# __add__
def test__add__2_geg_circle(circle_01_i):
    circle_B = GegCircle(radius=1, name='B')
    circle_AB = circle_01_i + circle_B
    assert str(circle_AB) == 'Circle A+B has attributes: Radius=4.0 | Diameter=8.0'

def test__add__geg_circle_with_int_number(circle_01_i):
    circle_B = circle_01_i + 10
    assert circle_B.name == 'A'
    assert circle_B.radius == 13
    assert circle_B.diameter == 26
    assert str(circle_B) == 'Circle A has attributes: Radius=13.0 | Diameter=26.0'

def test__add__geg_circle_with_float_number(circle_01_i):
    circle_B = circle_01_i + 10.5
    assert circle_B.name == 'A'
    assert circle_B.radius == 13.5
    assert circle_B.diameter == 27
    assert str(circle_B) == 'Circle A has attributes: Radius=13.5 | Diameter=27.0'

def test__add__geg_circle_with_chars(circle_01_i):
    circle_B = circle_01_i + 'Pippo'
    assert circle_B.name == 'APippo'
    assert circle_B.radius == 3
    assert circle_B.diameter == 6
    assert str(circle_B) == 'Circle APippo has attributes: Radius=3.0 | Diameter=6.0'

def test__add__geg_circle_failure(circle_01_i):
    no_obj = circle_01_i + True
    assert no_obj == None

# __radd__
def test__radd__geg_circle_with_int_number(circle_01_i):
    circle_B = 10 + circle_01_i
    assert circle_B.name == 'A'
    assert circle_B.radius == 13
    assert circle_B.diameter == 26
    assert str(circle_B) == 'Circle A has attributes: Radius=13.0 | Diameter=26.0'

def test__radd__geg_circle_with_float_number(circle_01_i):
    circle_B = 10.5 + circle_01_i
    assert circle_B.name == 'A'
    assert circle_B.radius == 13.5
    assert circle_B.diameter == 27
    assert str(circle_B) == 'Circle A has attributes: Radius=13.5 | Diameter=27.0'

def test__radd__geg_circle_with_chars(circle_01_i):
    circle_B = 'Bell' + circle_01_i
    assert circle_B.name == 'BellA'
    assert circle_B.radius == 3
    assert circle_B.diameter == 6
    assert str(circle_B) == 'Circle BellA has attributes: Radius=3.0 | Diameter=6.0'

def test__radd__geg_circle_failure(circle_01_i):
    no_obj = True + circle_01_i
    assert no_obj == None

# __eq__
def test__eq__geg_circle_are_equals(circle_01_i):
    circle_B = GegCircle(radius=3, name='B')
    assert circle_01_i == circle_B

def test__eq__geg_circle_are_not_equals(circle_01_i):
    circle_B = GegCircle(radius=4, name='B')
    assert circle_01_i != circle_B

def test__eq__geg_circle_with_other_obj(circle_01_i):
    assert circle_01_i != 'Pippo'

# __lt__
def test__lt__geg_circle(circle_01_i):
    circle_B = GegCircle(radius=4, name='B')
    assert circle_01_i < circle_B
    assert circle_B > circle_01_i

def test__lt__geg_circle_with_other_obj(circle_01_i):
    text = 'Pippo'
    with pytest.raises(TypeError) as lt_exception:
        circle_01_i < text
        assert lt_exception == f"operator '<' not supported between instances of 'GegCircle' and '{type(text)}'"