import sys
from collections import defaultdict
import signal

# Dictionary to store file size and status code counts
file_sizes = defaultdict(int)
status_code_counts = defaultdict(int)

# Total file size
total_size = 0


# Function to handle keyboard interruption (CTRL + C)
def signal_handler(signal, frame):
    print_stats()
    sys.exit(0)


# Function to print statistics
def print_stats():
    print(f"Total file size: File size: {total_size}")

    # Print status code counts in ascending order
    for status_code in sorted(status_code_counts):
        print(f"{status_code}: {status_code_counts[status_code]}")


        # Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line_number, line in enumerate(sys.stdin, start=1):
        # Split the input line into components
        components = line.split()

        # Extract file size and status code
        file_size = int(components[-1])
        status_code = components[-2]

        # Update total file size
        total_size += file_size

        # Update file size count
        file_sizes[line_number % 10] = total_size

        # Update status code count
        status_code_counts[status_code] += 1

        # Print statistics every 10 lines
        if line_number % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_stats()
    sys.exit(0)
