FROM python:3.10-slim

# Prevent Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1

# Prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy project files into the container
COPY . .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Set the default command to run the Django app with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]