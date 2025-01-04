FROM ubuntu:22.04
RUN apt-get update && apt-get install -y nmap curl
COPY run_nmap.py /run_nmap.py
RUN chmod +x /run_nmap.py
CMD ["python3", "/run_nmap.py"]
