# Automated Email Classifier

This project is an automated email screening system that fetches emails, extracts and formats the content, and sends WhatsApp messages using Twilio. It is designed to help users receive important email notifications directly on their WhatsApp.




## Tech Stack

- **Python**: The core language used for automation.
- **IMAP**: Used to fetch emails from the server.
- **Email**: For handling and parsing email messages.
- **Twilio**: For sending WhatsApp messages.
- **Pyinstaller** : For creating a executable file.

## How It Works

1. **Fetch Emails**: The script connects to the Gmail IMAP server and fetches emails from a specific sender.
2. **Extract and Format Content**: The content of the emails is extracted and formatted to include only relevant information.
3. **Send WhatsApp Messages**: The formatted email content is then sent as a WhatsApp message using Twilio's API.
4. **Executable File** : Using pyinstaller I have created a executable file that will run and find the most recent email from the given source and sent the required mails to the watsapp number


## Installation

Follow these steps to set up and run the project:

### Prerequisites

- Python 3.x
- Git
- Twilio Account
- Gmail Account

### Steps

1. **Clone the Repository**

    ```sh
    git clone https://github.com/VishalxVG/Automated-Email-Classifier.git
    cd Automated-Email-Classifier
    ```

2. **Create a Virtual Environment and Activate It**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set Environment Variables**

    Create a `.env` file in the root directory and add your credentials:

    ```sh
    TWILIO_ACCOUNT_SID=your_twilio_account_sid
    TWILIO_AUTH_TOKEN=your_twilio_auth_token
    TWILIO_WHATSAPP_FROM=your_twilio_whatsapp_sender_id
    TWILIO_WHATSAPP_TO=your_whatsapp_number
    IMAP_USERNAME=your_gmail_username
    IMAP_PASSWORD=your_gmail_app_password
    ```

5. **Run the Script**

    ```sh
    python your_script.py
    ```

## Usage

1. Make sure your environment variables are set correctly.
2. Run the script to start fetching emails and receiving WhatsApp notifications.
3. Adjust the fetch interval and sender email address as needed in the script.


## Screenshots

![WhatsApp Notification](https://github.com/VishalxVG/Automated-Email-Classifier/blob/main/img1.jpg)
![Email Fetching](https://github.com/VishalxVG/Automated-Email-Classifier/blob/main/img2.jpg)

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Twilio](https://www.twilio.com/) for the messaging API.


