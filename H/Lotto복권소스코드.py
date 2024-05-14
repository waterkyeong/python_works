
#아래는 파이썬 세트를 사용하여 로또 복권 6개 번호와 보너스 번호를 100장 발행하여 세트에 저장하는 코드입니다.

import random

# 두 세트 생성
set1 = {1, 2, 3, 4, 5}
set2 = {3, 2, 1, 5, 4}

# 두 세트가 동일한지 확인 (모든 요소가 같은지)
print("set1과 set2가 동일한지:", set1 == set2)

# 로또 복권 번호 생성 함수
def generate_lotto_numbers():
    # 1부터 45까지의 숫자 리스트 생성
    numbers = list(range(1, 46))
    
    # 무작위로 숫자 6개 선택하여 세트로 변환 (중복 없음)
    lotto_numbers = set(random.sample(numbers, 6))
    
    # 무작위로 숫자 1개 선택하여 보너스 번호 생성
    bonus_number = random.choice(numbers)
    
    return lotto_numbers, bonus_number

    # 로또 번호와 보너스 번호가 당첨 번호와 일치하는지 확인
def check_winner(idx, lotto_numbers,lotto_bonus_number,winning_numbers,winning_bonus_number):
    
    if lotto_numbers == winning_numbers and lotto_bonus_number == winning_bonus_number:
        print(f"{idx}번째 로또 복권: 1등 당첨!")
    elif lotto_numbers == winning_numbers or (len(lotto_numbers.intersection(winning_numbers)) == 5 and lotto_bonus_number == winning_bonus_number):
        print(f"{idx}번째 로또 복권: 2등 당첨! (보너스 번호 불일치) 또는 보너스 번호 포함 6개 일치")
    elif len(lotto_numbers.intersection(winning_numbers)) == 5 or (len(lotto_numbers.intersection(winning_numbers)) == 4 and lotto_numbers == winning_numbers):
        print(f"{idx}번째 로또 복권: 3등 당첨! (5개 일치 보너스 번호 포함)")
    elif (len(lotto_numbers.intersection(winning_numbers)) == 4) or (len(lotto_numbers.intersection(winning_numbers)) == 3 and lotto_numbers == winning_numbers):
        print(f"{idx}번째 로또 복권: 4등 당첨! (4개 일치)")
    elif len(lotto_numbers.intersection(winning_numbers)) == 3 or (len(lotto_numbers.intersection(winning_numbers)) == 2 and lotto_numbers == winning_numbers) :
        print(f"{idx}번째 로또 복권: 5등 당첨! (3개 일치)")
    else:
        print(f"{idx}번째 로또 복권: 꽝")
    

# 당첨 번호 생성
winning_numbers, winning_bonus_number = generate_lotto_numbers()
print("당첨 번호:", winning_numbers, "보너스 번호:", winning_bonus_number)
lotto_list = []

# 100장의 로또 번호 생성하여 당첨 여부 판별
for idx in range(1, 101):
    lotto_numbers, lotto_bonus_number = generate_lotto_numbers()
    # lotto_list.append()
    # (복권번호, 보너스번호) 튜플로 저장
    # [(0,0), (0,0), (,)] 등으로 100장 복권을 저장
    lotto_list.append((lotto_numbers, lotto_bonus_number))\
    
#     # 저장된 100장의 로또 번호 출력
# for idx, (lotto_numbers, lotto_bonus_number) in enumerate(lotto_list, start=1):
#     print(f"{idx}번째 로또 복권 - 복권 번호: {lotto_numbers}, 보너스 번호: {lotto_bonus_number}")


for idx in range(1, 101):
    # 100장 복권을 가져와 당첨번호와 비교
    check_winner(idx,lotto_numbers,lotto_bonus_number,winning_numbers,winning_bonus_number)