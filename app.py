import subprocess
import platform
import time
import pyautogui
import datetime
import webbrowser
import os

def search_web():
    query = input("Enter your search query: ")
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    print(f"Search results for '{query}' opened in the default browser.")

def validate_directory(directory):
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
            print(f"Directory '{directory}' created successfully.")
            return True
        except OSError as e:
            print(f"Failed to create directory '{directory}': {e}")
            return False
    else:
        print(f"Directory '{directory}' already exists.")
        return True

def open_application(app_name):
    try:
        if platform.system() == "Windows":
            subprocess.Popen(["start", f"{app_name}.exe"], shell=True)
        elif platform.system() == "Darwin":  # For macOS
            subprocess.Popen(["open", "-a", app_name])
        elif platform.system() == "Linux":  # For Linux-based systems
            subprocess.Popen([app_name.lower()])
        else:
            print("Unsupported operating system.")
            return False

        time.sleep(5)  # Pause to allow the application to open
        return True
    except FileNotFoundError:
        print(f"{app_name} not found or unable to open.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def execute_command():
    command = input("Enter the system command to execute: ")
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print("Command Output:")
        print(output)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e.output}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def close_application(app_name):
    try:
        if platform.system() == "Windows":
            subprocess.Popen(["taskkill", "/f", "/im", f"{app_name}.exe"], shell=True)
        elif platform.system() == "Darwin":  # For macOS
            subprocess.Popen(["pkill", "-f", app_name])
        elif platform.system() == "Linux":  # For Linux-based systems
            subprocess.Popen(["pkill", "-f", app_name.lower()])
        else:
            print("Unsupported operating system.")
            return False

        time.sleep(2)  # Pause to allow the application to close
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def open_url(url):
    try:
        if platform.system() == "Windows":
            subprocess.Popen(["start", url], shell=True)
        elif platform.system() == "Darwin":  # For macOS
            subprocess.Popen(["open", url])
        elif platform.system() == "Linux":  # For Linux-based systems
            subprocess.Popen(["xdg-open", url])
        else:
            print("Unsupported operating system.")
            return False

        time.sleep(2)  # Pause to allow the browser to open
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def automate_open_application():
    apps = {
        1: "Spotify",
        2: "Chrome",
    }

    print("Choose an application to open:")
    for idx, app in apps.items():
        print(f"{idx}. {app}")

    while True:
        try:
            choice = int(input("Enter the number of the application: "))
            if choice in apps:
                selected_app = apps.get(choice)
                if open_application(selected_app):
                    print(f"{selected_app} opened successfully.")
                else:
                    print(f"Failed to open {selected_app}.")
                break  
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def automate_close_application():
    apps = {
        1: "Spotify",
        2: "Chrome",
    }

    print("Choose an application to close:")
    for idx, app in apps.items():
        print(f"{idx}. {app}")

    while True:
        try:
            choice = int(input("Enter the number of the application to close (0 to go back): "))
            if choice == 0:
                break
            elif choice in apps:
                selected_app = apps.get(choice)
                if close_application(selected_app):
                    print(f"{selected_app} closed successfully.")
                else:
                    print(f"Failed to close {selected_app}.")
                break  # Break the loop after attempting to close the selected application
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def automate_open_url():    
    while True:
        user_url = input("Enter the URL to open: ")
        if not user_url.startswith(('http://', 'https://')):
            print("Please enter a valid URL starting with 'http://' or 'https://'")
            continue
        
        confirmation = input(f"Do you want to open '{user_url}'? (yes/no): ")
        if confirmation.lower() == "yes":
            if open_url(user_url):
                print(f"Opening {user_url} in the default browser...")
                print("URL opened successfully.")
                break
            else:
                print(f"Failed to open {user_url}.")
                break
        elif confirmation.lower() == "no":
            print("URL opening cancelled.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def take_screenshot():
    directory = './screenshots'
    if validate_directory(directory):
        try:
            now = datetime.datetime.now()
            timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
            screenshot = pyautogui.screenshot()
            screenshot.save(f'{directory}/screenshot_{timestamp}.png')
            print(f"Screenshot saved as 'screenshot_{timestamp}.png' in '{directory}'.")
            return True
        except Exception as e:
            print(f"Failed to take a screenshot: {e}")
            return False

def create_text_file():
    directory = './data'
    if validate_directory(directory):
        file_name = input("Enter the file name: ")
        content = input("Enter the content for the text file: ")
        try:
            with open(f'{directory}/{file_name}.txt', 'w') as file:
                file.write(content)
            print(f"Text file '{file_name}.txt' created successfully in '{directory}'.")
            return True
        except Exception as e:
            print(f"Failed to create the text file: {e}")
            return False


# Main function to run the automation
def main():
    directories_to_check = ['./screenshots', './data']
    for directory in directories_to_check:
        validate_directory(directory)
    while True:
        print("\nSelect an option:")
        print("1. Open Application")
        print("2. Close Application")
        print("3. Open URL")
        print("4. Take Screenshot")
        print("5. Create a Text File")
        print("6. Execute System Command")
        print("7. Search the Web")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                automate_open_application()
            elif choice == 2:
                automate_close_application()
            elif choice == 3:
                automate_open_url()
            elif choice == 4:
                take_screenshot()
            elif choice == 5:
                create_text_file()
            elif choice == 6:
                execute_command()
            elif choice == 7:
                search_web()
            elif choice == 8:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()