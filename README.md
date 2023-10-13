# BruteForce-Login

## Overview

This Python utility is designed to perform a basic brute-force login attack on a website using the provided username and a list of passwords. The script sends HTTP POST requests to the login page URL and checks the response to find a successful login combination.

### Details

- The script uses the `requests` library for making HTTP requests and `termcolor` for colorful console output.

- It takes the following user inputs:
    - Page URL: The URL of the login page.
    - Username: The target username.
    - Password List: A text file containing a list of passwords to try.
    - Login Failed String: The string that appears in the response when login fails.

### Usage

1. Clone this repository to your local machine.
2. Install the necessary dependencies using pip install requests termcolor.
3. Run the script using Python.
4. Follow the prompts and provide the required information.

### Legal and Ethical Considerations

- This script is provided for educational purposes only. Using it for unauthorized access to any system is illegal and unethical.
- Ensure that you have explicit permission to test the security of the target website.
- Always adhere to applicable laws, regulations, and ethical guidelines.

### Disclaimer

The author of this script is not responsible for any illegal or unethical use of the script. Use it responsibly and with permission.

### Dependencies

- [requests](https://pypi.org/project/requests/): Python library for making HTTP requests.
- [termcolor](https://pypi.org/project/termcolor/): Python library for colorful console output.

### Author

This tool was developed by Iftekhar Tahir. If you have any questions or feedback, feel free to contact me at iftekhar.tahir@proton.me.
