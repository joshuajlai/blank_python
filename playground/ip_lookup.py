from utils import run_command

target = input("Looking up A records for: ")
lookup_command = "dig +noall +answer -t a {}".format(target)
print(run_command(lookup_command))
