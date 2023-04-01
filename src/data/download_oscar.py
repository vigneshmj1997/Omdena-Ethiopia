"""
This file contains code to download Oscar dataset from hugginface datasets
"""

import os
import argparse

from datasets import load_dataset
from tqdm import tqdm
import huggingface_hub


def main():
    """
    This fucntion takes
    """
    parser = argparse.ArgumentParser(description="Args parse")
    parser.add_argument(
        "--output",
        type=str,
        help="output file name where to store the data",
        default="amharic.txt",
    )
    parser.add_argument(
        "--hftoken",
        type=str,
        help="output file name where to store the data",
        required=True,
    )
    args = parser.parse_args()
    huggingface_hub.login(token=args.hftoken)
    data = load_dataset("oscar-corpus/OSCAR-2201", "am")
    with open(os.path.join("downloads", args.output), "w") as file:
        lines = data["train"]["text"]
        for line in tqdm(lines[:-1]):
            file.write(line.rstrip() + "\n")
        file.write(lines[-1].rstrip())


if __name__ == "__main__":
    main()
