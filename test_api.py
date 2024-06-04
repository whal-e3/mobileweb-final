import requests

HOST = 'http://127.0.0.1:8000'
res = requests.post(HOST + '/api-token-auth/', {
            'username’:’kiokahn',
            'password’:’eugene512',
        },{
            'Accept' : 'application/json'
    }
    )

res.raise_for_status()
token = res.json()['token']
print(token)

# 인증이 필요한 요청에 아래의 headers를 붙임
headers = {'Authorization' : 'JWT ' + token, 'Accept' : 'application/json'}

# Post Create
data = {
    'title' : '제목 by code', 
    'text' : 'API내용 by code', 
    'created_date' : '2024-06-07T18:34:00+09:00', 
    'published_date' : '2024-06-07T18:34:00+09:00'
}

file = {'image' : open('/Users/kiokahn/Pictures/camera_a7-2/20231215/12440101/DSC01276.JPG', 'rb')}
res = requests.post(HOST + '/api_root/Post/', data=data, files=file, headers=headers)
print(res)
print(res.json())

#token b181ce4155b7413ebd1d86f1379151a7e035f8bd
'''
curl -X POST -S -H 'Accept: application/json' -F "username=kiokahn" -F "password=eugene512"  http://127.0.0.1:8000/api-token-auth/

curl -X POST -S -H 'Accept: application/json'  -u "kiokahn:eugene512" -F "author=1" -F "title=curl 테스트" -F "text=API curl로 작성된 AP 테스트 입력 입니다." -F "created_date=2024-06-03T18:34:00+09:00" -F "published_date=2024-06-03T18:34:00+09:00" -F "image=@/Users/kiokahn/Pictures/camera_a7-2/20231215/12440101/DSC01276.JPG;type=image/jpg" http://127.0.0.1:8000/api_root/Post/

curl -X POST -S -H "Authorization: JWT b181ce4155b7413ebd1d86f1379151a7e035f8bd" -F "author=1" -H 'Accept: application/json' -F "title=curl 테스트" -F "text=API curl로 작성된 AP 테스트 입력 입니다." -F "created_date=2024-06-03T18:34:00+09:00" -F "published_date=2024-06-03T18:34:00+09:00" -F "image=@/Users/kiokahn/Pictures/camera_a7-2/20231215/12440101/DSC01276.JPG;type=image/jpg" http://127.0.0.1:8000/api_root/Post/
'''