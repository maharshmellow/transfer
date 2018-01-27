python3 server.py &
echo $!

./ngrok http 5000 > /dev/null &
echo $!
