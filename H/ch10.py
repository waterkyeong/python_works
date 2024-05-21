from pathlib import Path
import os
print(os.getcwd()) #현재 작업 디렉토리 확인
new_pi_digits = "H" # 이동할 디렉토리 경로 설정 설정할때 명심할것 - "폴더"로만 이동가능! 파일을 읽진 않는다.
os.chdir(new_pi_digits) #디렉토리 변경
print(os.getcwd()) # 바뀐 디렉토리 확인
# 이러한 과정을 거치는 이유는 vscode는 최근에 연 폴더에서 파일을 찾기때문. 즉 난 python_works를 제일 최근에 열어서 거기서 여기까지 경로를 설정해주는것!


# path = Path('pi_digits.txt')
# contents = path.read_text()
# contents = contents.rstrip().lstrip()
# lines = contents.splitlines()
# pi_string = ''

# for line in lines:
#     line = line.lstrip()
#     pi_string += line
#     print(f'각 줄은 = {pi_string}')

# ================================================================

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
print(f'줄 수 : {len(lines)}')
for line in lines:
    # print(f'각줄 : {line}')
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

bth = input('enter ur bth mmddyy:')
if bth in pi_string:
    print('u have')
else:
    print('u dont have')