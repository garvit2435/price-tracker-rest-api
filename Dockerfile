FROM python:3.9-slim
WORKDIR /app

COPY ./app /app/app
COPY requirements.txt /app/
COPY main.py /app/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

ENV MODULE_NAME="main"
ENV VARIABLE_NAME="app"
ENV PORT="8000"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
