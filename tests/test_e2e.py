import subprocess
import requests

def get_stack_output(output_name):
    result = subprocess.run(
        ["pulumi", "stack", "output", output_name],
        stdout=subprocess.PIPE,
        text=True,
    )
    return result.stdout.strip()

def test_web_app_responds():
    web_app_url = get_stack_output("web_app_url")
    assert web_app_url, "Web App URL sollte im Stack-Output definiert sein"
    response = requests.get(web_app_url, timeout=30)
    assert response.status_code == 200, "Web App sollte mit Status 200 antworten"
