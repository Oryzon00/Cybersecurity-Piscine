# Stockholm

Stockholm is a Python application designed to encrypt and decrypt files, like a ransomware would.
The application uses the cryptography library to perform symmetric encryption and decryption.
The application operates on files located in the ```infection``` folder and uses a ```.key``` file for encryption and decryption processes. 

## Features

* Encrypt files: The application can encrypt files
* Decrypt files: The application can decrypt

## Installation

To install the application, clone the repository and navigate into project directory.
Then, run the Makefile commands to launch the docker.

## Docker

The Makefile includes commands for building, running, stopping, and removing the Docker container.

To build and run the Docker container, use:
```bash
make up
```
To run commands into the virtual environment, use:
```bash
make exec
```

## Usage

The application can be used from the command line. The available options are:

* `-v` or `--version`: Show the version of the program.
* `-s` or `--silent`: Silence the terminal output of the program.
* `-r` or `--reverse`: Reverse the malware infection using an encryption key.

Example usage:

```bash
python3 stockholm.py
```
```bash
python3 stockholm.py -r KEY
```
