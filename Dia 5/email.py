import nltk
import string
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

# Corpus de perguntas e respostas
corpus = {
    "oi": "Olá! Como posso ajudar você?",
    "qual é o seu nome?": "Eu sou um chatbot criado para ajudar você.",
    "como você está?": "Estou bem, obrigado por perguntar!",
    "adeus": "Tchau! Tenha um ótimo dia!"
}

def preprocess(text):
    text = text.lower()  # Converte o texto para minúsculas
    text = text.translate(str.maketrans("", "", string.punctuation))  # Remove a pontuação
    tokens = word_tokenize(text)  # Tokeniza o texto
    return tokens

class Chatbot:
    def __init__(self, corpus):
        self.corpus = corpus
        self.vectorizer = TfidfVectorizer(tokenizer=preprocess, stop_words='english')
        self.fit_corpus()

    def fit_corpus(self):
        self.vectorized_corpus = self.vectorizer.fit_transform(self.corpus.keys())

    def get_response(self, user_input):
        user_input_vector = self.vectorizer.transform([user_input])
        similarities = cosine_similarity(user_input_vector, self.vectorized_corpus)
        best_match_index = similarities.argmax()
        best_match_score = similarities[0][best_match_index]

        if best_match_score < 0.1:  # Se a similaridade for muito baixa, responder que não entendeu
            return "Desculpe, não entendi. Pode reformular a pergunta?"
        else:
            return list(self.corpus.values())[best_match_index]

# Cria uma instância do chatbot
chatbot = Chatbot(corpus)

def chat():
    print("Bem-vindo! Digite 'sair' para encerrar a conversa.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == 'sair':
            print("Chatbot: Tchau! Tenha um ótimo dia!")
            break
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

# Inicia a conversa
chat()
