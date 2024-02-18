import logging
from Method import Method
# Execute
while True:
    print("Please select an option:")
    print("1: Copy Files")
    print("2: Delete File")
    print("3: Exit")

    try:
        UserInput = int(input("Please input the number to select a feature of the software: "))
    except ValueError:
        print("Please enter a valid number.")
        logging.warning("Invalid input for feature selection")
        continue

    if UserInput == 1:
        source = input("Please enter the source path: ")
        destination = input("Please enter the destination path: ")
        Method.copy_file(source, destination)
    elif UserInput == 2:
        file_to_delete = input("Please enter the file path to delete: ")
        Method.delete_file(file_to_delete)
    elif UserInput == 3:
        print('Thank you!!')
        logging.info("User exited the program")
        break
    else:
        print("Invalid option, please try again.")
        logging.warning("User selected an invalid option")
