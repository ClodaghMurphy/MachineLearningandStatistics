Random numerical app.
Follow instructions!
Input the relevant line on your cmd linux/Windows/bash
Linux
export FLASK_APP=rando.py
python3 -m flask run
Windows
set FLASK_APP=rando.py
python -m flask run
Bash
docker build . -t rando-image
docker run --name rando-container -d -p 5000:5000 rando-image

A "hard kill" is required to close the application (Ctrl C)