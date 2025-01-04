FROM python:3.10
RUN pip install bandit
COPY run_bandit.sh /run_bandit.sh
RUN chmod +x /run_bandit.sh
CMD ["/run_bandit.sh"]
