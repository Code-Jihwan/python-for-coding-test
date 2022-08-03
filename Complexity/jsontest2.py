import json

file_path = '/Users/joojihwan/Desktop/python_for_coding_test/Complexity/jsonfile.json'

with open(file_path, 'r') as fp:    #읽기모드 접근
  data = json.load(fp)    #파일객체(fp)   #data에 jsontest.json 에서 읽어온 데이터들이 딕션너리 형태로 저장

# print(data['pie'])
# 값 접근시 [키]를 통해서 접근

# dumps 함수로 콘솔에 json으로 읽은 파일 출력
print(json.dumps(data, indent=4))