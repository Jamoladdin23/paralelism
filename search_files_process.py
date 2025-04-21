import os
import sys
import threading


def search_files(extension, directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                print(f"Found: {os.path.join(root, file)}")


def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <extension> <directory1> <directory2> ...")
        return

    extension = sys.argv[1]
    directories = sys.argv[2:]

    threads = []
    for directory in directories:
        thread = threading.Thread(target=search_files, args=(extension, directory))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
