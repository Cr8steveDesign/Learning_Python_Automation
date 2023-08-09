# Introduction to the urllib.requests inbuilt library in python for making
# HTTP Requests.
# Install the request package: pipenv install requests
# pip install requests

# Making Sample request with a context manager
# Guarding against error with the .raise_for_status() method
# import requests
# from requests.exceptions import HTTPError
#
# for url in ['https://api.github.com', 'https://api.github.com/invalid']:
#     try:
#         response = requests.get(url)
#
#         # If the response was successful, no Exception will be raised
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')  # Python 3.6
#     except Exception as err:
#         print(f'Other error occurred: {err}')  # Python 3.6
#     else:
#         print('Success!')

import requests

url = "https://www.w3resource.com/python-exercises/python-basic-exercises.php"

response = requests.get(url)
# print(response.content.decode())

print(response.text)
