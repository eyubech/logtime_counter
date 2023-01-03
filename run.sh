cd
mkdir logtime
cd logtime
git clone git@github.com:eyubech/logtime_counter.git
cd
python3 -m pip install requests
echo 'alias mylog="python3 ~/logtime/logtime_counter/main.py"' >> .zshrc
echo "Thanks for using my script :)"
