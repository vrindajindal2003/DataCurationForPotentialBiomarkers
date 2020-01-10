#!/bin/bash
# mkdir o-files
for file in input-files/* ; do awk 'BEGIN {print "PROTEINS\tPEPTIDES"} $2 ~ /^PVX/{print $2"\t"$NF}' $file | sort -k1 -k2 > o-files/o${file:12} ; done