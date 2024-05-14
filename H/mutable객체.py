def modify_string(s):#immutable 객체
    s = s+'world'
    print(f'함수내 출력={s}')
    
st ='hello'
modify_string(st) #string을 전달함으로
print(st)


def modify_string(number):#immutable 객체
    number = number+10
    print(f'함수내 출력={number}')
num = 10
modify_string(num) #string을 전달함으로
print(f'함수 종료 후 출력={num}')