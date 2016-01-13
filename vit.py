#!/usr/bin/env python
# encoding: utf-8

import arrow
now_utc = arrow.utcnow()
now_Beijing = now_utc.replace(hours=+8)
t_m = arrow.get("2014-12-28 20:16:00")
t_t= arrow.get("2016-01-03 22:00:00")

from_t_m = now_Beijing - t_m
from_t_t = now_Beijing - t_t
print "from_t_m:{}\nfrom_t_t{}".format(from_t_m,from_t_t)
#print t_t.humanize(locale='zh_cn')

