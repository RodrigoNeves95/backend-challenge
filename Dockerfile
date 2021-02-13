FROM python:3.8.2

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install joblib
RUN pip install uvicorn
RUN pip install loguru
RUN pip install fastapi

COPY . ./

ENV PYTHONPATH app
ENTRYPOINT ["python", "app/main.py"]
