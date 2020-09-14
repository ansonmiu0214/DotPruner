import argparse
import os
import sys

from . import process_from_file
from .utils import info, error

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)
    parser.add_argument('output', type=str)
    parser.add_argument('--overwrite', '-o', type=bool, default=False)

    parsed_args = parser.parse_args()

    final_graph = process_from_file(parsed_args.filename)

    if os.path.exists(parsed_args.output) and not parsed_args.overwrite:
        error(f'Path exists but overwrite flag not specified: "{parsed_args.output}"')
        return 1

    try:
        with open(parsed_args.output, 'w') as output_file:
            output_file.write(final_graph.to_string())
    except OSError:
        error(f'Error writing to file: "{parsed_args.output}"')
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())