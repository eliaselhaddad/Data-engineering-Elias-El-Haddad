from print_joke import get_random_reaction

def test_get_random_reaction_type():
    reaction = get_random_reaction()
    assert isinstance(reaction, str) # get_random_reaction() returns a string

def test_get_random_reaction_repeats():
    reactions_set = {get_random_reaction() for _ in range(10)}
    assert len(reactions_set) > 1, "get_random_reaction seems to be returning the same reaction multiple times"