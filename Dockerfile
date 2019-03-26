FROM vulhub/python:3.6

MAINTAINER evilys <evilys@foxmail.com>

RUN set -ex \
    && apt-get update \
    && pip install -U pip \
    && pip install "tornado==5.1.1" \
    && rm -rf /var/lib/apt/lists/*


COPY index.py /usr/src/
COPY flag.py /usr/src/

WORKDIR /usr/src/

CMD ["python", "index.py"]