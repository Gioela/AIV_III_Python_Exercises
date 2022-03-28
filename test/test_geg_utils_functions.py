from matplotlib.pyplot import text
import pytest
from utils.geg_utils import GegUtils

'''
Test the GegUtils class methods
'''

def test_str_geg_utils_class():
    utils = GegUtils()
    assert str(utils) == 'GegUtils is an utility class with static methods'

# is_numeric
def test_utils_int_is_numeric():
    assert GegUtils.is_numeric(1) == True

def test_utils_intstring_is_numeric():
    assert GegUtils.is_numeric('1') == True

def test_utils_negative_int_is_numeric():
    assert GegUtils.is_numeric(-1) == True

def test_utils_negative_intstring_is_numeric():
    assert GegUtils.is_numeric('-1') == True

def test_utils_float_is_numeric():
    assert GegUtils.is_numeric(1.5) == True

def test_utils_floatstring_is_numeric():
    assert GegUtils.is_numeric('1.5') == True

def test_utils_negative_float_is_numeric():
    assert GegUtils.is_numeric(-1.0) == True

def test_utils_negative_floatstring_is_numeric():
    assert GegUtils.is_numeric('-1.4') == True

# is_numeric with char
def test_utils_intstring_and_1_lower_char_is_numeric():
    assert GegUtils.is_numeric('1a') == False

def test_utils_intstring_and_1_upper_char_is_numeric():
    assert GegUtils.is_numeric('1A') == False

def test_utils_floatstring_and_1_lower_char_is_numeric():
    assert GegUtils.is_numeric('1.4a') == False

def test_utils_floatstring_and_1_upper_char_is_numeric():
    assert GegUtils.is_numeric('1.3A') == False

def test_utils_1_lower_char_and_floatstring_is_numeric():
    assert GegUtils.is_numeric('a1.4') == False

# is_alpha_value
def test_utils_1_lower_char_is_alpha():
    assert GegUtils.is_alpha_value('a') == True

def test_utils_1_upper_char_is_alpha():
    assert GegUtils.is_alpha_value('A') == True

def test_utils_more_lower_chars_are_alpha():
    assert GegUtils.is_alpha_value('appia') == True

def test_utils_more_upper_chars_are_alpha():
    assert GegUtils.is_alpha_value('APPIA') == True

def test_utils_1_lower_char_and_1_number_are_alpha():
    assert GegUtils.is_alpha_value('a1') == False

def test_utils_1_upper_char_and_1_number_are_alpha():
    assert GegUtils.is_alpha_value('A1') == False

# is_float_value
def test_utils_is_float_value_with_float_positive_number():
    assert GegUtils.is_float_value(3.5) == True

def test_utils_is_float_value_with_float_negative_number():
    assert GegUtils.is_float_value(-3.5) == True

def test_utils_is_float_value_with_floatstring_number():
    assert GegUtils.is_float_value('3.5') == True

def test_utils_is_float_value_with_int_number():
    assert GegUtils.is_float_value(3) == True

def test_utils_is_float_value_with_string_value():
    with pytest.raises(ValueError) as e:
        text = 'casa'
        GegUtils.is_float_value(text)
        assert e == f"could not convert {type(text)} to float: {text}"

# is_int_value
def test_utils_is_int_value_with_float_positive_number():
    assert GegUtils.is_int_value(3) == True

def test_utils_is_int_value_with_int_negative_number():
    assert GegUtils.is_int_value(-3) == True

def test_utils_is_int_valuewith_floatstring_number():
    with pytest.raises(ValueError) as e:
        value = '3.5'
        assert GegUtils.is_int_value(value) == False
        assert e == f"could not convert {type(value)} to int: {value}"

def test_utils_is_int_valuewith_float_number():
    assert GegUtils.is_int_value(3.5) == True

def test_utilsis_int_valuewith_string_value():
    with pytest.raises(ValueError) as e:
        text = 'casa'
        assert GegUtils.is_int_value(text) == False
        assert e == f"could not convert {type(text)} to int: {text}"

# is_value_type
def test_utils_is_value_type_string():
    assert GegUtils.is_value_type('text', str) == True

def test_utils_is_value_type_bool():
    assert GegUtils.is_value_type(True, bool) == True

def test_utils_is_value_type_int():
    assert GegUtils.is_value_type(3, int) == True

def test_utils_is_value_type_float():
    assert GegUtils.is_value_type(3.7, float) == True

def test_utils_is_value_type_intstring_with_string():
    assert GegUtils.is_value_type('7ga', str) == True

def test_utils_is_value_type_intstring_with_int():
    with pytest.raises(ValueError) as e:
        text = 'ga7'
        type_to_validate = int
        GegUtils.is_value_type(text, type_to_validate)
        assert e == f"could not convert {type(text)} to {type_to_validate}. Value: {text}"

def test_utils_is_value_type_boolstring_with_bool():
    text = 'True'
    type_to_validate = bool
    assert GegUtils.is_value_type(text, type_to_validate) == True

def test_utils_is_value_type_bool_with_string():
    with pytest.raises(AssertionError) as e:
        text = True
        type_to_validate = str
        GegUtils.is_value_type(text, type_to_validate)
        assert e == f"could not convert {type(text)} to {type_to_validate}. Value: {text}"

def test_utils_is_value_type_boolstring_with_string():
    with pytest.raises(AssertionError) as e:
        text = 'True'
        type_to_validate = str
        GegUtils.is_value_type(text, type_to_validate)
        assert e == f"could not convert {type(text)} to {type_to_validate}. Value: {text}"