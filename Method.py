import shutil
import os
import logging

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