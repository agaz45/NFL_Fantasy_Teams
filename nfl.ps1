$week = $args[0]

echo "Parsing standings"
python Parse.py $week

echo "Starting fantasy standings 8 team"
python Main.py $week "owners.json"

echo "Starting fantasy standings fam pool"
python Main.py $week "owners_fam.json"

echo "finished printing standings"