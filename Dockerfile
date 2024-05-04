
FROM python:3.12-slim


WORKDIR /app


RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    # This package provides the libgthread-2.0.so.0
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*


RUN pip install pipenv


COPY Pipfile Pipfile.lock ./

RUN pipenv install --deploy --system


COPY . /app


EXPOSE 8000


ENV TEST_SECRET "your_default_secret_key_here"


CMD ["pipenv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
