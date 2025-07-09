import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Mon Portfolio Interactif", layout="wide")

hide_sidebar_style = """
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)


# --- CSS effet wow ---
st.markdown("""
<style>
body {
    background-color: #f0f8ff;
    font-family: 'Segoe UI', sans-serif;
}
.big-button {
    border: none;
    border-radius: 15px;
    padding: 0;
    cursor: pointer;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s ease-in-out;
}
.big-button:hover {
    transform: scale(1.03);
}
.big-button img {
    width: 100%;
    height: 400px;
    object-fit: cover;
    filter: brightness(0.8);
}
.button-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    font-size: 36px;
    font-weight: bold;
    text-shadow: 2px 2px 8px #000;
}
</style>
""", unsafe_allow_html=True)



st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700&display=swap');

.header-bar {
    background: linear-gradient(135deg, #1e3c72 0%, #6e7dab 50%, #b8c6db 100%);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite, pulseGlow 3s ease-in-out infinite;
    padding: 70px 30px 50px 30px;
    border-radius: 0 0 40px 40px;
    color: white;
    text-align: center;
    font-family: 'Montserrat', sans-serif;
    box-shadow: 0 12px 35px rgba(0,0,0,0.4);
    position: relative;
    overflow: hidden;
    transition: background 1s ease;
}

.header-bar:hover {
    background: linear-gradient(135deg, #3a6073, #2c5364, #1d4350);
}

/* Halo rotatif doux */
.header-bar::before {
    content: "";
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255,255,255,0.06), transparent 70%);
    animation: rotateGlow 10s linear infinite;
    z-index: 0;
}

/* Conteneur des cœurs */
.heart-container {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    overflow: visible;
    z-index: 2;
    display: none;
}

.header-bar:hover .heart-container {
    display: block;
}

/* Style des cœurs avec teinte évolutive */
.heart {
    position: absolute;
    width: 40px;
    height: 40px;
    background: red;
    clip-path: polygon(
      50% 0%, 
      61% 14%, 
      75% 14%, 
      85% 27%, 
      85% 45%, 
      50% 80%, 
      15% 45%, 
      15% 27%, 
      25% 14%, 
      39% 14%
    );
    opacity: 0.8;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
    animation-name: fallRotateHeart, hueShift;
    animation-duration: 6s, 8s;
}

/* Animation : chute + rotation */
@keyframes fallRotateHeart {
    0% {
        transform: translateX(0) translateY(0) rotate(0deg);
        opacity: 1;
    }
    50% {
        transform: translateX(20px) translateY(60vh) rotate(540deg);
        opacity: 0.8;
    }
    100% {
        transform: translateX(0) translateY(120vh) rotate(1080deg);
        opacity: 0;
    }
}

/* Changement de couleur cœur : rouge → rose → orange → rouge */
@keyframes hueShift {
    0%   { background: #ff4b5c; }
    25%  { background: #ff6f91; }
    50%  { background: #ff9472; }
    75%  { background: #ffc1a1; }
    100% { background: #ff4b5c; }
}

.heart:nth-child(1)  { left: 5%;  animation-delay: 0s, 0s; }
.heart:nth-child(2)  { left: 15%; animation-delay: 1s, 1s; }
.heart:nth-child(3)  { left: 25%; animation-delay: 0.5s, 0.5s; }
.heart:nth-child(4)  { left: 35%; animation-delay: 1.2s, 1.2s; }
.heart:nth-child(5)  { left: 45%; animation-delay: 0.8s, 0.8s; }
.heart:nth-child(6)  { left: 55%; animation-delay: 1.5s, 1.5s; }
.heart:nth-child(7)  { left: 65%; animation-delay: 0.4s, 0.4s; }
.heart:nth-child(8)  { left: 75%; animation-delay: 1.7s, 1.7s; }
.heart:nth-child(9)  { left: 85%; animation-delay: 0.3s, 0.3s; }
.heart:nth-child(10) { left: 95%; animation-delay: 1.1s, 1.1s; }

.header-title, .header-subtitle {
    position: relative;
    z-index: 3;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.4);
}

.header-title {
    font-size: 52px;
    font-weight: 700;
    margin-bottom: 10px;
}

.header-subtitle {
    font-size: 22px;
    font-weight: 500;
    opacity: 0.9;
}

@keyframes rotateGlow {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes pulseGlow {
    0%, 100% {
        box-shadow: 0 12px 35px rgba(0,0,0,0.4), 0 0 20px 5px rgba(255,255,255,0.2);
    }
    50% {
        box-shadow: 0 12px 50px rgba(0,0,0,0.6), 0 0 35px 10px rgba(255,255,255,0.4);
    }
}
</style>

<div class="header-bar">
    <div class="heart-container">
        <div class="heart"></div>
        <div class="heart"></div>
        <div class="heart"></div>
        <div class="heart"></div>
        <div class="heart"></div>
        <div class="heart"></div>
        <div class="heart"></div>
        <div class="heart"></div>
        <div class="heart"></div>
        <div class="heart"></div>
    </div>
    <div class="header-title">Yamba Arsène GOUBGOU</div>
    <div class="header-subtitle">📈Statistiques-Mathématiques. 💰Economie. 📊Data. 🤖IA. 🌍Impact.</div>
    <div class="header-subtitle">Bienvenu dans mon univers de créativité!</div>
            
</div>
""", unsafe_allow_html=True)

