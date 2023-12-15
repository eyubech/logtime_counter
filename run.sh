python3 -m pip install requests

rm -rf $HOME/logtime_count
mkdir $HOME/.logtime

cp  main.py $HOME/.logtime/

echo 'alias logtime="python3 ~/.logtime/main.py"' >> $HOME/.zshrc
echo "**Installed uccessfully**"