FROM golang:1.20
RUN go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
COPY run_nuclei.py /run_nuclei.py
RUN chmod +x /run_nuclei.py
CMD ["python", "/run_nuclei.py"]
