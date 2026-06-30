import os
import hashlib
import argparse
from collections import defaultdict


def file_hash(path, block_size=65536):
    hasher = hashlib.md5()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            hasher.update(block)
    return hasher.hexdigest()


def find_duplicates(root_dir):
    hashes = defaultdict(list)

    for dirpath, _, filenames in os.walk(root_dir):
        for name in filenames:
            full_path = os.path.join(dirpath, name)
            try:
                h = file_hash(full_path)
                hashes[h].append(full_path)
            except (OSError, PermissionError):
                continue

    return {h: paths for h, paths in hashes.items() if len(paths) > 1}


def main():
    parser = argparse.ArgumentParser(description="Find duplicate files in a directory")
    parser.add_argument("directory", help="Directory to scan")
    parser.add_argument("--delete", action="store_true", help="Delete duplicates, keep first occurrence")

    args = parser.parse_args()

    duplicates = find_duplicates(args.directory)

    if not duplicates:
        print("No duplicates found.")
        return

    total_wasted = 0
    for h, paths in duplicates.items():
        print(f"\nDuplicate group ({len(paths)} files):")
        for p in paths:
            print(f"  {p}")

        if args.delete:
            for p in paths[1:]:
                size = os.path.getsize(p)
                os.remove(p)
                total_wasted += size
                print(f"  Deleted: {p}")

    if args.delete:
        print(f"\nFreed {total_wasted / 1024:.2f} KB")


if __name__ == "__main__":
    main()
