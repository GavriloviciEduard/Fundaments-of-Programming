import os
NULL=0

def test_add():

    assert add([],2)==[2]
    assert add([2],3)==[2,3]
    assert add([2,3],11)==[2,3,11]
    assert add([2,3,11],999)==[2,3,11,999]
    assert add([2,3,11,999],25)==[2,3,11,999,25]

def test_ins():

    assert ins([],2,23)==[2]
    assert ins([2],9,0)==[9,2]
    assert ins([9,2],99,1)==[9,99,2]
    assert ins([9,99,2],101,3)==[9,99,2,101]
    assert ins([9,99,2,101],8,1)==[9,8,99,2,101]

def test_remove():

    assert remove([],2)==0
    assert remove([2],0)==[]
    assert remove([2],999)==[]
    assert remove([2,7,8,9,10],2)==[2,7,9,10]
    assert remove([2,7,8,9,10],111)==[2,7,8,9]
    assert remove([2,7,8,9,10],4)==[2,7,8,9]

def test_remove_bt():

    assert remove_bt([],2,2)==0
    assert remove_bt([1],2,2)==0
    assert remove_bt([2,1],0,1)==[]
    assert remove_bt([2,3,4,5,6],3,4)==[2,3,4]
    assert remove_bt([2,3,4,5,6],4,3)==[2,3,4]
    assert remove_bt([2,3,4,5,6],3,99)==[2,3,4]

def test_replace():

    assert replace([],[2,2],[1])==0
    assert replace([1,2,3,4,5,1,3,5,1,3,5],[1,3,5],[5,3])==[1,2,3,4,5,5,3,5,3]
    assert replace([1,1,3,5,2,3,4],[1,3,5],[99])==[1,99,2,3,4]
    assert replace([1,1,1,1,1],[1],[9])==[9,9,9,9,9]
    assert replace([11,12,13,14,15,16],[12,13,14],[98,99])==[11,98,99,15,16]

def test_prime_interval():

    assert prime_interval([],2,3)==0
    assert prime_interval([1,2,3,4,5,6,7],0,6)==[2,3,5,7]
    assert prime_interval([1,2,3,4,5,6,7,8,9,17],5,99)==[7,17]
    assert prime_interval([2,3,5,7,13,17,19],0,67)==[2,3,5,7,13,17,19]
    assert prime_interval([4,6,8,10,12],0,78)==[]

def test_odd_interval():

    assert odd_interval([],9,67)==0
    assert odd_interval([1,2,3,4,5,6,7],0,6)==[1,3,5,7]
    assert odd_interval([1,2,3,4,5,6,7,8,9,17],5,99)==[7,9,17]
    assert odd_interval([2,3,5,7,13,17,19],0,67)==[3,5,7,13,17,19]
    assert odd_interval([4,6,8,10,12,3],0,78)==[3]

def test_sum_ar():

    assert sum_ar([],34,78)==0
    assert sum_ar([1,2,3],0,678)==6
    assert sum_ar([25,25,25,25],0,41351356)==100
    assert sum_ar([7,3,10,12],3123,41254)==12
    assert sum_ar([2,3,4,6,3],1,1)==3

def test_gcd_ar():

    assert gcd_ar([],12,43)==0
    assert gcd_ar([2,4,6,8,10],0,213)==2
    assert gcd_ar([1,2,3,4,5,6,],0,214412)==1
    assert gcd_ar([1,2,3,4,5,8,9],3,3)==4
    assert gcd_ar([1,2,3,4,6],3,4)==2

def test_max_ar():

    assert max_ar([],12,12)==0
    assert max_ar([1,2,3,4,5,6,7],0,3213)==7
    assert max_ar([1,2,3,4,5,6,7,12,34,5,6],1,2345)==34
    assert max_ar([1,2,3,4,5],0,0)==1
    assert max_ar([1,2,3,4,5,6],234324,3245)==6

def test_only_primes():

    assert only_primes([])==[]
    assert only_primes([1,2,3,4,5,6,7,8,9,11,13])==[2,3,5,7,11,13]
    assert only_primes([2,4,6,8,9,10,1])==[2]
    assert only_primes([-1,-4,-9,3,4,1])==[3]
    assert only_primes([2,3,7,5,11,13])==[2,3,7,5,11,13]

