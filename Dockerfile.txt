FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    gfortran \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN pip install --upgrade pip setuptools wheel build
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 10000
CMD ["streamlit", "run", "langchain.py", "--server.port=10000", "--server.address=0.0.0.0"]
