# Web-Automation-Login-Cracker

![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Disclaimer](#disclaimer)
- [Author](#author)

---

## Overview

The Web-Automation-Login-Cracker is a Python script that automates login attempts using Selenium, a popular web automation tool. This script is intended for educational and security testing purposes, helping you test the strength of your login system or understand the importance of using strong and unique passwords.

---

## Features

- Automated login attempts using provided username and password lists.
- Configurable wait times and element location methods.
- Output of successful login combinations.

---

## Getting Started

### Prerequisites

Before you can use the Web-Automation-Login-Cracker, you need to have the following installed:

- Python 3 (Python 3.6 or higher recommended)
- [Selenium WebDriver](https://selenium-python.readthedocs.io/installation.html#drivers) for your preferred web browser (e.g., ChromeDriver).
- The required Python packages, which can be installed using `pip install selenium`.

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/iftekharmickey/Web-Automation-Login-Cracker.git

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt

---

## Usage

1. Edit the configuration variables in the script to suit your testing needs. These variables include:

   - `WAIT_TIME`: Adjust this value to change the waiting time for elements (e.g., `WAIT_TIME = 10`).
   - `URL`: The URL of the login page you want to target (e.g., `URL = 'https://example.com/login'`).
   - `USERNAME_FILE`: The file containing a list of usernames to test (e.g., `USERNAME_FILE = 'usernames.txt'`).
   - `PASSWORD_FILE`: The file containing a list of passwords to test (e.g., `PASSWORD_FILE = 'passwords.txt'`).

2. Customize the element locators in the script to match your specific website. In the script, you'll find lines like:

   ```bash
   username_field = WebDriverWait(driver, WAIT_TIME).until(
    EC.presence_of_element_located((By.ID, 'username'))
   )
   password_field = WebDriverWait(driver, WAIT_TIME).until(
    EC.presence_of_element_located((By.ID, 'password'))
   )
   login_button = WebDriverWait(driver, WAIT_TIME).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'btn-outline-primary') and contains(@class, 'm-2')]"))
   )
 
3. You must define the criteria for a successful login based on your website's behavior, such as the URL that indicates a successful login.

   ```bash
   if '<login-url>' in driver.current_url:
    # This line checks for a successful login based on the URL.
    print(f'[+] Found Username: ==> {username}')
    print(f'[+] Found Password: ==> {password}')
    return True
  
6. Run the script:

   ```bash
   python login_bruteforce.py

7. The script will prompt you for the URL of the login page, username list, and password list.
8. The script will automate login attempts using the provided username and password lists. If it successfully logs in, it will display the combination of the correct username and password.

Make sure to customize these variables to match your specific testing requirements and update the element locators to match your website's attributes. Additionally, define the criteria for a successful login based on your website's behavior.

---

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/iftekharmickey/Web-Automation-Login-Cracker/blob/main/LICENSE) file for details.

---

## Disclaimer

Please use this script responsibly and only for legal and ethical purposes. Unauthorized use of this script may violate the law and is not endorsed. The author is not responsible for any misuse of this tool.

---

## Author

This tool was developed by Iftekhar Tahir.

Enjoy using the Web-Automation-Login-Cracker! For questions, issues, or feedback, feel free to contact me at iftekhar.tahir@proton.me.
