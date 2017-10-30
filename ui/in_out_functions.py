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


def print_ar(array):
    """
        print_ar=>
            IN: An array of integers 'array'.
            OUT: -
            DESC: The fuction prints an array of integers 'array'.
    """


    print(array)
    input("Press any key...")
