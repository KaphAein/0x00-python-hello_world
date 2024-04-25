#!/bin/bash
# status code
curl -s -L -X HEAD "%{http_code}" "$1"
