# Inherit from the Python Docker image
FROM python:3.7

RUN pip3 install pandas
RUN pip3 install configobj
RUN pip3 install matplotlib
RUN pip3 install fpdf
RUN pip3 install PyPDF2

#RUN echo "export JAVA_HOME=/usr/lib/jvm/java-11-oracle" >> ~/.bashrc

# Install OpenJDK-11
RUN apt-get update && \
apt-get install -y openjdk-11-jdk && \
apt-get install -y ant && \
apt-get clean;

# Fix certificate issues
RUN apt-get update && \
apt-get install ca-certificates-java && \
apt-get clean && \
update-ca-certificates -f;
# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

#expose 7617

# Copy the source code to app folder
COPY nj_perf /app/
RUN mkdir -p /app/bin
COPY bin/*  /app/bin/
#ADD bin ${HOME}/bin


# Change the working directory
WORKDIR /app/

# Set "python" as the entry point
ENTRYPOINT ["python3","./nj_perf"]
#CMD echo "Hello world"
~
