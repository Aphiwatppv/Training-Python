import logging
from Method import Method
# Execute
while True:
    print("Please select an option:")
    print("1: Copy Files")
    print("2: Delete File")
    print("3: Create New File")
    print("4: Exit")

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
        while True:
            print("1 for create a CSV file")
            print("2 for create a TXT file")
            print("3 Exits")
            try:
                UserCreateFile = int(input("Please input the number to select file type: "))
            except ValueError:
                print("Please enter a valid number.")
                logging.warning("Invalid input for feature selection")
                continue

            if UserCreateFile == 1:
                header = int(input("Please determine the number of headers for the csv file: "))
                headers = []
                for i in range(header):
                    headers.append(input(f"Header {i+1}: Please enter the header name: "))

                initial_data = []
                for h in headers:
                    initial_data.append(input(f"Please add initial data for the '{h}' header: "))

                data = [headers] + [initial_data]  # First row as header, followed by data
                try:
                    csv_name = input("Please enter the name of the CSV file (with .csv extension): ")
                    Method.create_file(csv_name, data)
                except Exception as e:
                    print(f"An error occurred: {e}")
                    logging.error(f"Error creating file: {e}")

            elif UserCreateFile == 2:
                txt_name = input("Please enter the name of the TXT file (with .txt extension): ")
                sample_sentence = input("Please enter sample sentence: ")
                try:
                    Method.create_file(txt_name, sample_sentence)
                except Exception as e:
                    print(f"An error occurred: {e}")
                    logging.error(f"Error creating file: {e}")
            elif UserCreateFile == 3:
                print('Thank you!!')
                logging.info("User exited the create file feature")
                break

            

    elif UserInput == 4:
        print('Thank you!!')
        logging.info("User exited the program")
        break
    else:
        print("Invalid option, please try again.")
        logging.warning("User selected an invalid option")
