FROM amazonlinux:2

# Install AWS CLI V2, Python3, and additional tools
RUN yum install -y unzip less python3 curl && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "/tmp/awscliv2.zip" && \
    unzip /tmp/awscliv2.zip -d /tmp && \
    /tmp/aws/install && \
    rm -rf /tmp/aws* && \
    pip3 install boto3

COPY run_aws.py /run_aws.py

RUN chmod +x /run_aws.py

CMD ["python3", "/run_aws.py"]
