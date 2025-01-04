FROM ubuntu:22.04
RUN apt-get update && apt-get install -y nikto
COPY run_nikto.sh /run_nikto.sh
RUN chmod +x /run_nikto.sh
CMD ["/run_nikto.sh"]
