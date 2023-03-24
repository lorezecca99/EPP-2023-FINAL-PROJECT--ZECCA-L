import pytest
from ss_us.analysis.steady_states import SS

def test_SS_labgen_values():
    """Tests that labgen0 and labgen1 are non-negative and less than 1."""
    # Call the SS function and get the labgen0 and labgen1 values
    labgen0, labgen1, _ = SS()
    
    # Check that labgen0 and labgen1 are non-negative
    assert labgen0 >= 0, "labgen0 is negative."
    assert labgen1 >= 0, "labgen1 is negative."
    
    # Check that labgen0 and labgen1 are less than 1
    assert labgen0 < 1, "labgen0 is greater than or equal to 1."
    assert labgen1 < 1, "labgen1 is greater than or equal to 1."