FROM gcc:13.2.0 AS build

COPY ./futex_test.c /futex_test.c

RUN set -xe; \
    gcc \
      -fPIC \
      -g \
      -o /futex_test \
      -O3 \
      -static-pie \
      -Wall \
      -Wextra \
      -Wno-unused \
      -Wno-unused-parameter \
      /futex_test.c

FROM scratch

COPY --from=build /futex_test /futex_test
COPY --from=build /lib/x86_64-linux-gnu/libc.so.6 /lib/x86_64-linux-gnu/
COPY --from=build /lib64/ld-linux-x86-64.so.2   /lib64/
