FROM python:3.7
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY Pipfile /usr/src/app/Pipfile
COPY Pipfile.lock /usr/src/app/Pipfile.lock
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
COPY . .