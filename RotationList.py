import datetime

emails_liste = ["Johann.berzlammer@gmail.de","Schopenhoff.E@gmail.com","johann.s.alex4@gmail.com","schimlernd@gmail.com","lambast_wbns@simplelogin.com","journalism_bigalow@simplelogin.com","osman_iber@simplelogin.com","eurocard_dawload@simplelogin.com","gahran_releasing@simplelogin.com","phytopathol_clarin@simplelogin.com","berlin.redlight@gmail.com","vincent.johanness.wagner@gmail.com","berlin.blacklight@gmail.com","hamami.fashion@gmail.com","jerbilkolaron@yahoo.com"]
#emails_liste = ['schopenhoff.e+1@gmail.com', 'paulgray.a+2@gmail.com', 'anngreen.c+3@gmail.com', 'sarahjones.d+4@gmail.com', 'jameswilliams.f+5@gmail.com', 'johnsmith.g+6@gmail.com', 'jessicamiller.h+7@gmail.com', 'amandawilson.i+8@gmail.com']
def update_logs(log_file="logs.txt"):
  now = datetime.datetime.now().timestamp()
  with open(log_file, 'r') as f:
    for line in f:
      line_split = line.split(',')
      email = line_split[0]
      date_time = datetime.datetime.strptime(line_split[2].replace('\n', '').strip(), '%Y-%m-%d %H:%M:%S.%f')
      timestamp = date_time.timestamp()
      if (now - timestamp) >= 86400 and now > timestamp:
        emails_liste.append(email)
      else:
        pass
  return emails_liste
print(update_logs(log_file="logs.txt"))