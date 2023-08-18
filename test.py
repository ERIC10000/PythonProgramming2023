from functions import *

# send_sms("+254740922861", "Hello there....")

otp_code = generate_random()
print(otp_code)

status = passwordValidity("12345678Admin@")
print(status)


valid_phone = check_phone("+256740922861")
print(valid_phone)

