#!/usr/bin/env python3

import os
import subprocess
import sys

VERSION = "1.0.0"

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

def get_current_level_dirs():
    return list(filter(lambda x: x not in ['target', '.git', 'src'], next(os.walk('.'))[1]))

def generate_examples():
    return dict( ( (str (k+1 ), v ) for k,v in zip( range( len( get_current_level_dirs() ) ), get_current_level_dirs() ) ) )

def main():
    choice = sys.argv[1] if len(sys.argv) > 1 else 0
    if choice == "-h" or choice == "--help":
        print(get_usage())
        sys.exit(0)
    elif choice == "--version":
        print(VERSION)
        sys.exit(0)
        
    examples = generate_examples()
    
    if choice not in list(examples.keys()):
        print("[!] Select a valid choice.")
        sys.exit(-1)
    
    print("[+] Running example {}".format(examples[choice]))

    try:
        path = "{}/{}/Cargo.toml".format(os.getcwd(), examples[choice])
        subprocess.run(["cargo", "run", "--manifest-path", path])
    except KeyboardInterrupt:
        print("[!] Exiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()
