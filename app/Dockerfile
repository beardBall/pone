FROM debian:latest
# FROM linuxcontainers/debian-slim:latest
# WORKDIR /usr/src/app

EXPOSE 8000
ENV HOST=0.0.0.0
WORKDIR /app


RUN apt-get update 
RUN apt-get install -y python3 python3-pip python3-venv pkg-config curl default-libmysqlclient-dev build-essential
# RUN python3 -m pip install --upgrade pip

# RUN python3 -m venv .venv
# RUN sh ./.venv/bin/activate



RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

COPY . /app

# RUN chmod +x wait-for-it.sh



CMD python3 exampleapp.py
# CMD ["python3", "./one.py"]
# CMD ["python3", "/usr/src/app/one.py"]
# CMD ["python3", "/usr/src/app/app.py"]


# # This Dockerfile sets up a simple Python web application using Flask.
# # It starts from the latest Debian image, installs Python and pip, and then installs the required packages listed in requirements.txt.
# # Finally, it exposes port 8000 and runs the application using Python.
# # To build the Docker image, run:






#     # using ubuntu LTS version
# FROM ubuntu:20.04 AS builder-image

# RUN apt-get update && apt-get install --no-install-recommends -y python3 python3 python3-venv python3-pip python3-wheel build-essential && \
#    apt-get clean && rm -rf /var/lib/apt/lists/*


# WORKDIR /usr/src
# COPY . .

# # create and activate virtual environment
# RUN python3 -m venv /opt/venv
# ENV PATH="/opt/venv/bin:$PATH"

# # install requirements
# # COPY requirements.txt .
# RUN pip3 install --no-cache-dir -r requirements.txt

# FROM ubuntu:20.04 AS runner-image
# RUN apt-get update && apt-get install --no-install-recommends -y python3 python3-venv && \
#    apt-get clean && rm -rf /var/lib/apt/lists/*

# COPY --from=builder-image /opt/venv /opt/venv

# # activate virtual environment
# ENV VIRTUAL_ENV=/opt/venv
# ENV PATH="/opt/venv/bin:$PATH"

# EXPOSE 8000

# CMD ["python3", "/usr/src/one.py"]
