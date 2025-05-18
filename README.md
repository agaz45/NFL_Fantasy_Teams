If you are running an 8 owner pool, update the owners.json file with the appropriate teams
If you are running a 4 owner pool, update the owners_fam.json file with the appropriate teams

In nfl.ps1, comment out the line whichever pool you are not using
e.g.:
  python Main.py $week "owners.json"      - Comment this out if you are using a 4 owner pool
  python Main.py $week "owners_fam.json"  - Comment this out if you are using a 8 owner pool

To run, all you need to do is run ./nfl.ps1 <week>

For example, to run week 8:

./nfl.ps1 8

Note: If you want to have performance week by week, make sure the keep the week<number>.txt file for the script to parse
