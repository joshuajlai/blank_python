import subprocess
UTF8 = 'utf-8'

'''
Simple wrapper around popen
'''
def run_command(command):
    command_parts = command.split()
    process = subprocess.Popen(command_parts, stdout=subprocess.PIPE)

    output, error = process.communicate()
    if error:
        raise Exception(error)
    return output.decode(UTF8).strip()
