from notes import moyenne, mention


def test_moyenne_simple():
    assert moyenne([10, 12, 14]) == 12


def test_moyenne_liste_vide():
    assert moyenne([]) == 0


def test_mention_bien():
    assert mention(14) == "Bien"


def test_mention_ajourne():
    assert mention(8) == "Ajourné"