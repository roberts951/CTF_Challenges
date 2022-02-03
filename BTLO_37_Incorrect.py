coord=-0.841600711036728
import re
the_prime=0
import itertools
from geopy.geocoders import Nominatim

#############   DIVIDE BY 2ND PRIME NUMBER   #################
def divide_second_prime():
    print("Executing Function 1")
    prime_function_list = []
    global coord

    for char in str(coord):
        if re.search('[2-9]',char):
            prime = True
            for i in range(2,int(char)):
                if (int(char) % i) == 0:
                    prime = False
            if prime:
                prime_function_list.append(char)
    the_prime = int(prime_function_list[1])
#    print("Diving coord",coord,"with prime #",the_prime,"...")
    coord=coord/the_prime
#    print(coord)
###############################################################

#############   SUBTRACT PI   #################################
def subtract_pi():
    print("Executing Function 2")
    global coord
    coord=coord-3.14
###############################################################

############# DIVIDE BY MULTIPLE ##############################
def multiple():
    print("Executing Function 3")
    global coord
    multiple_list = []
    m=1
    multiple = 0

    for char2 in str(coord):
        if re.search('[1-9]',char2):
            multiple_list.append(char2)

    while m < 5:
#        print(multiple_list[m])
        if multiple_list[m] == 0:
            m += 1
            break
        if multiple == 0:
            multiple = int(multiple_list[m])
            m += 1
        else:
            multiple = multiple * int(multiple_list[m])
            m += 1

    coord = coord * multiple
#########################

############## FIBONACCI 6th VALUE #############################
def fibo(): 
    print("Executing Function 4")
    global coord
    n2 = coord
    n1 = 0
    f = 0

    while f<6:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        f += 1
#        print("Coord Fibonacci sequence #",f,"=",nth)

    coord = coord + 5

################################################################

def_list = [divide_second_prime,subtract_pi,multiple,fibo]
print(coord)
coord=-0.841600711036728
st1 = 0
st2 = 0
st3 = 0
st4 = 0
calc_coords = []

for t1 in def_list:
    coord=-0.841600711036728
    t1()
    st1 == coord
    print("Applied from t1")

    for t2 in def_list:
        print("Checking t2")
        coord == st1
        if t1 == t2:
            continue
        t2()
        print("Applied from t2")
        st2 == coord

        for t3 in def_list:
            coord == st2
            print("Checking t3")
            if t3 in [t1,t2]:
                continue
            t3()
            st3 == coord
            print("Applied from t3")

            for t4 in def_list:
                coord == st3
                print("Checking t4")
                if t4 in [t1,t2,t3]:
                    continue
                t4()
                print("Applied from t4")


                print(coord)
                if -0 > coord > -90:
                    calc_coords.append(coord)
                coord=-0.841600711036728

print(calc_coords)
geolocator = Nominatim(user_agent="robdogapp")
locat2 = ", -73.99116596577247"

for cords_i in calc_coords:
    f = open("coordz.txt", "a")
    f.write(str(cords_i))
    f.close()

for locat in calc_coords:
#    locat3 = locat * -1
    full_locat = str(locat) + locat2
    location = geolocator.reverse(full_locat)
    if location is None:
        continue
    f = open("coordz2.txt", "a")
    f.write(str(location.address)+","+full_locat+"\n")
    f.close()
    print(location.address)
    print(full_locat)
