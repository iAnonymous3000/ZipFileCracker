# Zip File Cracker

Zip File Cracker is a Python script demonstrating brute force password cracking techniques on encrypted ZIP archives. It utilizes multithreading to enhance performance in password guessing.

## Overview

This project illustrates concepts like brute force attacks and multithreaded processing in Python. 

**Important: This tool is not meant for unauthorized or illegal use. Users are responsible for their actions with this script.**

## Legal and Ethical Considerations

This tool is intended for educational purposes, authorized security testing, and other lawful uses only. Unauthorized hacking, accessing, or attempting to access computer systems or data without consent is illegal and punishable by law. Users must ensure they have explicit permission to test target systems and comply with all relevant laws and regulations.

Users are responsible for their actions with this script. The developer disclaims any liability for misuse of this tool or any unlawful activities conducted with it.

## Features

- Multi-threaded password guessing for improved efficiency.
- Customizable character set and maximum password length.
- Periodic status updates during the cracking process.
- Automatic termination upon successful password discovery.

## Prerequisites

- Python 3.x
- Standard Python libraries: `zipfile`, `itertools`, `threading`, `time`

## Installation 

Clone the repository:

```
git clone https://github.com/iAnonymous3000/ZipFileCracker.git
```

Navigate to the project directory:

```
cd zip_cracker
```

## Usage

Run the script as follows:

```
python zip_cracker.py <zip_file> <charset> <max_length> 
```

- `zip_file`: Path to the encrypted ZIP file.
- `charset`: Set of characters to be used for password generation.
- `max_length`: Maximum length of password combinations to try.

### Examples

Simple example:
```
python zip_cracker.py test.zip abc 3
```

More complex example:
```
python zip_cracker.py secret.zip abcd1234 8
```

## Implementation

The `ZipCracker` class is initialized with the zip file path, charset, and maximum password length. It generates password combinations and uses multiple threads to attempt to crack the encrypted zip file.

## License 

This project is licensed under the MIT License - see the `LICENSE` file for details.
