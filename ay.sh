#!/bin/bash
export CF_API_EMAIL=ay1681688@gmail.com
export CF_API_KEY=7688003357becab6a6d79389a338c4bf170fa
for domain in $(cat domains.txt); do \
  curl -X POST -H "X-Auth-Key: $CF_API_KEY" -H "X-Auth-Email: $CF_API_EMAIL" \
  -H "Content-Type: application/json" \
  "https://api.cloudflare.com/client/v4/zones" \
  --data '{"name":"'$domain'","jump_start":true}'; done
