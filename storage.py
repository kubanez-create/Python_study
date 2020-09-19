
import os
import tempfile
import argparse
import json

def my_func():
    parser = argparse.ArgumentParser(description="store the data in storage")
    parser.add_argument("--key", type=str, help="the key")
    parser.add_argument("--val", type=int, help="the value")
    args = parser.parse_args()

    if not os.path.exists('storage.data'):
        d = {}
        if args.key and args.val:
            if args.key not in d.keys():
                d[args.key] = args.val
            elif args.key in d.keys():
                if type(d[args.key]) == type([]):
                    d[args.key].append(args.val)
                elif type(d[args.key]) != type([]):
                    tv = d[args.key]
                    d[args.key] = []
                    d[args.key].append(tv)
        storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

        with open(storage_path, 'w') as f:
            json.dump(d, f)
        
    
    else:
        d = {}

        if args.key and args.val:
            if args.key not in d.keys():
                d[args.key] = args.val
            elif args.key in d.keys():
                if type(d[args.key]) == type([]):
                    d[args.key].append(args.val)
                elif type(d[args.key]) != type([]):
                    tv = d[args.key]
                    d[args.key] = []
                    d[args.key].append(tv)
        with open('storage.data') as feed:
            temp = json.load(feed)
        temp.append(d)
        with open('storage.data', 'w') as f:
            json.dump(d, f)


    if args.key and not args.val:
        with open(storage_path) as json_file:
            data = json.load(json_file)
            print(data)

if __name__ == "__main__":
    my_func()