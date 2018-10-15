
FROM alpine:3.8

RUN apk --no-cache add py-pip curl

RUN pip install flask==1.0.2 requests giphypop

ADD / /app

WORKDIR /app

CMD python app.py