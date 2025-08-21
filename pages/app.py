import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Portfolio Interactif", layout="wide")

# Masquer le menu de navigation standard de Streamlit (pages)
hide_default_menu = """
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
"""
st.markdown(hide_default_menu, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <style>
        .sidebar-container {
            text-align: center;
            padding-top: 10px;
        }
        .sidebar-container img {
            border-radius: 50%;
            width: 300px;
            height: 300px;
            object-fit: cover;
            border: 3px solid #ff6600;
            margin-bottom: 10px;
        }
        .sidebar-container h4 {
            margin-bottom: 5px;
            color: #ff6600;
        }
        .sidebar-container h3 {
            font-size: 18px;
            color: #444;
            margin-bottom: 20px;
        }

        .sidebar-carousel-container {
            width: 100%;
            text-align: center;
            margin-top: 20px;
        }
        .carousel-sidebar-wrapper {
            position: relative;
            width: 90%;
            margin: 0 auto;
            height: 120px;
        }
        .carousel-sidebar-wrapper img.carousel-image {
            width: 100%;
            height: 100px;
            object-fit: contain;
            border-radius: 10px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            transition: opacity 0.6s;
            position: absolute;
            left: 0;
            top: 0;
        }
        .carousel-sidebar-wrapper button {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background-color: rgba(0,0,0,0.4);
            color: white;
            border: none;
            padding: 6px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 14px;
            z-index: 1;
        }
        .carousel-sidebar-wrapper .prev {
            left: -20px;
        }
        .carousel-sidebar-wrapper .next {
            right: -20px;
        }
    </style>

    <div class="sidebar-container">
        <img src="https://raw.githubusercontent.com/ygoubgou/share.py/refs/heads/master/graphiques/moi_1.jpg" alt="Photo de profil">
        <h4>Yamba Arsène GOUBGOU</h4>
        <h3>Économiste quantitatif et data engineer</h3>
    </div>
    <script>
    let sidebarCurrent = 0;
    const sidebarSlides = window.parent.document.querySelectorAll('.carousel-image');

    function showSidebarSlide(index) {
      sidebarSlides.forEach((img, i) => {
        img.style.opacity = i === index ? '1' : '0';
      });
    }
    function changeSidebarSlide(n) {
      sidebarCurrent = (sidebarCurrent + n + sidebarSlides.length) % sidebarSlides.length;
      showSidebarSlide(sidebarCurrent);
    }
    setInterval(() => changeSidebarSlide(1), 5000);
    </script>
    """, unsafe_allow_html=True)
import base64

# Charger ton fichier PDF
with st.sidebar:
    with open("cv/CV_YAMBA_BASE.pdf", "rb") as f:
        cv_bytes = f.read()
        cv_base64 = base64.b64encode(cv_bytes).decode()

    # CSS + bouton stylé dans la sidebar
    st.markdown(f"""
        <style>
            .sidebar-download {{
                background-color: #e0f0ff;
                padding: 10px;
                text-align: center;
                border-radius: 10px;
                margin-top: 20px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}
            .sidebar-download a {{
                display: inline-block;
                color: #0077cc;
                font-weight: 600;
                text-decoration: none;
                padding: 8px 16px;
                border: 2px solid #0077cc;
                border-radius: 6px;
                transition: all 0.3s ease;
                background-color: white;
            }}
            .sidebar-download a:hover {{
                background-color: #0077cc;
                color: white;
            }}
        </style>
        <div class="sidebar-download">
            <a href="data:application/pdf;base64,{cv_base64}" download="CV_Yamba_Arsene_GOUBGOU.pdf">
                📄 Télécharger mon CV
            </a>
        </div>
    """, unsafe_allow_html=True)


with st.sidebar:
    #st.markdown("---")
    #st.markdown("### 🔙 Revenir à l'accueil")

    st.markdown("""
        <a href="/" target="_self">
            <button style="padding:10px 20px; font-size:16px; border-radius:8px; background-color:#4CAF50; color:white; border:none; cursor:pointer;">
                🏠 Retour à l'accueil
            </button>
        </a>
    """, unsafe_allow_html=True)

# --- CSS personnalisé ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    h1, h2, h3 {
        color: #ff6600;
    }
    .carousel {
        display: flex;
        overflow-x: auto;
        scroll-behavior: smooth;
    }
    .carousel img {
        height: 300px;
        margin-right: 10px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Menu horizontal en haut de page ---
selected = option_menu(
    menu_title=None,
    options=["Accueil", "Projets","Formation", "Références",  "Contact"],
    icons=["house", "briefcase", "people", "book", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

# --- Page Accueil ---
if selected == "Accueil":
    st.markdown("""
        <style>
        .animated-title {
            font-size: 3em;
            font-weight: bold;
            background: linear-gradient(90deg, #FFA500, #00BFFF);
            -webkit-background-clip: text;
            color: transparent;
            animation: slide 3s ease-in-out infinite alternate;
            text-align: center;
        }

        @keyframes slide {
            0% { letter-spacing: 1px; }
            100% { letter-spacing: 5px; }
        }

        .bio-box {
            background-color: #f9f9f9;
            border-left: 5px solid #00BFFF;
            padding: 1.2em;
            border-radius: 10px;
            font-size: 1.1em;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }

        .warning-custom {
            background-color: #fff8e1;
            border-left: 5px solid #FFA500;
            padding: 1.2em;
            border-radius: 10px;
            margin-top: 20px;
            font-size: 1.05em;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }
        </style>
        <div class="animated-title">Bienvenue sur mon portfolio</div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="bio-box">
        Je suis <strong>Yamba Arsène GOUBGOU</strong>, <em>économiste quantitatif</em>, <em>ingénieur data & analyste</em>, passionné par la programmation et l’analyse de données.<br><br>
        Ce portfolio interactif vous invite à explorer mes <strong>projets</strong>, <strong>références</strong> et mon <strong>parcours professionnel</strong>.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="warning-custom">
        J’aime concevoir des solutions élégantes à des problèmes complexes à la croisée de l’économie, de la data science et de l’ingénierie logicielle.
        </div>
    """, unsafe_allow_html=True)

    components.html("""
    <div style="margin-top: 30px; display: flex; justify-content: center;">
    <div style="position: relative; width: 90%; max-width: 800px; height: 420px; overflow: hidden; border-radius: 15px; box-shadow: 0 4px 16px rgba(0,0,0,0.15); background-color: #f9f9f9;">
        <img class="carousel-image" src="https://raw.githubusercontent.com/ygoubgou/share.py/refs/heads/master/graphiques/certification_1.png" style="width: 100%; height: 100%; object-fit: contain; position: absolute; transition: opacity 1s;" />
        <img class="carousel-image" src="https://raw.githubusercontent.com/ygoubgou/share.py/refs/heads/master/graphiques/certification_2.png" style="width: 100%; height: 100%; object-fit: contain; position: absolute; opacity: 0; transition: opacity 1s;" />
        <img class="carousel-image" src="https://raw.githubusercontent.com/ygoubgou/share.py/refs/heads/master/graphiques/certification_3.png" style="width: 100%; height: 100%; object-fit: contain; position: absolute; opacity: 0; transition: opacity 1s;" />

        <button onclick="changeSlide(-1)" style="position: absolute; top: 50%; left: 15px; transform: translateY(-50%); background-color: rgba(255,255,255,0.7); color: black; border: none; padding: 10px; border-radius: 50%; cursor: pointer; font-size: 1.2em;">❮</button>
        <button onclick="changeSlide(1)" style="position: absolute; top: 50%; right: 15px; transform: translateY(-50%); background-color: rgba(255,255,255,0.7); color: black; border: none; padding: 10px; border-radius: 50%; cursor: pointer; font-size: 1.2em;">❯</button>

        <div id="carousel-dots" style="position: absolute; bottom: 10px; width: 100%; display: flex; justify-content: center; gap: 10px;">
        <span class="dot" onclick="goToSlide(0)" style="width: 12px; height: 12px; border-radius: 50%; background: #ccc; display: inline-block; cursor: pointer;"></span>
        <span class="dot" onclick="goToSlide(1)" style="width: 12px; height: 12px; border-radius: 50%; background: #ccc; display: inline-block; cursor: pointer;"></span>
        <span class="dot" onclick="goToSlide(2)" style="width: 12px; height: 12px; border-radius: 50%; background: #ccc; display: inline-block; cursor: pointer;"></span>
        </div>
    </div>
    </div>

    <script>
    let currentSlide = 0;
    const slides = document.getElementsByClassName('carousel-image');
    const dots = document.getElementsByClassName('dot');

    function showSlide(index) {
        for (let i = 0; i < slides.length; i++) {
        slides[i].style.opacity = '0';
        dots[i].style.background = '#ccc';
        }
        slides[index].style.opacity = '1';
        dots[index].style.background = '#007BFF';
    }

    function changeSlide(n) {
        currentSlide = (currentSlide + n + slides.length) % slides.length;
        showSlide(currentSlide);
    }

    function goToSlide(n) {
        currentSlide = n;
        showSlide(currentSlide);
    }

    // Auto slide
    setInterval(() => changeSlide(1), 5000);
    showSlide(currentSlide);
    </script>
    """, height=460)


# --- Page Projets ---
elif selected == "Projets":
    st.header("📁 Quelques projets réalisés")
    st.markdown("Voici une sélection de projets personnels illustrant mes compétences en **data science**, **modélisation statistique** et **visualisation interactive** :")

    projets = [
        {
            "nom": "🧓 Évaluation d'impact du veuvage",
            "desc": """
**Objectif :** Évaluer l'impact du veuvage sur les personnes âgées en Europe.  
**Méthodes utilisées :** Machine Learning, approche de type Difference-in-Differences (DiD), données socioéconomiques issues d'enquêtes européennes.  
🔗 [Accéder à l'application Streamlit](https://dossierdiscriminationmarchedutravail.streamlit.app/)
""",
            "img": "https://raw.githubusercontent.com/ygoubgou/share.py/refs/heads/master/graphiques/veuvage.jpg",
            "lien": None
        },
        {
            "nom": "🚗 Estimation du prix des véhicules",
            "desc": """
**Objectif :** Prédire le prix de véhicules d'occasion en France à partir de leurs caractéristiques.  
**Méthodes utilisées :** Web scraping, analyse statistique, modèles de régression avancés.  
🔗 [Accéder à l'application Streamlit](https://ygoubgou-algopy-projetsalgopydossier-pyapp-ifqtbh.streamlit.app/)
""",
            "img": "https://raw.githubusercontent.com/ygoubgou/share.py/refs/heads/master/graphiques/voitures.png",
            "lien": "https://ygoubgou-algopy-projetsalgopydossier-pyapp-ifqtbh.streamlit.app/"
        },
        {
            "nom": "📉 Prédiction du taux de chômage",
            "desc": """
**Objectif :** Estimer le taux de chômage en France métropolitaine.  
**Méthodes utilisées :** Séries temporelles (SARIMA), traitement de données macroéconomiques, modélisation prédictive.
""",
            "img": "https://raw.githubusercontent.com/ygoubgou/share.py/refs/heads/master/graphiques/chomage.png",
            "lien": None
        },
        {
            "nom": "🚦 Analyse des accidents de la route",
            "desc": """
**Objectif :** Construire un pipeline complet pour analyser et prédire la gravité des accidents de la route en France.  
**Méthodes utilisées :**  
- Économétrie (Logit/Probit ordonné, Poisson) pour les déterminants de la gravité  
- Machine Learning (Random Forest, XGBoost, KNN) pour la prédiction  
- Base de données **PostgreSQL** hébergée sur le cloud pour stocker les données  
- Automatisation des **visualisations interactives** (Dash / Streamlit) connectées à la BDD.  
🔗 [Accéder à l'application Streamlit](https://securiteroutiere-yamba.streamlit.app/)
""",
            "img": "https://github.com/ygoubgou/prive_moi/blob/private/Images/im.png",
            "lien": None
        }
    ]

    for projet in projets:
        st.markdown("----")
        st.subheader(projet["nom"])
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(projet["img"], use_container_width=True)
        with col2:
            st.markdown(projet["desc"])
    st.markdown("----")

# --- Page Références ---
elif selected == "Références":
    st.header("👥 Références")
    references = [
        {"nom": "Hamidou Traoré", "poste": "Developpeur full stack", "citation": "Une personne créative, rigoureuse, gentille et toujours force de proposition."},
        {"nom": "Pauline Pedehour", "poste": "Enseignante chercheuse", "citation": "Une excellente enseignante, capable de résoudre des problèmes complexes avec élégance."},
        {"nom": "Alexandre Tolub", "poste": "Directeur conseil et innovation chez CerFrance", "citation": "Un modèle de personnalité!"}
    ]
    for ref in references:
        st.subheader(f"{ref['nom']} - {ref['poste']}")
        st.write(f"\"{ref['citation']}\"")
        st.markdown("---")

# --- Page Contact ---
elif selected == "Contact":
    st.header("📨 Me contacter")

    # Point d'envoi Formspree (remplace par le tien !)
    formspree_url = "https://formspree.io/f/xblyvplw"  
    # Code HTML brut du formulaire
    contact_form = f"""
    <form action="{formspree_url}" method="POST">
        <input type="text" name="name" placeholder="Votre nom" required style="width: 100%; padding: 10px; margin-bottom: 10px;">
        <input type="email" name="email" placeholder="Votre email" required style="width: 100%; padding: 10px; margin-bottom: 10px;">
        <textarea name="message" placeholder="Votre message" required style="width: 100%; height: 150px; padding: 10px; margin-bottom: 10px;"></textarea>
        <button type="submit" style="background-color:#ff6600; color:white; padding:10px 20px; border:none; border-radius:5px;">Envoyer</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)


elif selected == "Formation":
    st.header("🎓 Formation & Expériences")

    st.subheader("📚 Formation académique")
    st.markdown("""
- **Mastère Spécialisé MQDEF**, ENSAE Paris *(2025 - 2026)*  
  *Modélisation et Méthodes Quantitatives pour la Décision Économique et Financière*

- **Master 2 Économie Appliquée - Parcours Ingénierie des Données**, Université d'Angers  
  *Major de promotion – Mention Bien*

- **Licence en Sciences Économiques**, Université de Ouagadougou

- **Certifications** :
  -  Data Engineering (traitement de données massives, pipelines ETL)
  -  Machine Learning (scikit-learn, modélisation supervisée & non supervisée)
  -  Statistiques & Probabilités appliquées à l’analyse économique
    """)

    st.markdown("---")

    st.subheader("💼 Expériences professionnelles")
    st.markdown("""
- **Data Engineer & Data Analyst**, *Cerfrance Loire-Atlantique* *(Avril 2025 - aujourd’hui)*  
  Conception de pipelines de données, automatisation de reporting, accompagnement des conseillers sur l’exploitation de la donnée métier (Power BI, Excel VBA, Python).

- **Tuteur en Mathématiques & Probabilités**, *Université d'Angers* *(2023 - 2024)*  
  Encadrement personnalisé d’étudiants de Licence et Master.  
  Animation d’ateliers de remise à niveau en statistiques, calcul différentiel, lois de probabilité et estimation.
    """)

    st.markdown("----")
