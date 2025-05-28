# Syscall Difference
- List of supported system calls in Unikraft stored in [`supported_syscalls.txt`](supported_syscalls.txt)
- List out all system calls using `strace -o strace_out.log -f ...`. Note that some applications list writing stderr to strace_out.log, however that has been updated 
- May have to remove first few lines from `strace_out.log`
- List out all unique system calls using `awk '{split($2, a, "("); print a[1]}' strace_out.txt | sort | uniq`
- Write out the output of previous command to some file
- Copy the file from previous command to `check_syscalls.txt` using `docker copy ...`
- Run the `syscall_validator.py` script. This gives the list of system calls used by application which is currently not supported.
