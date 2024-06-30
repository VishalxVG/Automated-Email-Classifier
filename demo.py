import imaplib
import email
from email.header import decode_header
from bs4 import BeautifulSoup
from twilio.rest import Client
import yagmail
import os

# Twilio credentials
account_sid = ''
auth_token = ''
whatsapp_from='',  # Replace with your Twilio WhatsApp Sender ID
whatsapp_to = ''  # Replace with your WhatsApp number

# IMAP settings
imap_server = 'imap.gmail.com'
imap_username = ''
imap_password = ''

def send_whatsapp_message(body):
    try:
        client = Client(account_sid, auth_token)
        for i in range(0, len(body), 1600):
            chunk = body[i:i+1600]
            message = client.messages.create(
                body=chunk,
                from_=whatsapp_from,
                to=whatsapp_to,
                
            )

        print(f"WhatsApp message sent: {message.sid}")
    except Exception as e:
        print(f"Failed to send WhatsApp message: {e}")


def extract_and_format_content(body):
    try:
        start_index = body.find("Date:")
        end_index = body.find("Regards")
        
        if start_index != -1 and end_index != -1:
            message = body[start_index:end_index + len("Regards") - 7]
            return message
        else:
            return body  # Return the original body if the required parts are not found
    except Exception as e:
        print(f"Error in extracting and formatting content: {e}")
        return body  




def fetch_email():
    try:
        # Connect to the IMAP server
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(imap_username, imap_password)
        print("Logged into IMAP server")

        # Select the mailbox you want to check
        mail.select("inbox")

        # Search for emails from a specific sender
        status, messages = mail.search(None, 'FROM', '""')
        email_ids = messages[0].split()
        print(f"Found {len(email_ids)} emails from the specified sender")

        for email_id in email_ids:
            # Fetch the email by ID
            status, msg_data = mail.fetch(email_id, "(RFC822)")
            msg = email.message_from_bytes(msg_data[0][1])
            
            # Decode the email subject
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else "utf-8")
            print(f"Subject: {subject}")

            # Process the email content
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))

                    if "attachment" not in content_disposition:
                        payload = part.get_payload(decode=True)
                        if payload and content_type == "text/plain":
                            charset = part.get_content_charset() or "utf-8"
                            body = payload.decode(charset)
                            msg = extract_and_format_content(body)
                            print(f"Email body (text/plain): {msg}")
                            
                            send_whatsapp_message(msg)
            else:
                payload = msg.get_payload(decode=True)
                if payload and msg.get_content_type() == "text/plain":
                    charset = msg.get_content_charset() or "utf-8"
                    body = payload.decode(charset)
                    print(f"Email body (text/plain): {body}")
                    msg = extract_and_format_content(body)
                    send_whatsapp_message(msg)

        # Logout from the IMAP server
        mail.logout()
        print("Logged out from IMAP server")

    except Exception as e:
        print(f"Error: {e}")




if __name__ == "__main__":
    fetch_email()
