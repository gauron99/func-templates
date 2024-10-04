from parliament import Context
from flask import Request
import json

def main(context: Context):
    """
    Function template 'hello' -- prints "Received request" on server
    and "Hello, World!" on client on success
    """

    # Add your business logic here
    print("Received request")
    if 'request' in context.keys():
        return "Hello, World!",200
    else:
        print("Empty request", flush=True)
        return "{}", 200
