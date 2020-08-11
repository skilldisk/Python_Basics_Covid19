emails = [
    "test1@gmail.com",
    "test2@outlook.com",
    "test3@yahoo.com",
    "test4@gmx.com",
    "test4@mail.com",
    "test4@post.com",
]

for email in emails:

    # split the string data at '@' and access the index 1
    service_provider = email.split("@")[1]
    print(service_provider)
