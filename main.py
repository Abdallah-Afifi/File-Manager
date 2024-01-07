import os

class FileManager:
    def __init__(self):
        self.current_directory = os.getcwd()

    def display_files(self):
        print("\nFiles in the current directory:")
        files = os.listdir(self.current_directory)
        for file in files:
            print(file)

    def create_file(self, file_name):
        file_path = os.path.join(self.current_directory, file_name)
        try:
            with open(file_path, 'w'):
                pass  # Create an empty file
            print(f"File '{file_name}' created successfully.")
        except Exception as e:
            print(f"Error creating file: {e}")

    def delete_file(self, file_name):
        file_path = os.path.join(self.current_directory, file_name)
        try:
            os.remove(file_path)
            print(f"File '{file_name}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting file: {e}")

    def rename_file(self, old_name, new_name):
        old_path = os.path.join(self.current_directory, old_name)
        new_path = os.path.join(self.current_directory, new_name)
        try:
            os.rename(old_path, new_path)
            print(f"File '{old_name}' renamed to '{new_name}' successfully.")
        except Exception as e:
            print(f"Error renaming file: {e}")

def main():
    file_manager = FileManager()

    while True:
        print("\nOptions:")
        print("1. Display Files")
        print("2. Create File")
        print("3. Delete File")
        print("4. Rename File")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            file_manager.display_files()
        elif choice == '2':
            file_name = input("Enter the name of the file to create: ")
            file_manager.create_file(file_name)
        elif choice == '3':
            file_name = input("Enter the name of the file to delete: ")
            file_manager.delete_file(file_name)
        elif choice == '4':
            old_name = input("Enter the current name of the file: ")
            new_name = input("Enter the new name of the file: ")
            file_manager.rename_file(old_name, new_name)
        elif choice == '5':
            print("Exiting the File Manager Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
