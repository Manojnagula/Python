with open(r"mail_merger\sample.docx",'r') as mail:
    raw_mail = mail.read()
with open(r"mail_merger\names.txt",'r') as names:
        for name in names:
                mail_content =    raw_mail.replace('[name]',name.strip())
                with open(rf"mail_merger\output_mails\mail_to_{name.strip()}.txt",'w') as out_put_mail:
                    out_put_mail.write(mail_content)