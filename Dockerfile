FROM httpd:2.4-alpine

LABEL org.opencontainers.image.source https://github.com/DarthMikke/millim-webhost

RUN apk add openssh git bash python3 py3-pip nodejs apache2-mod-wsgi graphviz

# Kopier tilgangsnøkkelen til Git-repoet
RUN mkdir /root/.ssh
COPY ./ssh/config /root/.ssh/
RUN mkdir /ssh
COPY ./ssh/*.key /ssh
VOLUME [ "/ssh" ]

COPY ./srv /srv
VOLUME [ "/srv" ]

RUN echo "Include /srv/base.conf" >> /usr/local/apache2/conf/httpd.conf
# Inkluder httpd-konfigurasjonen frå git-repoet
RUN echo "IncludeOptional /srv/apache/*.conf" >> /usr/local/apache2/conf/httpd.conf

COPY ./scripts/* /scripts/
RUN chmod +x /scripts/*
CMD /scripts/run.sh
