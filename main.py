from addProduct import addProduct
from broadcast import broadcast
from listOrders import listOrder
from listProduct import listProduct
from updateProduct import updateProduct
from utils import clearShell
from takeOrder import takeOrder


def takeInput():
    clearShell()
    print("""== = == = Welcome to POS System == = == =

    1. Take order
    2. List orders
    3. Add Product
    4. List Products
    5. Update Products
    6. Broadcast Offer
    7. Exit
    """)
    return int(input("Choose an action(1-7): "))

def main():
    choice = takeInput()
    clearShell()
    if choice == 1:
        takeOrder()
    elif choice == 2:
        listOrder()
    elif choice == 3:
        addProduct()
    elif choice == 4:
        listProduct()
    elif choice == 5:
        updateProduct()
    elif choice == 6:
        broadcast()
    elif choice == 7:
        exit()


main()