def test_only_negatives():

    assert only_negatives([])==[]
    assert only_negatives([1,2,434,215,4125,3643])==[]
    assert only_negatives([-1,3,4,5,6,0,0,0])==[-1]
    assert only_negatives([-1,-9,-9,6,7,-10,1])==[-1,-9,-9,-10]
    assert only_negatives([-1,-2,-5,-8,-9,-10])==[-1,-2,-5,-8,-9,-10]


################################################################################

def add(array,x):
    """
        add=>
            IN: An array of integers 'array' and an integer 'x'.
            OUT: An array of integers 'array'.
            DESC: The fuction adds an integer 'x' in an array of integers 'array'.
    """

    array.append(x)
    return array

def ins(array,x,index):
    """
        ins=>
            IN: An array of integers 'array', an integer 'x' and an integer 'index' representing the index of an array.
            OUT: An array of integers 'array'.
            DESC: The fuction adds an integer 'x', at a given index 'index', in an array of integers 'array'.
    """

    array.insert(index,x)
    return array

def read_number():
    """
        read_number=>
            IN:-
            OUT: An integer 'x'.
            DESC: The fuction reads and returns the value of an integer 'x'.
    """


    x=int(input("Give a number:"))
    return x

def read_index():

    """
        read_index=>
            IN:-
            OUT: An integer 'x'.
            DESC: The fuction reads and returns the value of an integer 'index' which represents the index of an array.
    """

    index=int(input("Give an index:"))
    return index

def remove(array,index):
    """
        remove=>
            IN: An array of integers 'array' and an integer 'index' representing the index  of an array.
            OUT: An array of integers 'array'.
            DESC: The fuction removes an element from an array of integers 'array' at a given index 'index'.
    """

    if array!=[]:
        if index > len(array)-1:
            index=len(array)-1

        array.pop(index)
        return array

    else:
        return NULL



def remove_bt(array,index_1,index_2):
    """
        remove_bt=>
            IN: An array of integers 'array' and two integers 'index_1' && 'index_2' representing the indexes of an array.
            OUT: An array of integers 'array'.
            DESC: The fuction removes the element from an array of integers 'array' between two given indexes 'index_1' && 'index_2'
    """

    if len(array)>1:
        if index_1 > index_2:
            index_1,index_2=index_2,index_1

        while index_2>len(array)-1:
            index_2-=1

        array[index_1:index_2+1]=[]




        return array

    else:
        return NULL


def read_sub_ar():
    """
        read_sub_ar=>
            IN: -
            OUT: An array of integers 'sub_ar'.
            DESC: The fuction reads an array of integers until 0 is given.
    """


    print("Enter a sub-array.The fuction will stop when 0 is read.")
    sub_ar=[]

    i=read_number()

    while i:
        sub_ar.append(i)
        i=read_number()

    return sub_ar

def list_to_string(array):
    """
        list_to_string=>
            IN: An array of integers 'array'.
            OUT: A string 'string'.
            DESC: The fuction converts an array of integers 'array' into a string 'string'.
    """


    string= ' '.join(str(e) for e in array)

    return string

def string_to_list(array):
    """
        string_to_list=>
            IN: A string 'array'.
            OUT: An array of integers 'array_1'.
            DESC: The fuction converts a string 'array' into an array of integers 'array_1'.
    """

    lst=array.split(" ")
    array_1=[]

    for el in lst:
        if el!=' ':
            array_1.append(int(el))


    return array_1

def replace(array,sub_ar_1,sub_ar_2):
    """
        replace=>
            IN: 3 arrays of integers 'arrays', 'sub_ar_1', 'sub_ar_2'.
            OUT: An array of integers 'array'.
            DESC: The fuction replaces all given sub-arrays with another given sub-array. To do this, every array is converted
                  into a string and the method replace() is used. At the end, the string is converted back into an array of integers.
    """

    if array!=[]:
        array=list_to_string(array)
        sub_ar_1=list_to_string(sub_ar_1)
        sub_ar_2=list_to_string(sub_ar_2)



        array=array.replace(sub_ar_1,sub_ar_2)

        array=string_to_list(array)


        return array

    else:
        return NULL



