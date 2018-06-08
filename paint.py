#point 를 임포트 하여 사용
from point import Point 

p1 = Point(10,10)
print("repr:",repr(p1))
print("instance count:", Point.instance_count)
p2 = Point(20,20)
print("p2", p2)
print("repr:",repr(p2))


print("instance count : " , Point.instance_count)

# repr 메세지 확인

p2_copy= eval(repr(p2))
print("p2_copy:", p2_copy)

