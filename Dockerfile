# Inherit from the Python Docker image
FROM python:3.7

RUN pip3 install pandas
RUN pip3 install configobj
RUN pip3 install matplotlib


# Copy the source code to app folder
COPY ./neo4j_health.py /app/

# Change the working directory
WORKDIR /app/

# Set "python" as the entry point
ENTRYPOINT ["python3","./neo4j_health.py"]
