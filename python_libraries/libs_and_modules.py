# Libraries and Modules

# from random import *
# import math
# import os, datetime, sys
import requests

# print(random())

# num_float = 23.66
# print(math.ceil(num_float)) # 24
# print(math.floor(num_float)) # 23
# print(math.pi)

# working_dir = os.getcwd()
# login = os.getlogin()
# print(working_dir)
# print(login)

# print(datetime.date.today())

# print(sys.version)

request_bbc = requests.get("https://www.bbc.co.uk/")
print(request_bbc.status_code) # 200
# print(request_bbc.content)

