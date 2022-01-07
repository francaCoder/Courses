"""
Make a code that read two values and show on screen:
[ 1 ] Sum
[ 2 ] Multiply
[ 3 ] Higher number
[ 4 ] New numbers
[ 5 ] Exit
"""

from time import sleep

n1 = int(input("First Value: "))
n2 = int(input("Second Value: "))
option = 0
while option != 5:
    print("""
    [ 1 ] Sum
    [ 2 ] Multiply
    [ 3 ] Higher number
    [ 4 ] New numbers
    [ 5 ] Exit
    """)
    option = int(input("→ What's your choice? "))
    if option == 1:
        r = n1 + n2
        print("The sum between {} + {} is {}".format(n1, n2, r))
    elif option == 2:
        r = n1 * n2
        print("The result between {} x {} is {}".format(n1, n2, r))
    elif option == 3:
        if n1 > n2:
            higher = n1
        else:
            higher = n2
        print("Between {} and {} the higher number is {}".format(n1, n2, higher))
    elif option == 4:
        print("Inform the new numbers:")
        n1 = int(input("First Value: "))
        n2 = int(input("Second Value: "))
    elif option == 5:
        print("Finishing...")
        sleep(0.7)
    else:
        print("Invalid option")
    sleep(1)
print("End")
