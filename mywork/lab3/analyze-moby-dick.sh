#!/bin/bash

SEARCH_PATTERN="$1"
OUTPUT="$2"

OCCURRENCES=$(grep -o "$SEARCH_PATTERN" mobydick.txt | wc -l)

echo "The search pattern $SEARCH_PATTERN was found $OCCURRENCES time(s)." > "$OUTPUT"