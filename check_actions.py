import urllib.request
import json

url = 'https://api.github.com/repos/Nystic-Shadow/Nystic-Shadow/actions/runs'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    res = urllib.request.urlopen(req).read().decode('utf-8')
    data = json.loads(res)
    total_count = data.get('total_count', 0)
    print(f"Total workflow runs: {total_count}")
    runs = data.get('workflow_runs', [])
    for r in runs[:5]:
        print(f"Run #{r.get('run_number')}: name='{r.get('name')}', status='{r.get('status')}', conclusion='{r.get('conclusion')}'")
except Exception as e:
    print(f"Workflow API check error: {e}")
