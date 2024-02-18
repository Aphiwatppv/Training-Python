import shutil
import os
import logging
import csv
    # Configure logging
logging.basicConfig(filename='file_management.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

class Method:
    
    @staticmethod
    def copy_file(source_path, destination_path):
        try:
            shutil.copy2(source_path, destination_path)
            print(f"File copied successfully from {source_path} to {destination_path}")
            logging.info(f"File copied from {source_path} to {destination_path}")
        except FileNotFoundError:
            print(f"The file {source_path} was not found.")
            logging.warning(f"File not found: {source_path}")
        except PermissionError:
            print(f"Permission denied to copy to {destination_path}.")
            logging.error(f"Permission denied for copying to {destination_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
            logging.error(f"Error copying file: {e}")

    @staticmethod
    def delete_file(file_path):
        try:
            os.remove(file_path)
            print(f"File {file_path} has been deleted successfully.")
            logging.info(f"File deleted: {file_path}")
        except FileNotFoundError:
            print(f"The file {file_path} does not exist.")
            logging.warning(f"Attempted to delete non-existent file: {file_path}")
        except PermissionError:
            print(f"Permission denied: unable to delete {file_path}.")
            logging.error(f"Permission denied for deleting file: {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
            logging.error(f"Error deleting file: {e}")

    @staticmethod
    def create_file(file_path, content=None):
        try:
            # Check if the file is a CSV
            if file_path.endswith('.csv'):
                with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerows(content or [])
            else:  # Assume it's a text file
                with open(file_path, mode='w', encoding='utf-8') as file:
                    file.write(content or '')
            
            print(f"File {file_path} has been created successfully.")
            logging.info(f"File created: {file_path}")
        except PermissionError:
            print(f"Permission denied: unable to create {file_path}.")
            logging.error(f"Permission denied for creating file: {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
            logging.error(f"Error creating file: {e}")