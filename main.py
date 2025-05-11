import secrets
import string
import hashlib
import requests
import sys

lengthpass = int(input("Введите длинну пароля: "))

if lengthpass <= 8:
	print("Такой пароль будет легко разгадать.")
	sys.exit()
else: 
	def gen_pass(length=lengthpass):
		chars = string.ascii_letters + string.digits + "!@#$%^&*" #Берем буквы (верхний и нижний регистр), цифры и спецсимволы.
		password = "".join(secrets.choice(chars) for _ in range(length)) #secrets.choice() гарантирует криптографическую стойкость.
		return password

date = gen_pass()
print(date)

def check_pass(password):
	sha1_pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	prefix, suffix = sha1_pass[:5], sha1_pass[5:]

	url = f"https://api.pwnedpasswords.com/range/{prefix}"
	response = requests.get(url)

	for line in response.text.splitlines():
		if suffix in line:
			return True, int(line.split(":")[1])
		return False, 0

is_leaked, count = check_pass(date)
if is_leaked:
	print(f'Пароль найден в {count} утечках')
else:
	print("Пароль безопасен")