from py80211.scan import *
import netlink.capi as nl
from py80211.cli import bss_info
import sys

ifidx = nl.if_nametoindex(sys.argv[1])
print("%s: ididx=%d" % (sys.argv[1], ifidx))
if sys.argv[2] == 'start':
	rh = sched_scan_start(ifidx)
	rh.add_matches([{ 'ssid': 'lemonhead'}])
	rh.set_interval(30000)
elif sys.argv[2] == 'stop':
	rh = sched_scan_stop(ifidx, nl.NL_CB_DEBUG)

rh.send()
