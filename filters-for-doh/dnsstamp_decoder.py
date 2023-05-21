#!/usr/bin/env python3

import dnsstamps, sys

parameter = dnsstamps.parse(sys.argv[1])
dnsstamps.format(parameter)
