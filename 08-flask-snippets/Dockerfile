FROM python:3.11-slim

# allow statements and log messages to immediately appear in logs
ENV PYTHONUNBUFFERED True

# Copy local code to container image
ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . ./

# Install dependencies
RUN pip install -r requirements.txt

EXPOSE 5000

# Run the web service on container startup.
# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
# CMD exec gunicorn --bind :5000 --workers 1 --threads 8 --timeout 0 main:app

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app", "--timeout", "1000", "--workers=1", "--log-level", "debug" ]
