# 문자형 
#시퀀스형
#변경불가(immutable) 자료형
str1 = "Life is too short, you need python"
str2 = " wlcom python"
# 타입 판별
print(type(str1), type(str2))
#instance 판별
#print(str1, " str?: "  , isinstance(str1, str))

#여러줄 문자열
multiline = """
java
python
linux
"""
print(multiline)

#문자열 :"" ' ' 
print("I said yes")
#solution
print('I said "yes"')
#solution 2   \ 사용
print("I said \"yes\"")
#문자열의 인덱싱 
print(len(str1))   # 길이   : len
print(str1[5])   #인덱스 접근 기능 : 시퀀스형
print(str1[5:7]) # 슬라이싱
#print(str[5:])   # 생략시 끝가지
print(str1[:6]) # 처음부터
print(str1[:]) #시퀀스 전체



#str[0] = '1'   # 변경 안됨  : Type Error 

#대소문자 관련
#    upper() : 전체 대문자
#    lower() : 전체 소문자
#    swapcase() : 대 < = > 소 문자 전하ㄴ
#    capitalize() : 첫문자 대무나자
#    title()      : 각 단어 첫글자 대문자 
str3 = str1.lower().title()

print(str3)

# 검색 관련
print(str1.count("short"))   # 검색어 개수
print("find()", str1.find("python")) # 문자열 내검사
print("find()", str1.find("life",6)) # 6 번 인덱스 부터 life 검색 
print("rfind()", str1.rfind("Life")) # 우측부터 검색

print("find() 없는 값: " , str1.find("java"))
#찾는 내용ㅇ 없으면 -1 반환
print("index(): ",  str1.index("python"))
#print("index() 없는값 : " , str1.index("java"))   # 인덱스 없으면 valueError 

#분리와 결합
print(" ========== 분리, 결합 =======")
s= " java and python"
lines = '''\
java
python
linux
oracle '''

num = input("정수를 입력하세요")
result = num *2
print("result", result)

# 분리 ㅣ split  #문자 ㅣㄱ준 분리
print(s.split())# 공백 문자 기준 분리
print(s.split(" and ")) # 특정 문자열 기준분리

# 합치기
t= s.split("and ")
print(t)
#  L : 문자를 넣어서 합쳐
print(":".join(t))

s2 = "abc:def:ghi:jkl"
# : 기준  2개만 분리
print(s2.split(":", 2)) 
print(s2.rsplit(":", 2))

# splitline() 개행 문자 기주느 분리
print(lines.splitlines())
'''
result= int(num)*2
print("result:",result)
'''
if num.insight():
num.int(num) *2
else:
    result = "정수가 아니에요"

print("result", result)
