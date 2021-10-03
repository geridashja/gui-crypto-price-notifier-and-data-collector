import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Send_Mail():
    def __init__(self, email, password, main_email):
        self.email = email
        self.password = password
        self.main_email = main_email

    def send_main(self):
        sender_email = self.email
        receiver_email = self.main_email
        password = self.password

        message = MIMEMultipart("alternative")
        message["Subject"] = "BUY THE DIP"
        message["From"] = sender_email
        message["To"] = receiver_email

        text = """\
        Hi,
        How are you? Good? Wanna make money??
        BUYYYY THE DIPPPP!!!
        CHECK THE PRICE:
        """
        html = """\
        <html>
        <body>
            <p>Hi,<br>
            This is a reminder that your coin has reached the price you want to buy it. BUYYYYY THE DIPPPPPPPPPPPP<br>
            <a href="https://www.binance.com/en">Binance</a>
            </p>
        </body>
        </html>
        """

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        message.attach(part1)
        message.attach(part2)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
