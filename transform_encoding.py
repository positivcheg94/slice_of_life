import os
import glob


def transform(binary, encoding_in="cp1251", encoding_out="utf-8"):
    return binary.decode(encoding=encoding_in).encode(encoding=encoding_out)


def tranform_files_by_pattern(path, pattern):
    p = os.path.join(path, "**", pattern)
    files = glob.glob(p, recursive=True)
    for file in files:
        data = open(file, "rb").read()
        try:
            transformed = transform(data)
            file = open(file, "wb").write(transformed)
        except:
            pass
