from django.shortcuts import render
from apis.models import TiLoginUserData2
from django.http import HttpResponse
from datetime import datetime
import re

def login_func(request, **kwargs):
    if request.session.has_key('id') and request.session['id'] == 'root':
        return render(request, 'login/profile.html', {'view_data' : 1 })
    return render(request, 'login/login.html', {})

def logged_in_action(request,**kwargs):
    if request.session.has_key('id') and request.session['id'] == 'root':
        return render(request, 'login/profile.html', {'view_data' : 1 })
    print(request.POST)
    user = request.POST.get('user','')
    passwd = request.POST.get('passwd','')
    if user.lower() in ['root'] and passwd.lower() in ['nirav@avika']:
        request.session['id']='root'
        return render(request, 'login/profile.html', {'view_data' : 1 })
    else:
        return render(request, 'login/login.html', {})

def edit_continuation(request,**kwargs):
    if request.session.has_key('id') and request.session['id'] == 'root':
        return render(request, 'login/profile.html', {'view_data' : 1 })
    else:
        return render(request, 'login/login.html', {})

def edit_attandance(request,**kwargs):
    if request.session.has_key('id') and request.session['id'] == 'root':
        str_atta='GAURI :: '
        str_atta2='NITI :: '
        currentMonth = datetime.now().strftime('%m')
        currentYear = datetime.now().strftime('%Y')
        pss,pss1=('',)*2
        arr =[]
        arr1=arr[:]
        qs = TiLoginUserData2.objects.filter(user_id=20983)
        qs1 = TiLoginUserData2.objects.filter(user_id=20977)
        if qs:pss=qs[0].password
        if qs1:pss1=qs1[0].password
        # nested Paramiko
        #
        try:
            import paramiko
            import sys
            import subprocess
            #
            # we instantiate a new object referencing paramiko's SSHClient class
            #
            vm = paramiko.SSHClient()
            vm.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                vm.connect('203.122.32.147', port=8228,username='gauravvaid', password=pss)
            except Exception as e:
                vm.connect('203.122.32.147', port=8228,username='niharikakalra', password=pss1)
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
            stdin, stdout, stderr = jhost.exec_command(f'''PGPASSWORD=ti_hacker /usr/bin/psql -h149.129.179.160 -Utradein_dev tradein_clients -c "select time,out_time,(out_time - time) as duration ,general.date_id_sql_date(date_id) as date,remark  from erp.payroll_full_insense a join erp.attendance_log b using(user_id)  where month={currentMonth} and year={currentYear} and b.user_id = 20983 order by date_id"''') #edited#
            # 20983
            for l in stdout.readlines():
                if re.search(r'^.*\|.*',l):arr.extend(list(map(lambda x : x.strip(),re.split(r'\s*\|\s*',l))))
                str_atta +=l
                print(l)
            stdin, stdout, stderr = jhost.exec_command(f'''PGPASSWORD=ti_hacker /usr/bin/psql -h149.129.179.160 -Utradein_dev tradein_clients -c "select time,out_time,(out_time - time) as duration ,general.date_id_sql_date(date_id) as date,remark  from erp.payroll_full_insense a join erp.attendance_log b using(user_id)  where month={currentMonth} and year={currentYear} and b.user_id = 20977 order by date_id"''') #edited#
            for l in stdout.readlines():
                if re.search(r'^.*\|.*',l):arr1.extend(list(map(lambda x : x.strip(),re.split(r'\s*\|\s*',l))))
                str_atta2 +=l
                print(l)
            jhost.close()
            vm.close()
            # End
        except Exception as e:
            print(e)
            return render(request, 'login/login.html', {})
        else:
            print(arr)
            gauri_atta_data = {
                'th':['In Time','Out Time','Duration','Date','Remark'],
                'tr_all_data': [dict(zip(['In Time','Out Time','Duration','Date','Remark'],arr[i:i+5] )) for i in range(5,len(arr[:]),5) ]
            }
            niti_atta_data = {
                'th':['In Time','Out Time','Duration','Date','Remark'],
                'tr_all_data': [dict(zip(['In Time','Out Time','Duration','Date','Remark'],arr1[i:i+5] )) for i in range(5,len(arr1[:]),5) ]
            }
            print(gauri_atta_data)
            return render(request, 'login/profile.html', { 'view_atta' : 0 ,'show_atta': 1 ,
            'str_atta' :str_atta ,'str_atta2' :str_atta2, 'gauri_atta_data':gauri_atta_data , 'niti_atta_data' : niti_atta_data })
    else:
        return render(request, 'login/login.html', {})

def edit_passwd(request,**kwargs):
    if request.session.has_key('id') and request.session['id'] == 'root':
        return render(request, 'login/profile.html', {'view_data' : 0, 'edit_passwd' : 1 })
    else:
        return render(request, 'login/login.html', {})

def logged_out_action(request,**kwargs):
    if request.session.has_key('id') and request.session['id'] == 'root':
        del request.session['id']
        del request.COOKIES['sessionid']
        request.session.modified = True
        return render(request, 'login/login.html', {})
    else:
        return render(request, 'login/login.html', {})
