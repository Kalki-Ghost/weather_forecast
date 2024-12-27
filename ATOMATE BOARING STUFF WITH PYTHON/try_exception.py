def division():
    try:
        print('val')
    except ZeroDivisionError:
        print("No")
    else:
        print("hi")
    finally:
        print("hel")


try:
    division()
except ZeroDivisionError:
    print("Yes")
else:
    print("N")

finally:
    print("f")
