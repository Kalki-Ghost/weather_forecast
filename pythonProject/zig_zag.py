import sys
import time

indent = 0
indent_increasing = True
try:
    while True:
        print(' ' * indent, end='')
        print("********")
        time.sleep(.2)
        if indent_increasing:
            indent += 1
            if indent == 20:
                indent_increasing = False
        else:
            indent -= 1
            if indent == 0:
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()
