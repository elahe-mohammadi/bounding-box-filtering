# Use the Alpine-based Python image
FROM python:3.9.5-alpine

# Set the working directory for the application
WORKDIR /app

# Copy the application code to the container
COPY app.py requirements.txt data.txt ./

RUN apk update && apk add python3-dev musl-dev gcc libc-dev 
RUN apk add --no-cache g++ make libffi-dev openssl-dev

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the application will listen on
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]