import os
import pytest
import math
import random
import json
from unittest.mock import patch

pwd = os.getcwd()
if not os.path.exists('feladat.py'):
    with open('tasks.json', 'r', encoding='utf-8') as json_data:
        lista = json.load(json_data)
    
    random.shuffle(lista)
    text = "'''\n\n\n\n#--------------------------\n'''".join(lista)
    
    with open('feladat.py', 'w',encoding='utf-8') as f:
        f.write("#--------------------------\n'''")
        f.writelines(text)
        f.write("'''\n\n\n\n#======================================================================================================================"+pwd)        

from feladat import *

def test_osszead():
    assert osszead(2, 3) == 5
    assert osszead(-1, 1) == 0
    assert osszead(0, 0) == 0
    assert osszead(2.5, 3.5) == 6

    @patch('builtins.sum')
    def test_sum_not_called(mock_sum):
        osszead(1, 2)
        mock_sum.assert_not_called()

def test_osszead_pont2():
    assert osszead(2, 3) == 5
    assert osszead(-1, 1) == 0
    assert osszead(0, 0) == 0
    assert osszead(2.5, 3.5) == 6

    @patch('builtins.sum')
    def test_sum_not_called(mock_sum):
        osszead(1, 2)
        mock_sum.assert_not_called()

def test_kettovel_oszthato():
    assert kettovel_oszthato(2) == True
    assert kettovel_oszthato(4) == True
    assert kettovel_oszthato(0) == True
    assert kettovel_oszthato(1) == False
    assert kettovel_oszthato(3) == False
    assert kettovel_oszthato(-2) == True

def test_kettovel_oszthato_pont2():
    assert kettovel_oszthato(2) == True
    assert kettovel_oszthato(4) == True
    assert kettovel_oszthato(0) == True
    assert kettovel_oszthato(1) == False
    assert kettovel_oszthato(3) == False
    assert kettovel_oszthato(-2) == True

def test_kor_terulete():
    assert kor_terulete(5) == math.pi * 5 ** 2
    assert kor_terulete(0) == 0
    assert kor_terulete(2.5) == math.pi * 2.5 ** 2

def test_kor_terulete_pont2():
    assert kor_terulete(5) == math.pi * 5 ** 2
    assert kor_terulete(0) == 0
    assert kor_terulete(2.5) == math.pi * 2.5 ** 2

def test_nagyobb():
    assert nagyobb(2, 3) == 3
    assert nagyobb(3, 2) == 3
    assert nagyobb(-1, 1) == 1
    assert nagyobb(1, -1) == 1
    assert nagyobb(0, 0) == 0
    assert nagyobb(2.5, 3.5) == 3.5
    assert nagyobb(3.5, 2.5) == 3.5


    @patch('builtins.max')
    def test_max_not_called(mock_max):
        nagyobb(1, 2)
        mock_max.assert_not_called()

def test_nagyobb_pont2():
    assert nagyobb(2, 3) == 3
    assert nagyobb(3, 2) == 3
    assert nagyobb(-1, 1) == 1
    assert nagyobb(1, -1) == 1
    assert nagyobb(0, 0) == 0
    assert nagyobb(2.5, 3.5) == 3.5
    assert nagyobb(3.5, 2.5) == 3.5


    @patch('builtins.max')
    def test_max_not_called(mock_max):
        nagyobb(1, 2)
        mock_max.assert_not_called()

def test_elso_karakter():
    assert elso_karakter("alma") == "a"
    assert elso_karakter("körte") == "k"
    assert elso_karakter("szilva") == "s"
    assert elso_karakter("") == None  # Ha üres stringet kap

def test_elso_karakter_pont2():
    assert elso_karakter("alma") == "a"
    assert elso_karakter("körte") == "k"
    assert elso_karakter("szilva") == "s"
    assert elso_karakter("") == None  # Ha üres stringet kap

def test_legkisebb():
    with patch('feladat.min', side_effect=Exception("min() is not allowed")) as mock_min:
        assert legkisebb([7, 4, 9, -4, -8, 3]) == -8
        assert legkisebb([1, 2, 3, 4, 5]) == 1
        assert legkisebb([-1, -2, -3, -4, -5]) == -5
        assert legkisebb([0, 0, 0, 0]) == 0
        assert legkisebb([5]) == 5  # Egy elemű lista
        assert legkisebb([]) == None  # Null elemű lista

