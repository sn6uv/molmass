MOLMASS
=======

The MOLMASS program is a simple python script for calculating molecular masses.
Rather than tediously calculating the mass of endless compounds just use this
one script. 

Usage
-----
    >$ ./molmass.py molecular_formula

    >$ ./molmass.py H2O
    {H: 2, O: 1}
    H2O : 18.0148g/mol

Note: you may need to surround the molecular formula in quotes to avoid your
shell misintepreting brackets

    >$ ./molmass.py Ni(NH2-CH2-CH2-NH2)3Cl2
    -bash: syntax error near unexpected token `('

    >$ ./molmass.py "Ni(NH2-CH2-CH2-NH2)3Cl2"
    {H: 24, C: 6, N: 6, Cl: 2, Ni: 1}
    Ni(NH2-CH2-CH2-NH2)3Cl2 : 309.9136g/mol

Advanced Features
-----------------
MOLMASS handles a variety of brackets including round () curly {} and square []
brackets however all brackets are treated equally. 

    >$ ./molmass.py "Fe{H2O)"
    {H: 12, O: 6, Fe: 1}
    Fe{H2O) : 163.9358g/mol

MOLMASS ignores all non alphanumeric-bracket charachters 