st.markdown("""
<hr style="margin-top: 50px; margin-bottom: 20px;">

<div style="text-align: center; font-size: 24px; padding-bottom: 10px;">
    🌐 Retrouvez-moi aussi sur :
</div>

<div style="display: flex; justify-content: center; gap: 25px; font-size: 28px;">

<div class="social-icons">
    <a href="https://www.linkedin.com/in/yamba-ars%C3%A8ne-goubgou/" target="_blank">🔗</a>
    <a href="https://www.instagram.com/ton-profil-insta/" target="_blank">📸</a>
    <a href="https://www.facebook.com/arsene.goubgou.1">📘</a>
</div>
""", unsafe_allow_html=True)


# --- CSS pour les boutons cliquables ---
st.markdown("""
<style>
.button-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 30px;
    padding-top: 40px;
}

.big-button {
    border: none;
    border-radius: 18px;
    cursor: pointer;
    overflow: hidden;
    box-shadow: 0 6px 25px rgba(0, 0, 0, 0.15);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    width: 100%;
    max-width: 350px;
    height: 260px;
    position: relative;
}

.big-button:hover {
    transform: scale(1.05);
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.25);
}

.big-button img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: brightness(0.7);
}

.button-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    font-size: 22px;
    font-weight: bold;
    text-shadow: 2px 2px 6px #000;
    text-align: center;
    padding: 0 12px;
}
</style>
""", unsafe_allow_html=True)

# --- Accueil effet "wow" avec deux zones cliquables ---
st.markdown("""
    <div style="display: flex; gap: 30px; justify-content: center;">
        <form action="/vie" target="_self">
            <button class="big-button" type="submit">
                <div style="position: relative;">
                    <img src="https://raw.githubusercontent.com/ygoubgou/share.py/refs/heads/master/graphiques/moi.jpg" alt="Portfolio">
                    <div class="button-text">Mon Portfolio</div>
                </div>
            </button>
        </form>
        <form action="app" target="_self">
            <button class="big-button" type="submit">
                <div style="position: relative;">
                    <img src="https://raw.githubusercontent.com/ygoubgou/share.py/refs/heads/master/graphiques/moi_1.jpg" alt="Vie">
                    <div class="button-text">Découvrir Yamba</div>
                </div>
            </button>
        </form>
        <form action="ia" target="_self">
            <button class="big-button" type="submit">
                <div style="position: relative;">
                    <img src="https://raw.githubusercontent.com/ygoubgou/share.py/refs/heads/master/graphiques/IA_image.png" alt="Vie">
                    <div class="button-text">🤖 Mon Agent IA</div>
                </div>
            </button>
        </form>
            

            
    </div>
""", unsafe_allow_html=True)


