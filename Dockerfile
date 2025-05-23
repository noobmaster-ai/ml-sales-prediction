# Python image
FROM python:3.9-slim

# Set the working directory in container
WORKDIR /app

# Copy source code and dependencies
COPY . /app

# Install necessary python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app will run on
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]
