
import os
import tempfile
import argparse
import json

def my_func():
    parser = argparse.ArgumentParser(description="store the data in storage")
    parser.add_argument("--key", type=str, help="the key")
    parser.add_argument("--val", help="the value")
    args = parser.parse_args()

    if not os.path.exists(os.path.join(tempfile.gettempdir(), 'storage.data')):
        d = {}
        if args.key and args.val:
            d[args.key] = []
            d[args.key].append(args.val)
            storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

            with open(storage_path, 'w') as f:
                json.dump(d, f)
        
    
    else:
        with open(os.path.join(tempfile.gettempdir(), 'storage.data')) as feed:
            d = json.load(feed)

        if args.key and args.val:
            if args.key not in d.keys():
                d[args.key] = []
                d[args.key].append(args.val)
            elif args.key in d.keys():
                d[args.key].append(args.val)
            with open(os.path.join(tempfile.gettempdir(), 'storage.data'), 'w') as f:
                json.dump(d, f)


        if args.key and not args.val:
            with open(os.path.join(tempfile.gettempdir(), 'storage.data')) as json_file:
                data = json.load(json_file)
                if data.get(args.key) != None:
                    print(*(data.get(args.key)), sep=', ')
                else:
                    print('')

if __name__ == "__main__":
    my_func()