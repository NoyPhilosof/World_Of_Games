from time import sleep


def x():
    s = "This message will destroy itself in 0.7 seconds"
    print()
    print(s, end="\r")


def y():
    s = "This message will destroy itself in 0.7 seconds"
    print("<>?" * int(len(s) / 3))


x()
sleep(1.5)
y()
