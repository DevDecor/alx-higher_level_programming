#!/bin/bash
"Prints the size downloaded"
curl -s -o /dev/null -w "%{size_download}\n" $1
