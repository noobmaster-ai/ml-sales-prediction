FROM python:3.9-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and model
COPY . .

# Expose the Flask port
EXPOSE 8080

# Only one CMD — used to start the app at container runtime
CMD ["python", "app.py"]
