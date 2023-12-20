import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket
# Define your SMTP server details
smtp_server = 'smtp.gmail.com'  # Update with your SMTP server details
smtp_port = 587  # Update with your SMTP server port

sender_email = 'satyamk.verve@gmail.com'  # Update with your email address
sender_password = 'jacc vafa usoo rqbk'  # Update with your email password
receiver_email = 'skofficial7479@gmail.com'  # Update with the recipient's email address
cc_email = 'sk6005848@gmail.com'  # Update with the CC recipient's email address


try:
    ip_address = socket.gethostbyname(smtp_server)
    print(f"Resolved IP address: {ip_address}")
except socket.gaierror as e:
    print(f"Error resolving hostname: {e}")


# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Cc'] = cc_email
msg['Subject'] = 'Sample Email Subject'

# Create the email body as an HTML table with 5 rows and 4 columns
email_body = """
<!DOCTYPE html>
<html>
<head>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }

        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }

        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <table>
        <tr>
            <th>Name</th>
            <th>Satyam Kumar</th>
            <th></th>
            <th></th>
        </tr>
        <tr>
            <td>Report Date</td>
            <td>09-Oct-2023</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Report Type</td>
            <td>SOD Report</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>#</td>
            <td>Task of the Day</td>
            <td>Status</td>
            <td>Completed (%)</td>
        </tr>
        <tr>
            <td>1</td>
            <td>Python Modules and Libraries</td>
            <td>Process</td>
            <td>0%</td>
        </tr>
    </table>
    <p>--<br>
        Regards,<br>
        Satyam Kumar | Software Engineer Trainee<br>
        Mail: satyamk.verve@gmail.com | Skype: satyam.verve
     </p> 
</body>
</html>
"""

msg.attach(MIMEText(email_body, 'html'))

# Initialize the SMTP server connection
server = None

try:
    # Establish a connection to the SMTP server
    server = smtplib.SMTP(smtp_server,smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, [receiver_email, cc_email], msg.as_string())
    print('Email sent successfully!')

except Exception as e:
    print(f'Error: {e}')
finally:
    # Close the SMTP server connection if it was established
    if server:
        server.quit()
