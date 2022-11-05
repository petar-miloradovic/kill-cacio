# '#' is for comment line, this line does not affect the code but can be considered as a little 'documentation' in a single line
# != means not equal/disequal
# == exactly equal(used in 'if' structures)
# >= means ≥ (and then <= means ≤)

q = input("do cacio have qualifications?(y/n) >>> ") # y/n
while q != 'y' and q != 'n':
    q = input("try again >>> ")

gs = input("is cacio a good slave?(y/n) >>> ") # y/n
while gs != 'y' and gs != 'n':
    gs = input("try again >>> ")

f = input("is cacio a funny?(y/n) >>> ") # y/n
while f != 'y' and f != 'n':
    f = input("try again >>> ")

b = int(input("how many money do cacio have?(0,n) >>> ")) # 0,n

o = input("which are cacio's origins?(n/s) >>> ") # n/s
while o != 'n' and o != 's':
    o = input("try again >>> ")

w = input("is cacio worth more alive or dead?(y/n) >>> ") # y/n
while w != 'y' and w != 'n':
    w = input("try again >>> ")

if q == 'y' and gs == 'y' and f == 'y' and b >= 69104 and o == 'n' and w == 'y':
    print('cacio is unfortunatelly still alive')
else:
    print('we finally have decapitated cacio')