myFile = 'C:/Users/navkumar16/PycharmProjects/Practise/Programs/Basics/Resources/ChurnEmail.txt'
handle = open('/Programs/Basics/Resources/ChurnEmail.txt', 'r')


# content = handle.read()
# print(content)

def number_of_lines():
    content = handle.read()
    count = 0
    for con in content.split("\n"):
        # print(con)
        count = count + 1
    conten = content.split("\n")
    print(f'Last content: {conten[len(conten) - 1]}')
    return count

    # content = handle.readlines()
    # return len(content)


print(number_of_lines())


def average_spam_confidence():
    count, spam = 0, ""
    spamConf = 0.00
    for line in open(myFile, 'r'):
        line.rstrip()
        if line.startswith("X-DSPAM-Confidence:"):
            count = count + 1
            spam = spam + line
            conf = line.split()
            spamConf = spamConf + float(conf[len(conf) - 1])
    print(spam)
    return float(spamConf / count)


print(f'************* SPAMS: {average_spam_confidence()}')


def find_email_sent_days():
    send_days = dict()
    for line in open(myFile, 'r'):
        if line.startswith("From "):
            words = line.split(" ")
            try:
                day = words[2]
            except IndexError:
                print(f'Indexing error for line:\n\t{line}')

            if day not in send_days:
                send_days[day] = 0
            send_days[day] = send_days[day] + 1
    return send_days


print(f'Email sent days: {find_email_sent_days()}')


def find_email_sender():
    emailSenders = dict()
    for line in open(myFile, 'r'):
        if line.startswith("From"):
            words = line.split(" ")
            email = words[1].strip()

            if email not in emailSenders:
                emailSenders[email] = 0
            emailSenders[email] = emailSenders[email] + 1
    return emailSenders


print(f'Email sender with counts: {find_email_sender()}')

def message_from_domain():
    domain = dict()
    mail_details = find_email_sender()
    for email in mail_d;etails:
        dom = email.split("@")[1]
        if dom not in domain:
            domain[dom] = 0
        domain[dom] = domain[dom] + mail_details[email]
    return domain

print(f'Domain sent details: {message_from_domain()}')