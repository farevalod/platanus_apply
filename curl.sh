#/bin/bash
curl -H "Content-Type: application/json" -XPOST --data-binary @/home/sp/platanus/data.json -L -v -D headers http://platan.us/jobs/apply
