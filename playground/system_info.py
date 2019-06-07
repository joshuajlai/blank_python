from future.utils import iteritems
from utils import run_command

computer_info = {}
computer_info['ip_address'] = run_command('hostname -I')
computer_info['hostname'] = run_command('hostname')

print('Computer Info')
for (key, value) in iteritems(computer_info):
    print('{} {}'.format(key, value))
