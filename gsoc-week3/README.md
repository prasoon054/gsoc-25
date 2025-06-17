# Adding mosquitto 2.0.21

```sh
which mosquitto
    /usr/sbin/mosquitto
ldd $(which mosquitto)
	/lib/ld-musl-x86_64.so.1 (0x7c29c0a6c000)
	libssl.so.3 => /usr/lib/libssl.so.3 (0x7c29c0937000)
	libcrypto.so.3 => /usr/lib/libcrypto.so.3 (0x7c29c04eb000)
	libc.musl-x86_64.so.1 => /lib/ld-musl-x86_64.so.1 (0x7c29c0a6c000)
strace -e open /usr/sbin/mosquitto -c /mosquitto/config/mosquitto.conf > /dev/null
    open("/etc/ld-musl-x86_64.path", O_RDONLY|O_LARGEFILE|O_CLOEXEC) = -1 ENOENT (No such file or directory)
    open("/lib/libssl.so.3", O_RDONLY|O_LARGEFILE|O_CLOEXEC) = -1 ENOENT (No such file or directory)
    open("/usr/local/lib/libssl.so.3", O_RDONLY|O_LARGEFILE|O_CLOEXEC) = -1 ENOENT (No such file or directory)
    open("/usr/lib/libssl.so.3", O_RDONLY|O_LARGEFILE|O_CLOEXEC) = 3
    open("/lib/libcrypto.so.3", O_RDONLY|O_LARGEFILE|O_CLOEXEC) = -1 ENOENT (No such file or directory)
    open("/usr/local/lib/libcrypto.so.3", O_RDONLY|O_LARGEFILE|O_CLOEXEC) = -1 ENOENT (No such file or directory)
    open("/usr/lib/libcrypto.so.3", O_RDONLY|O_LARGEFILE|O_CLOEXEC) = 3
    open("/etc/ssl/openssl.cnf", O_RDONLY|O_LARGEFILE) = 4
    open("/mosquitto/config/mosquitto.conf", O_RDONLY|O_LARGEFILE|O_CLOEXEC|O_DIRECTORY) = -1 ENOTDIR (Not a directory)
    open("/mosquitto/config/mosquitto.conf", O_RDONLY|O_LARGEFILE) = 4
    open("/etc/passwd", O_RDONLY|O_LARGEFILE|O_CLOEXEC) = 4
    open("/etc/group", O_RDONLY|O_LARGEFILE|O_CLOEXEC) = 4

```
