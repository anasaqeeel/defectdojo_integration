FROM amazonlinux:2

# Install AWS CLI V2 or just V1
RUN yum install -y unzip less python3 curl && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "/tmp/awscliv2.zip" && \
    unzip /tmp/awscliv2.zip -d /tmp && \
    /tmp/aws/install && \
    rm -rf /tmp/aws* 

COPY run_aws.sh /run_aws.sh
RUN chmod +x /run_aws.sh

CMD ["/run_aws.sh"]