def prime(n):
    """
        prime=>
            IN: An integer 'n'.
            OUT: 0 - if n is not prime and 1 - if n is prime .
            DESC: The fuction checks if a given integer 'n' is prime.
    """

    if n<2:
        return 0

    if n==2:
        return 1

    if n%2==0:
        return 0

    i=3

    while i*i<=n:
        if n%i==0:
            return 0
        i+=2

    return 1

def prime_interval(array,index_1,index_2):

    """
        prime_interval=>
            IN: An array of integers 'array' and two integers 'index_1' && 'index_2' representing the indexes of an array.
            OUT: An array of prime numbers 'primes'.
            DESC: The fuction finds all the prime numbers from an array 'array' between a given interval.
    """

    if array!=[]:
        primes=[]

        if index_1>index_2:
            index_1,index_2=index_2,index_1

        if index_2>=len(array):
            index_2=len(array)-1

        if index_1>=len(array):
            index_1=len(array)-1

  

        for i in range(index_1,index_2+1):
            if prime(array[i]):
                primes.append(array[i])

        return primes

    else:
        return NULL

def odd(n):
    """
        odd=>
            IN: An integer 'n'.
            OUT: 0 - if n is not odd and 1 - if n is odd .
            DESC: The fuction checks if a given integer 'n' is odd.
    """


    if n%2==0:
        return 0
    else:
        return 1

def odd_interval(array,index_1,index_2):
    """
        odd_interval=>
            IN: An array of integers 'array' and two integers 'index_1' && 'index_2' representing the indexes of an array.
            OUT: An array of odd numbers 'odds'.
            DESC: The fuction finds all the odds numbers from an array 'array' between a given interval.
    """

    if array!=[]:

        odds=[]

        if index_2>=len(array):
            index_2=len(array)-1

        if index_1>=len(array):
            index_1=len(array)-1

        for i in range(index_1,index_2+1):
            if odd(array[i]):
                odds.append(array[i])
        return odds


    else:
        return NULL

def sum_ar(array,index_1,index_2):

    """
        sum_ar=>
            IN: An array of integers 'array' and two integers 'index_1' && 'index_2' representing the indexes of an array.
            OUT: An integer 'su' representing the sum of the elements between two indexes of an array.
            DESC: The fuction computes and returns the sum of the elements of an array which are between two indexes of an array.
    """

    su=0

    if array!=[]:
        
        if index_2>=len(array):
            index_2=len(array)-1

        if index_1>=len(array):
            index_1=len(array)-1

 

        for i in range(index_1,index_2+1):
            su+=array[i]

    return su



def gcd(a,b):

    """
        gcd=>
            IN: Two integeres 'a' && 'b'.
            OUT: An integer 'a' representing the GCD of 'a' and 'b'.
            DESC: The fuction computes and returns the GCD of 'a' and 'b'. gcd is implemented as a recursive function and it's based on Euclid's algorithm.
    """

    if not(b):
        return a

    else:
        return gcd(b,a%b)

def gcd_ar(array,index_1,index_2):

    """
        gcd_ar=>
            IN:  An array of integers 'array' and two integers 'index_1' && 'index_2' representing the indexes of an array.
            OUT: An integer 'gc' representing the GCD of the elements of an array that are between two indexes.
            DESC: The fuction computes and returns the GCD of the elements of an array which are between two given indexes.
    """

    gc=0

    if array!=[]:

        if index_2>=len(array):
            index_2=len(array)-1

        if index_1>=len(array):
            index_1=len(array)-1

        if(index_1<len(array)-1 and index_1!=index_2):
            gc=gcd(array[index_1],array[index_1+1])
        else:
            gc=gcd(array[index_1],array[index_1])

        if index_1!=index_2:
            for i in range(index_1+2,index_2+1):
                if i<len(array):
                    gc=gcd(gc,array[i])
    return gc

def max(a,b):

    """
        max=>
            IN: Two integeres 'a' && 'b'.
            OUT: An integer 'a' or 'n' representing the maximum of 'a' and 'b'.
            DESC: The fuction computes and returns the maximum of 'a' and 'b'.
    """
    
    if a>b:
        return a

    elif b>a:
        return b

    else:
        return a

