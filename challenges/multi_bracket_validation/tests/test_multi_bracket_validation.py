from multi_bracket_validation import __version__


def test_version():
    assert __version__ == '0.1.0'

from multi_bracket_validation.multi_bracket_validation import multi_bracket_validation


def test_multi_bracket_validation1():
    assert multi_bracket_validation("{}")=='True'



def test_multi_bracket_validation2():
    assert multi_bracket_validation("{}(){}")=='True'    


def test_multi_bracket_validation3():
    assert multi_bracket_validation("()[[Extra Characters]]")=='True'        



def test_multi_bracket_validation4():
    assert multi_bracket_validation("(){}[[]]")=='True'            


def test_multi_bracket_validation5():
    assert multi_bracket_validation("{}{Code}[Fellows](())")=='True'                


def test_multi_bracket_validation6():
    assert multi_bracket_validation("[({}]")=='False'                    



def test_multi_bracket_validation7():
    assert multi_bracket_validation("(](")=='False'                        


def test_multi_bracket_validation8():
    assert multi_bracket_validation("{(})")=='False'                        

