#!/bin/bash
# status code
curl -s -L -X HEAD -w "%{http_code}" "$1"
