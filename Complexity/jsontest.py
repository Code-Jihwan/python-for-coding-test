import json

a = dict()
a['id'] = 1
a['name'] = 'pie'
a['hobby'] = ['game', 'tv', 'work']
a['test'] = True

#저장할 파일 경로(이름)
file_path = '/Users/joojihwan/Desktop/python_for_coding_test/Complexity/jsontest.json'

with open(file_path, 'w', encoding='UTF-8') as fp:      #쓰기 모드 접근
    json.dump(a, fp, indent=4)    #파이썬 오브젝트(a), 파일객체(fp), indent 옵션으로 들여쓰기 가능
 
#json 테스트 코드.