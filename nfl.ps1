$week = $args[0]

echo "Parsing standings"
python Parse.py $week

echo "Starting fantasy standings 8 team"
python Main.py $week

echo "finished printing standings"