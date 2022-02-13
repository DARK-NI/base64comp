import marshal
import zlib
import base64
import os
import sys
import random
try:
  r = sys.argv[1]
except:
  exit("\nUsage: Just Type nibase64 ")
cyan = "\x1b[1;96m"
if not os.path.isfile(r):
  exit("\n File not found")
  
a = open(r).read()
b = marshal.dumps(a)
c = zlib.compress(b)
d = base64.b64encode(c)

sv = '# Compiled By Md Nazmul Islam (DARK-NI)\n# Github: github.com/DARK-NI\n# Facebook: fb.com/link.copy.koro.kno.babu\n# Teligram: t.me/md_nazmulislam\n# Note: Dont Try to decrypt this tool.\n\n\nimport marshal, zlib, base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("{}"))))'

ni = random.randint(111,999)

i = "dark_ni_" + str(ni) + (".py")
open(i , "w").write(sv.format(d))
print("\n\n\n   Encrypt Successfull !")
print("\n   Encrypted file name : \x1b[1;92m" + i + cyan)
exit("\n   Encrypted File Path :\x1b[1;92m $HOME/base64comp")
