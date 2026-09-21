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
http://127.0.0.1:8000



