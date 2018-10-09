import pytest
import L2

def test_L2_result():
    assert L2.L2([3, 4], [2, 2]) == 10.0


def test_L2_lengtherror():
    with pytest.raises(ValueError):
        L2.L2([1, 2, 3], [1, 2])