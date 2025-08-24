# Use an official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /redirect-service

# Copy your app files
COPY . .

# Install dependencies
RUN pip install flask

# Expose the port your app runs on
EXPOSE 8080

# Run the app
CMD ["python", "local-flask-web-redirect.py"]