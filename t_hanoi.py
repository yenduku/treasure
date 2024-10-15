def t_hanoi(disks,from_rod,to_rod,aux_rod):
    if disks == 0:
        return
    t_hanoi(disks-1,from_rod,aux_rod,to_rod)
    print(f"Moved {disks} from {from_rod} to {to_rod}  || [{disks}]  {from_rod} -> {to_rod}")
    print()
    t_hanoi(disks-1,aux_rod,to_rod,from_rod)

def main():
    while True:
        print("Enter exit to EXIT the program") 
        print("We have 3 Towers  A , B , C")
        disks = input("Enter the no of Disks : ")
        if disks.lower() == 'exit':
            print("Exiting the program")
            break
        try:
            disks = int(disks)
            if disks < 0:
                raise ValueError("Enter Postive values.")
            elif disks == 0:
                raise ValueError("Enter values greater than 0.")
            t_hanoi(disks,'A','B','C')
            break
        except ValueError:
            print(f'Invalid Input. Enter the +ve values')
main()