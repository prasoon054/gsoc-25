FROM gcc:13.2.0 AS build

COPY ./shared_eg2.c /shared_eg2.c

RUN set -xe; \
    gcc \
      -fPIC \
      -g \
      -o /eg2 \
      -O3 \
      -static-pie \
      -Wall \
      -Wextra \
      -Wno-unused \
      -Wno-unused-parameter \
      /shared_eg2.c

FROM scratch

COPY --from=build /eg2 /eg2
COPY --from=build /lib/x86_64-linux-gnu/libc.so.6 /lib/x86_64-linux-gnu/
COPY --from=build /lib64/ld-linux-x86-64.so.2   /lib64/
