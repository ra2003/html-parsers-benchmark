from lxml import etree
import time
import sys


def main():
    with open(sys.argv[1], 'r') as f:
        do_parse_test(f.read(), int(sys.argv[2]))


def do_parse_test(html, n):
    start = time.time()
    for i in xrange(n):
        tree = etree.HTML(html)
        len(tree)
    stop = time.time()
    print stop - start, "s"


if __name__ == '__main__':
    main()