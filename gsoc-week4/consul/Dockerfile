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
    git clone https://github.com/hashicorp/consul.git;

RUN set -xe; \
    cd consul; \
    git checkout tags/v1.21.0; \
    VERSION=v1.21.1; \
    GIT_COMMIT=$(git rev-parse --verify HEAD); \
    BUILD_TIME=$(date -u +%Y-%m-%dT%H:%M:%SZ); \
    GOLDFLAGS="-X github.com/hashicorp/consul/version.Version=${VERSION} \
    -X github.com/hashicorp/consul/version.GitCommit=${GIT_COMMIT} \
    -X github.com/hashicorp/consul/version.BuildTime=${BUILD_TIME}"; \
    mkdir -p bin; \
    CGO_ENABLED=1 \
    GO111MODULE=on \
    go build \
        -buildmode=pie \
        -ldflags "${GOLDFLAGS} -linkmode=external" \
        -o /usr/bin/consul \
        .;
    # cp /go/consul/bin/consul /usr/bin/consul

FROM alpine:3.22 AS sys

RUN set -xe;

FROM scratch

COPY --from=sys /lib/ld-musl-x86_64.so.1 /lib/ld-musl-x86_64.so.1

COPY --from=builder /usr/bin/consul /usr/bin/consul
