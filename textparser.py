import config

def check_entry(message_text):
    if len(message_text.split(' - ')) < 2:
        return False

    if message_text.split(' - ')[1] not in config.GRADES:
        return False

    return True

def parse_entry(message_text):
    text = message_text.split(' - ')

    return text
