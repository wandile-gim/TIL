# [Docker] Docker Image



## 도커 이미지?

도커에서 서비스 운영에 필요한 프로젝트(서버 프로그램, 소스코드, 라이브러리)등을 Image로 묶어 만든다.

더이상의 의존성 파일을 추가적으로 컴파일 하거나 설치하지 않고 정형화된 상태로 만들어진 파일을 의미한다. 



도커에서 이미지를 만들기 위해 Dockerfile을 정의할 필요가 있다. 이미지는 필수이며 이미지와 컨테이너가 도커의 전부라고 볼 수 있다.



Dockerfile에서 이미지를 정의하기 위해 알아두어야 할 명령어를 정리해보면,



### 명령어

#### `COPY` . . 

```dockerfile
COPY Host file system Image container file system
```

- 이미지를 빌드한 디렉터리의 모든 파일을 컨테이너의 `app/` 디렉터리로 복사

```dockerfile
WORKDIR app/
COPY . .
```

첫 번째로 올 경로는 Host file system이다. 즉 이미지로 올릴 파일의 경로를 말하고나머지는 그 파일을 저장해야할 이미지 내부의 경로다.

지정하지 않고 .로 두면 현재 경로의 모든 파일을 포함하고 ./를 입력하면 현재 경로를 의미한다.

모든 이미지와 이미지를 기반으로 생성된 모든 컨테이너에는 자체적인 로컬 머신과 분리된 자체 내부 파일 시스템이 있다.루트 폴더의 사용보다 사용자 폴더를 생성하는 것이 좋다.



#### `WORKDIR`

WORKDIR '경로'

도커 컨테이너의 작업 디렉토리를 선택하는 명령어 이후에 실행할 명령어에 속하는 파일들의 기준이 된다.

```dockerfile
WORKDIR <이동할 경로>
```

- `/usr/app`으로 작업 디렉터리 전환

```dockerfile
WORKDIR /usr/app
```



#### `RUN` 

RUN 명령어는 도커 컨테이너 및 이미지의 작업 디렉토리에서 실행된다. 실행하는 디렉토리를 기준으로 파일을 실행함. 

**디폴트는 파일 시스템의 루트 폴더**

- 커맨드 실행

```dockerfile
RUN ["<커멘드>", "<커멘드>"]
RUN <커멘드>	
```

- 디렉터리 생성, 의존성 설치

```dockerfile
RUN mkdir '경로'
RUN pip install <?>
```



#### `CMD`

RUN과 달리 이미지를 기반으로 컨테이너가 시작될 때 실행된다. 

```dockerfile
CMD ["<커맨드>", "<커맨드>"]
```



#### `EXPOSE`

```dockerfile
EXPOSE <포트>
```

도커는 로컬 환경과 독립적으로 분리되어 있다. 또한 자체적 컨테이너 내부의 네트워크도 존재한다. 컨테이너 내부의 서버에서 포트를 수신할 때 컨테이너는 그 포트를 로컬에 노출시키고 있지 않는다. EXPOSE를 통해 특정 포트를 로컬에 노출하고 싶다는 것을 도커에 알린다.

프로토콜은 TCP와 UDP 중 선택할 수 있는데 지정하지 않으면 TCP가 기본값으로 사용된다.

 `EXPOSE` 명령문으로 지정된 포트는 해당 컨테이너의 내부에서만 유효하기 때문에 호스트는 `docker run` 커맨드와 `-p` 옵션을 통해 호스트 컴퓨터의 특정 포트를 포워딩(forwarding)시켜줘야 한다.

- 80/TCP 

```dockerfile
EXPOSE 80
```

- 9999/UDP

```dockerfile
EXPOSE 9999/udp
```

```dockerfile
FROM python:3.9.13
# python 3.7.7 버전의 컨테이너 이미지를 base이미지

LABEL WON JAE GIM <dnjswo6066@gmail.com>
# Docker의 컨테이너를 생성 및 관리 하는 사람의 정보를 기입해줍니다.

RUN mkdir /root/.ssh/

ADD imdb_docker /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa

RUN touch ~/.ssh/known_hosts
RUN ssh-keyscan github.com >> ~/.ssh/known_hosts

ENV PYTHONUNBUFFERED 1

RUN git clone git@github.com:Oops-nana/udemy-django-basic.git /src

#requirements 카피해서 실행
RUN python -m pip install --upgrade pip

WORKDIR /src/imdb-django

RUN pip install -r requirements.txt

VOLUME /src

#포트 노출
EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 127.0.0.1:8000

```

