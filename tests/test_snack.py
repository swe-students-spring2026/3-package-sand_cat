import pytest
from sandcat_fun.snack import cat_snack

# --- tests for valid outputs ---

def test_cat_snack_returns_string():
    result = cat_snack("coffee", 1)
    assert isinstance(result, str)

def test_cat_snack_coffee_low():
    result = cat_snack("coffee", 1)
    assert "one coffee" in result.lower() or "Meow" in result
    assert "sand cat" in result

def test_cat_snack_coffee_high():
    result = cat_snack("coffee", 5)
    assert "MROW" in result
    assert "FIVE" in result
    assert "water" in result

def test_cat_snack_tea_moderate():
    result = cat_snack("tea", 2)
    assert "Purrr" in result
    assert "two teas" in result.lower() or "Two" in result

def test_cat_snack_chips_extreme():
    result = cat_snack("chips", 5)
    assert "HISS" in result
    assert "salad" in result

def test_cat_snack_cookies_mid():
    result = cat_snack("cookies", 3)
    assert "Three" in result or "three" in result
    assert "sand cat" in result

def test_cat_snack_water_max():
    result = cat_snack("water", 5)
    assert "PURRR" in result
    assert "biggest fan" in result

def test_cat_snack_normalizes_whitespace_and_case():
    result = cat_snack("  COFFEE  ", 2)
    assert isinstance(result, str)
    assert "Two" in result or "two" in result

# --- tests for invalid inputs ---

def test_cat_snack_invalid_snack_name():
    with pytest.raises(ValueError) as excinfo:
        cat_snack("pizza", 1)
    assert "snack must be one of" in str(excinfo.value)

def test_cat_snack_empty_snack():
    with pytest.raises(ValueError):
        cat_snack("", 1)

def test_cat_snack_whitespace_snack():
    with pytest.raises(ValueError):
        cat_snack("   ", 1)

def test_cat_snack_quantity_too_low():
    with pytest.raises(ValueError):
        cat_snack("coffee", 0)

def test_cat_snack_quantity_too_high():
    with pytest.raises(ValueError):
        cat_snack("coffee", 6)

def test_cat_snack_snack_not_string():
    with pytest.raises(TypeError):
        cat_snack(42, 1)

def test_cat_snack_quantity_not_int():
    with pytest.raises(TypeError):
        cat_snack("coffee", "lots")

def test_cat_snack_quantity_bool_rejected():
    with pytest.raises(TypeError):
        cat_snack("coffee", True)
