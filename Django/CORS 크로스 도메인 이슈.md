# Django CORS 크로스 도메인 이슈



API서버를 만드는 도중에 jwt를 쿠키에 담아 전달하는 도중에 CORS 오류가 나와 검색을 통해 정리한 문서다.



CORS는 도메인 혹은 포트가다른 서버의 자원을 요청하는 방법인데, javascript를 통해 통신 할 때, 다른 도메인을 가진 서버의 url을 호출해 데이터를 통신하는 경우에 CORS 보안 이슈가 발생한다.

javascript의 동일 출처 정책으로 인한 이슈인데, 도메인이 다른 서버로부터 요청을 받으면 보안 문제로 간주한다는 것이다.

## 해결방법

외부 서버와 통신하는 요청 헤더에 cross origin http요청을 허가해서 접근을 가능하게 추가해주면 된다.

1.  Django-cors-headers를 설치 
2. response에 CORS헤더를 추가



주의할 점은 settings.py에서 Django CommonMiddleware, WhiteNoiseMiddleware와 같은 응답을 생성할 수 있는 미들웨어 전이어야한다.

**MIDDLEWARE 리스트의 최상단에 위치시켜준다.**



쿠키를 cross-site HTTP 요청에 담아주는 것이 목적이었으므로,

설정 파일(settings.py)에 CORS_ALLOW_CREDENTIALS에 대해 명시해준다.

`CORS_ALLOW_CREDENTIALS = True` 

CORS_ALLOW_CREDENTIALS를 설정해주지 않으면 프론트엔드는 쿠키에 대한 정보를 얻을 수 없게된다.