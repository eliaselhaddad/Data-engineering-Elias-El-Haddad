# Use the official Python 3.9 image from the Docker Hub
FROM python:3.9

# Set the working directory to /Exercise1-Docker
WORKDIR /Exercise1-Docker

# Copy the current directory contents into the container at /Exercise1-Docker
COPY . .

# Update pip
RUN pip install --upgrade pip

# Install the required packages
RUN pip install matplotlib plotly_express pandas numpy dash sklearn

# Run ex1_0_setup.py when the container launches
CMD ["python", "./src/ex1_0_setup.py"]

