FROM python:3.9-buster AS compile-image
WORKDIR /opt/app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .

RUN pip install -r requirements.txt

FROM python:3.9-slim AS build-image
COPY --from=compile-image /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

ENV PYTHON_PATH=/opt/app/src
WORKDIR /opt/app/src
COPY . /opt/app

EXPOSE 9000
CMD ["python", "/opt/app/src/main.py"]
