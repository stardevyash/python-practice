from data import l

def main():
    i = input("Enter  your name:")
    if i == "exit":
        print("Thank you for using this program\nExiting...")
        exit(0)
    elif i.upper() in l:
        print(f"Hello {i}")
    else:
        print(f"Hello {i}, we are saving your name in our database")
        return i