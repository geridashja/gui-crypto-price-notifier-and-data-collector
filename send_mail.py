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
        # password = input("Type your password and press enter:")

        message = MIMEMultipart("alternative")
        message["Subject"] = "BUY THE DIP"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
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
            has many great tutorials.
            </p>
        </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
