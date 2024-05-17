# a = list(input())
# if a == a[::-1]:
#     print(1)
# else:
#     print(0)

# 문자 입력받고 대소문자 섞여있으니 하나로 통일해주고 그안에서 돌면서 각자 몇개인지 볼건데 중복으로 볼 필요없으니까 중복없이 만들고 각자 몇개인지 세고 가장 많은걸 출력
# 근데 이제 각자 몇개인지 센다음 가장 많은게 어떤 문자인지,,, 어떻게 도출하지? 딕셔너리 써야하나,,,

a = input()
b = set(a.lower())
c =[]
for i in b:
    c.append(a.count(i))

if len(max(c))==1:
    i
    print()
elif 