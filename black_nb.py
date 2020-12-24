#!/usr/bin/env python

import sys
import json
import black

def black_notebook(path):
    j = {}

    with open(path, "r") as f:
        s = f.read()
        j = json.loads(s)
        cells = j["cells"]
        for cell in cells:
            if cell["cell_type"] != "code":
                continue
            code = cell["source"]
            code = "".join(code)
            o = code
            try:
                o = black.format_str(o, mode=black.FileMode())
                # black 20 adds 1 \n to the output
                o = o.rstrip("\n")
            except:
                print("error: black")
            # notebook format
            o = o.split("\n")
            for i, _ in enumerate(o):
                if i == (len(o) - 1):
                    break
                o[i] += "\n"
            cell["source"] = o

    with open(path, "w") as f:
        s = json.dumps(j, indent=2, ensure_ascii=False)
        f.write(s)

if __name__ == "__main__":
    args = sys.argv[1:]
    for arg in args:
        black_notebook(arg)
