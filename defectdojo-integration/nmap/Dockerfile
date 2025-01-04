FROM ubuntu:22.04
RUN apt-get update && apt-get install -y nmap curl
COPY run_nmap.sh /run_nmap.sh
RUN chmod +x /run_nmap.sh
CMD ["/run_nmap.sh"]
