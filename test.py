import streamlit as st
import requests
from sentence_transformers import SentenceTransformer, util
import torch

# --- Configuration de la page ---
st.set_page_config(page_title="IAMBA - Chatbot IA", page_icon="🤖")

# --- Fond personnalisé et style ---
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(to bottom right, #f0f8ff, #e6e6fa);
        background-size: cover;
        color: #000000;
    }
    .stChatMessage {
        font-size: 16px;
        line-height: 1.5;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 IAMBA - Chatbot IA de Yamba")
st.markdown("Pose-moi tes questions sur le profil de Yamba : ses études, expériences, compétences ou contact !" \
"NB: Je ne réponds qu'aux questions sur Yamba")

# --- Chargement des blocs du profil ---
def charger_profil(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        texte = f.read()
    blocs = [bloc.strip() for bloc in texte.split("\n\n") if bloc.strip()]
    return blocs

blocs_profil = charger_profil("profil.txt")

# --- Modèle d'embedding ---
embedder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def bloc_pertinent(question, blocs, k=3):
    embeddings_blocs = embedder.encode(blocs, convert_to_tensor=True)
    embedding_question = embedder.encode(question, convert_to_tensor=True)
    scores = util.cos_sim(embedding_question, embeddings_blocs)[0]
    top_indices = torch.topk(scores, k=k).indices
    return "\n\n".join([blocs[i] for i in top_indices])

# --- Appel à l'API Hugging Face (roberta-base-squad2) ---
API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
headers = {"Authorization": "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"}

def question_reponse(question, contexte):
    payload = {"inputs": {"question": question, "context": contexte}}
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
        data = response.json()
        # Debug possible : print(data)
        if isinstance(data, dict) and "answer" in data:
            return data["answer"]
        elif isinstance(data, list) and len(data) > 0 and "answer" in data[0]:
            return data[0]["answer"]
        else:
            return "Je n’ai pas trouvé d’information précise dans le contexte fourni."
    except Exception as e:
        return "Désolé, une erreur est survenue avec l'API Hugging Face."

# --- Réponses personnalisées ---
def reponse_personnalisee(question):
    q = question.lower()
    if any(kw in q for kw in ["bonjour", "salut", "hello"]):
        return "Bonjour et bienvenue ! Je suis IAMBA, l’agent IA de Yamba. 😊"
    if "merci" in q:
        return "Avec plaisir ! Si tu veux en savoir plus, je suis là."
    if "contact" in q or "email" in q:
        return "Tu peux contacter Yamba à **lamoussama225@gmail.com** ou sur GitHub : [ygoubgou](https://github.com/ygoubgou)."
    if any(kw in q for kw in ["ça va", "comment ça va", "comment vas-tu"]):
        return "Je vais bien, merci ! Pose-moi des questions sur le profil de Yamba."
    if "pourquoi" in q:
        return "Je suis conçu pour répondre aux questions sur le profil de Yamba. Pour d’autres questions, je suis limité."
    return None

# --- Filtre avant appel API ---
def doit_appeler_api(question):
    mots_cles_pertinents = ["formation", "expérience", "compétence", "projet", "contact", "études", "enseignement", "langues", "localisation"]
    return any(mot in question.lower() for mot in mots_cles_pertinents)

# --- Historique multi-tours ---
if "history" not in st.session_state:
    st.session_state["history"] = []

for user_msg, bot_msg in st.session_state["history"]:
    with st.chat_message("user"):
        st.markdown(user_msg)
    with st.chat_message("assistant"):
        st.markdown(bot_msg)

question = st.chat_input("Pose ta question ici...")

if question:
    with st.chat_message("user"):
        st.markdown(question)

    reponse = reponse_personnalisee(question)
    if not reponse:
        if doit_appeler_api(question):
            contexte = bloc_pertinent(question, blocs_profil)
            reponse = question_reponse(question, contexte)
        else:
            reponse = "Je suis désolé, je ne peux répondre qu’à des questions liées au profil de Yamba."

    with st.chat_message("assistant"):
        st.markdown(reponse)

    st.session_state["history"].append((question, reponse))
