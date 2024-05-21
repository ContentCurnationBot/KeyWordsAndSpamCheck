from key_words import check_for_keywords


if __name__ == '__main__':
    text = input('Enter your message: ')
    keywords = input('Enter your keywords separated by spaces: ').split(' ')
    print(check_for_keywords(text, keywords))