def test_legkisebb_pont2():
    with patch('feladat.min', side_effect=Exception("min() is not allowed")) as mock_min:
        assert legkisebb([7, 4, 9, -4, -8, 3]) == -8
        assert legkisebb([1, 2, 3, 4, 5]) == 1
        assert legkisebb([-1, -2, -3, -4, -5]) == -5
        assert legkisebb([0, 0, 0, 0]) == 0
        assert legkisebb([5]) == 5  # Egy elemű lista
        assert legkisebb([]) == None  # Null elemű lista

def test_osszeg():
    with patch('feladat.sum', side_effect=Exception("sum() is not allowed")) as mock_sum:
        assert osszeg([1, 2, 3, 4, 5, 6]) == 21
        assert osszeg([1, 2, 3]) == 6
        assert osszeg([-1, -2, -3]) == -6
        assert osszeg([0, 0, 0]) == 0
        assert osszeg([5]) == 5  # Egy elemű lista
        assert osszeg([]) == 0  # Üres lista

def test_osszeg_pont2():
    with patch('feladat.sum', side_effect=Exception("sum() is not allowed")) as mock_sum:
        assert osszeg([1, 2, 3, 4, 5, 6]) == 21
        assert osszeg([1, 2, 3]) == 6
        assert osszeg([-1, -2, -3]) == -6
        assert osszeg([0, 0, 0]) == 0
        assert osszeg([5]) == 5  # Egy elemű lista
        assert osszeg([]) == 0  # Üres lista

def test_negativok_szama():
    assert negativok_szama([-7, -4, 9, -4, -8, 3, 1, 0]) == 4
    assert negativok_szama([-1, -2, -3, -4, -5]) == 5
    assert negativok_szama([1, 2, 3, 4, 5]) == 0
    assert negativok_szama([0, 0, 0]) == 0
    assert negativok_szama([1, -1, 0]) == 1
    assert negativok_szama([]) == 0  # Üres lista

def test_negativok_szama_pont2():
    assert negativok_szama([-7, -4, 9, -4, -8, 3, 1, 0]) == 4
    assert negativok_szama([-1, -2, -3, -4, -5]) == 5
    assert negativok_szama([1, 2, 3, 4, 5]) == 0
    assert negativok_szama([0, 0, 0]) == 0
    assert negativok_szama([1, -1, 0]) == 1
    assert negativok_szama([]) == 0  # Üres lista

def test_lista_atlag():
    assert lista_atlag([1, 2, 3, 4, 5]) == 3.0
    assert lista_atlag([1, 2, 3]) == 2.0
    assert lista_atlag([-1, -2, -3]) == -2.0
    assert lista_atlag([0, 0, 0]) == 0.0
    assert lista_atlag([5]) == 5.0
    assert lista_atlag([]) == 0  # Üres lista

def test_lista_atlag_pont2():
    assert lista_atlag([1, 2, 3, 4, 5]) == 3.0
    assert lista_atlag([1, 2, 3]) == 2.0
    assert lista_atlag([-1, -2, -3]) == -2.0
    assert lista_atlag([0, 0, 0]) == 0.0
    assert lista_atlag([5]) == 5.0
    assert lista_atlag([]) == 0  # Üres lista

