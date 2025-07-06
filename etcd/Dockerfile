FROM alpine:3.22 AS builder

RUN set -xe; \
    echo "https://dl-cdn.alpinelinux.org/alpine/edge/community" \
      >> /etc/apk/repositories; \
    apk update; \
    apk add --no-cache \
      etcd=3.5.18-r3 \
      tzdata; \
    mkdir -p /target/etc; \
    mkdir -p /target/var/lib/etcd;

FROM scratch

COPY --from=builder /target/etc /etc
COPY --from=builder /target/var/lib/etcd /var/lib/etcd

COPY --from=builder /usr/bin/etcd /usr/bin/etcd
COPY --from=builder /etc/etcd /etc/etcd
COPY --from=builder /lib/ld-musl-x86_64.so.1 /lib/ld-musl-x86_64.so.1
COPY ./conf.yml /conf.yml
