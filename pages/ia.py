import streamlit as st

st.set_page_config(page_title="Accueil - Mon Portfolio", layout="wide")

hide_default_menu = """
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
"""
st.markdown(hide_default_menu, unsafe_allow_html=True)

st.markdown("en cours")
st.stop()

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
                url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1470&q=80') no-repeat center center/cover;
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
        <p>Développeur passionné | Data Scientist | Créateur de solutions innovantes</p>
        <a href="#about" class="cta-btn">Découvrir mon parcours</a>
    </div>
</div>
""", unsafe_allow_html=True)


# --- Carousel ---
images = [
    "https://picsum.photos/id/1018/900/400",
    "https://picsum.photos/id/1015/900/400",
    "https://picsum.photos/id/1019/900/400",
    "https://picsum.photos/id/1020/900/400"
]

carousel_html = """
<div class="carousel" id="carousel">
"""

for i, img in enumerate(images):
    active_class = "active" if i == 0 else ""
    carousel_html += f'<img src="{img}" class="{active_class}">'

carousel_html += "</div>"

st.markdown(carousel_html, unsafe_allow_html=True)

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
            <p>Maîtrise de Python, data science, machine learning, et développement web.</p>
        </div>
        <div class="feature">
            <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/></svg>
            <h4>Créativité</h4>
            <p>Solutions innovantes adaptées aux besoins spécifiques.</p>
        </div>
        <div class="feature">
            <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 2 L15 8 L21 9 L17 14 L18 21 L12 18 L6 21 L7 14 L3 9 L9 8 Z"/></svg>
            <h4>Engagement</h4>
            <p>Travail rigoureux et communication claire avec les équipes.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
