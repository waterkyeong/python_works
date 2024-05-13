# chap 02 p. simple_message

a='hi'
print(a)
a = 4
print(a)

# p.65-66 name_cases
msg = 'kim'
print(f"안녕하세요.{msg},오늘 파이썬 배워 보는 게 어떨까요?")
print(msg.capitalize())
print(msg.upper())
print(msg.lower())
# 2-6
famous_person = '알베르트 아인슈타인'
message = '" 한 번도 실수한 적이 없는 사람은 한 번도 새로운 것에 도전해 본 적이 없는 사람이다."'
print(f"{famous_person},{message}")

# 2-7
famous_person ='  \n알베르트 아인슈타인  \t   '
famous_person = famous_person.lstrip()
print(famous_person)
famous_person = famous_person.rstrip()
print(famous_person)
famous_person = famous_person.strip()
print(famous_person)

# 2-8
