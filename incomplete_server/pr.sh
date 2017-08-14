echo "Start: parser"

echo "Start: server\n"

(node server.js) || (echo "Error: server\n" exit)
echo "Start: indexing and searching"
(python3 search.py) || (echo "Error: index and search" exit)
