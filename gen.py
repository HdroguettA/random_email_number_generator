import string
import random

email_string_size = 7
print_qantity = 17

def random_string_generator(size=email_string_size, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
   return ''.join(random.choice(chars) for x in range(size))

def random_phone_number_generator(size=9, chars=string.digits):
     return ''.join(random.choice(chars) for x in range(size))

#enter specific email domain if needed
email_domain = random_string_generator()

x = range(print_qantity)

for n in x:
    print(random_string_generator() + '@' + email_domain + '.com')

for n in x:
     print ('0' + random_phone_number_generator())
