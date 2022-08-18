#!/usr/bin/env python3


def main():
    from sys import version_info, exit

    if not (version_info[0] == 3 and version_info[1] >= 7):
        exit("Sorry, Please use Python3 > 3.7")

    import src

    print(src.result)


if __name__ == "__main__":
    main()
