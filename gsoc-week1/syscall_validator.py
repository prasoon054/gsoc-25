def read_syscalls_from_file(file_path):
    """Read system call names from a file, one per line."""
    try:
        with open(file_path, 'r') as file:
            syscalls = [line.strip() for line in file if line.strip()]
        return syscalls
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

def read_supported_syscalls(file_path):
    """Read supported system call names from a file into a set."""
    try:
        with open(file_path, 'r') as file:
            supported = {line.strip() for line in file if line.strip()}
        return supported
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return set()

def main():
    supported_syscalls = read_supported_syscalls('supported_syscalls.txt')
    used_syscalls = read_syscalls_from_file('check_syscalls.txt')
    
    unsupported_syscalls = [sc for sc in used_syscalls if sc not in supported_syscalls]
    
    print(f"\nNumber of unsupported system calls: {len(unsupported_syscalls)}")
    if unsupported_syscalls:
        print("Unsupported system calls:")
        for sc in unsupported_syscalls:
            print(sc)

if __name__ == "__main__":
    main()
