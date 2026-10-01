# Use a lightweight Python 3.9 image as the base environment
FROM python:3.9-slim

# Set /app as the working directory inside the container
WORKDIR /app

# Copy the dependency list into the container
COPY requirements.txt .

# Install the Python packages required by the Flask application
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application files into the container
COPY . .

# Document that the Flask application uses port 5000
EXPOSE 5000

# Start the Flask application and allow connections from outside the container
CMD ["flask", "--app", "hello", "run", "--host=0.0.0.0"]