#!/bin/bash

. ~/.bashrc && figpay-p

rsync \
  -arvP \
  public \
  server.js \
  package.json \
  stef@wf-31-170-122-44.webfaction.com:/home/stef/figpay-pos/
