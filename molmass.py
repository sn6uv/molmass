#!/usr/bin/python3

import sys
from data import elements

open_brackets = ["(", "[", "{"]
close_brackets= ["}", "]", ")"] 

def calc_mass(instr):
    """Calculates the mass of a molecule from a molecular formula
    >>> calc_mass("H2O")
    {H: 2, O: 1}
    18.0148

    HexaaquaIron(II) 
    >>> calc_mass("Fe(H2O)6")
    {H: 12, O: 6, Fe: 1}
    163.9358

    Tris(ethylenediamine)nickel(II) chloride
    >>> calc_mass("Ni(NH2-CH2-CH2-NH2)3Cl2")
    {H: 24, C: 6, N: 6, Cl: 2, Ni: 1}
    309.9136
    """


    atom = {}
    i = 0

    while (i < len(instr)):
        if (ord(instr[i]) >= 65 and ord(instr[i]) <= 90):
            if (i+1 < len(instr) and ord(instr[i+1]) >= 97 
                and ord(instr[i+1]) <= 122):
                el = instr[i:i+2]
                i+=1
            else:
                el = instr[i]
        else:
            i+=1
            continue

            #print(el)
        if (el not in elements.keys()):
            print("Element {} not found in dict".format(el))
            exit(1)

        # Find how many of this atom
        j = i+1
        while (j < len(instr) and ord(instr[j]) <= 57 
            and ord(instr[j]) >= 48):
            j += 1

        if (i+1 == j):
            nel = 1
        else:
            nel = int(instr[i+1:j])
        i=j-1

        # Check for surrounding brackets
        brac_level = 0 #bracket depth level
        for l in instr[:i]:
            if (l in open_brackets):
                brac_level += 1
            if (l in close_brackets):
                brac_level -= 1

        # Find the multiplication factor
        multf = 1

        # Esape out of the brackets one level at a time
        for b in range(brac_level, 0, -1):
            b_current = b
            for l in range(i, len(instr)):
                if (instr[l] in open_brackets):
                    b_current += 1
                    break

                if instr[l] in close_brackets:
                    b_current -= 1 
                    if (b_current == b-1):
                        k = l+1
                        while (k < len(instr) and ord(instr[k]) <= 57
                            and ord(instr[k]) >= 48):
                            k += 1
    
                        if (k+1 == l):
                            multf *= 1
                        else:
                            multf *= int(instr[l+1:k])
                        l=k-1
                        break
                
        if (el not in atom):
            atom[el] = multf*nel
        else:
            atom[el] += multf*nel
        i+=1

    mass = 0.0
    for i in atom:
        mass += atom[i]*elements[i]

    a=sorted([(k,value) for (k,value) in atom.items()],key=lambda x: elements[x[0]])
    print("{" + ', '.join("{}: {}".format(ke,ve) for (ke,ve) in a) + "}")
    return mass


def main():
    # Check input
    if (len(sys.argv) < 2):
        print ("Invalid number of arguments")
        exit(1)

    instr =  [s for s in sys.argv[1:] if s[0] != '-']

    for s in instr:
        print("{} : {}g/mol".format(s, calc_mass(s)))

    exit(0)

if __name__=="__main__":
    import doctest
    doctest.testmod()
    main()
