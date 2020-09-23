echo "start"

$html = Invoke-WebRequest -Uri "https://www.nfl.com/standings/league/2020/reg/"
echo "finished request"

$html.ParsedHtml.body.getElementsByTagName("table") | %{$_.innerText} > tmp.txt
echo "finished printing table"

Get-Content tmp.txt | select -Skip 41 > tmp2.txt
echo "finished removing header"

rm  tmp.txt
echo "remove first temp file"

Get-Content tmp2.txt | Where-Object { ($i % 7 -eq 2) -or ($i % 7 -eq 3); $i++ } > week3.txt
echo "finished cleaning up rest of file"

rm tmp2.txt
echo "remove second temp file"

(Get-Content -Encoding Unicode "week3.txt" ) | Out-File -Encoding UTF8 "week3.txt"
echo "change codepage of file"

python Main.py
echo "finished printing standings