# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a non-root user
RUN useradd -ms /bin/bash link_spider

# Set the user to the non-root user
USER link_spider

# Create a working directory
WORKDIR /home/link_spider/app

# Copy the current directory contents into the container 
COPY  --chown=link_spider:link_spider . ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make the entrypoint.sh script executable
RUN chmod +x entrypoint.sh

# Run the entrypoint.sh script as the entry point
ENTRYPOINT ["./entrypoint.sh"]

