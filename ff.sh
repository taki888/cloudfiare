#!/bin/bash
export CF_API_EMAIL=feifan668@gmail.com
export CF_API_KEY=5fcdedfb14c6c090f7aef5c2f6ce7fef7212a
for domain in $(cat domains.txt); do \
  curl -X POST -H "X-Auth-Key: $CF_API_KEY" -H "X-Auth-Email: $CF_API_EMAIL" \
  -H "Content-Type: application/json" \
  "https://api.cloudflare.com/client/v4/zones" \
  --data '{"name":"'$domain'","jump_start":true}'; done
