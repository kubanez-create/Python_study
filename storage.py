
import os
import tempfile
import argparse

parser = argparse.ArgumentParser(description="store the data in storage")
parser.add_argument("--key", type=str, help="the key")
parser.add_argument("--value", type=int, help="the value")
args = parser.parse_args()

if args.key and args.value:
    d = {args.key: args.value}
if args.key in d.keys:
    d[args.key].append({args.key: args.value})

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'w') as f:


answer = args.x**args.y