FROM golang:1.20
RUN go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
COPY run_nuclei.sh /run_nuclei.sh
RUN chmod +x /run_nuclei.sh
CMD ["/run_nuclei.sh"]
