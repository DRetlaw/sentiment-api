https://chatgpt.com/c/6ab0fd1d-2e60-83e8-a1e1-f38f7812e6c4

mkdir sentiment-api
cd sentiment-api

mkdir app
touch app/__init__.py
touch app/main.py
touch requirements.txt
touch Dockerfile
touch .dockerignore
touch README.md

python3 -m venv .venv
source .venv/bin/activate

python3 -m venv .venv
source .venv/bin/activate


pip install transformers torch

python test_model.py

Add code to main.py (it's a emplty file till now)

pip install fastapi uvicorn transformers torch

uvicorn app.main:app --reload
http://127.0.0.1:8000/docs


CURL
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"I absolutely love this product!"}'

Add in requirements.txt
fastapi
uvicorn[standard]
transformers
torch


Add in .dockerignore
.venv
__pycache__
*.pyc
.git
.gitignore
.env

Add in Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
EXPOSE 7860
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]


docker build -t sentiment-api .

docker images

