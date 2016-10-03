__all__ = ['crawler_init',
           'predefine']

import sys

from crawler.crawler_init import smtm_crawler

if __name__ == "__main__":
    a = smtm_crawler(sys.argv[1], sys.argv[2], sys.argv[3])
    a.init()
    a.signin()
    a.start()
