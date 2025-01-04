FROM node:18

# 1) Install Python3, make, g++, and python-is-python3 for symlinks
RUN apt-get update && apt-get install -y \
    python3 \
    python-is-python3 \
    make \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# 2) Install Bearer CLI globally
RUN npm install -g @bearer/bearer-cli --unsafe-perm

COPY run_bearer.sh /run_bearer.sh
RUN chmod +x /run_bearer.sh

CMD ["/run_bearer.sh"]
