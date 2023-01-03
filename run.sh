cd
mkdir logtime_count
cd logtime_count
git clone git@github.com:eyubech/logtime_counter.git
cd
python3 -m pip install requests
echo 'alias logtime="python3 ~/logtime/logtime_counter/main.py"' >> .zshrc
echo "Thanks for using my script :)"