def max_ar(array,index_1,index_2):

    """
        max_ar=>
            IN:  An array of integers 'array' and two integers 'index_1' && 'index_2' representing the indexes of an array.
            OUT: An integer 'mx' representing the maximum of the elements of an array that are between two indexes.
            DESC: The fuction computes and returns the maximum of the elements of an array which are between two given indexes.
    """

    mx=0

    if array!=[]:
    
        if index_2>=len(array):
            index_2=len(array)-1

        if index_1>=len(array):
            index_1=len(array)-1

        if(index_1<len(array)-1 and index_1!=index_2):
            mx=max(array[index_1],array[index_1+1])
        else:
            mx=max(array[index_1],array[index_1])

        if index_1!=index_2:
            for i in range(index_1+2,index_2+1):
                if i<len(array):
                    mx=max(mx,array[i])

    return mx



def print_ar(array):
    """
        print_ar=>
            IN: An array of integers 'array'.
            OUT: -
            DESC: The fuction prints an array of integers 'array'.
    """


    print(array)
    input("Press any key...")

def only_primes(array):

    """
        only_primes=>
            IN: An array of integers 'array'.
            OUT: An array of integers 'o_primes' representing only the prime numbers of the given array.
            DESC: The fuction computes and returns an array of only prime numbers.
    """

    o_primes=[]

    for el in array:
        if prime(el):
            o_primes.append(el)

    return o_primes

def negative(n):

    """
        negative=>
            IN: An integer 'n'.
            OUT: 1-'True' or '0'-False
            DESC: The fuction checks if a given number is negative or not. 
    """

    if n<0:
        return 1

    else:
        return 0

def only_negatives(array):

    """
        only_negatives=>
            IN: An array of integers 'array'.
            OUT: An array of integers 'o_negatives' representing only the negative numbers of the given array.
            DESC: The fuction computes and returns an array of only negative numbers.
    """

    o_negatives=[]

    for el in array:
        if negative(el):
            o_negatives.append(el)

    return o_negatives


def Demo():

    array=[]

    print("\t \n Demo-Soft \n\n")

    print("DATA 1=>\n") #1
    for i in range(1,11):
        array=add(array,i)
    print_ar(array)
    print("\nInsert 99 at the 3rd index of the array.")
    array=ins(array,99,3)
    print(array)
    print("\nRemove the 5th element of the array.")
    array=remove(array,5)
    print(array)
    print("\nRemove the elements between the 1st and 4th index.")
    array=remove_bt(array,1,4)
    print(array)
    print("\nReplace '9,10' with '273,256,278' .")
    array=replace(array,[9,10],[273,256,278])
    print(array)
    print("\nPrint the prime numbers between the 0 and last index.")
    primes=prime_interval(array,0,234)
    print(primes)
    print("\nPrint the odd numbers between the 0 and last index.")
    odds=odd_interval(array,0,234)
    print(odds)
    print("\nPrint the sum between the 2nd and last index.")
    su=sum_ar(array,2,3435)
    print(su)
    print("\nPrint the gcd between the 2nd and last index.")
    gc=gcd_ar(array,2,3245)
    print(gc)
    print("\nPrint the max between the 2nd and last index.")
    mx=max_ar(array,2,3513)
    print(mx)
    print("\nKeep only the prime numbers in the array.")
    array=only_primes(array)
    print(array)
    print("\nKeep only the negative numbers in the array.")
    array=only_negatives(array)
    print(array)
    input("Press any key...")


    print("\nDATA 2=>\n") #2
    for i in range(91,124):
        array=add(array,i)
    print_ar(array)
    print("\nInsert 8976 at the last index of the array.")
    array=ins(array,8976,1234)
    print(array)
    print("\nRemove the 1st element of the array.")
    array=remove(array,1)
    print(array)
    print("\nRemove the elements between the 3rd and 7th index.")
    array=remove_bt(array,3,7)
    print(array)
    print("\nReplace '119,118' with '978,456,123456' .")
    array=replace(array,[119,118],[978,456,123456])
    print(array)
    print("\nPrint the prime numbers between the 2nd and last index.")
    primes=prime_interval(array,2,234)
    print(primes)
    print("\nPrint the odd numbers between the 2nd and last index.")
    odds=odd_interval(array,2,234)
    print(odds)
    print("\nPrint the sum between the 2nd and last index.")
    su=sum_ar(array,2,3435)
    print(su)
    print("\nPrint the gcd between the 2nd and last index.")
    gc=gcd_ar(array,2,3245)
    print(gc)
    print("\nPrint the max between the 2nd and last index.")
    mx=max_ar(array,2,3513)
    print(mx)
    print("\nKeep only the prime numbers in the array.")
    array=only_primes(array)
    print(array)
    print("\nKeep only the negative numbers in the array.")
    array=only_negatives(array)
    print(array)
    input("Press any key...")

