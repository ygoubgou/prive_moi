from transformers import pipeline

qa = pipeline("question-answering", model="deepset/roberta-base-squad2")

context = "Jean Dupont a travaillé chez Airbus pendant 5 ans comme ingénieur en intelligence artificielle."

question = "Où Jean Dupont a-t-il travaillé ?"

result = qa(question=question, context=context)

print(result["answer"])



import streamlit as st
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
import torch

# Masquer le menu de navigation standard de Streamlit (pages)
hide_default_menu = """
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
"""
st.markdown(hide_default_menu, unsafe_allow_html=True)


# --- Chargement des modèles ---
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
embedder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# --- Charger et découper le fichier profil.txt ---
def charger_profil(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        texte = f.read()
    # Découper le texte en blocs pertinents
    blocs = [bloc.strip() for bloc in texte.split("\n\n") if bloc.strip()]
    return blocs

# --- Trouver le bloc le plus pertinent ---
def bloc_pertinent(question, blocs):
    embeddings_blocs = embedder.encode(blocs, convert_to_tensor=True)
    embedding_question = embedder.encode(question, convert_to_tensor=True)
    scores = util.cos_sim(embedding_question, embeddings_blocs)
    meilleur_index = torch.argmax(scores)
    return blocs[meilleur_index]

# --- Répondre à une question ---
def repondre(question, contexte):
    try:
        result = qa_pipeline(question=question, context=contexte)
        return result["answer"]
    except:
        return "Désolé, je n’ai pas pu répondre à cette question."

# --- Gestion manuelle de questions simples ---
def reponse_personnalisee(question):
    q = question.lower()

    if any(kw in q for kw in ["bonjour", "salut", "hello", "bonsoir"]):
        return "Bonjour et bienvenue ! Je suis IAMBA, l’agent IA de Yamba Arsène Goubgou. Pose-moi toutes tes questions sur son parcours, ses compétences, ses projets ou son expérience. 😊"
    
    elif any(kw in q for kw in ["merci", "thanks"]):
        return "Avec plaisir ! Si tu veux en savoir plus, je suis toujours disponible."
    
    elif any(kw in q for kw in ["qui es-tu", "présente-toi", "tu es qui", "c'est quoi iamba"]):
        return ("Je suis IAMBA, un agent conversationnel intelligent conçu pour représenter "
                "Yamba Arsène Goubgou. Je peux t’aider à découvrir son parcours académique, "
                "son expérience professionnelle, ses compétences techniques et humaines, "
                "ainsi que ses distinctions et projets.")
    
    elif any(kw in q for kw in ["ça va", "tu vas bien", "comment tu vas"]):
        return "Je vais très bien, merci ! Et toi ? Je suis prêt à répondre à toutes tes questions. 😄"

    elif any(kw in q for kw in ["contact", "joindre", "email", "téléphone"]):
        return ("Tu peux contacter Yamba par email à **lamoussama225@gmail.com** ou par téléphone au **+33 7 53 60 73 32**. "
                "Tu peux aussi consulter ses projets techniques sur GitHub : [github.com/ygoubgou](https://github.com/ygoubgou).")

    return None  # Si rien de détecté

# --- Interface Streamlit ---
st.set_page_config(page_title="Chatbot IA - IAMBA", page_icon="🤖")
st.title("🤖 Agent IA - IAMBA")

# Chargement du profil
blocs_profil = charger_profil("profil.txt")

# Champ de saisie utilisateur
question = st.text_input("Pose ta question à IAMBA (ex: Formation, Compétences, Expériences...)")

if question:
    # Vérifie s’il y a une réponse personnalisée
    reponse_man = reponse_personnalisee(question)
    if reponse_man:
        st.markdown("**🧠 Réponse :**")
        st.success(reponse_man)
    else:
        contexte = bloc_pertinent(question, blocs_profil)
        reponse = repondre(question, contexte)
        
        st.markdown("**📄 Contexte utilisé :**")
        st.info(contexte)
        
        st.markdown("**🧠 Réponse :**")
        st.success(reponse)



import requests

API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
headers = {"Authorization": "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"}  # Ton token Hugging Face

def question_reponse(question, contexte):
    payload = {
        "inputs": {
            "question": question,
            "context": contexte
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]["answer"]










# Bon dans AI.PY
import streamlit as st
import requests
from sentence_transformers import SentenceTransformer, util
import torch

# --- Masquer le menu Streamlit ---
hide_default_menu = """
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
"""
st.markdown(hide_default_menu, unsafe_allow_html=True)
st.set_page_config(page_title="Chatbot IA - IAMBA", page_icon="🤖")
st.title("🤖 Agent IA - IAMBA")

# --- API Hugging Face ---
API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
headers = {"Authorization": "Bearer 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"}

def question_reponse(question, contexte):
    payload = {"inputs": {"question": question, "context": contexte}}
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
        data = response.json()
        if isinstance(data, list) and len(data) > 0 and "answer" in data[0]:
            return data[0]["answer"]
        else:
            return "Je n’ai pas trouvé d’information précise dans le contexte fourni."
    except:
        return "Désolé, une erreur est survenue avec l'API Hugging Face."

# --- Embeddings pour contexte ---
embedder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def charger_profil(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        texte = f.read()
    blocs = [bloc.strip() for bloc in texte.split("\n\n") if bloc.strip()]
    return blocs

def bloc_pertinent(question, blocs):
    embeddings_blocs = embedder.encode(blocs, convert_to_tensor=True)
    embedding_question = embedder.encode(question, convert_to_tensor=True)
    scores = util.cos_sim(embedding_question, embeddings_blocs)[0]
    top_indices = torch.topk(scores, k=3).indices
    return " ".join([blocs[i] for i in top_indices])

# --- Réponses manuelles enrichies ---
def reponse_personnalisee(question):
    q = question.lower()
    if any(kw in q for kw in ["bonjour", "salut", "hello", "bonsoir"]):
        return "Bonjour et bienvenue ! Je suis IAMBA, l’agent IA de Yamba. Pose-moi toutes tes questions 😊"
    elif any(kw in q for kw in ["merci", "thanks"]):
        return "Avec plaisir ! Je suis toujours disponible."
    elif any(kw in q for kw in ["qui es-tu", "présente-toi", "tu es qui", "c'est quoi iamba"]):
        return "Je suis IAMBA, l’agent conversationnel de Yamba Arsène Goubgou, économiste et data scientist basé à Nantes."
    elif any(kw in q for kw in ["ça va", "tu vas bien", "comment tu vas"]):
        return "Je vais très bien, merci ! Et toi ? 😊"
    elif any(kw in q for kw in ["contact", "joindre", "email", "téléphone"]):
        return ("Tu peux joindre Yamba à **lamoussama225@gmail.com**, au **+33 7 53 60 73 32** ou via GitHub : [github.com/ygoubgou](https://github.com/ygoubgou)")
    elif "expérience" in q:
        return ("Yamba travaille comme Data Engineer / Analyst chez Cerfrance à Nantes, où il développe des outils de prévision "
                "et de reporting avec Python, Power BI et Excel. Il a aussi encadré des étudiants en économétrie à l’Université d’Angers.")
    elif "formation" in q:
        return ("Yamba est diplômé en économie appliquée (Burkina Faso), en ingénierie des données (Université d’Angers), "
                "et suit actuellement un Mastère Spécialisé MQDE à l’ENSAE Paris.")
    elif "compétences" in q:
        return ("Il maîtrise Python, R, Stata, SAS, Power BI, Git, et des méthodes avancées en économétrie, machine learning et data visualisation.")
    elif "localisation" in q or "disponibilité" in q:
        return "Il est basé à Nantes, disponible en télétravail ou en présentiel, et titulaire du permis B."
    return None

# --- Chargement du profil ---
blocs_profil = charger_profil("profil.txt")
question = st.text_input("Pose ta question à IAMBA (ex: Formation, Compétences, Expériences...)")

if question:
    reponse_man = reponse_personnalisee(question)
    if reponse_man:
        st.markdown("**🧠 Réponse personnalisée :**")
        st.success(reponse_man)
    else:
        contexte = bloc_pertinent(question, blocs_profil)
        reponse = question_reponse(question, contexte)
        st.markdown("**📄 Contexte utilisé :**")
        st.info(contexte)
        st.markdown("**🧠 Réponse API :**")
        st.success(reponse)
