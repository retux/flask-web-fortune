from flask import Flask, render_template
import subprocess
import sys
import os

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

	
@app.context_processor	
def my_processor():
    def run_command(command):
        p = subprocess.Popen(command, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
        return iter(p.stdout.readline, b'')        
		
    def get_fortune():
        cwd = os.path.dirname(os.path.realpath(__file__))
        stdout = ""
        #for line in run_command("python {0}/fortune.py".format(cwd)):	
        for line in run_command("./fortune.py"):	
            stdout += line + "\n"
        return stdout
    
    return dict(get_fortune=get_fortune)
	
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
