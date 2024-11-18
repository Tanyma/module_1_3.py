sender_urban = "urban.student@gmail.com"
def send_email(sms,recipient,sender = sender_urban):
    sen = str.endswith(recipient, (".com", ".ru", ".net"))
    rec = str.endswith(sender, (".com", ".ru", ".net"))
    if sen == False or rec == False or "@" not in recipient or "@" not in sender:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print(f"Невозможно отправить письмо самому себе")
    elif sender != sender_urban:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender}")
    else:
        print(f"{sms} \nПисьмо успешно отправлено с адреса {sender} на адрес {recipient}")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')