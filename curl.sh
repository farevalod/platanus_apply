#/bin/bash
curl -H "Content-Type: application/json" -XPOST --data-binary @/home/sp/platanus/data.json -L -v https://platan.us/jobs/apply
