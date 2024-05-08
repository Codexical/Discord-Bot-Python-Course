echo "Start installation"

echo "> Update System"
sudo apt update > /dev/null 2>&1 &

echo "> Installing Discord"
pip install discord.py > /dev/null 2>&1 &

echo "Finish installation"