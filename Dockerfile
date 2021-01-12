FROM python:3-alpine

RUN apk add --no-cache tzdata
ENV TZ 'Asia/Shanghai'

# 设置 python 环境变量
ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
COPY . /app

RUN ./manage.py migrate && ./manage.py collectstatic --noinput


ENV DJANGO_DEBUG ''
ENV PORT 8000
CMD [ "gunicorn", "-w 4", "mysite.wsgi" ]