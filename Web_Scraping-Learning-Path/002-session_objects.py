import requests
from getpass import getpass
from requests.exceptions import Timeout

# By using a context manager, you can ensure the resources used by
# the session will be released after use
# with requests.Session() as session:
# session.auth = ('username', getpass())

# Instead of requests.get(), you'll use session.get()

session = requests.Session()

try:
	response = session.get("https://api.ipify.org?format=json", timeout=2)
except Timeout:
	print("Request timed out")
else:
	print("Request not timed out")
	# print(response.headers)
	print(response.json().get('ip', "0.0.0.0"))

# You can inspect the response just like you did before
