from pathlib import Path
import re

fun = Path("PicoMite_User_Manual_f.txt")
_fun = Path("PicoMite_User_Manual_f_.txt")
enc = "utf-8"
content = fun.read_text(encoding=enc)
fun_re = r"^([A-Z\d]+\$?)\W(?:[^\n]+\n)+"

cut_pos = []
names = []
with open(_fun, "w", encoding=enc) as f:
    for m in re.finditer(fun_re, content, flags=re.MULTILINE):
        name = m.group(1)
        _content = content[m.start():m.end()]
        print(name, m.start(),m.end())
        first_line = _content.splitlines()[0]
        print(first_line)
        col_pos = re.search(r"   +",first_line).end()
        print(" "*col_pos+"^", col_pos)
        left = " ".join([line[:col_pos] for line in _content.splitlines()])
        left = re.sub(r"  +", " ", left).strip()
        print(left)
        f.write(f"### {left}\n\n")

        right = "\n".join([line[col_pos:] for line in _content.splitlines()])
        right = re.sub(r"\.\n", ".\n\n", right).strip()+"\n"
        print (right)
        f.write(f"{right}\n\n")
