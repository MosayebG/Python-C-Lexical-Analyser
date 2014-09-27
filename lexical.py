#!/usr/bin/python
import sys

prz = ['(', ')']
qot = ['[', ']']
spc = [' ']
nc = ['`', '^', '@', '$']
term = ['{', '}', '(', ')', ';', ',', '[', ']', ':', '#']
op = ['+', '-', '*', '/', '=', '%', '>', '<', '&', '~', '!', ]
sq = ['{', '}', '(', ')', ';', ',', ]
sh = ['#']
pnt = ['']
dig = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


let_a = ['a', 'A']

let_c = ['c', 'C']

let_v = ['v', 'V']

let_d = ['d', 'D']

let_l = ['l', 'L']

let_s = ['s', 'S']

let_e = ['e', 'E']

let_f = ['f', 'F']

let_w = ['w', 'W']

let_h = ['h', 'H']

let_i = ['i', 'I']

let_u = ['u', 'U']

let_m = ['m', 'M']

let_t = ['t', 'T']

let_r = ['r', 'R']

let_n = ['n', 'N']

let_o = ['o', 'O']

let = ['.','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x',
       'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
       'U', 'V',
       'W', 'X',
       'Y', 'Z', ]

st_let = [ 'b', 'g', 'h', 'j', 'k', 'l', 'n', 'o', 'p', 'q', 'r', 't', 'u', 'x',
       'y', 'z', 'B', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'T',
       'U',
       'X',
       'Y', 'Z', ]

w_let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x',
       'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
       'U', 'V', 'X',
       'Y', 'Z', ]

c_let = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x',
       'y', 'z', 'A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
       'U', 'V',
       'W', 'X',
       'Y', 'Z', ]

d_let = ['a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x',
       'y', 'z', 'A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
       'U', 'V',
       'W', 'X',
       'Y', 'Z', ]

l_let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x',
       'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
       'U', 'V',
       'W', 'X',
       'Y', 'Z', ]

h_let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x',
       'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
       'U', 'V',
       'W', 'X',
       'Y', 'Z', ]

l_o_let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x',
       'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
       'U', 'V',
       'W', 'X',
       'Y', 'Z', ]

n_f_let = ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x',
       'y', 'z', 'A', 'B', 'C', 'D', 'E', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T',
       'U', 'V',
       'W', 'X',
       'Y', 'Z', ]

r_let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 's', 't', 'u', 'v',
       'w', 'x',
       'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'S', 'T',
       'U', 'V',
       'W', 'X',
       'Y', 'Z', ]

i_let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x',
       'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
       'U', 'V',
       'W', 'X',
       'Y', 'Z', ]

s_t_let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'u', 'v',
       'w', 'x',
       'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
       'U', 'V',
       'W', 'X',
       'Y', 'Z', ]

h_o_a_let = ['b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x',
       'y', 'z', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
       'U', 'V',
       'W', 'X',
       'Y', 'Z', ]

n_let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x',
       'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T',
       'U', 'V',
       'W', 'X',
       'Y', 'Z', ]

a_let = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x',
       'y', 'z', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
       'U', 'V',
       'W', 'X',
       'Y', 'Z', ]

s_let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 't', 'u', 'v',
       'w', 'x',
       'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'T',
       'U', 'V',
       'W', 'X',
       'Y', 'Z', ]

e_let = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x',
       'y', 'z', 'A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
       'U', 'V',
       'W', 'X',
       'Y', 'Z', ]

st_let = ['h', 'j', 'k', 'n', 'o', 'p', 'q',
          'x',
          'y', 'z', 'H', 'J', 'K', 'N', 'O', 'P', 'Q',
          'X',
          'Y', 'Z', ]

u_let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w',
         'x',
         'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         'V', 'W',
         'X',
         'Y', 'Z', ]
t_let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v',
         'w', 'x',
         'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'U',
         'V',
         'W', 'X',
         'Y', 'Z', ]

t_c_let = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v',
         'w', 'x',
         'y', 'z', 'A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'U',
         'V',
         'W', 'X',
         'Y', 'Z', ]

o_let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x',
         'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'V',
         'W', 'X',
         'Y', 'Z', ]

if len(sys.argv) < 2:
    print "Pleae give the C program as argument!!!"
    exit()

filename = sys.argv[1]

data = open(filename).read()

prog = []

for item in data:
    if item == '\n' or item == '\t':
        item = ' '
    prog.append(item)
prog.append(' ')
prog = "".join(prog)

l = len(prog)
i = 0
k = 0
t = 0

