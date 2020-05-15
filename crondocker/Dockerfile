FROM muyajil/crondocker:latest

# Install python
RUN apt-get update && apt-get install -y python3 python3-pip borgbackup rsync

# Install python dependencies
RUN pip3 install retry requests

# Add files to be run using crontab
COPY ./public_ip_monitor.py /public_ip_monitor.py
COPY ./backup.sh /backup.sh
RUN chmod +x /backup.sh