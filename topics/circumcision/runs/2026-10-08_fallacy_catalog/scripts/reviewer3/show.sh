#!/bin/bash
f=/workspace/gta_repo/topics/circumcision/articles/$1/snapshots/2026-10-01.txt
awk 'p{print} /^====/{p=1}' $f | grep -v '^$'
