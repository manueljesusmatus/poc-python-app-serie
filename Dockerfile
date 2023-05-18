# SETTINGS
FROM python:3.9.16-alpine
LABEL maintainer="mmatush <mmatushdeveloper@gmail.com>"
WORKDIR /app
ENV TZ=America/Santiago

# DEPENDENCIES
RUN python -m pip install --upgrade pip
RUN pip install beautifulsoup4
RUN pip install mysql-connector-python
RUN pip install envparse

# FILES
COPY crontab /etc/cron.d/crontab
ADD . /app

# INSTRUCTIONS
RUN crontab /etc/cron.d/crontab
CMD ["/usr/sbin/crond", "-f"]