import subprocess


UTF8 = 'utf-8'


def run_command(command):
    '''
    Simple wrapper around popen
    '''

    command_parts = command.split()
    process = subprocess.Popen(command_parts, stdout=subprocess.PIPE)

    output, error = process.communicate()
    if error:
        raise Exception(error)
    return output.decode(UTF8).strip()
