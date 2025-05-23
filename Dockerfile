# Python image
FROM python:3.9-slim

# Set the working directory in container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install necessary python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app will run on
EXPOSE 8080

# Command to run the Flask app
RUN python app.py
