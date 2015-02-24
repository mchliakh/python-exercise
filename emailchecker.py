# 1) Checks if the format of the address is valid and throws an error if it isn't
# 2) Obtains the MX record for the domain the email is hosted at
# 3) Queries the SMTP server and tells if the email address exists or not by returning a boolean

import re, dns.resolver, smtplib

def check_if_email_exists(email):
  if not is_valid(email):
    raise Exception('Inalid email address')

  try:
    for host in smtp_hosts(email.split('@')[-1]):
      smtp = smtplib.SMTP()
      smtp.connect(host)

      status, _ = smtp.helo()
      if status != 250:
        smtp.quit()
        continue

      smtp.mail('')
      status, _ = smtp.rcpt(email)
      if status == 250:
        smtp.quit()
        return True

      smtp.quit()

  except:
    return False

  return False

def is_valid(email):
  return bool(re.match(r'[^@]+@[^@]+\.[^@]+', email))

def smtp_hosts(domain):
  records = dns.resolver.query(domain, 'MX')
  return map(lambda r: r.exchange.__str__()[:-1], records)
