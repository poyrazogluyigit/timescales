#syntax=docker/dockerfile:1
FROM python:3.10

# add zenoh private repo to apt sources list
RUN echo "deb [trusted=yes] https://download.eclipse.org/zenoh/debian-repo/ /" | tee -a /etc/apt/sources.list > /dev/null
RUN apt-get update


# install cyclonedds
RUN apt-get install -y git cmake gcc

RUN git clone https://github.com/eclipse-cyclonedds/cyclonedds.git
RUN cd cyclonedds; \
mkdir build; \ 
cd build; \
cmake -DCMAKE_INSTALL_PREFIX=/cyclonedds -DBUILD_EXAMPLES=OFF ..; \
cmake --build . --parallel; \
cmake --build . --target install

ENV PATH="${PATH}:/cyclonedds/bin"

RUN apt-get install -y zenoh

WORKDIR /home/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN CYCLONEDDS_HOME="/cyclonedds" pip install git+https://github.com/eclipse-cyclonedds/cyclonedds-python


# now run zenoh daemon
RUN zenohd >> /dev/null &

