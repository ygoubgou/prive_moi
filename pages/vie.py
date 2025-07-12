import streamlit as st
import time

st.set_page_config(page_title="Ma Vie", layout="wide")

hide_sidebar_style = """
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)


#st.markdown("---")
#st.markdown("### 🔙 Revenir à l'accueil")

st.markdown("""
    <a href="/" target="_self">
        <button style="padding:10px 20px; font-size:16px; border-radius:8px; background-color:#4CAF50; color:white; border:none; cursor:pointer;">
            🏠 Retour à l'accueil
        </button>
    </a>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #FF914D;'>📸 Tout savoir sur <span style='color:#4FC3F7;'>Yamba</span> en image</h1>", unsafe_allow_html=True)


#st.write("Bienvenue dans la section où je partage mon parcours personnel, mes passions et mes expériences !")

# --- CSS personnalisé ---
st.markdown("""
<style>
/* Reset et body */
body, .main {
    background-color: #f0f8ff;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0; padding: 0;
}

/* Hero Section */
.hero {
    position: relative;
    height: 600px;
    background: linear-gradient(rgba(0,55,102,0.6), rgba(0,55,102,0.6)),
                url('https://raw.githubusercontent.com/ygoubgou/share.py/refs/heads/master/graphiques/moi_1.jpg') no-repeat center center/cover;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    text-align: center;
    padding: 0 20px;
}

.hero h1 {
    font-size: 64px;
    font-weight: 900;
    margin-bottom: 20px;
    text-shadow: 2px 2px 10px rgba(0,0,0,0.7);
}

.hero p {
    font-size: 24px;
    margin-bottom: 40px;
    font-weight: 400;
    text-shadow: 1px 1px 8px rgba(0,0,0,0.5);
}

/* Call to Action Button */
.cta-btn {
    background-color: #ff6600;
    color: white;
    font-size: 22px;
    padding: 15px 50px;
    border-radius: 40px;
    font-weight: 700;
    cursor: pointer;
    border: none;
    box-shadow: 0 5px 15px rgba(255,102,0,0.6);
    transition: background-color 0.3s ease, transform 0.3s ease;
    text-decoration: none;
    display: inline-block;
}

.cta-btn:hover {
    background-color: #e65500;
    transform: scale(1.05);
    box-shadow: 0 7px 20px rgba(230,85,0,0.8);
}

/* Carousel container */
.carousel {
    margin: 60px auto;
    max-width: 900px;
    position: relative;
    overflow: hidden;
    border-radius: 15px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.15);
}

/* Carousel images */
.carousel img {
    width: 100%;
    height: 400px;
    object-fit: cover;
    display: none;
    border-radius: 15px;
    transition: opacity 1s ease-in-out;
}

.carousel img.active {
    display: block;
    opacity: 1;
}

/* About Section */
.about {
    max-width: 900px;
    margin: 60px auto 100px;
    padding: 0 20px;
    text-align: center;
}

.about h2 {
    font-size: 38px;
    color: #003766;
    margin-bottom: 40px;
    font-weight: 800;
}

.about p {
    font-size: 20px;
    line-height: 1.6;
    color: #333;
    margin-bottom: 40px;
}

/* Features icons container */
.features {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 40px;
}

.feature {
    max-width: 200px;
    color: #ff6600;
}

.feature svg {
    width: 60px;
    height: 60px;
    margin-bottom: 20px;
}

.feature h4 {
    font-size: 20px;
    color: #003766;
    margin-bottom: 10px;
    font-weight: 700;
}

.feature p {
    font-size: 16px;
    color: #555;
}

/* Responsive */
@media (max-width: 768px) {
    .hero h1 {
        font-size: 42px;
    }
    .hero p {
        font-size: 18px;
    }
    .carousel img {
        height: 250px;
    }
    .features {
        flex-direction: column;
        align-items: center;
    }
}
</style>
""", unsafe_allow_html=True)

# --- HTML Hero Section ---
st.markdown("""
<div class="hero">
    <div>
        <h1>Bienvenue sur mon Portfolio</h1>
        <p>Economiste-Statisticien | Data Scientist | Créateur de solutions innovantes</p>
        <a href="#about" class="cta-btn">Découvrir mon parcours</a>
    </div>
</div>
""", unsafe_allow_html=True)



# --- Script pour animer le carousel ---
st.markdown("""
<script>
let currentIndex = 0;
const slides = document.querySelectorAll('#carousel img');
if (slides.length > 0) {
    setInterval(() => {
        slides[currentIndex].classList.remove('active');
        currentIndex = (currentIndex + 1) % slides.length;
        slides[currentIndex].classList.add('active');
    }, 3500);
}
</script>
""", unsafe_allow_html=True)


# --- About Section ---
st.markdown("""
<div class="about" id="about">
    <h2>À propos de moi</h2>
    <p>Je suis un professionnel passionné par les technologies modernes et l'analyse des données, toujours prêt à relever de nouveaux défis et à créer des projets innovants.</p>
    <div class="features">
        <div class="feature">
            <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/></svg>
            <h4>Expertise Technique</h4>
            <p>Maîtrise de Python, statistiques, mathématiques, data science, machine learning, et développement web avec python.</p>
        </div>
        <div class="feature">
            <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/></svg>
            <h4>Forte créativité</h4>
            <p>Solutions innovantes adaptées aux besoins spécifiques, selon vos demandes.</p>
        </div>
        <div class="feature">
            <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 2 L15 8 L21 9 L17 14 L18 21 L12 18 L6 21 L7 14 L3 9 L9 8 Z"/></svg>
            <h4>Engagement total</h4>
            <p>Travail rigoureux et communication claire avec les équipes.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Liste d'URLs par défaut (tu pourras les changer)
images = [
    "https://raw.githubusercontent.com/ygoubgou/share.py/refs/heads/master/graphiques/moi_1.jpg",
    "https://raw.githubusercontent.com/ygoubgou/share.py/refs/heads/master/graphiques/moi_2.jpg",
    "https://raw.githubusercontent.com/ygoubgou/share.py/refs/heads/master/graphiques/moi.jpg",
    "https://raw.githubusercontent.com/ygoubgou/share.py/refs/heads/master/graphiques/IA_image.png"
]

# Initialise le compteur dans session_state si pas existant
if "image_index" not in st.session_state:
    st.session_state.image_index = 0
else:
    # Passe à l'image suivante
    st.session_state.image_index = (st.session_state.image_index + 1) % len(images)

# Affiche l'image courante
st.markdown(f"""
    <div style="text-align: center;">
        <img src="{images[st.session_state.image_index]}" width="900" style="border-radius:15px; box-shadow: 0 8px 20px rgba(0,0,0,0.2);" />
    </div>
""", unsafe_allow_html=True)

# Pause avant rafraîchissement
time.sleep(3)

# Relance le script pour changer d'image
st.rerun()


