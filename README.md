# PasswordAssault #

This Python utility is designed to perform a brute-force attack against a web login page, attempting to find valid usernames and passwords from a provided list. It utilizes the requests library to send POST requests to the specified URL, systematically testing each password from a given password list until a successful login is achieved or all possibilities have been exhausted.

The script prompts the user for the target URL, a username to target, a password list, and a login failure string. It iteratively sends login requests with different passwords, checking for the presence of the login failure string in the response. If the login fails, the script continues with the following password in the list. When a successful login is detected, it outputs the discovered username and password.

Note: Always use this script responsibly and within the boundaries of the law and ethical guidelines. Unauthorized use for malicious purposes is strictly prohibited.

## Usage ##

```python3 bruteforce.py```

- Target URL: Provide the URL of the login page to breach
- Username: Specify the username of the target account
- Password List: Furnish the list of passwords for the brute-force attack
- Login Failure Indicator: Define the string that indicates a failed login attempt
