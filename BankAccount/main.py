
def initial_screen():
    print("[1] Open a new account" )
    print("[2] Access an existing account")
    print("[3] Exit")

    s = ""
    while s != "3":
        print("Please Enter from menu. Use [3] to exit: ", end='')
        s = input().strip()
        if s == "1":
            return new_account_screen
        elif s == "2":
            return existing_account_screen
        elif s == "3":
            return None


def new_account_screen():
    print("New Account Screen")
    return initial_screen

def existing_account_screen():
    print("Existing Account Screen")
    return initial_screen

if __name__ == '__main__':

    next = initial_screen

    # process screens until done
    while next:
        next = next()
    print("\nExiting")
