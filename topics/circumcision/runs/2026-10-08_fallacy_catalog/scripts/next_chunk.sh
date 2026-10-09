#!/bin/bash
# Print the next unread chunks (up to ~19,000 characters) from CHUNK_DIR.
# Mark a chunk as read with: echo NNN >> $CHUNK_DIR/done.txt
cd "${CHUNK_DIR:?set CHUNK_DIR}"; touch done.txt; tot=0
for f in [0-9]*.txt; do n=$(basename $f .txt); grep -qx $n done.txt && continue
 s=$(wc -c < $f); if [ $tot -gt 0 ] && [ $((tot+s)) -gt 19000 ]; then break; fi
 echo "#### CHUNK $n"; cat $f; tot=$((tot+s)); done
