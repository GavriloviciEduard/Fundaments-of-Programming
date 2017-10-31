import os
import ui.in_out_functions
import domain.o_array
import test.tst

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
        print("13.Undo the last operation.")
        print("99. Demo-Soft")
        print("0. Exit program.")

        opt=input("Select an option:")

        if opt=='1':
            test.tst.test_add()
            x= ui.in_out_functions.read_number()
            array= domain.o_array.add(array,x)
            ui.in_out_functions.print_ar(array)

        elif opt=='2':
            test.tst.test_ins()
            x=ui.in_out_functions.read_number()
            index=ui.in_out_functions.read_index()
            array=domain.o_array.ins(array,x,index)
            ui.in_out_functions.print_ar(array)

        elif opt=='3':
            test.tst.test_remove()
            index=ui.in_out_functions.read_index()
            array=domain.o_array.remove(array,index)
            if not (array):
                input("The array is empty!")
            else:
                ui.in_out_functions.print_ar(array)

        elif opt=='4':
            test.tst.test_remove_bt()
            index_1=ui.in_out_functions.read_index()
            index_2=ui.in_out_functions.read_index()
            array=domain.o_array.remove_bt(array,index_1,index_2)
            ui.in_out_functions.print_ar(array)

        elif opt=='5':
            test.tst.test_replace()
            sub_ar_1=ui.in_out_functions.read_sub_ar()
            sub_ar_2=ui.in_out_functions.read_sub_ar()
            array=domain.o_array.replace(array,sub_ar_1,sub_ar_2)
            if not (array):
                input("The array is empty or only has one element!")
            else:
                ui.in_out_functions.print_ar(array)

        elif opt=='6':
            test.tst.test_prime_interval()
            index_1=ui.in_out_functions.read_index()
            index_2=ui.in_out_functions.read_index()
            primes=domain.o_array.prime_interval(array,index_1,index_2)
            if not (primes):
                input("The array is empty!")
            else:
                ui.in_out_functions.print_ar(primes)

        elif opt=='7':
            test.tst.test_odd_interval()
            index_1=ui.in_out_functions.read_index()
            index_2=ui.in_out_functions.read_index()
            odds=domain.o_array.odd_interval(array,index_1,index_2)
            if not (odds):
                input("The array is empty!")
            else:
                ui.in_out_functions.print_ar(odds)

        elif opt=='8':
            test.tst.test_sum_ar()
            index_1=ui.in_out_functions.read_index()
            index_2=ui.in_out_functions.read_index()
            su=domain.o_array.sum_ar(array,index_1,index_2)
            print(array)
            print("The sum is ",su)
            input("Press any key...")

        elif opt=='9':
            test.tst.test_gcd_ar()
            index_1=ui.in_out_functions.read_index()
            index_2=ui.in_out_functions.read_index()
            gc=domain.o_array.gcd_ar(array,index_1,index_2)
            print(array)
            if gc:
                print("The gcd is ",gc)
            else:
                print("The array is empty.")
            input("Press any key...")

        elif opt=='10':
            test.tst.test_max_ar()
            index_1=ui.in_out_functions.read_index()
            index_2=ui.in_out_functions.read_index()
            mx=domain.o_array.max_ar(array,index_1,index_2)
            print(array)
            if mx:
                print("The max is ",mx)
            else:
                print("The array is empty.")
            input("Press any key...")

        elif opt=='11':
            test.tst.test_only_primes()
            array=domain.o_array.only_primes(array)
            if array:
                print(array)
            else:
                print("There are no prime numbers in the array.")
            input("Press any key...")

        elif opt=='12':
            test.tst.test_only_negatives()
            array=domain.o_array.only_negatives(array)
            if array:
                print(array)
            else:
                print("There are no negatives numbers in the array.")
            input("Press any key...")
            
        elif opt=='13':
            print(array,end="")
            array=domain.o_array.undo()
            print("=>",array)
            input("Press any key...")
        
                

        elif opt == '99':
            test.tst.Demo()

        elif opt=='0':
            break

        else:
            input("The option doesn't exist! Press any key...")
