#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is needed as multiprocessing shouldn't include nsz
# as it won't be able to optain __main__.__file__ and so crash inside Keys.py
if __name__ == '__main__':
	import sys
	if sys.hexversion < 0x03060000:
		raise ImportError("NSZ requires at least Python 3.6!\nCurrent python version is " + sys.version)
	import multiprocessing
	multiprocessing.freeze_support()
	import nsz
	nsz.main()
