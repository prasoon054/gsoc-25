FROM alpine:latest
RUN apk add --no-cache curl bash
RUN curl -O https://dl.min.io/server/minio/release/linux-amd64/minio && \
    chmod +x minio && \
    mv minio /usr/local/bin/
