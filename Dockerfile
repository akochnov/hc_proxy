# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install the required Python packages
RUN pip install --no-cache-dir Flask requests python-dotenv

# Expose port 3452 for the Flask app
EXPOSE 3452

# Define environment variable
ENV FLASK_APP=proxy_server.py

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]