FROM python:3.9
WORKDIR /Exercise1
ADD src/ex1_0_setup.py .
ADD list_packages.sh .
ADD list_packages.sh /Exercise1/list_packages.sh
RUN pip install matplotlib plotly_express pandas numpy dash sklearn
RUN chmod +x /Exercise1/list_packages.sh

# # Dockerfile
# FROM python:3.9

# WORKDIR /Exercise1

# ADD src/ex1_0_setup.py .

# RUN pip install matplotlib plotly_express pandas numpy dash sklearn

# CMD ["python", "./ex1_0_setup.py"]




