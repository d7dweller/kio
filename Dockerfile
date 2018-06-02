FROM python:alpine

LABEL maintainer="contact@khris.io"

COPY . /builder

WORKDIR /builder

RUN apk update && apk upgrade && apk add make
RUN pip install -r requirements.txt

CMD [ "make", "html" ]

