from pathlib import Path
import re

fun = Path("PicoMite_User_Manual_f.txt")
fun2 = Path("PicoMite_User_Manual_f_.md")
fun3 = Path("PicoMite_User_Manual_f__.md")
enc = "utf-8"

def cleanup(fun,fun2):
    content = fun.read_text(encoding=enc)
    fun_re = r"^([A-Z\d]+\$?)\W(?:[^\n]+\n)+"

    cut_pos = []
    names = []
    with open(fun2, "w", encoding=enc) as f:
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

def chap(fun2,fun3):
    content = fun2.read_text(encoding=enc)
    for m in re.finditer(r"^#{3}", content, flags=re.MULTILINE):
        start = m.start()
        next_chapter = re.compile(r"^#", flags=re.MULTILINE)
        if m2 := next_chapter.search( content, pos=m.start()+10):
            end = m2.start()
        else:
            end = len(content)-1
        print(start, end)

chap(fun2, None)