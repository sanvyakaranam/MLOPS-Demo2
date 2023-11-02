FROM python:3.10.11-slim-buster

RUN python -m pip install --upgrade pip
COPY . /ml_model
WORKDIR  /ml_model
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# CMD ["python", "app.py"]
EXPOSE 8000
ENTRYPOINT ["uvicorn"]
CMD ["app:app", "--reload", "--host", "0.0.0.0"]
# RUN uvicorn app:app --reload
# RUN uvicorn app:app --reload --workers 1 --host 0.0.0.0 --port 8000
