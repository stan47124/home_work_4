# 1. Создайте словарь email
email = {
    "subject": " Weekd plans ",
    "from": "Katya_yan@yandex.ru ",
    "to": "Frid@mail.com ",
    "body": "\tHey!\nLet's go hiking this weekd.\nBring snacks!\n"
}

# 2. Добавьте дату отправки

import datetime
send_date = datetime.datetime.now()
formatted_date = send_date.strftime("%Y-%m-%d")
email['send_date'] = formatted_date

# 3. Нормализуйте e-mail адреса

email["from"] = email["from"].lower().strip()
email["to"] = email["to"].lower().strip()

# 4. Извлеките логин и домен отправителя в две переменные login и domain.

login = email["from"].split('@')[0]
domain = email["from"].split('@')[1]

# 5. Создайте сокращённую версию текста

email["short_body"] = email["body"][:10] + "..."

# 6. Списки доменов

list_private_domains = ['gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru']
list_private_domains = list(set(list_private_domains))
list_corporation_domains = ['company.ru','corporation.com','university.edu','organization.org','company.ru', 'business.net']
list_corporation_domains = list(set(list_corporation_domains))

# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений

personal_set = set(list_private_domains)
corporate_set = set(list_corporation_domains)
intersection = personal_set & corporate_set
if intersection:
    print("Найдены общие домены:", intersection)
else:
    print("Пересечений нет, списки корректны.")

# 8. Проверьте «корпоративность» отправителя

is_corporate = domain in corporate_set

print(f"Домен отправителя: {domain}")
print(f"Корпоративный? {is_corporate}")

# 9. Соберите «чистый» текст сообщения

email["clean_body"] = email["body"].replace("\t", " ").replace("\n", " ")

# 10. Сформируйте текст отправленного письма

email["sent_text"] = f"""
Кому: {email["to"]}
От: {email["from"]}
Тема: {email["subject"]}
Дата: {email["send_date"]}
"""

# 11. Рассчитайте количество страниц печати

email.pages = dsf123214