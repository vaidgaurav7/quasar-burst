import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "heroku_django.settings")
import django
django.setup()

# import paramiko
# ssh = paramiko.SSHClient()
#
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# # ssh.connect('<hostname>', username='<username>', password='<password>', key_filename='<path/to/openssh-private-key-file>')
# ssh.connect('203.122.32.147', port=8228,username='gauravvaid', password='filled#buxom')
#
# stdin, stdout, stderr = ssh.exec_command('ps -auwxx')
# for l in stdout.readlines():
#     print(l)
# # print stdout.readlines()
# ssh.close()



#
# nested Paramiko
#
import paramiko
import sys
import subprocess
#
# we instantiate a new object referencing paramiko's SSHClient class
#
vm = paramiko.SSHClient()
vm.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vm.connect('203.122.32.147', port=8228,username='gauravvaid', password='filled#buxom')
#
vmtransport = vm.get_transport()
dest_addr = ('192.168.0.88', 22) #edited#
local_addr = ('203.122.32.147', 22) #edited#
vmchannel = vmtransport.open_channel("direct-tcpip", dest_addr, local_addr)
#
jhost = paramiko.SSHClient()
jhost.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#jhost.load_host_keys('/home/osmanl/.ssh/known_hosts') #disabled#
jhost.connect('192.168.0.88', username='gauravvaid', password='moshimo123!@#', sock=vmchannel)
#
# stdin, stdout, stderr = jhost.exec_command('PGPASSWORD=ti_hacker /usr/bin/psql -h149.129.179.160 -Utradein_dev tradein_clients -c "select * from general.product_gallery limit 1"') #edited#
stdin, stdout, stderr = jhost.exec_command(f'''PGPASSWORD=ti_hacker /usr/bin/psql -h149.129.179.160 -Utradein_dev tradein_clients -c "select time,out_time,(out_time - time) as duration ,general.date_id_sql_date(date_id) as date,remark  from erp.payroll_full_insense a join erp.attendance_log b using(user_id)  where month='05' and year='2020' and b.user_id = 20983 order by date_id"''') #edited#
#
for l in stdout.readlines():
     print(l)
jhost.close()
vm.close()
# End
