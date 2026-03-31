import pytest
from sandcat_fun.tip import cat_tip

# --- tests for valid outputs ---

def test_cat_tip_returns_string():
    result = cat_tip("git", "beginner")
    assert isinstance(result, str)

def test_cat_tip_git_beginner():
    result = cat_tip("git", "beginner")
    assert "commit" in result.lower()
    assert "sand cat" in result

def test_cat_tip_git_intermediate():
    result = cat_tip("git", "intermediate")
    assert "rebase" in result.lower() or "Meow" in result
    assert "sand cat" in result

def test_cat_tip_git_expert():
    result = cat_tip("git", "expert")
    assert "bisect" in result.lower()
    assert "MROW" in result

def test_cat_tip_debugging_beginner():
    result = cat_tip("debugging", "beginner")
    assert "print" in result.lower()
    assert "Purrr" in result

def test_cat_tip_testing_intermediate():
    result = cat_tip("testing", "intermediate")
    assert "edge" in result.lower()
    assert "sand cat" in result

def test_cat_tip_refactoring_expert():
    result = cat_tip("refactoring", "expert")
    assert "test" in result.lower()
    assert "MROW" in result

def test_cat_tip_documentation_beginner():
    result = cat_tip("documentation", "beginner")
    assert "docstring" in result.lower()
    assert "sand cat" in result

def test_cat_tip_normalizes_whitespace_and_case():
    result = cat_tip("  GIT  ", "  BEGINNER  ")
    assert isinstance(result, str)
    assert "commit" in result.lower()

# --- tests for invalid inputs ---

def test_cat_tip_invalid_skill():
    with pytest.raises(ValueError) as excinfo:
        cat_tip("cooking", "beginner")
    assert "skill must be one of" in str(excinfo.value)

def test_cat_tip_invalid_level():
    with pytest.raises(ValueError) as excinfo:
        cat_tip("git", "newbie")
    assert "level must be one of" in str(excinfo.value)

def test_cat_tip_empty_skill():
    with pytest.raises(ValueError):
        cat_tip("", "beginner")

def test_cat_tip_empty_level():
    with pytest.raises(ValueError):
        cat_tip("git", "")

def test_cat_tip_whitespace_skill():
    with pytest.raises(ValueError):
        cat_tip("   ", "beginner")

def test_cat_tip_whitespace_level():
    with pytest.raises(ValueError):
        cat_tip("git", "   ")

def test_cat_tip_skill_not_string():
    with pytest.raises(TypeError):
        cat_tip(123, "beginner")

def test_cat_tip_level_not_string():
    with pytest.raises(TypeError):
        cat_tip("git", False)
