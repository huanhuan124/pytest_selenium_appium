import pytest




def test_raise():
    with pytest.raises(ValueError, match="must be 0 or none"):
        raise ValueError("must be 0 or none")

