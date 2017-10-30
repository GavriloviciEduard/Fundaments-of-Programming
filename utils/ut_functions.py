def list_to_string(array):
    """
        list_to_string=>
            IN: An array of integers 'array'.
            OUT: A string 'string'.
            DESC: The fuction converts an array of integers 'array' into a string 'string'.
    """


    string= " ".join(str(e) for e in array)
    return string

def string_to_list(array):
    """
        string_to_list=>
            IN: A string 'array'.
            OUT: An array of integers 'array_1'.
            DESC: The fuction converts a string 'array' into an array of integers 'array_1'.
    """

    array=array.split(" ")

    array_1=[]

    for el in array:
        if el!=" ":
            array_1.append(int(el))


    return array_1

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
    


    




