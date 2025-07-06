FROM golang:1.25rc1-alpine3.22 AS builder

RUN set -xe; \
    apk --no-cache add \
      gcc \
      make \
      musl-dev \
      wget \
      bash \
      git \
      npm \
    ; \
    git clone https://github.com/go-gitea/gitea.git;

RUN set -xe; \
    cd gitea; \
    git checkout release/v1.24; \
    CGO_ENABLED=1 \
    GOOS=linux \
    GOARCH=amd64 \
    TAGS="bindata sqlite sqlite_unlock_notify" \
    make build GOFLAGS="-v -buildmode=pie"; \
    cp ./gitea /usr/bin/gitea; \
    mkdir -p /data/gitea/conf /data/gitea/log /data/gitea/data

FROM alpine:3.22 AS sys

RUN set -xe; \
    mkdir -p /target/etc; \
    apk --no-cache add \
      ca-certificates \
      tzdata \
    ; \
    update-ca-certificates; \
    ln -sf ../usr/share/zoneinfo/Etc/UTC /target/etc/localtime; \
    echo "Etc/UTC" > /target/etc/timezone;

FROM scratch

COPY --from=builder /usr/bin/gitea /usr/bin/gitea
COPY --from=builder /usr/bin/git /usr/bin/git
COPY --from=builder /lib/ld-musl-x86_64.so.1 /lib/ld-musl-x86_64.so.1
COPY --from=builder /usr/lib/libz.so.1 /usr/lib/libz.so.1
COPY --from=builder /usr/lib/libpcre2-8.so.0 /usr/lib/libpcre2-8.so.0
COPY --from=builder /data /data

COPY --from=sys /target/etc /etc
COPY --from=sys /etc/passwd /etc/passwd
COPY --from=sys /usr/share/zoneinfo/Etc/UTC /usr/share/zoneinfo/Etc/UTC
COPY --from=sys /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt

COPY ./app.ini /data/gitea/conf/app.ini
