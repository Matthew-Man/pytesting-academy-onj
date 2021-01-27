from main import capitaliseString

def test_capitaliseString():
    assert capitaliseString("fish") == "FISH"
    assert capitaliseString("flamingo") == "FLAMINGO"
    assert capitaliseString("peacock") == "PEACOCK"
    assert capitaliseString("sloth") == "SLOTH"