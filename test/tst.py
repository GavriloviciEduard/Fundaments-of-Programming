import domain.o_array
import ui.in_out_functions


def test_add():

    assert domain.o_array.add([],2)==[2]
    assert domain.o_array.add([2],3)==[2,3]
    assert domain.o_array.add([2,3],11)==[2,3,11]
    assert domain.o_array.add([2,3,11],999)==[2,3,11,999]
    assert domain.o_array.add([2,3,11,999],25)==[2,3,11,999,25]

def test_ins():

    assert domain.o_array.ins([],2,23)==[2]
    assert domain.o_array.ins([2],9,0)==[9,2]
    assert domain.o_array.ins([9,2],99,1)==[9,99,2]
    assert domain.o_array.ins([9,99,2],101,3)==[9,99,2,101]
    assert domain.o_array.ins([9,99,2,101],8,1)==[9,8,99,2,101]

def test_remove():

    assert domain.o_array.remove([],2)==0
    assert domain.o_array.remove([2],0)==[]
    assert domain.o_array.remove([2],999)==[]
    assert domain.o_array.remove([2,7,8,9,10],2)==[2,7,9,10]
    assert domain.o_array.remove([2,7,8,9,10],111)==[2,7,8,9]
    assert domain.o_array.remove([2,7,8,9,10],4)==[2,7,8,9]

def test_remove_bt():

    assert domain.o_array.remove_bt([],2,2)==0
    assert domain.o_array.remove_bt([1],2,2)==0
    assert domain.o_array.remove_bt([2,1],0,1)==[]
    assert domain.o_array.remove_bt([2,3,4,5,6],3,4)==[2,3,4]
    assert domain.o_array.remove_bt([2,3,4,5,6],4,3)==[2,3,4]
    assert domain.o_array.remove_bt([2,3,4,5,6],3,99)==[2,3,4]

def test_replace():

    assert domain.o_array.replace([],[2,2],[1])==0
    assert domain.o_array.replace([1,2,3,4,5,1,3,5,1,3,5],[1,3,5],[5,3])==[1,2,3,4,5,5,3,5,3]
    assert domain.o_array.replace([1,1,3,5,2,3,4],[1,3,5],[99])==[1,99,2,3,4]
    assert domain.o_array.replace([1,1,1,1,1],[1],[9])==[9,9,9,9,9]
    assert domain.o_array.replace([11,12,13,14,15,16],[12,13,14],[98,99])==[11,98,99,15,16]

def test_prime_interval():

    assert domain.o_array.prime_interval([],2,3)==0
    assert domain.o_array.prime_interval([1,2,3,4,5,6,7],0,6)==[2,3,5,7]
    assert domain.o_array.prime_interval([1,2,3,4,5,6,7,8,9,17],5,99)==[7,17]
    assert domain.o_array.prime_interval([2,3,5,7,13,17,19],0,67)==[2,3,5,7,13,17,19]
    assert domain.o_array.prime_interval([4,6,8,10,12],0,78)==[]

def test_odd_interval():

    assert domain.o_array.odd_interval([],9,67)==0
    assert domain.o_array.odd_interval([1,2,3,4,5,6,7],0,6)==[1,3,5,7]
    assert domain.o_array.odd_interval([1,2,3,4,5,6,7,8,9,17],5,99)==[7,9,17]
    assert domain.o_array.odd_interval([2,3,5,7,13,17,19],0,67)==[3,5,7,13,17,19]
    assert domain.o_array.odd_interval([4,6,8,10,12,3],0,78)==[3]

def test_sum_ar():

    assert domain.o_array.sum_ar([],34,78)==0
    assert domain.o_array.sum_ar([1,2,3],0,678)==6
    assert domain.o_array.sum_ar([25,25,25,25],0,41351356)==100
    assert domain.o_array.sum_ar([7,3,10,12],3123,41254)==12
    assert domain.o_array.sum_ar([2,3,4,6,3],1,1)==3

def test_gcd_ar():

    assert domain.o_array.gcd_ar([],12,43)==0
    assert domain.o_array.gcd_ar([2,4,6,8,10],0,213)==2
    assert domain.o_array.gcd_ar([1,2,3,4,5,6,],0,214412)==1
    assert domain.o_array.gcd_ar([1,2,3,4,5,8,9],3,3)==4
    assert domain.o_array.gcd_ar([1,2,3,4,6],3,4)==2

