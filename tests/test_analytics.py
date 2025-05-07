import pytest
from app.services.portefeuille import calcul_score_risque, calcul_note_rentabilite

def test_calcul_score_risque_normal():
    score = calcul_score_risque(solde=-50000, plafond=100000)
    assert 0 <= score <= 1

def test_calcul_score_risque_zero_plafond():
    score = calcul_score_risque(solde=-50000, plafond=0)
    assert score == 1.0

def test_calcul_note_rentabilite_base():
    rentabilite = calcul_note_rentabilite(verse=100000, preleve=50000)
    assert 0 <= rentabilite <= 100

def test_calcul_note_rentabilite_haut():
    rentabilite = calcul_note_rentabilite(verse=1000000, preleve=10000)
    assert abs(rentabilite - 99.0) < 1e-6

def test_calcul_note_rentabilite_zero():
    rentabilite = calcul_note_rentabilite(verse=0, preleve=10000)
    assert rentabilite == 0
