import poplib
from email.parser import Parser
          
host = 'pop.mail.yahoo.co.jp'
username = 'vpngateurl@yahoo.co.jp'
pwd = 'python'

pp = poplib.POP3_SSL(host)
pp.set_debuglevel(1)
print(pp.getwelcome().decode('utf-8'))
pp.user(username)
pp.pass_(pwd)

m, s = pp.stat()
print('Messages: %s. Size: %s' % (m, s))

for i in range(m,0,-1):
    msg_c = b'\r\n'.join(pp.retr(i)[1]).decode('utf-8')
    msg = Parser().parsestr(msg_c)
    if msg.get('Subject','') == 'VPN Gate Daily Mirror URLs': break
pp.quit()

print('\n\n\nText:\n%s'%msg.get_payload(decode=True).decode('us-ascii'))
input('Press Enter to Exit')

