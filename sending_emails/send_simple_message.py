def send_simple_message():
    return requests.post(request_url, auth=("api", key),
        data={"from": sender,
              "to": cf_list,
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})
