#튜플
#시퀀스행, 변경불가 자료형


#튜플생성

t=(1,2,3)
print(t,type)

# () 를 생략해도 튜플로 인식
t= 1,2, 'python'
print(t,type(t))

#연결
t2=t+(3,4,5)
print("t2" ,t2)

#반복    : = 
print(t*3)

#언덱싱과 슬라이싱 가능
# t2에서 'python', 3,4 추출해 봅시다
print(t2[2:5])

#길이를 얻어옵시다
print("len", len(t2))

print("---------------------")
print("Packing^unpacking")
#packing unpacking
print("t2",t2)

a,b,c,d,e,f =t2
print("unpacking" , a,b,c,d,e,f)

# 튜플의 요소보다 변수의 수가 적을때
'''
a , b =t2   #value error
print(a,b)
'''

a,*b=t2
print(a, b)

a,b,*c,d,e=t2
print(a,b,c,d,e)

