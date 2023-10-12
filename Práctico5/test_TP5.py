import pytest
from funciones import *

# @pytest.mark.parametrize("a, b, c, res",[
#     ("Nicolas Federico", "Willemet", 42914807, "Nicolas8429"),
#     ("Juan José", "Roca", 26945623, "Juan4269")
# ])
# def test_identifier(a, b, c, res):
#     assert identifier(a,b,c) == res

# @pytest.mark.parametrize("a, b, res",[
#     (4,20, "20 es múltiplo de 4"),
#     (5,20, "20 es múltiplo de 5"),
# ])
# def test_multiplier(a, b, res):
#     assert multiplier(a,b) == res

@pytest.mark.parametrize("a, res",[
    ("Hola buenas tardes", 6),
    ("Mi nombre es Nicolas y tengo 23 años", 4),
])
def test_length_last_word(a, res):
    assert length_last_word(a) == res

@pytest.mark.parametrize("a, res",[
    ("Hola buenas tardes", "H o l a  b u e n a s  t a r d e s"),
    ("Mi nombre es Nicolas y tengo 23 años", "M i  n o m b r e  e s  N i c o l a s  y  t e n g o  2 3  a ñ o s"),
])
def test_space_between(a, res):
    assert space_between(a) == res