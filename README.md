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
- [Contributing](#contributing)
- [License](#license)

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
   [git clone https://github.com/iftekharmickey/Selenium-Login-Cracker.git](https://github.com/iftekharmickey/Web-Automation-Login-Cracker.git)

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt

---

## Usage

1. Edit the configuration variables in the script (`WAIT_TIME`, `URL`, `USERNAME_FILE`, and `PASSWORD_FILE`) to suit your testing needs.
2. Run the script:

   ```bash
   python login_bruteforce.py

3. The script will prompt you for the URL of the login page, username list, and password list.
4. The script will automate login attempts using the provided username and password lists. If it successfully logs in, it will display the combination of the correct username and password.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---