while True:
    while i < len(prog):
        j = 0
        t = i
        if prog[i] in spc:
            j += 1
            i += 1
            continue
        elif prog[i] in st_let:
            i += 1

            while i < len(prog):
                if prog[i] in let:
                    i += 1
                    continue
                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                    i += 1
                    print "In Character " + str(i + 1) + " accur an Error!!!"
                    exit()
                    break
                elif prog[i] in dig:
                    i += 1
                    while i < len(prog):
                        if prog[i] in dig:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " Error!!!"
                            exit()
                            break
                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break
                elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                    t += j
                    token = prog[t:i]

                    print str(token) + "   ------------>   " + "ID"
                    break

        elif prog[i] in dig:
            while i < len(prog):
                if prog[i] in dig:
                    i += 1
                    continue
                elif prog[i] in sh or prog[i] in nc or prog[i] in let:
                    i += 1
                    print "In Character " + str(i + 1) + " accur an Error!!!"
                    exit()
                    break
                elif prog[i] in pnt:
                    i += 1
                    if prog[i] in dig:
                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in let:
                                i += 1
                                print "In Character " + str(i + 1) + " Error!!!"
                                exit()
                                break

                            elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "Digit"
                                break
                elif prog[i] in spc or prog[i] in op or prog[i] in term:
                    t += j
                    token = prog[t:i]
                    print str(token) + "        ------->       " + "Digit"
                    break
                break
        elif prog[i] in let_a:
            i += 1
            if prog[i] in u_let:

                while i < len(prog):
                    if prog[i] in let:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                        i += 1
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in dig:
                        i += 1
                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                        t += j
                        token = prog[t: i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in dig:

                while i < len(prog):
                    if prog[i] in dig:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in spc or prog[i] in op or prog[i] in term:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in spc or prog[i] in term:
                t += j
                token = prog[t:i]
                print str(token) + "        ------->       " + "ID"
                break

            elif prog[i] in let_u:
                i += 1
                if prog[i] in t_let:
                    i += 1
                    while i < len(prog):
                        if prog[i] in let:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in dig:
                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                            t += j
                            token = prog[t: i]
                            print str(token) + "        ------->       " + "ID"
                            break

                elif prog[i] in dig:
                    while i < len(prog):
                        if prog[i] in dig:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in spc or prog[i] in op or prog[i] in term:
                            t += j
                            token = prog[t:i]

                            print str(token) + "        ------->       " + "ID"

                            break
                        continue
                elif prog[i] in spc:
                    t += j
                    token = prog[t:i]
                    print str(token) + "        ------->       " + "ID"
                    break
                elif prog[i] in let_t:
                    i += 1
                    if prog[i] in o_let:
                        while i < len(prog):
                            if prog[i] in let:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in dig:
                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        i += 1
                                        print "In Character " + str(i + 1) + " Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                                t += j
                                token = prog[t: i]
                                print str(token) + "        ------->       " + "ID"
                                break

                    elif prog[i] in dig:

                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc \
                                or prog[i] in let or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                            continue
                    elif prog[i] in spc:
                        t += j
                        token = prog[t:i]

                        print str(token) + "        ------->       " + "ID"
                        break
                    elif prog[i] in let_o:
                        i += 1
                        if prog[i] in let:
                            while i < len(prog):
                                if prog[i] in let:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in dig:

                                    while i < len(prog):
                                        if prog[i] in dig:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                            i += 1
                                            print "In Character " + str(i + 1) + " Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                            t += j
                                            token = prog[t:i]
                                            print str(token) + "        ------->       " + "ID"
                                            break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                                    t += j
                                    token = prog[t: i]

                                    print str(token) + "        ------->       " + "ID"
                                    break

                        elif prog[i] in dig:

                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[
                                    i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                            continue
                        elif prog[i] in spc:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "Keyword"
                            break
                        elif prog[i] in sh or prog[i] in nc or prog[i] in op:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break

        elif prog[i] in let_c:
            i += 1
            if prog[i] in h_o_a_let:

                while i < len(prog):
                    if prog[i] in let:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                        i += 1
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in dig:
                        i += 1
                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                        t += j
                        token = prog[t: i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in dig:

                while i < len(prog):
                    if prog[i] in dig:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in spc or prog[i] in op or prog[i] in term:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in spc or prog[i] in term:
                t += j
                token = prog[t:i]
                print str(token) + "        ------->       " + "ID"
                break

            elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break

            elif prog[i] in let_a:
                i += 1
                if prog[i] in s_let:
                    i += 1
                    while i < len(prog):
                        if prog[i] in let:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in dig:
                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                            t += j
                            token = prog[t: i]
                            print str(token) + "        ------->       " + "ID"
                            break

                elif prog[i] in dig:
                    while i < len(prog):
                        if prog[i] in dig:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in spc or prog[i] in op or prog[i] in term:
                            t += j
                            token = prog[t:i]

                            print str(token) + "        ------->       " + "ID"

                            break
                        continue

                elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                    print "In Character " + str(i + 1) + " accur an Error!!!"
                    exit()
                    break

                elif prog[i] in spc or prog[i] in term:
                    t += j
                    token = prog[t:i]
                    print str(token) + "        ------->       " + "ID"
                    break
                elif prog[i] in let_s:
                    i += 1
                    if prog[i] in e_let:
                        while i < len(prog):
                            if prog[i] in let:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in dig:
                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        i += 1
                                        print "In Character " + str(i + 1) + " Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                                t += j
                                token = prog[t: i]
                                print str(token) + "        ------->       " + "ID"
                                break

                    elif prog[i] in dig:

                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc \
                                or prog[i] in let or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                            continue
                    elif prog[i] in spc or prog[i] in term:
                        t += j
                        token = prog[t:i]

                        print str(token) + "        ------->       " + "ID"
                        break

                    elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break

                    elif prog[i] in let_e:
                        i += 1
                        if prog[i] in let:
                            while i < len(prog):
                                if prog[i] in let:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in dig:

                                    while i < len(prog):
                                        if prog[i] in dig:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                            i += 1
                                            print "In Character " + str(i + 1) + " Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                            t += j
                                            token = prog[t:i]
                                            print str(token) + "        ------->       " + "ID"
                                            break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                                    t += j
                                    token = prog[t: i]

                                    print str(token) + "        ------->       " + "ID"
                                    break

                        elif prog[i] in dig:

                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[
                                    i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                            continue
                        elif prog[i] in spc or prog[i] in term :
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "Keyword"
                            break
                        elif prog[i] in sh or prog[i] in nc or prog[i] in op:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
            elif prog[i] in let_o:
                i += 1
                if prog[i] in n_let:

                    while i < len(prog):
                        if prog[i] in let:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                            i += 1
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in dig:
                            i += 1
                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    i += 1
                                    print "In Character " + str(i + 1) + " Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                            t += j
                            token = prog[t: i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in dig:

                    while i < len(prog):
                        if prog[i] in dig:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in spc or prog[i] in op or prog[i] in term:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in spc or prog[i] in term:
                    t += j
                    token = prog[t:i]
                    print str(token) + "        ------->       " + "ID"
                    break

                elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                    print "In Character " + str(i + 1) + " accur an Error!!!"
                    exit()
                    break

                elif prog[i] in let_n:
                    i += 1
                    if prog[i] in s_t_let:

                        while i < len(prog):
                            if prog[i] in let:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in dig:
                                i += 1
                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        i += 1
                                        print "In Character " + str(i + 1) + " Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t: i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        break
                    elif prog[i] in dig:

                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        break
                    elif prog[i] in spc or prog[i] in term:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break

                    elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break

                    elif prog[i] in let_s:
                        i += 1
                        if prog[i] in t_let:

                            while i < len(prog):
                                if prog[i] in let:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    i += 1
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in dig:
                                    i += 1
                                    while i < len(prog):
                                        if prog[i] in dig:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                            i += 1
                                            print "In Character " + str(i + 1) + " Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                            t += j
                                            token = prog[t:i]
                                            print str(token) + "        ------->       " + "ID"
                                            break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t: i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                            break
                        elif prog[i] in dig:

                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                            break
                        elif prog[i] in spc or prog[i] in term:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break

                        elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break

                        elif prog[i] in let_t:
                            i += 1
                            if prog[i] in let:
                                while i < len(prog):
                                    if prog[i] in let:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        print "In Character " + str(i + 1) + " accur an Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in dig:

                                        while i < len(prog):
                                            if prog[i] in dig:
                                                i += 1
                                                continue
                                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                                i += 1
                                                print "In Character " + str(i + 1) + " Error!!!"
                                                exit()
                                                break
                                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                                t += j
                                                token = prog[t:i]
                                                print str(token) + "        ------->       " + "ID"
                                                break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                                        t += j
                                        token = prog[t: i]

                                        print str(token) + "        ------->       " + "ID"
                                        break

                            elif prog[i] in dig:

                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                        print "In Character " + str(i + 1) + " accur an Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                                continue
                            elif prog[i] in spc or prog[i] in term :
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "Keyword"
                                break
                            elif prog[i] in sh or prog[i] in nc or prog[i] in op:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break

                    elif prog[i] in let_t:
                        i += 1
                        if prog[i] in i_let:

                            while i < len(prog):
                                if prog[i] in let:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    i += 1
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in dig:
                                    i += 1
                                    while i < len(prog):
                                        if prog[i] in dig:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                            i += 1
                                            print "In Character " + str(i + 1) + " Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                            t += j
                                            token = prog[t:i]
                                            print str(token) + "        ------->       " + "ID"
                                            break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t: i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                            break
                        elif prog[i] in dig:

                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                            break
                        elif prog[i] in spc or prog[i] in term:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break

                        elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break

                        elif let_i:
                            i += 1
                            if prog[i] in n_let:

                                while i < len(prog):
                                    if prog[i] in let:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        i += 1
                                        print "In Character " + str(i + 1) + " accur an Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in dig:
                                        i += 1
                                        while i < len(prog):
                                            if prog[i] in dig:
                                                i += 1
                                                continue
                                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                                i += 1
                                                print "In Character " + str(i + 1) + " Error!!!"
                                                exit()
                                                break
                                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                                t += j
                                                token = prog[t:i]
                                                print str(token) + "        ------->       " + "ID"
                                                break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                        t += j
                                        token = prog[t: i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                                break
                            elif prog[i] in dig:

                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                        print "In Character " + str(i + 1) + " accur an Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                                break
                            elif prog[i] in spc or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break

                            elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in let_n:
                                i += 1
                                if prog[i] in u_let:

                                    while i < len(prog):
                                        if prog[i] in let:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                            i += 1
                                            print "In Character " + str(i + 1) + " accur an Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in dig:
                                            i += 1
                                            while i < len(prog):
                                                if prog[i] in dig:
                                                    i += 1
                                                    continue
                                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                                    i += 1
                                                    print "In Character " + str(i + 1) + " Error!!!"
                                                    exit()
                                                    break
                                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                                    t += j
                                                    token = prog[t:i]
                                                    print str(token) + "        ------->       " + "ID"
                                                    break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                            t += j
                                            token = prog[t: i]
                                            print str(token) + "        ------->       " + "ID"
                                            break
                                    break
                                elif prog[i] in dig:

                                    while i < len(prog):
                                        if prog[i] in dig:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                            print "In Character " + str(i + 1) + " accur an Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                            t += j
                                            token = prog[t:i]
                                            print str(token) + "        ------->       " + "ID"
                                            break
                                    break
                                elif prog[i] in spc or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break

                                elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break

                                elif prog[i] in let_u:
                                    i += 1
                                    if prog[i] in e_let:

                                        while i < len(prog):
                                            if prog[i] in let:
                                                i += 1
                                                continue
                                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                                i += 1
                                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                                exit()
                                                break
                                            elif prog[i] in dig:
                                                i += 1
                                                while i < len(prog):
                                                    if prog[i] in dig:
                                                        i += 1
                                                        continue
                                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                                        i += 1
                                                        print "In Character " + str(i + 1) + " Error!!!"
                                                        exit()
                                                        break
                                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                                        t += j
                                                        token = prog[t:i]
                                                        print str(token) + "        ------->       " + "ID"
                                                        break
                                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                                t += j
                                                token = prog[t: i]
                                                print str(token) + "        ------->       " + "ID"
                                                break
                                        break
                                    elif prog[i] in dig:

                                        while i < len(prog):
                                            if prog[i] in dig:
                                                i += 1
                                                continue
                                            elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                                exit()
                                                break
                                            elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                                t += j
                                                token = prog[t:i]
                                                print str(token) + "        ------->       " + "ID"
                                                break
                                        break
                                    elif prog[i] in spc or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break

                                    elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                                        print "In Character " + str(i + 1) + " accur an Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in let_e:
                                        i += 1
                                        if prog[i] in let:
                                            while i < len(prog):
                                                if prog[i] in let:
                                                    i += 1
                                                    continue
                                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                                    exit()
                                                    break
                                                elif prog[i] in dig:

                                                    while i < len(prog):
                                                        if prog[i] in dig:
                                                            i += 1
                                                            continue
                                                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                                            i += 1
                                                            print "In Character " + str(i + 1) + " Error!!!"
                                                            exit()
                                                            break
                                                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                                            t += j
                                                            token = prog[t:i]
                                                            print str(token) + "        ------->       " + "ID"
                                                            break
                                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                                                    t += j
                                                    token = prog[t: i]

                                                    print str(token) + "        ------->       " + "ID"
                                                    break

                                        elif prog[i] in dig:

                                            while i < len(prog):
                                                if prog[i] in dig:
                                                    i += 1
                                                    continue
                                                elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                                    exit()
                                                    break
                                                elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                                    t += j
                                                    token = prog[t:i]
                                                    print str(token) + "        ------->       " + "ID"
                                                    break
                                            continue
                                        elif prog[i] in spc or prog[i] in term :
                                            t += j
                                            token = prog[t:i]
                                            print str(token) + "        ------->       " + "Keyword"
                                            break
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in op:
                                            print "In Character " + str(i + 1) + " accur an Error!!!"
                                            exit()
                                            break
            elif prog[i] in let_h:
                i += 1
                if prog[i] in a_let:

                    while i < len(prog):
                        if prog[i] in let:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                            i += 1
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in dig:
                            i += 1
                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    i += 1
                                    print "In Character " + str(i + 1) + " Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                            t += j
                            token = prog[t: i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in dig:

                    while i < len(prog):
                        if prog[i] in dig:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in spc or prog[i] in op or prog[i] in term:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in spc or prog[i] in term:
                    t += j
                    token = prog[t:i]
                    print str(token) + "        ------->       " + "ID"
                    break

                elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                    print "In Character " + str(i + 1) + " accur an Error!!!"
                    exit()
                    break

                elif prog[i] in let_a:
                    i += 1
                    if prog[i] in r_let:

                        while i < len(prog):
                            if prog[i] in let:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in dig:
                                i += 1
                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        i += 1
                                        print "In Character " + str(i + 1) + " Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t: i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        break
                    elif prog[i] in dig:

                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        break
                    elif prog[i] in spc or prog[i] in term:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break

                    elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in let_r:
                        i += 1
                        if prog[i] in let:
                            while i < len(prog):
                                if prog[i] in let:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in dig:

                                    while i < len(prog):
                                        if prog[i] in dig:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                            i += 1
                                            print "In Character " + str(i + 1) + " Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                            t += j
                                            token = prog[t:i]
                                            print str(token) + "        ------->       " + "ID"
                                            break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                                    t += j
                                    token = prog[t: i]

                                    print str(token) + "        ------->       " + "ID"
                                    break

                        elif prog[i] in dig:

                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                            continue
                        elif prog[i] in spc or prog[i] in term :
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "Keyword"
                            break
                        elif prog[i] in sh or prog[i] in nc or prog[i] in op:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()

        elif prog[i] in let_i:
            i += 1
            if prog[i] in n_f_let:

                while i < len(prog):
                    if prog[i] in let:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                        i += 1
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in dig:
                        i += 1
                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                        t += j
                        token = prog[t: i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in dig:

                while i < len(prog):
                    if prog[i] in dig:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in spc or prog[i] in op or prog[i] in term:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in spc or prog[i] in term or prog[i] in op:
                t += j
                token = prog[t:i]
                print str(token) + "        ------->       " + "ID"
                break

            elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break

            elif prog[i] in let_f:
                i += 1
                if prog[i] in let:
                    while i < len(prog):
                        if prog[i] in let:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in dig:

                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    i += 1
                                    print "In Character " + str(i + 1) + " Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                            t += j
                            token = prog[t: i]

                            print str(token) + "        ------->       " + "ID"
                            break

                elif prog[i] in dig:

                    while i < len(prog):
                        if prog[i] in dig:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in spc or prog[i] in op or prog[i] in term:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    continue
                elif prog[i] in spc or prog[i] in term :
                    t += j
                    token = prog[t:i]
                    print str(token) + "        ------->       " + "Keyword"
                    break
                elif prog[i] in sh or prog[i] in nc or prog[i] in op:
                    print "In Character " + str(i + 1) + " accur an Error!!!"
                    exit()
                    break

            elif prog[i] in let_n:
                i += 1
                if prog[i] in t_c_let:

                    while i < len(prog):
                        if prog[i] in let:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                            i += 1
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in dig:
                            i += 1
                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    i += 1
                                    print "In Character " + str(i + 1) + " Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                            t += j
                            token = prog[t: i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in dig:

                    while i < len(prog):
                        if prog[i] in dig:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in spc or prog[i] in op or prog[i] in term:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in spc or prog[i] in term or prog[i] in op:
                    t += j
                    token = prog[t:i]
                    print str(token) + "        ------->       " + "ID"
                    break

                elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                    print "In Character " + str(i + 1) + " accur an Error!!!"
                    exit()
                    break
                elif prog[i] in let_t:
                    i += 1
                    if prog[i] in let:
                        while i < len(prog):
                            if prog[i] in let:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in dig:

                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        i += 1
                                        print "In Character " + str(i + 1) + " Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                                t += j
                                token = prog[t: i]

                                print str(token) + "        ------->       " + "ID"
                                break

                    elif prog[i] in dig:

                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        continue
                    elif prog[i] in spc or prog[i] in term :
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "Keyword"
                        break
                    elif prog[i] in sh or prog[i] in nc or prog[i] in op:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break

                elif prog[i] in let_c:
                    i += 1
                    if prog[i] in l_let:

                        while i < len(prog):
                            if prog[i] in let:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in dig:
                                i += 1
                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        i += 1
                                        print "In Character " + str(i + 1) + " Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t: i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        break
                    elif prog[i] in dig:

                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        break
                    elif prog[i] in spc or prog[i] in term or prog[i] in op:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break

                    elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break

                    elif prog[i] in let_l:
                        i += 1
                        if prog[i] in u_let:

                            while i < len(prog):
                                if prog[i] in let:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    i += 1
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in dig:
                                    i += 1
                                    while i < len(prog):
                                        if prog[i] in dig:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                            i += 1
                                            print "In Character " + str(i + 1) + " Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                            t += j
                                            token = prog[t:i]
                                            print str(token) + "        ------->       " + "ID"
                                            break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t: i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                            break
                        elif prog[i] in dig:

                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                            break
                        elif prog[i] in spc or prog[i] in term or prog[i] in op:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break

                        elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break

                        elif let_u:
                            i += 1
                            if prog[i] in d_let:

                                while i < len(prog):
                                    if prog[i] in let:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        i += 1
                                        print "In Character " + str(i + 1) + " accur an Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in dig:
                                        i += 1
                                        while i < len(prog):
                                            if prog[i] in dig:
                                                i += 1
                                                continue
                                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                                i += 1
                                                print "In Character " + str(i + 1) + " Error!!!"
                                                exit()
                                                break
                                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                                t += j
                                                token = prog[t:i]
                                                print str(token) + "        ------->       " + "ID"
                                                break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                        t += j
                                        token = prog[t: i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                                break
                            elif prog[i] in dig:

                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                        print "In Character " + str(i + 1) + " accur an Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                                break
                            elif prog[i] in spc or prog[i] in term or prog[i] in op:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break

                            elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in let_d:
                                i += 1
                                if prog[i] in e_let:
                                    while i < len(prog):
                                        if prog[i] in let:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                            i += 1
                                            print "In Character " + str(i + 1) + " accur an Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in dig:
                                            i += 1
                                            while i < len(prog):
                                                if prog[i] in dig:
                                                    i += 1
                                                    continue
                                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                                    i += 1
                                                    print "In Character " + str(i + 1) + " Error!!!"
                                                    exit()
                                                    break
                                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                                    t += j
                                                    token = prog[t:i]
                                                    print str(token) + "        ------->       " + "ID"
                                                    break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                            t += j
                                            token = prog[t: i]
                                            print str(token) + "        ------->       " + "ID"
                                            break
                                    break
                                elif prog[i] in dig:
                                    while i < len(prog):
                                        if prog[i] in dig:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                            print "In Character " + str(i + 1) + " accur an Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                            t += j
                                            token = prog[t:i]
                                            print str(token) + "        ------->       " + "ID"
                                            break
                                    break
                                elif prog[i] in spc or prog[i] in term or prog[i] in op:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                                elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in let_e:
                                    i += 1
                                    if prog[i] in let:
                                        while i < len(prog):
                                            if prog[i] in let:
                                                i += 1
                                                continue
                                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                                exit()
                                                break
                                            elif prog[i] in dig:
                                                while i < len(prog):
                                                    if prog[i] in dig:
                                                        i += 1
                                                        continue
                                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                                        i += 1
                                                        print "In Character " + str(i + 1) + " Error!!!"
                                                        exit()
                                                        break
                                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                                        t += j
                                                        token = prog[t:i]
                                                        print str(token) + "        ------->       " + "ID"
                                                        break
                                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                                                t += j
                                                token = prog[t: i]

                                                print str(token) + "        ------->       " + "ID"
                                                break

                                    elif prog[i] in dig:

                                        while i < len(prog):
                                            if prog[i] in dig:
                                                i += 1
                                                continue
                                            elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                                exit()
                                                break
                                            elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                                t += j
                                                token = prog[t:i]
                                                print str(token) + "        ------->       " + "ID"
                                                break
                                        continue
                                    elif prog[i] in spc or prog[i] in term :
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "Keyword"
                                        break
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in op:
                                        print "In Character " + str(i + 1) + " accur an Error!!!"
                                        exit()
                                        break


        elif prog[i] in let_f:
            i += 1
            if prog[i] in l_o_let:

                while i < len(prog):
                    if prog[i] in let:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                        i += 1
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in dig:
                        i += 1
                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                        t += j
                        token = prog[t: i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in dig:

                while i < len(prog):
                    if prog[i] in dig:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in spc or prog[i] in op or prog[i] in term:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in spc or prog[i] in term or prog[i] in op:
                t += j
                token = prog[t:i]
                print str(token) + "        ------->       " + "ID"
                break

            elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break

            elif prog[i] in let_o:
                i += 1
                if prog[i] in r_let:

                    while i < len(prog):
                        if prog[i] in let:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                            i += 1
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in dig:
                            i += 1
                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    i += 1
                                    print "In Character " + str(i + 1) + " Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                            t += j
                            token = prog[t: i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in dig:

                    while i < len(prog):
                        if prog[i] in dig:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in spc or prog[i] in op or prog[i] in term:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in spc or prog[i] in term or prog[i] in op:
                    t += j
                    token = prog[t:i]
                    print str(token) + "        ------->       " + "ID"
                    break

                elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                    print "In Character " + str(i + 1) + " accur an Error!!!"
                    exit()
                    break
                elif prog[i] in let_r:
                    i += 1
                    if prog[i] in let:
                        while i < len(prog):
                            if prog[i] in let:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in dig:

                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        i += 1
                                        print "In Character " + str(i + 1) + " Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                                t += j
                                token = prog[t: i]

                                print str(token) + "        ------->       " + "ID"
                                break

                    elif prog[i] in dig:

                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        continue
                    elif prog[i] in spc or prog[i] in term or prog[i] in op:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "Keyword"
                        break
                    elif prog[i] in sh or prog[i] in nc or prog[i] in op:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
            elif prog[i] in let_l:
                i += 1
                if prog[i] in o_let:

                    while i < len(prog):
                        if prog[i] in let:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                            i += 1
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in dig:
                            i += 1
                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    i += 1
                                    print "In Character " + str(i + 1) + " Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                            t += j
                            token = prog[t: i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in dig:

                    while i < len(prog):
                        if prog[i] in dig:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in spc or prog[i] in op or prog[i] in term:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in spc or prog[i] in term or prog[i] in op:
                    t += j
                    token = prog[t:i]
                    print str(token) + "        ------->       " + "ID"
                    break

                elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                    print "In Character " + str(i + 1) + " accur an Error!!!"
                    exit()
                    break

                elif prog[i] in let_o:
                    i += 1
                    if prog[i] in a_let:

                        while i < len(prog):
                            if prog[i] in let:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in dig:
                                i += 1
                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        i += 1
                                        print "In Character " + str(i + 1) + " Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t: i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        break
                    elif prog[i] in dig:

                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        break
                    elif prog[i] in spc or prog[i] in term or prog[i] in op:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break

                    elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break

                    elif prog[i] in let_a:
                        i += 1
                        if prog[i] in t_let:

                            while i < len(prog):
                                if prog[i] in let:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    i += 1
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in dig:
                                    i += 1
                                    while i < len(prog):
                                        if prog[i] in dig:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                            i += 1
                                            print "In Character " + str(i + 1) + " Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                            t += j
                                            token = prog[t:i]
                                            print str(token) + "        ------->       " + "ID"
                                            break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t: i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                            break
                        elif prog[i] in dig:

                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                            break
                        elif prog[i] in spc or prog[i] in term or prog[i] in op:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break

                        elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break

                        elif prog[i] in let_t:
                            i += 1
                            if prog[i] in let:
                                while i < len(prog):
                                    if prog[i] in let:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        print "In Character " + str(i + 1) + " accur an Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in dig:

                                        while i < len(prog):
                                            if prog[i] in dig:
                                                i += 1
                                                continue
                                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                                i += 1
                                                print "In Character " + str(i + 1) + " Error!!!"
                                                exit()
                                                break
                                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                                t += j
                                                token = prog[t:i]
                                                print str(token) + "        ------->       " + "ID"
                                                break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                                        t += j
                                        token = prog[t: i]

                                        print str(token) + "        ------->       " + "ID"
                                        break

                            elif prog[i] in dig:

                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                        print "In Character " + str(i + 1) + " accur an Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                                continue
                            elif prog[i] in spc or prog[i] in term or prog[i] in op:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "Keyword"
                                break
                            elif prog[i] in sh or prog[i] in nc or prog[i] in op:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break

        elif prog[i] in let_w:
            i += 1
            if prog[i] in h_let:

                while i < len(prog):
                    if prog[i] in let:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                        i += 1
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in dig:
                        i += 1
                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                        t += j
                        token = prog[t: i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in dig:

                while i < len(prog):
                    if prog[i] in dig:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in spc or prog[i] in op or prog[i] in term:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in spc or prog[i] in term or prog[i] in op:
                t += j
                token = prog[t:i]
                print str(token) + "        ------->       " + "ID"
                break

            elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break

            elif prog[i] in let_h:
                i += 1
                if prog[i] in i_let:

                    while i < len(prog):
                        if prog[i] in let:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                            i += 1
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in dig:
                            i += 1
                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    i += 1
                                    print "In Character " + str(i + 1) + " Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                            t += j
                            token = prog[t: i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in dig:

                    while i < len(prog):
                        if prog[i] in dig:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in spc or prog[i] in op or prog[i] in term:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in spc or prog[i] in term or prog[i] in op:
                    t += j
                    token = prog[t:i]
                    print str(token) + "        ------->       " + "ID"
                    break

                elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                    print "In Character " + str(i + 1) + " accur an Error!!!"
                    exit()
                    break

                elif prog[i] in let_i:
                    i += 1
                    if prog[i] in l_let:

                        while i < len(prog):
                            if prog[i] in let:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in dig:
                                i += 1
                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        i += 1
                                        print "In Character " + str(i + 1) + " Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t: i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        break
                    elif prog[i] in dig:

                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        break
                    elif prog[i] in spc or prog[i] in term or prog[i] in op:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break

                    elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break

                    elif prog[i] in let_l:
                        i += 1
                        if prog[i] in e_let:

                            while i < len(prog):
                                if prog[i] in let:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    i += 1
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in dig:
                                    i += 1
                                    while i < len(prog):
                                        if prog[i] in dig:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                            i += 1
                                            print "In Character " + str(i + 1) + " Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                            t += j
                                            token = prog[t:i]
                                            print str(token) + "        ------->       " + "ID"
                                            break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t: i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                            break
                        elif prog[i] in dig:

                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                            break
                        elif prog[i] in spc or prog[i] in term or prog[i] in op:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break

                        elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break

                        elif prog[i] in let_e:
                            i += 1
                            if prog[i] in let:
                                while i < len(prog):
                                    if prog[i] in let:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        print "In Character " + str(i + 1) + " accur an Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in dig:

                                        while i < len(prog):
                                            if prog[i] in dig:
                                                i += 1
                                                continue
                                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                                i += 1
                                                print "In Character " + str(i + 1) + " Error!!!"
                                                exit()
                                                break
                                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                                t += j
                                                token = prog[t:i]
                                                print str(token) + "        ------->       " + "ID"
                                                break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                                        t += j
                                        token = prog[t: i]

                                        print str(token) + "        ------->       " + "ID"
                                        break

                            elif prog[i] in dig:

                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                        print "In Character " + str(i + 1) + " accur an Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                                continue
                            elif prog[i] in spc or prog[i] in term :
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "Keyword"
                                break
                            elif prog[i] in sh or prog[i] in nc or prog[i] in op:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break

        elif prog[i] in let_m:
            i += 1
            if prog[i] in a_let:

                while i < len(prog):
                    if prog[i] in let:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                        i += 1
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in dig:
                        i += 1
                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                        t += j
                        token = prog[t: i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in dig:

                while i < len(prog):
                    if prog[i] in dig:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in spc or prog[i] in op or prog[i] in term:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in spc or prog[i] in term or prog[i] in op:
                t += j
                token = prog[t:i]
                print str(token) + "        ------->       " + "ID"
                break

            elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break

            elif prog[i] in let_a:
                i += 1
                if prog[i] in i_let:

                    while i < len(prog):
                        if prog[i] in let:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                            i += 1
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in dig:
                            i += 1
                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    i += 1
                                    print "In Character " + str(i + 1) + " Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                            t += j
                            token = prog[t: i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in dig:

                    while i < len(prog):
                        if prog[i] in dig:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in spc or prog[i] in op or prog[i] in term:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in spc or prog[i] in term or prog[i] in op:
                    t += j
                    token = prog[t:i]
                    print str(token) + "        ------->       " + "ID"
                    break

                elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                    print "In Character " + str(i + 1) + " accur an Error!!!"
                    exit()
                    break

                elif prog[i] in let_i:
                    i += 1
                    if prog[i] in n_let:

                        while i < len(prog):
                            if prog[i] in let:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in dig:
                                i += 1
                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        i += 1
                                        print "In Character " + str(i + 1) + " Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t: i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        break
                    elif prog[i] in dig:

                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        break
                    elif prog[i] in spc or prog[i] in term or prog[i] in op:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break

                    elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break

                    elif prog[i] in let_n:
                        i += 1
                        if prog[i] in let:
                            while i < len(prog):
                                if prog[i] in let:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in dig:

                                    while i < len(prog):
                                        if prog[i] in dig:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                            i += 1
                                            print "In Character " + str(i + 1) + " Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                            t += j
                                            token = prog[t:i]
                                            print str(token) + "        ------->       " + "ID"
                                            break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                                    t += j
                                    token = prog[t: i]

                                    print str(token) + "        ------->       " + "ID"
                                    break

                        elif prog[i] in dig:

                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                            continue
                        elif prog[i] in spc or prog[i] in term :
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "Keyword"
                            break
                        elif prog[i] in sh or prog[i] in nc or prog[i] in op:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break


        elif prog[i] in let_d:
            i += 1
            if prog[i] in o_let:

                while i < len(prog):
                    if prog[i] in let:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                        i += 1
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in dig:
                        i += 1
                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                        t += j
                        token = prog[t: i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in dig:

                while i < len(prog):
                    if prog[i] in dig:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in spc or prog[i] in op or prog[i] in term:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in spc or prog[i] in term or prog[i] in op:
                t += j
                token = prog[t:i]
                print str(token) + "        ------->       " + "ID"
                break

            elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break

            elif prog[i] in let_o:
                i += 1
                if prog[i] in let:
                    while i < len(prog):
                        if prog[i] in let:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in dig:

                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    i += 1
                                    print "In Character " + str(i + 1) + " Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                            t += j
                            token = prog[t: i]

                            print str(token) + "        ------->       " + "ID"
                            break

                elif prog[i] in dig:

                    while i < len(prog):
                        if prog[i] in dig:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in spc or prog[i] in op or prog[i] in term:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    continue
                elif prog[i] in spc or prog[i] in term :
                    t += j
                    token = prog[t:i]
                    print str(token) + "        ------->       " + "Keyword"
                    break
                elif prog[i] in sh or prog[i] in nc or prog[i] in op:
                    print "In Character " + str(i + 1) + " accur an Error!!!"
                    exit()
                    break

        elif prog[i] in let_e:
            i += 1
            if prog[i] in l_let:

                while i < len(prog):
                    if prog[i] in let:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                        i += 1
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in dig:
                        i += 1
                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                        t += j
                        token = prog[t: i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in dig:

                while i < len(prog):
                    if prog[i] in dig:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in spc or prog[i] in op or prog[i] in term:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in spc or prog[i] in term or prog[i] in op:
                t += j
                token = prog[t:i]
                print str(token) + "        ------->       " + "ID"
                break

            elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break

            elif prog[i] in let_l:
                i += 1
                if prog[i] in s_let:

                    while i < len(prog):
                        if prog[i] in let:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                            i += 1
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in dig:
                            i += 1
                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    i += 1
                                    print "In Character " + str(i + 1) + " Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                            t += j
                            token = prog[t: i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in dig:

                    while i < len(prog):
                        if prog[i] in dig:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in spc or prog[i] in op or prog[i] in term:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in spc or prog[i] in term or prog[i] in op:
                    t += j
                    token = prog[t:i]
                    print str(token) + "        ------->       " + "ID"
                    break

                elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                    print "In Character " + str(i + 1) + " accur an Error!!!"
                    exit()
                    break

                elif prog[i] in let_s:
                    i += 1
                    if prog[i] in e_let:

                        while i < len(prog):
                            if prog[i] in let:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in dig:
                                i += 1
                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        i += 1
                                        print "In Character " + str(i + 1) + " Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t: i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        break
                    elif prog[i] in dig:

                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        break
                    elif prog[i] in spc or prog[i] in term or prog[i] in op:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break

                    elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break

                    elif prog[i] in let_e:
                        i += 1
                        if prog[i] in let:
                            while i < len(prog):
                                if prog[i] in let:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in dig:

                                    while i < len(prog):
                                        if prog[i] in dig:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                            i += 1
                                            print "In Character " + str(i + 1) + " Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                            t += j
                                            token = prog[t:i]
                                            print str(token) + "        ------->       " + "ID"
                                            break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                                    t += j
                                    token = prog[t: i]

                                    print str(token) + "        ------->       " + "ID"
                                    break

                        elif prog[i] in dig:

                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                            continue
                        elif prog[i] in spc or prog[i] in term :
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "Keyword"
                            break
                        elif prog[i] in sh or prog[i] in nc or prog[i] in op:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break

        elif prog[i] in let_v:
            i += 1
            if prog[i] in o_let:

                while i < len(prog):
                    if prog[i] in let:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                        i += 1
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in dig:
                        i += 1
                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                        t += j
                        token = prog[t: i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in dig:

                while i < len(prog):
                    if prog[i] in dig:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in spc or prog[i] in op or prog[i] in term:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in spc or prog[i] in term or prog[i] in op:
                t += j
                token = prog[t:i]
                print str(token) + "        ------->       " + "ID"
                break

            elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break

            elif prog[i] in let_o:
                i += 1
                if prog[i] in i_let:

                    while i < len(prog):
                        if prog[i] in let:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                            i += 1
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in dig:
                            i += 1
                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    i += 1
                                    print "In Character " + str(i + 1) + " Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                            t += j
                            token = prog[t: i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in dig:

                    while i < len(prog):
                        if prog[i] in dig:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in spc or prog[i] in op or prog[i] in term:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in spc or prog[i] in term or prog[i] in op:
                    t += j
                    token = prog[t:i]
                    print str(token) + "        ------->       " + "ID"
                    break

                elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                    print "In Character " + str(i + 1) + " accur an Error!!!"
                    exit()
                    break

                elif prog[i] in let_i:
                    i += 1
                    if prog[i] in d_let:

                        while i < len(prog):
                            if prog[i] in let:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in dig:
                                i += 1
                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        i += 1
                                        print "In Character " + str(i + 1) + " Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t: i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        break
                    elif prog[i] in dig:

                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        break
                    elif prog[i] in spc or prog[i] in term or prog[i] in op:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break

                    elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break

                    elif prog[i] in let_d:
                        i += 1
                        if prog[i] in let:
                            while i < len(prog):
                                if prog[i] in let:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in dig:

                                    while i < len(prog):
                                        if prog[i] in dig:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                            i += 1
                                            print "In Character " + str(i + 1) + " Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                            t += j
                                            token = prog[t:i]
                                            print str(token) + "        ------->       " + "ID"
                                            break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                                    t += j
                                    token = prog[t: i]

                                    print str(token) + "        ------->       " + "ID"
                                    break

                        elif prog[i] in dig:

                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                            continue
                        elif prog[i] in spc or prog[i] in term :
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "Keyword"
                            break
                        elif prog[i] in sh or prog[i] in nc or prog[i] in op:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break

        elif prog[i] in let_s:
            i += 1
            if prog[i] in w_let:

                while i < len(prog):
                    if prog[i] in let:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                        i += 1
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in dig:
                        i += 1
                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                        t += j
                        token = prog[t: i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in dig:

                while i < len(prog):
                    if prog[i] in dig:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in spc or prog[i] in op or prog[i] in term:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in spc or prog[i] in term or prog[i] in op:
                t += j
                token = prog[t:i]
                print str(token) + "        ------->       " + "ID"
                break

            elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break

            elif prog[i] in let_w:
                i += 1
                if prog[i] in i_let:

                    while i < len(prog):
                        if prog[i] in let:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                            i += 1
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in dig:
                            i += 1
                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    i += 1
                                    print "In Character " + str(i + 1) + " Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                            t += j
                            token = prog[t: i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in dig:

                    while i < len(prog):
                        if prog[i] in dig:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in spc or prog[i] in op or prog[i] in term:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in spc or prog[i] in term or prog[i] in op:
                    t += j
                    token = prog[t:i]
                    print str(token) + "        ------->       " + "ID"
                    break

                elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                    print "In Character " + str(i + 1) + " accur an Error!!!"
                    exit()
                    break

                elif prog[i] in let_i:
                    i += 1
                    if prog[i] in t_let:

                        while i < len(prog):
                            if prog[i] in let:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in dig:
                                i += 1
                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        i += 1
                                        print "In Character " + str(i + 1) + " Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t: i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        break
                    elif prog[i] in dig:

                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        break
                    elif prog[i] in spc or prog[i] in term or prog[i] in op:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break

                    elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break

                    elif prog[i] in let_t:
                        i += 1
                        if prog[i] in c_let:

                            while i < len(prog):
                                if prog[i] in let:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    i += 1
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in dig:
                                    i += 1
                                    while i < len(prog):
                                        if prog[i] in dig:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                            i += 1
                                            print "In Character " + str(i + 1) + " Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                            t += j
                                            token = prog[t:i]
                                            print str(token) + "        ------->       " + "ID"
                                            break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t: i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                            break
                        elif prog[i] in dig:

                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                            break
                        elif prog[i] in spc or prog[i] in term or prog[i] in op:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break

                        elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break

                        elif let_c:
                            i += 1
                            if prog[i] in h_let:

                                while i < len(prog):
                                    if prog[i] in let:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        i += 1
                                        print "In Character " + str(i + 1) + " accur an Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in dig:
                                        i += 1
                                        while i < len(prog):
                                            if prog[i] in dig:
                                                i += 1
                                                continue
                                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                                i += 1
                                                print "In Character " + str(i + 1) + " Error!!!"
                                                exit()
                                                break
                                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                                t += j
                                                token = prog[t:i]
                                                print str(token) + "        ------->       " + "ID"
                                                break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                        t += j
                                        token = prog[t: i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                                break
                            elif prog[i] in dig:

                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                        print "In Character " + str(i + 1) + " accur an Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                                break
                            elif prog[i] in spc or prog[i] in term or prog[i] in op:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break

                            elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in let_h:
                                i += 1
                                if prog[i] in let:
                                    while i < len(prog):
                                        if prog[i] in let:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                            print "In Character " + str(i + 1) + " accur an Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in dig:
                                            while i < len(prog):
                                                if prog[i] in dig:
                                                    i += 1
                                                    continue
                                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                                    i += 1
                                                    print "In Character " + str(i + 1) + " Error!!!"
                                                    exit()
                                                    break
                                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                                    t += j
                                                    token = prog[t:i]
                                                    print str(token) + "        ------->       " + "ID"
                                                    break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                                            t += j
                                            token = prog[t: i]
                                            print str(token) + "        ------->       " + "ID"
                                            break

                                elif prog[i] in dig:
                                    while i < len(prog):
                                        if prog[i] in dig:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                            print "In Character " + str(i + 1) + " accur an Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                            t += j
                                            token = prog[t:i]
                                            print str(token) + "        ------->       " + "ID"
                                            break
                                    continue
                                elif prog[i] in spc or prog[i] in term :
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "Keyword"
                                    break
                                elif prog[i] in sh or prog[i] in nc or prog[i] in op:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break

        elif prog[i] in let_i:
            i += 1
            if prog[i] in n_let:

                while i < len(prog):
                    if prog[i] in let:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                        i += 1
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in dig:
                        i += 1
                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                        t += j
                        token = prog[t: i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in dig:

                while i < len(prog):
                    if prog[i] in dig:
                        i += 1
                        continue
                    elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break
                    elif prog[i] in spc or prog[i] in op or prog[i] in term:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break
                break
            elif prog[i] in spc or prog[i] in term or prog[i] in op:
                t += j
                token = prog[t:i]
                print str(token) + "        ------->       " + "ID"
                break

            elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break

            elif prog[i] in let_n:
                i += 1
                if prog[i] in c_let:

                    while i < len(prog):
                        if prog[i] in let:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                            i += 1
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in dig:
                            i += 1
                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    i += 1
                                    print "In Character " + str(i + 1) + " Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                            t += j
                            token = prog[t: i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in dig:

                    while i < len(prog):
                        if prog[i] in dig:
                            i += 1
                            continue
                        elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break
                        elif prog[i] in spc or prog[i] in op or prog[i] in term:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break
                    break
                elif prog[i] in spc or prog[i] in term or prog[i] in op:
                    t += j
                    token = prog[t:i]
                    print str(token) + "        ------->       " + "ID"
                    break

                elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                    print "In Character " + str(i + 1) + " accur an Error!!!"
                    exit()
                    break

                elif prog[i] in let_c:
                    i += 1
                    if prog[i] in l_let:

                        while i < len(prog):
                            if prog[i] in let:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                i += 1
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in dig:
                                i += 1
                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        i += 1
                                        print "In Character " + str(i + 1) + " Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                t += j
                                token = prog[t: i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        break
                    elif prog[i] in dig:

                        while i < len(prog):
                            if prog[i] in dig:
                                i += 1
                                continue
                            elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break
                        break
                    elif prog[i] in spc or prog[i] in term or prog[i] in op:
                        t += j
                        token = prog[t:i]
                        print str(token) + "        ------->       " + "ID"
                        break

                    elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                        print "In Character " + str(i + 1) + " accur an Error!!!"
                        exit()
                        break


                    elif prog[i] in let_l:
                        i += 1
                        if prog[i] in u_let:

                            while i < len(prog):
                                if prog[i] in let:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                    i += 1
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in dig:
                                    i += 1
                                    while i < len(prog):
                                        if prog[i] in dig:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                            i += 1
                                            print "In Character " + str(i + 1) + " Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                            t += j
                                            token = prog[t:i]
                                            print str(token) + "        ------->       " + "ID"
                                            break
                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                    t += j
                                    token = prog[t: i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                            break
                        elif prog[i] in dig:

                            while i < len(prog):
                                if prog[i] in dig:
                                    i += 1
                                    continue
                                elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                            break
                        elif prog[i] in spc or prog[i] in term or prog[i] in op:
                            t += j
                            token = prog[t:i]
                            print str(token) + "        ------->       " + "ID"
                            break

                        elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                            print "In Character " + str(i + 1) + " accur an Error!!!"
                            exit()
                            break

                        elif let_u:
                            i += 1
                            if prog[i] in d_let:

                                while i < len(prog):
                                    if prog[i] in let:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                        i += 1
                                        print "In Character " + str(i + 1) + " accur an Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in dig:
                                        i += 1
                                        while i < len(prog):
                                            if prog[i] in dig:
                                                i += 1
                                                continue
                                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                                i += 1
                                                print "In Character " + str(i + 1) + " Error!!!"
                                                exit()
                                                break
                                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                                t += j
                                                token = prog[t:i]
                                                print str(token) + "        ------->       " + "ID"
                                                break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                        t += j
                                        token = prog[t: i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                                break
                            elif prog[i] in dig:

                                while i < len(prog):
                                    if prog[i] in dig:
                                        i += 1
                                        continue
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                        print "In Character " + str(i + 1) + " accur an Error!!!"
                                        exit()
                                        break
                                    elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "ID"
                                        break
                                break
                            elif prog[i] in spc or prog[i] in term or prog[i] in op:
                                t += j
                                token = prog[t:i]
                                print str(token) + "        ------->       " + "ID"
                                break

                            elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                exit()
                                break
                            elif prog[i] in let_d:
                                i += 1
                                if prog[i] in e_let:
                                    while i < len(prog):
                                        if prog[i] in let:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                            i += 1
                                            print "In Character " + str(i + 1) + " accur an Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in dig:
                                            i += 1
                                            while i < len(prog):
                                                if prog[i] in dig:
                                                    i += 1
                                                    continue
                                                elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                                    i += 1
                                                    print "In Character " + str(i + 1) + " Error!!!"
                                                    exit()
                                                    break
                                                elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                                    t += j
                                                    token = prog[t:i]
                                                    print str(token) + "        ------->       " + "ID"
                                                    break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                            t += j
                                            token = prog[t: i]
                                            print str(token) + "        ------->       " + "ID"
                                            break
                                    break
                                elif prog[i] in dig:
                                    while i < len(prog):
                                        if prog[i] in dig:
                                            i += 1
                                            continue
                                        elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                            print "In Character " + str(i + 1) + " accur an Error!!!"
                                            exit()
                                            break
                                        elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                            t += j
                                            token = prog[t:i]
                                            print str(token) + "        ------->       " + "ID"
                                            break
                                    break
                                elif prog[i] in spc or prog[i] in term or prog[i] in op:
                                    t += j
                                    token = prog[t:i]
                                    print str(token) + "        ------->       " + "ID"
                                    break
                                elif prog[i] in nc or prog[i] in sh or prog[i] in pnt:
                                    print "In Character " + str(i + 1) + " accur an Error!!!"
                                    exit()
                                    break
                                elif prog[i] in let_e:
                                    i += 1
                                    if prog[i] in let:
                                        while i < len(prog):
                                            if prog[i] in let:
                                                i += 1
                                                continue
                                            elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                                exit()
                                                break
                                            elif prog[i] in dig:
                                                while i < len(prog):
                                                    if prog[i] in dig:
                                                        i += 1
                                                        continue
                                                    elif prog[i] in sh or prog[i] in nc or prog[i] in pnt:
                                                        i += 1
                                                        print "In Character " + str(i + 1) + " Error!!!"
                                                        exit()
                                                        break
                                                    elif prog[i] in spc or prog[i] in op or prog[i] in qot or l == i + 1 or prog[i] in term:
                                                        t += j
                                                        token = prog[t:i]
                                                        print str(token) + "        ------->       " + "ID"
                                                        break
                                            elif prog[i] in spc or prog[i] in op or prog[i] in qot or prog[i] in term:
                                                t += j
                                                token = prog[t: i]

                                                print str(token) + "        ------->       " + "ID"
                                                break

                                    elif prog[i] in dig:

                                        while i < len(prog):
                                            if prog[i] in dig:
                                                i += 1
                                                continue
                                            elif prog[i] in sh or prog[i] in nc or prog[i] in let or prog[i] in pnt:
                                                print "In Character " + str(i + 1) + " accur an Error!!!"
                                                exit()
                                                break
                                            elif prog[i] in spc or prog[i] in op or prog[i] in term:
                                                t += j
                                                token = prog[t:i]
                                                print str(token) + "        ------->       " + "ID"
                                                break
                                        continue
                                    elif prog[i] in spc or prog[i] in term :
                                        t += j
                                        token = prog[t:i]
                                        print str(token) + "        ------->       " + "Keyword"
                                        break
                                    elif prog[i] in sh or prog[i] in nc or prog[i] in op:
                                        print "In Character " + str(i + 1) + " accur an Error!!!"
                                        exit()
                                        break

        elif '+' == prog[i]:
            i += 1
            if prog[i] == '=':
                t += j
                i += 1
                token = prog[t:i]
                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] == '+':
                t += j
                i += 1
                token = prog[t:i]
                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] in spc or prog[i] in dig or prog[i] in let or prog[i] in prz:
                t += j
                token = prog[t:i]

                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] in nc or prog[i] in pnt:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break

        elif '<' == prog[i]:
            i += 1
            if prog[i] == '=':
                t += j
                i += 1
                token = prog[t:i]
                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] == '<':
                t += j
                i += 1
                token = prog[t:i]
                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] in spc or prog[i] in dig or prog[i] in let or prog[i] in prz:
                t += j
                token = prog[t:i]

                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] in nc or prog[i] in pnt:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break

        elif '=' == prog[i]:
            i += 1
            if prog[i] == '=':
                t += j
                i += 1
                token = prog[t:i]
                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] in spc or prog[i] in dig or prog[i] in let or prog[i] in prz:
                t += j
                token = prog[t:i]

                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] in nc or prog[i] in pnt:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break

        elif '-' == prog[i]:
            i += 1
            if prog[i] == '=':
                t += j
                i += 1
                token = prog[t:i]
                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] == '-':
                t += j
                i += 1
                token = prog[t:i]
                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] in spc or prog[i] in dig or prog[i] in let or prog[i] in prz:
                t += j
                token = prog[t:i]

                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] in nc or prog[i] in pnt:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break

        elif '*' == prog[i]:
            i += 1
            if prog[i] == '=':
                t += j
                i += 1
                token = prog[t:i]
                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] in spc or prog[i] in dig or prog[i] in let or prog[i] in prz:
                t += j
                token = prog[t:i]

                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] in nc or prog[i] in pnt:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break

        elif '!' == prog[i]:
            i += 1
            if prog[i] == '=':
                t += j
                i += 1
                token = prog[t:i]
                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] in spc or prog[i] in dig or prog[i] in let or prog[i] in prz:
                t += j
                token = prog[t:i]

                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] in nc or prog[i] in pnt:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break

        elif '%' == prog[i]:
            i += 1
            if prog[i] == '=':
                t += j
                i += 1
                token = prog[t:i]
                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] in spc or prog[i] in dig or prog[i] in let or prog[i] in prz:
                t += j
                token = prog[t:i]

                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] in nc or prog[i] in pnt:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break

        elif '~' == prog[i]:
            i += 1
            if prog[i] in spc or prog[i] in dig or prog[i] in let or prog[i] in prz:
                t += j
                token = prog[t:i]

                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] in nc or prog[i] in pnt:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break
        elif '>' == prog[i]:
            i += 1
            if prog[i] == '=':
                t += j
                i += 1
                token = prog[t:i]
                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] == '>':
                t += j
                i += 1
                token = prog[t:i]
                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] in spc or prog[i] in dig or prog[i] in let or prog[i] in prz:
                t += j
                token = prog[t:i]

                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] in nc or prog[i] in pnt:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break

        elif '/' == prog[i]:
            i += 1
            if prog[i] == '=':
                t += j
                i += 1
                token = prog[t:i]
                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] in spc or prog[i] in dig or prog[i] in let or prog[i] in prz:
                t += j
                token = prog[t:i]

                print str(token) + "        ------->       " + "OP"
                break
            elif prog[i] in nc or prog[i] in pnt:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break
            elif prog[i] == '*':
                i += 1
                while i < len(prog):
                        if prog[i] != '*':
                            i += 1
                            continue
                        elif prog[i] == '*':
                                i += 1
                                if prog[i] == '/':
                                    break
                                else:
                                    i += 1
                                    continue

        elif prog[i] in term:
            i += 1
            if prog[i] in spc or prog[i] in dig or prog[i] in let or prog[i] in op or prog[i] in term:
                t += j
                token = prog[t:i]
                print str(token) + "        ------->       " + "Term"
                break
            elif prog[i] in nc or prog[i] in pnt or prog[i] in sh:
                print "In Character " + str(i + 1) + " accur an Error!!!"
                exit()
                break
