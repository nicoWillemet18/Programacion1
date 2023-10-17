import pytest
from funciones import *

#1

@pytest.mark.parametrize("dni, res",[
   (2222222,True),
   (12,False),
])


def test_dni_valido(dni,res):
   assert dni_valido(dni)==res
#2
@pytest.mark.parametrize("phrase, res",[
   ("hola como estas",5),
   ("chau amigos",6),
])
def test_length_last_word(phrase,res):
   assert length_last_word(phrase)==res

#5

@pytest.mark.parametrize("temp_max, tem_min, res",[
   (20,10,15),

])
def test_calculate_average_temperature(temp_max, tem_min, res):
   assert calculate_average_temperature(temp_max, tem_min)==res

calculate_average_temperature

#6
space_between

@pytest.mark.parametrize("phrase, res",[
   ("hola mateo","h o l a  m a t e o "),

])
def test_space_between(phrase,res):
   assert space_between(phrase)==res

#7
@pytest.mark.parametrize("lista, res",[
   ([1,2,3,4,5],(5,1)),

])
def test_max_min(lista,res):
   assert max_min(lista)==res

#9
@pytest.mark.parametrize("user, password, res",[
   ("123","123",False),

])
def test_login(user, password,res):
   assert login(user, password)==res

#12
@pytest.mark.parametrize("sentence, res",[
   ("hola mundo",{'hola':4,'mundo':5}),

])
def test_words_length_dictionary(sentence, res):
   assert words_length_dictionary(sentence)==res

#14
@pytest.mark.parametrize("number, res",[
   (3,True),

])
def test_is_prime(number, res):
   assert is_prime(number)==res

#15
@pytest.mark.parametrize("n, res",[
   (0,1),

])
def test_factorial(n, res):
   assert factorial(n)==res

#17
@pytest.mark.parametrize("number, res",[
   (11,2),

])
def test_sum_digits(number, res):
   assert sum_digits(number)==res












