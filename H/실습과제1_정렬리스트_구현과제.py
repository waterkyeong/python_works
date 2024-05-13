# 구글 검색, chatGPT 사용하여 다음 코드를 완성 

import random

# 빈 리스트 생성
random_numbers = []

# 난수를 20개 생성하여 리스트에 추가
for _ in range(20):
    random_numbers.append(random.randint(1, 100))

# 저장된 리스트 출력
print(f"난수 생성 = {random_numbers}")
# s 다음에 숫자를 가진 변수들을 생성하여 리스트에 저장하는 예제

# 빈 리스트 생성
string_list = []

# s 다음에 숫자를 가진 변수들 생성하여 리스트에 추가: s1, s2, s3 등을 생성 
for i in range(1, 21):
   string_list.append(i)

# 저장된 리스트 출력
print(f"sno 리스트 = {string_list}")

students = string_list
scores = random_numbers

score_dic = { # //students, scores로 구성된 딕셔너리를 만든다 
    student: score for student, score in zip(students, random_numbers)
}

print(f"학번과 점수 딕셔너리={score_dic}")
# 점수를 기준으로 내림차순으로 정렬한 튜플 리스트 생성
sorted_scores = dict(sorted(score_dic.items(), key=lambda x: x[1]))

# 정렬된 튜플 리스트를 다른 딕셔너리에 저장
sorted_score_dic = sorted_scores.copy()

# 결과 출력
print(f"점수로 정렬된 딕셔너리= {sorted_score_dic}")
# 정렬된 튜플 리스트에서 상위 5개 추출하여 리스트로 저장
top_5_list = list(sorted_score_dic.items())[15:]
# 상위 5개 추출하여 딕셔너리로 저장
top_5 = dict(top_5_list)

# 결과 출력
print(f"상위 5개= {top_5}")
# 딕셔너리의 키-값 쌍을 튜플로 묶어 리스트에 추가
score_list = []
for key, value in score_dic.items():
    score_list.append((key, value))

# 결과 출력
print(f"리스트로 변환된 딕셔너리: {score_list}")
# 딕셔너리의 각 요소를 enumerate를 사용하여 변환
transformed_score_dic = {}
for index, (key, value) in enumerate(score_dic.items()):
    # Transform the elements as desired (for example, adding the index to the value)
    transformed_value = value + index
    # Add the transformed elements to the new dictionary
    transformed_score_dic[key] = transformed_value

# 결과 출력
print(f"변환된 딕셔너리: {transformed_score_dic}")