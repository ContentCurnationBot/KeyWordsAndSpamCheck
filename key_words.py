from natasha import Segmenter, MorphVocab, NewsEmbedding, NewsMorphTagger, Doc

# Инициализация компонентов Natasha
segmenter = Segmenter()
morph_vocab = MorphVocab()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)


# Функция для нормализации слов
def normalize_word(word):
    doc = Doc(word)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    for token in doc.tokens:
        token.lemmatize(morph_vocab)
    return doc.tokens[0].lemma


# Текст для проверки
text = "Это тексты, которые нужно проверить на наличие ключевых слов."

# Ключевые слова
keywords = ["ключевое", "слово"]

# Нормализуем текст
normalized_text = [normalize_word(word) for word in text.split()]

# Нормализуем ключевые слова
normalized_keywords = [normalize_word(word) for word in keywords]

# Проверяем наличие ключевых слов в нормализованном тексте
for keyword in normalized_keywords:
    if keyword in normalized_text:
        print(f"Ключевое слово '{keyword}' найдено!")
    else:
        print(f"Ключевое слово '{keyword}' не найдено.")