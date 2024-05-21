import os
from pathlib import Path
print(f'현재경로 : {os.getcwd()}')
new_파일쓰기 = "H"
os.chdir(new_파일쓰기)
print(f'바뀐 현재경로 : {os.getcwd()}')

# 파일 생성 및 쓰기
with open('example.txt', 'w') as file:  # 현재 경로에 파일이 생성되므로 항상 현재경로 신경쓸것!
    file.write("Hello, World!\n")       # file변수는 open
    file.write("This is a new line.\n")
    # file.write_text() 메소드가 없다

print("File created and written successfully.")
path = Path('example.txt')
with path.open('example.txt', 'a'):
    path.write_text('path 객체를 사용한 쓰기')

# 파일에 내용 추가하기
with open('example.txt', 'a') as file:
    file.write("Adding a new line.\n")
    file.write("Appending another line.\n")

print("Content appended to the file successfully.")

# 새로운 파일 생성하기
try:
    with open('new_file.txt', 'x') as file:
        file.write("This is a newly created file.\n")
    print("New file created and written successfully.")
except FileExistsError:
    print("File already exists.")