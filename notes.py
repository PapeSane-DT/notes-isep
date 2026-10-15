def moyenne(notes):
    """Moyenne d'une liste de notes."""
    if len(notes) == 0:
        return 0
    return sum(notes) / len(notes)


def mention(note):
    """Mention d'une note sur 20."""
    if note >= 16:
        return "Très bien"
    if note >= 14:
        return "Bien"
    if note >= 12:
        return "Assez bien"
    if note >= 10:
        return "Passable"
    return "Ajourné"