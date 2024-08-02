
import requests
from bs4 import BeautifulSoup
import hashlib
import re
import os
import sys


import urllib.request

def print_loading_bar(iteration, total, length=40):
    percent = (iteration / total) * 100
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r[testing website][{bar}] {percent:.2f}% Complete')
    sys.stdout.flush()

def is_valid_url(url):
    # Simple regex to check for a valid URL format
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def is_reachable(url):
    # Send request to website and HTTP status code
    webcode = urllib.request.urlopen(url).getcode()
    return  webcode == 200

def scrape_text(url):
    try:
        response = requests.get(url)
        # Raise HTTPError for bad responses
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])
        return text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def generate_password(text, length):
    hash_object = hashlib.sha3_512(text.encode())
    hex_dig = hash_object.hexdigest()

    # Create a character pool from alphanumeric and special characters
    char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=<>?'

    # Deterministically select characters from the hash
    password = ''.join([char_pool[int(hex_dig[i:i+2], 16) % len(char_pool)] for i in range(0, length * 2, 2)])

    return password

def save_to_file(password, filename):
    with open(filename, 'a') as file:
        file.write(password + '\n')


if __name__ == "__main__":
    url = input("Enter the website URL: ").strip()
    input_length = input("Enter a password length (4-50 characters): ").strip()

    # Input validation for URL and length
    try:
        length = int(input_length)
    except ValueError:
        print("That is not an integer.")
        exit()

    # Make sure password length is within range
    if length > 50 or length < 4:
        raise ValueError("Password length needs to be in the range 4 to 120 characters")

    # Make sure the URL is valid and the website is up and running (200 HTTP status code)
    if not is_valid_url(url):
        print("Invalid URL format. Please enter a valid URL.")
    elif not is_reachable(url):
        print("The website is not reachable. Please check the URL or your network connection.")
    else:
        passwords = [None] * 20

    for i in range(20):
        text = scrape_text(url)
        if text:
            password = generate_password(text, length)
            passwords[i] = password
            if i < 1:
              print(f'[info] generated Password: {password}')
        else:
            raise ValueError("Failed to scrape the text from the website.")
       # Update and display the loading bar
        print_loading_bar(i + 1, 20)

    # Compare the passwords
    for i in range(19):
      if passwords[i] != passwords[i+1]:
          raise ValueError("\n Passwords differ after multiple scrapes. Make sure you are using a static website")
    print("\n[info] Passwords are consistent after multiple scrapes")

    save_choice = input("Would you like to save the password or the website URL to a file? (password/url/[N]o): ").strip().lower()
    if save_choice in ['password', 'url', 'no', 'nO', 'No', 'NO','N', 'n']:
        if save_choice == 'password':
            filename = input("Enter the filename to save to: ").strip()
            app_pass = input("input name entry for password (e.g. netflix, instagram, ...)")
            combo_pass = app_pass + ":" + password
            save_to_file(combo_pass, filename)
            print(f'{save_choice.capitalize()} has been saved to {filename}')
        elif save_choice == 'url':
            filename = input("Enter the filename to save to: ").strip()
            app_pass = input("input name entry for password (e.g. netflix, instagram, ...)")
            url_combo = 'password for ' + app_pass + ' - website url: ' + url + ", password length = " + str(length)
            save_to_file(url_combo, filename)
            print(f'{save_choice.capitalize()} has been saved to {filename}')
        else:
          print(f'Password: {password}')
    else:
        print("Invalid choice. Nothing was saved.")
