# Use the official Python image as the base image for the build stage
FROM python:3.10-slim as builder

# Set the working directory
WORKDIR /app

# Copy only requirements.txt to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Now create a second stage for the production image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages/

# Copy the application code
COPY . .

# Expose port 8000
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "your_module_name:app", "--host", "0.0.0.0", "--port", "8000"]