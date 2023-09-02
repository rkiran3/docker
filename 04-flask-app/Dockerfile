FROM python:3.11-slim

# allow statements and log messages to immediately appear in logs
ENV PYTHONUNBUFFERED True

ENV PORT 5000

# Copy local code to container image
ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . ./

# Install dependencies
# RUN pip install Flask gunicorn python-dotenv
RUN pip install -r requirements.txt

# Run the web service on container startup.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
