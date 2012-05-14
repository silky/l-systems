#! /usr/bin/env python
# coding: utf-8

__all__ = ['expand']

import re

def expand(grammar, axiom, times=1):
    """
    Get the l_string of the expanded axiom string N times for the given
    grammar rules
    """
    l_string = []
    for char in axiom:
        if char in grammar:
            l_string.append( grammar[char])
        else:
            l_string.append( char )

    return ''.join( l_string )

if __name__ == "__main__":

    # Input: L-System grammar, axiom and apply times
    # Ouput: Generated L-String (stdout)

    # Command line parameters:
    # Axiom (one string parameter)
    # Rules (zero or more string parameters in the form: .:.*)
    # Times (optional integer > 0 parameter)

    pass
