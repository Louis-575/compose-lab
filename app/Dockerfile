# Chosing container type
FROM python:3.12-slim

# Chosing directory
WORKDIR /app

# Copying requirements.txt to app dir and installing
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copying script to app dir
COPY main.py /app/main.py

# Exposing port and running program
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]
