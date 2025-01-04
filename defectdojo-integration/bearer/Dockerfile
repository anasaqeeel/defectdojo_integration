FROM node:18

# Install Python3, pip, make, g++, and symlinks for Python3
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python-is-python3 \
    make \
    g++ \
    && rm -rf /var/lib/apt/lists/*

RUN npm install -g @bearer/bearer-cli --unsafe-perm

RUN pip install requests

COPY run_bearer.py /run_bearer.py
CMD ["python3", "/run_bearer.py"]
