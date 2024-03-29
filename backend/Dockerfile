# 파이썬 버젼 지정
FROM python:3.12
# 관리자? 지정
LABEL maintainer = 'DogGoDev'
# 파이썬이 실행될때 버퍼링을 비활성화하는 환경변수 지정
ENV PYTHONUNBUFFERED 1
# 파일, 폴더를 도커 내로 복사
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
COPY ./scripts /scripts

# /app 경로에서 실행
WORKDIR /app 
# 8000 포트 지정
EXPOSE 8000
# DEV 개발환경에서 실행여부
ARG DEV=true
# 실행 시킬 스크립트?코드
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    apt-get update && \
    if [ $DEV = "true" ] ; \
        then echo "===THIS IS DEVELOPMENT BUILD===" && \
        /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    # chmod : change mode, chown : change owner
    chown -R django-user:django-user /vol && \
    chown -R django-user:django-user /app && \
    # 폴더에 대한 접근 권한부여 
    chmod -R 755 /vol && \
    chmod -R 755 /app && \
    # 권한 적용
    chmod -R +x /scripts

# 환경변수
ENV PATH="/scripts:/py/bin:$PATH"

# 유저생성
USER django-user

CMD ["run.sh"]
