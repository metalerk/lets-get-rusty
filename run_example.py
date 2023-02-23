#!/usr/bin/env python3

import os
import subprocess
import sys

VERSION = "1.0.0"

EXAMPLES = {
    "1": "guessing_game",
}

def get_usage():
    usage = """
        ***********************************************************
        *                                                         *
        *                                                          *
        *            Let's Get Rusty Exercises                      *
        *                                                          *
        *                                                         *
        ***********************************************************

        Usage: run_example [options] [arguments]

        Options:
        -h, --help        Show usage
        
        Arguments:
        run_example       Run Rust exercise
        
        Examples:
        run_example 1
        run_example -h
        run_example --help
        run_example --version
        
        Author: Luis Esteban Rodriguez <rodriguezjluis0@gmail.com>
        """
    return usage

def main():
    choice = sys.argv[1] if len(sys.argv) > 1 else 0
    
    if choice == "-h" or choice == "--help":
        print(get_usage())
        sys.exit(0)
    elif choice == "--version":
        print(VERSION)
        sys.exit(0)
    
    if choice not in list(EXAMPLES.keys()):
        print("[!] Select a valid choice.")
        sys.exit(-1)
    
    print("[+] Running example {}".format(EXAMPLES[choice]))

    try:
        path = "{}/{}/Cargo.toml".format(os.getcwd(), EXAMPLES[choice])
        subprocess.run(["cargo", "run", "--manifest-path", path])
    except KeyboardInterrupt:
        print("[!] Exiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()
