# Use the official Python 3.9 Alpine-based image as the base  , Alpine is a lightweight Linux distribution (smaller image size)
FROM python:3.9-alpine

# Set the working directory inside the container to /app
WORKDIR /app

# Copy all files from the current directory (on host) to /app (in container)
COPY . .

# Install the Flask package using pips IT runs during the image build process
RUN pip install flask

# Inform Docker that the container listens on port 5000
EXPOSE 5000

# Set an environment variable named NAME with value "World"
ENV NAME World

# Uses Python to execute app.py (your Flask application)
CMD ["python", "app.py"]