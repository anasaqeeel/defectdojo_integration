FROM ubuntu:22.04
RUN apt-get update && apt-get install -y nikto
COPY run_nikto.py /run_nikto.py
RUN chmod +x /run_nikto.py
CMD ["python3", "/run_nikto.py"]
