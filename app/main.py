# app/main.py

import sys

print("Hello from inside the Docker container!")
print(f"Python version: {sys.version}")

if __name__ == "__main__":
    print("It works")