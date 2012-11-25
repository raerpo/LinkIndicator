indicator-cpuspeed
==================

On Ubuntu 12.04 Unity, I was missing an indicator that could show me the
current frequency of all 4 my CPU cores, so I wrote this minimal sample
in Python to do just that.

It uses PyGObject, and simply parses out /proc/cpuinfo every few seconds
to extract the current frequencies of ALL your CPU cores. These frequencies
are then shown in a label in the indicator area.

It looks like this:

![screenshot of indicator-cpuspeed](http://dl.dropbox.com/u/207154/indicator-cpuspeed.png)

I'm making this available under the BSD license just in case someone else
needs a minimal sample to get started with, or an indicator to show the CPU
frequency (but that would be weird).

-- 
Charl P. Botha
http://charlbotha.com/

