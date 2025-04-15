# This is a file to input and get output of the default shell.
import subprocess
import os

def initialized_shell_path(path, run_in_background):
    subprocess.call(['bash', path], text=run_in_background)


def get_bash_script_variables(path):
    output = os.popen(f'bash {path}').read()
    return output


def input_terminal(input_message):
    os.system(input_message)
