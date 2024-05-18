import csv
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os


# Функция для чтения сообщений из .csv файла
def read_messages_from_csv(filename):
    messages = []
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            messages.append(row[0])
    return messages


# Сохранение и загрузка объектов с использованием joblib
def save_vectorizer_and_matrix(vectorizer, matrix, filename):
    joblib.dump((vectorizer, matrix), filename)


def load_vectorizer_and_matrix(filename):
    return joblib.load(filename)


# Инициализация файлов
messages_file = 'messages.csv'
vectorizer_file = 'vectorizer.pkl'

# Чтение сообщений из файла
messages = read_messages_from_csv(messages_file)

# Проверка, существует ли файл с векторизатором и матрицей
if os.path.exists(vectorizer_file):
    vectorizer, tfidf_matrix = load_vectorizer_and_matrix(vectorizer_file)
else:
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(messages)
    save_vectorizer_and_matrix(vectorizer, tfidf_matrix, vectorizer_file)

# Новые сообщения для тестирования
new_messages = [
    "Сегодня погода отличная!",
    "Привет, как у тебя дела?",
    "Программирование на Python - это весело.",
    "На выходных можно встретиться.",
    "Недавно наткнулся на интересную статью.",
    "Что нового у тебя?",
    "Сегодня просто чудесная погода!",
    "Каникулы начинаются совсем скоро.",
    "Как идут дела на работе?",
    "Вчера смотрел потрясающий фильм в кино!",
    "Aboba"
]

# Пороговое значение для определения сходства
threshold = 0.8

# Проверка новых сообщений поочередно
for new_message in new_messages:
    # Преобразование нового сообщения в TF-IDF вектор
    new_message_tfidf = vectorizer.transform([new_message])

    # Вычисление косинусного сходства между новым сообщением и уже имеющимися
    cosine_similarities = cosine_similarity(new_message_tfidf, tfidf_matrix)

    if any(similarity > threshold for similarity in cosine_similarities[0]):
        print(f"Сообщение '{new_message}' похоже на одно из предыдущих, оно может быть спамом.")
    else:
        print(f"Сообщение '{new_message}' успешно отправлено.")
        # Добавление нового сообщения в список сообщений
        messages.append(new_message)
        # Обновление TF-IDF матрицы
        tfidf_matrix = vectorizer.fit_transform(messages)
        # Сохранение обновленного векторизатора и матрицы
        save_vectorizer_and_matrix(vectorizer, tfidf_matrix, vectorizer_file)
        # Сохранение обновленного списка сообщений в .csv файл
        with open(messages_file, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([new_message])
