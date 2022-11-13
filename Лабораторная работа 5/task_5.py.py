import string
from random import sample
def get_random_password() -> str:
   return sample((string.digits + string.ascii_letters), 8)

print(get_random_password())