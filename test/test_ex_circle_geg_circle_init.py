import pytest
from core.ex_circle import GegCircle

'''
Test general behaviour of GegCircle class and its methods, in particular here
 are validated the custom constructor methods of the class
'''

# init GegCircle with wrong parameters
def test_geg_circle_init_without_r_d():
    with pytest.raises(ValueError) as init_exception:
        circle = GegCircle()
        assert circle == None
        assert init_exception == 'Missing arguments'

def test_geg_circle_init_with_wrong_input_radius_value():
    with pytest.raises(ValueError) as init_exception:
        r = 5
        d = 7
        circle = GegCircle(radius=r, diameter=d, name='pippo')
        assert circle == None
        assert init_exception == f'Init values r:\'{r}\' and d:\'{d}\' are incompatible'

def test_geg_circle_init_with_wrong_input_radius_value():
    with pytest.raises(ValueError) as init_exception:
        circle = GegCircle(radius='pippo', diameter=6, name=4)
        assert circle == None
        assert init_exception == 'One or more init arguments are not numeric'

def test_geg_circle_init_with_wrong_input_diameter_value():
    with pytest.raises(ValueError) as init_exception:
        circle = GegCircle(radius=3, diameter='pippo', name=4)
        assert circle == None
        assert init_exception == 'One or more init arguments are not numeric'


# init GegCircle with radius class method
def test_cls_method_geg_circle_from_int_radius():
    circle = GegCircle.from_radius(radius=3)
    assert circle.name == 'C'
    assert circle.radius == 3
    assert circle.diameter == 6
    assert str(circle) == 'Circle C has attributes: Radius=3.0 | Diameter=6.0'

def test_cls_method_geg_circle_from_negative_int_radius():
    with pytest.raises(ValueError) as init_exc:
        circle = GegCircle.from_radius(radius=-3)
        assert circle == None
        assert init_exc == 'Init arguments must be positive numbers'
    
def test_cls_method_geg_circle_from_intstr_radius():
    circle = GegCircle.from_radius(radius='3')
    assert circle.name == 'C'
    assert circle.radius == 3
    assert circle.diameter == 6
    assert str(circle) == 'Circle C has attributes: Radius=3.0 | Diameter=6.0'

def test_cls_method_geg_circle_from_negative_intstr_radius():
    with pytest.raises(ValueError) as init_exc:
        circle = GegCircle.from_radius(radius='-3')
        assert circle == None
        assert init_exc == 'Init arguments must be positive numbers'

def test_cls_method_geg_circle_from_invalid_radius():
    with pytest.raises(ValueError) as init_exception:
        circle = GegCircle.from_radius(radius='a3')
        assert circle == None
        assert init_exception == 'One or more init arguments are not numeric'

def test_cls_method_geg_circle_from_float_radius():
    circle = GegCircle.from_radius(radius=3.0)
    assert circle.name == 'C'
    assert circle.radius == 3.0
    assert circle.diameter == 6.0
    assert str(circle) == 'Circle C has attributes: Radius=3.0 | Diameter=6.0'

def test_cls_method_geg_circle_from_float_radius():
    circle = GegCircle.from_radius(radius=3.0, name='A')
    assert circle.name == 'A'
    assert circle.radius == 3.0
    assert circle.diameter == 6.0
    assert str(circle) == 'Circle A has attributes: Radius=3.0 | Diameter=6.0'

# init GegCircle with diameter
def test_cls_method_geg_circle_from_int_diameter():
    circle = GegCircle.from_diameter(diameter=6)
    assert circle.name == 'C'
    assert circle.radius == 3
    assert circle.diameter == 6
    assert str(circle) == 'Circle C has attributes: Radius=3.0 | Diameter=6.0'

def test_cls_method_geg_circle_from_negative_int_diameter():
    with pytest.raises(ValueError) as init_exc:
        circle = GegCircle.from_diameter(diameter=-6)
        assert circle == None
        assert init_exc == 'Init arguments must be positive numbers'

def test_cls_method_geg_circle_from_intstr_diameter():
    circle = GegCircle.from_diameter(diameter='6')
    assert circle.name == 'C'
    assert circle.radius == 3
    assert circle.diameter == 6
    assert str(circle) == 'Circle C has attributes: Radius=3.0 | Diameter=6.0'

def test_cls_method_geg_circle_from_negative_intstr_diameter():
    with pytest.raises(ValueError) as init_exc:
        circle = GegCircle.from_diameter(diameter='-6')
        assert circle == None
        assert init_exc == 'Init arguments must be positive numbers'

def test_cls_method_geg_circle_from_invalid_diameter():
    with pytest.raises(ValueError) as init_exception:
        circle = GegCircle.from_diameter(diameter='a6')
        assert circle == None
        assert init_exception == 'One or more init arguments are not numeric'
        
def test_cls_method_geg_circle_from_float_diameter():
    circle = GegCircle.from_diameter(diameter=6.0)
    assert circle.name == 'C'
    assert circle.radius == 3.0
    assert circle.diameter == 6.0
    assert str(circle) == 'Circle C has attributes: Radius=3.0 | Diameter=6.0'

# 
def test_add_circle_in_list():
    c_01 = GegCircle(radius=3, name='C.1')
    c_02 = GegCircle(diameter=8, name='C.2')
    c_list = [c_01, c_02]
    assert len(c_list) == 2
    assert c_list[0] == c_01
    assert c_list[1] == c_02