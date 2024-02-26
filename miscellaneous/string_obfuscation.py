import sys

if len(sys.argv) < 2:
    exit()

KEY = "gobbledygook".replace("b", "").replace("e", "").replace("oo", "").replace("gk", "").replace("y", "en")
print(KEY)
FLAG = chr(51)+chr(70)+chr(120)+chr(89)+chr(70)+chr(109)+chr(52)+chr(117)+chr(84)+chr(89)+chr(68)+chr(70)+chr(70)+chr(122)+chr(109)+chr(98)+chr(51)

if sys.argv[1] == KEY:
    print("flag{%s}" % FLAG)
