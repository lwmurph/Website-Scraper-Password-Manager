# Password Generator from Website Scraper
This script generates passwords by scraping text from a website and hashing it. It includes a loading bar to show progress and allows saving the result to a file. The script ensures that passwords are consistent across multiple scrapes.

## Features

- Scrapes text from a specified URL.
- Generates a deterministic password using SHA-3-512 hashing.
- Displays a loading bar to indicate progress.
- Compares passwords from multiple scrapes to ensure consistency.
- Offers options to save the generated password or the website URL to a file.

## Requirements

- requests: For making HTTP requests to the website.
- beautifulsoup4: For parsing HTML and extracting text.
- hashlib: For hashing text to generate passwords.
- re: For regular expression operations.
- sys: For displaying progress in the terminal.

## Installation

Ensure you have the required libraries. You can install them using pip:

```
pip install requests beautifulsoup4
```

## Usage

1. **Run the Script:**

```
python password_generator.py
```

2. **Input Prompts:** \
 - Website URL: Enter the URL of the website you want to scrape. \
 - Password Length: Enter the desired length of the password (between 4 and 50 characters). \
3. **Progress Indicator:**
 - The script will display a loading bar showing the progress of password generation.

4. Save Options:
 - After generating passwords, you can choose to save either the password or the URL to a file.
 - Enter a filename and a descriptive name for the password (e.g., Netflix, Instagram).

## Example
```
Enter the website URL: http://example.com
Enter a password length (4-50 characters): 12
[testing website][██████████████████████████████████████] 100.00% Complete
[info] Passwords are consistent after multiple scrapes
Would you like to save the password or the website URL to a file? (password/url/[N]o): password
Enter the filename to save to: passwords.txt
input name entry for password (e.g. netflix, instagram, ...): netflix

```
In this example, a password is generated from http://example.com, checked for consistency, and saved to passwords.txt with the label Netflix.


## Error Handling


- Invalid URL Format: The script checks if the URL is valid.
- Website Unreachable: The script ensures the website is reachable and responds with HTTP status code 200.
- Inconsistent Passwords: If passwords differ between scrapes, an error is raised.

## Notes
- Ensure that the website you are scraping is static and does not change frequently to get consistent results.
- The script currently assumes that the content of the website is in <p> tags. Adjust the scraping logic if necessary.



**To ensure the repeatability of your password generation, you should choose websites or sources where the content remains static and unchanging. Here are some examples of such sources:**


>**Public Domain Books:** Websites hosting public domain books, like Project Gutenberg, where the content of books remains unchanged.\
*Example: Project Gutenberg* \
> **Government Websites:** Certain government documents or archives that do not change frequently.\
*Example: USA.gov* \
> **Static Educational Resources:** Websites hosting educational resources or historical documents that are not updated frequently.\
*Example: Khan Academy*\
>**Archived Web Pages:** Websites like the Internet Archive that provide archived snapshots of web pages. \
*Example: Internet Archive*\
> **PDF Documents:** Direct links to PDF documents hosted on websites that are not updated frequently.