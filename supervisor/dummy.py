#! /usr/bin/python3
import time

def main():
    while 1:
        time.sleep(1)
        with open("test.txt", "a+") as t:
            t.write(time.strftime("%I %M %S %p")+"\n")


if __name__ == "__main__":
    main()