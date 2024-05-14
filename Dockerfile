# Use the official Python image as base
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install required Python dependencies
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Specify the command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
