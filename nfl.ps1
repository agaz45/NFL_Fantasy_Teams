echo "start"
$week = $args[0]
$weekFile = "week"+$week+".txt"

$html = Invoke-WebRequest -Uri "https://www.nfl.com/standings/league/2020/reg/"
echo "finished request"

$html.ParsedHtml.body.getElementsByTagName("table") | %{$_.innerText} > tmp.txt
echo "finished printing table"

Get-Content tmp.txt | select -Skip 41 > tmp2.txt
rm  tmp.txt
echo "finished removing header"

Get-Content tmp2.txt | Where-Object { ($i % 7 -eq 2) -or ($i % 7 -eq 3); $i++ } > $weekFile
rm tmp2.txt
echo "finished cleaning up rest of file"

(Get-Content -Encoding Unicode "$weekFile" ) | Out-File -Encoding UTF8 "$weekFile"
echo "change codepage of file"

python Main.py $week
echo "finished printing standings"