def menu():
    """
        menu=>
            IN: -
            OUT: -
            DESC: The fuction creates a menu.
    """

    array=[]

    while True:

        os.system("cls")
        print("1. Add numbers in the array.")
        print("2. Insert a number at an given index in the array.")
        print("3. Remove a number at an given index in the array.")
        print("4. Remove numbers from the array between two given indexes.")
        print("5. Replace a given sub-array with another.")
        print("6. Print the numbers between two indexes that are prime.")
        print("7. Print the numbers between two indexes that are odd.")
        print("8. Print the sum between two indexes.")
        print("9. Print the gcd between two indexes.")
        print("10. Print the max between two indexes.")
        print("11. Keep only prime numbers, remove the other elements.")
        print("12. Keep only negative numbers, remove the other elements.")
        print("99. Demo-Soft")
        print("0. Exit program.")

        opt=input("Select an option:")

        if opt=='1':
            test_add()
            x=read_number()
            array=add(array,x)
            print_ar(array)

        elif opt=='2':
            test_ins()
            x=read_number()
            index=read_index()
            array=ins(array,x,index)
            print_ar(array)

        elif opt=='3':
            test_remove()
            index=read_index()
            array=remove(array,index)
            if not (array):
                input("The array is empty!")
            else:
                print_ar(array)

        elif opt=='4':
            test_remove_bt()
            index_1=read_index()
            index_2=read_index()
            array=remove_bt(array,index_1,index_2)
            print_ar(array)

        elif opt=='5':
            test_replace()
            sub_ar_1=read_sub_ar()
            sub_ar_2=read_sub_ar()
            array=replace(array,sub_ar_1,sub_ar_2)
            if not (array):
                input("The array is empty or only has one element!")
            else:
                print_ar(array)

        elif opt=='6':
            test_prime_interval()
            index_1=read_index()
            index_2=read_index()
            primes=prime_interval(array,index_1,index_2)
            if not (primes):
                input("The array is empty!")
            else:
                print_ar(primes)

        elif opt=='7':
            test_odd_interval()
            index_1=read_index()
            index_2=read_index()
            odds=odd_interval(array,index_1,index_2)
            if not (odds):
                input("The array is empty!")
            else:
                print_ar(odds)

        elif opt=='8':
            test_sum_ar()
            index_1=read_index()
            index_2=read_index()
            su=sum_ar(array,index_1,index_2)
            print(array)
            print("The sum is ",su)
            input("Press any key...")

        elif opt=='9':
            test_gcd_ar()
            index_1=read_index()
            index_2=read_index()
            gc=gcd_ar(array,index_1,index_2)
            print(array)
            if gc:
                print("The gcd is ",gc)
            else:
                print("The array is empty.")
            input("Press any key...")

        elif opt=='10':
            test_max_ar()
            index_1=read_index()
            index_2=read_index()
            mx=max_ar(array,index_1,index_2)
            print(array)
            if mx:
                print("The max is ",mx)
            else:
                print("The array is empty.")
            input("Press any key...")

        elif opt=='11':
            test_only_primes()
            array=only_primes(array)
            if array:
                print(array)
            else:
                print("There are no prime numbers in the array.")
            input("Press any key...")

        elif opt=='12':
            test_only_negatives()
            array=only_negatives(array)
            if array:
                print(array)
            else:
                print("There are no negatives numbers in the array.")
            input("Press any key...")
        
                

        elif opt == '99':
            Demo()

        elif opt=='0':
            break

        else:
            input("The option doesn't exist! Press any key...")


menu()
