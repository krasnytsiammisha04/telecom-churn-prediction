# Use the official lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install all required libraries
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for Jupyter Notebook
EXPOSE 8888

# Command to run Jupyter Notebook when the container starts
CMD ["jupyter", "notebook", "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root"]
