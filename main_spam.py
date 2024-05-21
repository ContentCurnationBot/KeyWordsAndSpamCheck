from spam_messages import SpamChecker


if __name__ == '__main__':
    spam_checker = SpamChecker('vectorizer.pkl', 'messages.csv')
    messages = input('Enter messages separated by semicolons: ').split(';')
    print(spam_checker.check_spam(messages, threshold=0.5))
