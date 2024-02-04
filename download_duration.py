def cal_MB_GB():
    inputMB = float(input("Number of MB: "))
    result = (inputMB / 1000)
    print(f"{result} GB")

def cal_remaining():
    remaining_data = float(input("Remaining GB: "))
    data_speed = float(input("Dataspeed in MB/s: "))
    result = remaining_data * 1000 / data_speed / 60
    print(f"{result:.2f} minutes")


while True:
    choice = input("1 to calculate GB in MB\n2 to calculate speed\n3 to stop the program\nYour choice: ")

    if choice == '1':
        cal_MB_GB()
    if choice == '2':
        cal_remaining()
    elif choice == '3':
        break
    else:
        print("Please choose a valid number!")