def test_paratlanok_kivalogatasa():
    assert paratlanok_kivalogatasa([7, 4, 9, 4, 8, 3, 1, 12, 0]) == [7, 9, 3, 1]
    assert paratlanok_kivalogatasa([2, 4, 6, 8, 10]) == []
    assert paratlanok_kivalogatasa([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
    assert paratlanok_kivalogatasa([-1, 1, 3]) == [-1, 1, 3]
    assert paratlanok_kivalogatasa([]) == []  # Üres lista

def test_paratlanok_kivalogatasa_pont2():
    assert paratlanok_kivalogatasa([7, 4, 9, 4, 8, 3, 1, 12, 0]) == [7, 9, 3, 1]
    assert paratlanok_kivalogatasa([2, 4, 6, 8, 10]) == []
    assert paratlanok_kivalogatasa([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
    assert paratlanok_kivalogatasa([-1, 1, 3]) == [-1, 1, 3]
    assert paratlanok_kivalogatasa([]) == []  # Üres lista

def test_benne_van_a_stringben():
    assert benne_van_a_stringben("abrakadabra", "x") == False
    assert benne_van_a_stringben("abrakadabra", "d") == True
    assert benne_van_a_stringben("alma", "a") == True
    assert benne_van_a_stringben("alma", "b") == False
    assert benne_van_a_stringben("", "a") == False  # Üres string

def test_benne_van_a_stringben_pont2():
    assert benne_van_a_stringben("abrakadabra", "x") == False
    assert benne_van_a_stringben("abrakadabra", "d") == True
    assert benne_van_a_stringben("alma", "a") == True
    assert benne_van_a_stringben("alma", "b") == False
    assert benne_van_a_stringben("", "a") == False  # Üres string

def test_karakterek_szama():
    assert karakterek_szama('lorem.txt') == 18047
    assert karakterek_szama('lorem2.txt') == 37943

def test_karakterek_szama_pont2():
    assert karakterek_szama('lorem.txt') == 18047
    assert karakterek_szama('lorem2.txt') == 37943

def test_sorok_szama():
    assert sorok_szama('lorem.txt') == 82
    assert sorok_szama('lorem2.txt') == 167

def test_sorok_szama_pont2():
    assert sorok_szama('lorem.txt') == 82
    assert sorok_szama('lorem2.txt') == 167

def test_szavak_szama():
    assert szavak_szama('lorem.txt') == 2304
    assert szavak_szama('lorem2.txt') == 5010

def test_szavak_szama_pont2():
    assert szavak_szama('lorem.txt') == 2304
    assert szavak_szama('lorem2.txt') == 5010

def test_teglalap():
    t = Teglalap(3, 4)
    assert t.kerulet() == 14
    assert t.terulet() == 12
    t2 = Teglalap(5, 9)
    assert t2.kerulet() == 28
    assert t2.terulet() == 45

def test_teglalap_pont2():
    t = Teglalap(3, 4)
    assert t.kerulet() == 14
    assert t.terulet() == 12
    t2 = Teglalap(5, 9)
    assert t2.kerulet() == 28
    assert t2.terulet() == 45

def test_string_fajlba():
    string_fajlba("Hello World!", 'test_file.txt')
    with open('test_file.txt', 'r') as f:
        assert f.read() == "Hello World!"
    os.remove('test_file.txt')

def test_string_fajlba_pont2():
    string_fajlba("Hello World!", 'test_file.txt')
    with open('test_file.txt', 'r') as f:
        assert f.read() == "Hello World!"
    os.remove('test_file.txt')

def test_legkisebb_szam_a_fajlban():
    assert legkisebb_szam_a_fajlban('szamok1.txt') == -6  
    assert legkisebb_szam_a_fajlban('szamok2.txt') == -45

def test_legkisebb_szam_a_fajlban_pont2():
    assert legkisebb_szam_a_fajlban('szamok1.txt') == -6  
    assert legkisebb_szam_a_fajlban('szamok2.txt') == -45

def test_harommal_oszthato_szamok_a_fajlban():
    assert harommal_oszthato_szamok_a_fajlban('szamok1.txt') == [3, 3, 0, -6, 0] 
    assert harommal_oszthato_szamok_a_fajlban('szamok2.txt') ==  [3, 3, 0, -6, 0, 12, -45, 66, -3]

def test_harommal_oszthato_szamok_a_fajlban_pont2():
    assert harommal_oszthato_szamok_a_fajlban('szamok1.txt') == [3, 3, 0, -6, 0] 
    assert harommal_oszthato_szamok_a_fajlban('szamok2.txt') ==  [3, 3, 0, -6, 0, 12, -45, 66, -3]

def test_elso_karakter_a_fajlban():
    with open('test_file.txt', 'w') as f:
        f.write("Hello World!")
    assert elso_karakter_a_fajlban('test_file.txt') == "H"
    os.remove('test_file.txt')

def test_elso_karakter_a_fajlban_pont2():
    with open('test_file.txt', 'w') as f:
        f.write("Hello World!")
    assert elso_karakter_a_fajlban('test_file.txt') == "H"
    os.remove('test_file.txt')

def test_kocka():
    k = Kocka(3)
    assert k.terfogat() == 27
    assert k.felszin() == 54
    k2 = Kocka(3)
    assert k2.terfogat() == 27
    assert k2.felszin() == 54

def test_kocka_pont2():
    k = Kocka(3)
    assert k.terfogat() == 27
    assert k.felszin() == 54
    k2 = Kocka(3)
    assert k2.terfogat() == 27
    assert k2.felszin() == 54