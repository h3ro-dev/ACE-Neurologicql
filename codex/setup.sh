#!/bin/bash
set -euo pipefail

apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y postgresql redis-server tree-sitter

pip install --no-cache-dir mcp-server-filesystem mcp-server-git mcp-server-sqlite mcp-server-memory mcp-server-sequential mcp-server-time mcp-server-aidd

service postgresql start
service redis-server start

nohup python -m mcp.git &
nohup python -m mcp.filesystem &
nohup python -m mcp.sqlite &
nohup python -m mcp.memory &
nohup python -m mcp.sequential &
nohup python -m mcp.time &
nohup python -m mcp.server.aidd &

sleep 2

python -m unittest discover -s tests -p 'test_*.py' -v
