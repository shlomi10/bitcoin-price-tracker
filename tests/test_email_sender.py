from unittest.mock import patch, MagicMock

import allure

from utils.email_sender import send_email


@allure.suite("Email Sender")
@allure.feature("send_email")
def test_send_email_mocked(tmp_path):
    attachment_path = tmp_path / "dummy.png"
    attachment_path.write_bytes(b"fake-image-data")

    with patch("smtplib.SMTP") as mock_smtp:
        smtp_instance = MagicMock()
        mock_smtp.return_value.__enter__.return_value = smtp_instance

        send_email(
            smtp_host="smtp.test.com",
            smtp_port=587,
            sender_email="sender@test.com",
            password="password",
            recipient_email="recipient@test.com",
            subject="Test Subject",
            body="Test Body",
            attachment_path=str(attachment_path)
        )

        smtp_instance.starttls.assert_called_once()
        smtp_instance.login.assert_called_once_with("sender@test.com", "password")
        smtp_instance.send_message.assert_called_once()
