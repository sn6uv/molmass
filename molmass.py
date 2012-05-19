#!/usr/bin/python3

import sys
from data import elements

open_brackets = ["(", "[", "{"]
close_brackets= ["}", "]", ")"] 

def calc_mass(instr):
    # Find elements

    atom = {}

    i = 0
    while (i < len(instr)):
        if (ord(instr[i]) >= 65 and ord(instr[i]) <= 90):
            if (i+1 < len(instr) and ord(instr[i+1]) >= 97 
                and ord(instr[i+1]) <= 122):
                el = instr[i:i+1]
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
            print("*", multf)
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
    print(atom)
    return mass

def main():
    

    if (len(sys.argv) != 2):
        print ("Invalid number of arguments")
        exit(1)

    instr = sys.argv[1]

    print("{} : {}g/mol".format(instr, calc_mass(instr)))

    exit(0)

if __name__=="__main__":
    main()

