# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements_server.txt .
RUN pip install --no-cache-dir -r requirements_server.txt

# Copy application code
COPY . .

# Create directory for database
RUN mkdir -p /app/data

# Expose port
EXPOSE 5001

# Set environment variables
ENV FLASK_APP=simple_pos.py
ENV FLASK_ENV=production
ENV PYTHONPATH=/app

# Run the application
CMD ["gunicorn", "--config", "gunicorn_config.py", "wsgi:app"]
