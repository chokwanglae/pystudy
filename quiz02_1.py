# 정수 입력 받아
while True:
    num = input("Enter a number: ")

    if num.isdigit:
        break
    
        print("정수가 아닙니다. 다시 입력하세요")

total = 0
to = int(num)
    
for i in range(1,to +1):
    if i%3 == 0:
        total+= i
        
print("1부터 {} 까지 3의 배수 합= {}".format((to,total)))



