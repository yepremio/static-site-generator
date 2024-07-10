python3 -m unittest discover -s src

if [ $? -eq 0 ]; then
  echo "OK"
else
  echo "Tests failed"
  exit 1
fi
