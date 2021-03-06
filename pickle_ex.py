# 피클 사용을 위해 pickle을 임폴트
import pickle

def pwrite01():
    f = open("./sample/players.bin", "wb") #  꼭 바이너리 모드
    data = {"baseball": 9 } 
    pickle.dump(data,f)
    f.close()

#pwrite01()

def pread01():
    f = open ("./sample/players.bin", "rb") # b 모드
    data = pickle.load(f)
    f.close()
    print(data, type(data))

#pread01()

def pwrite02():
    # 복수의 객체 저장
    with open("./sample/players.bin", "wb") as f:
        pickle.dump({"baseball":9},f,1) # protocol 1
        pickle.dump({"basketball" : 5 },f ,2) # protocol2 
        pickle.dump({"soccer": 11 }, f, pickle.HIGHEST_PROTOCOL  )

pwrite02()

def pread02():
    # 복수의 객체 읽기
    with open ("./sample/players.bin","rb") as f:
        print(pickle.load(f))
        print(pickle.load(f))
        print(pickle.load(f))
        print(pickle.load(f))

#pread02() # eof 오류



def pread03():
    # 복수의 객체 읽기
    with open ("./sample/players.bin","rb") as f:
        data_list = []
        while True:
            try:
                data=pickle.load(f)
            except EOFError:
                break

            data_list.append(data)

        print(data_list)

pread03()

