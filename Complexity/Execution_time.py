import time

from numpy import array
from prometheus_client import Summary
start_time = time.time()  #측정 시작 (현재시간 반환에서 start_time 넣음.)

#프로그램 소스코드 작성
array = [2, 0, 8, 4, 7]   #5개의 데이터(N = 5)
summary = 0               #합계를 저장할 변수

#모든 데이터를 하나씩 확인하며 합계를 계산
for i in array:
  summary += i

print(summary)            #결과출력

end_time = time.time()    #측정 종료
print("Time :", end_time - start_time)  #수행 시간 출력 (계산해서)