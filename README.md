Check target site if it's alive.
======
Usage:
docker run -it --rm -e MAIL_TO=XXX -e MAIL_USER=XXX -e MAIL_PASSWD=XXX \
    -e TARGET=XXX -e SMTP_HOST=XXX -e INTERVAL=60 tsutomu7/check-alive
