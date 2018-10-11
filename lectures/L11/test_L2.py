import pytest
import L2

<<<<<<< HEAD
def test_L2_result():
    assert L2.L2([3, 4], [2, 2]) == 10.0


def test_L2_lengtherror():
    with pytest.raises(ValueError):
        L2.L2([1, 2, 3], [1, 2])
=======
class TestL2:

    def test_L2_result(self):
        assert L2.L2([3.0, 4.0], [1.0, 2.0]) == 8.54400374531753
    
    def test_L2_types(self):
        with pytest.raises(ValueError):
            L2.L2([1.0, -1.0], [1.0, 3.0, 5.0])
    
    def test_L2_noweights(self):
        assert L2.L2([3.0, 4.0]) == 5.0
>>>>>>> cbdd711a503cadd47ce71efd2c3c1327e1ab6f76
