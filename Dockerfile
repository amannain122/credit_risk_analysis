# Use an official Python runtime (Python 3.10) as a base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Streamlit will run on (default is 8501)
EXPOSE 8501

# Set the command to run the Streamlit app when the container starts
CMD ["streamlit", "run", "src/app.py"]
