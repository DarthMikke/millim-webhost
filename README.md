# Millim webhost

## What is it?
HTTPD configuration serving as a file server, Python web app server and
reverse proxy.

## Installed mods
- Proxy & reverse proxy
- WSGI
- SSL
- Rewrite

## File structure

Defined in code:
- `/srv/portfolio`: served directory
- `/srv/config`: HTTPD config files
- `/ssh`: Place for SSH configuration

`/srv` and `/ssh` are marked as volumes in Dockerfile.

Advised directories:
- `/srv/certs`: An obvious place for SSL certificates
