from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("a", "b")
        encrypt_message(1, 2)
    
    assert encrypt_message("segredo", 3) == "ges_oder"
    assert encrypt_message("segredo", 9) == "oderges"
    assert encrypt_message("segredo", 4) == "ode_rges"
    assert encrypt_message("segredo", 5) == "erges_od"
    assert encrypt_message("segredo", 6) == "o_derges"