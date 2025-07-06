FROM golang:1.25rc1-alpine3.22 AS builder

RUN set -xe; \
    apk --no-cache add \
      gcc \
      make \
      musl-dev \
      wget \
      bash \
      git \
    ; \
    git clone https://github.com/minio/minio.git;

RUN set -xe; \
    cd minio; \
    VERSION="RELEASE.2025-06-13T11-33-47Z"; \
    git checkout tags/$VERSION; \
    LDFLAGS="-s -w \
      -X github.com/minio/minio/cmd.Version=${VERSION} \
      -X github.com/minio/minio/cmd.CopyrightYear=2025 \
      -X github.com/minio/minio/cmd.ReleaseTag=DEVELOPMENT.${VERSION} \
      -X github.com/minio/minio/cmd.CommitID=a6c538c5a113a588d49b4f3af36ae3046cfa5ac6 \
      -X github.com/minio/minio/cmd.ShortCommitID=a6c538c5a113 \
      -X github.com/minio/minio/cmd.GOPATH=/go"; \
    CGO_ENABLED=1 GOOS=linux GOARCH=amd64 \
      go build \
        -buildmode=pie \
        -tags kqueue \
        -trimpath \
        --ldflags "$LDFLAGS" \
        -o /usr/bin/minio

FROM alpine:3.22 AS sys

RUN set -xe; \
    mkdir -p /target/etc; \
    mkdir -p /blank; \
    apk --no-cache add \
      ca-certificates \
      tzdata \
    ; \
    update-ca-certificates; \
    ln -sf ../usr/share/zoneinfo/Etc/UTC /target/etc/localtime; \
    echo "Etc/UTC" > /target/etc/timezone;

FROM scratch

COPY --from=builder /usr/bin/minio /usr/bin/minio
COPY --from=builder /lib/ld-musl-x86_64.so.1 /lib/ld-musl-x86_64.so.1

COPY --from=sys /target/etc /etc
COPY --from=sys /usr/share/zoneinfo/Etc/UTC /usr/share/zoneinfo/Etc/UTC
COPY --from=sys /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
COPY --from=sys /blank /data
