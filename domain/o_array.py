NULL=0
import utils.ut_functions

prev_array=[]

def add(array,x):
    """
        add=>
            IN: An array of integers 'array' and an integer 'x'.
            OUT: An array of integers 'array'.
            DESC: The fuction adds an integer 'x' in an array of integers 'array'.
    """
    
    global prev_array
    prev_array=array[:]

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


def remove(array,index):
    """
        remove=>
            IN: An array of integers 'array' and an integer 'index' representing the index  of an array.
            OUT: An array of integers 'array'.
            DESC: The fuction removes an element from an array of integers 'array' at a given index 'index'.
    """
    
    global prev_array
    prev_array=array[:]

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
    
    global prev_array
    prev_array=array[:]

    if len(array)>1:
        if index_1 > index_2:
            index_1,index_2=index_2,index_1

        while index_2>len(array)-1:
            index_2-=1

        array[index_1:index_2+1]=[]




        return array

    else:
        return NULL

def replace(array,sub_ar_1,sub_ar_2):
    """
        replace=>
            IN: 3 arrays of integers 'arrays', 'sub_ar_1', 'sub_ar_2'.
            OUT: An array of integers 'array'.
            DESC: The fuction replaces all given sub-arrays with another given sub-array. To do this, every array is converted
                  into a string and the method replace() is used. At the end, the string is converted back into an array of integers.
    """
    
    global prev_array
    prev_array=array[:]

    if array!=[]:
        array=utils.ut_functions.list_to_string(array)
        sub_ar_1=utils.ut_functions.list_to_string(sub_ar_1)
        sub_ar_2=utils.ut_functions.list_to_string(sub_ar_2)



        array=array.replace(sub_ar_1,sub_ar_2)

        array=utils.ut_functions.string_to_list(array)


        return array

    else:
        return NULL

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
            if utils.ut_functions.prime(array[i]):
                primes.append(array[i])

        return primes

    else:
        return NULL
    
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
            if utils.ut_functions.odd(array[i]):
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
            gc=utils.ut_functions.gcd(array[index_1],array[index_1+1])
        else:
            gc=utils.ut_functions.gcd(array[index_1],array[index_1])

        if index_1!=index_2:
            for i in range(index_1+2,index_2+1):
                if i<len(array):
                    gc=utils.ut_functions.gcd(gc,array[i])
    return gc

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

def only_primes(array):

    """
        only_primes=>
            IN: An array of integers 'array'.
            OUT: An array of integers 'o_primes' representing only the prime numbers of the given array.
            DESC: The fuction computes and returns an array of only prime numbers.
    """
    
    global prev_array
    prev_array=array[:]

    o_primes=[]

    for el in array:
        if utils.ut_functions.prime(el):
            o_primes.append(el)

    return o_primes

def only_negatives(array):

    """
        only_negatives=>
            IN: An array of integers 'array'.
            OUT: An array of integers 'o_negatives' representing only the negative numbers of the given array.
            DESC: The fuction computes and returns an array of only negative numbers.
    """
    
    global prev_array
    prev_array=array[:]

    o_negatives=[]

    for el in array:
        if utils.ut_functions.negative(el):
            o_negatives.append(el)

    return o_negatives

def undo():
    """
        undo=>
            IN: -
            OUT: An array of integers 'prev_list' representing the last array.
            DESC: The fuction undoes the last operation.
    """
    global prev_array
    return prev_array