def test_max_ar():

    assert domain.o_array.max_ar([],12,12)==0
    assert domain.o_array.max_ar([1,2,3,4,5,6,7],0,3213)==7
    assert domain.o_array.max_ar([1,2,3,4,5,6,7,12,34,5,6],1,2345)==34
    assert domain.o_array.max_ar([1,2,3,4,5],0,0)==1
    assert domain.o_array.max_ar([1,2,3,4,5,6],234324,3245)==6

def test_only_primes():

    assert domain.o_array.only_primes([])==[]
    assert domain.o_array.only_primes([1,2,3,4,5,6,7,8,9,11,13])==[2,3,5,7,11,13]
    assert domain.o_array.only_primes([2,4,6,8,9,10,1])==[2]
    assert domain.o_array.only_primes([-1,-4,-9,3,4,1])==[3]
    assert domain.o_array.only_primes([2,3,7,5,11,13])==[2,3,7,5,11,13]

def test_only_negatives():

    assert domain.o_array.only_negatives([])==[]
    assert domain.o_array.only_negatives([1,2,434,215,4125,3643])==[]
    assert domain.o_array.only_negatives([-1,3,4,5,6,0,0,0])==[-1]
    assert domain.o_array.only_negatives([-1,-9,-9,6,7,-10,1])==[-1,-9,-9,-10]
    assert domain.o_array.only_negatives([-1,-2,-5,-8,-9,-10])==[-1,-2,-5,-8,-9,-10]
    
def Demo():

    array=[]

    print("\t \n Demo-Soft \n\n")

    print("DATA 1=>\n") #1
    for i in range(1,11):
        array=domain.o_array.add(array,i)
    ui.in_out_functions.print_ar(array)
    print("\nInsert 99 at the 3rd index of the array.")
    array=domain.o_array.ins(array,99,3)
    print(array)
    print("\nRemove the 5th element of the array.")
    array=domain.o_array.remove(array,5)
    print(array)
    print("\nRemove the elements between the 1st and 4th index.")
    array=domain.o_array.remove_bt(array,1,4)
    print(array)
    print("\nReplace '9,10' with '273,256,278' .")
    array=domain.o_array.replace(array,[9,10],[273,256,278])
    print(array)
    print("\nPrint the prime numbers between the 0 and last index.")
    primes=domain.o_array.prime_interval(array,0,234)
    print(primes)
    print("\nPrint the odd numbers between the 0 and last index.")
    odds=domain.o_array.odd_interval(array,0,234)
    print(odds)
    print("\nPrint the sum between the 2nd and last index.")
    su=domain.o_array.sum_ar(array,2,3435)
    print(su)
    print("\nPrint the gcd between the 2nd and last index.")
    gc=domain.o_array.gcd_ar(array,2,3245)
    print(gc)
    print("\nPrint the max between the 2nd and last index.")
    mx=domain.o_array.max_ar(array,2,3513)
    print(mx)
    print("\nKeep only the prime numbers in the array.")
    array=domain.o_array.only_primes(array)
    print(array)
    print("\nKeep only the negative numbers in the array.")
    array=domain.o_array.only_negatives(array)
    print(array)
    input("Press any key...")


    print("\nDATA 2=>\n") #2
    for i in range(91,124):
        array=domain.o_array.add(array,i)
    ui.in_out_functions.print_ar(array)
    print("\nInsert 8976 at the last index of the array.")
    array=domain.o_array.ins(array,8976,1234)
    print(array)
    print("\nRemove the 1st element of the array.")
    array=domain.o_array.remove(array,1)
    print(array)
    print("\nRemove the elements between the 3rd and 7th index.")
    array=domain.o_array.remove_bt(array,3,7)
    print(array)
    print("\nReplace '119,118' with '978,456,123456' .")
    array=domain.o_array.replace(array,[119,118],[978,456,123456])
    print(array)
    print("\nPrint the prime numbers between the 2nd and last index.")
    primes=domain.o_array.prime_interval(array,2,234)
    print(primes)
    print("\nPrint the odd numbers between the 2nd and last index.")
    odds=domain.o_array.odd_interval(array,2,234)
    print(odds)
    print("\nPrint the sum between the 2nd and last index.")
    su=domain.o_array.sum_ar(array,2,3435)
    print(su)
    print("\nPrint the gcd between the 2nd and last index.")
    gc=domain.o_array.gcd_ar(array,2,3245)
    print(gc)
    print("\nPrint the max between the 2nd and last index.")
    mx=domain.o_array.max_ar(array,2,3513)
    print(mx)
    print("\nKeep only the prime numbers in the array.")
    array=domain.o_array.only_primes(array)
    print(array)
    print("\nKeep only the negative numbers in the array.")
    array=domain.o_array.only_negatives(array)
    print(array)
    input("Press any key...")

