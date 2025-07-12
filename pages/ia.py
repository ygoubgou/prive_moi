import streamlit as st

st.set_page_config(
    page_title="Maintenance",
    page_icon="🛠️",
    layout="centered"
)
# --- Masquer le menu Streamlit ---
hide_default_menu = """
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
"""
st.markdown(hide_default_menu, unsafe_allow_html=True)


st.markdown(
    """
    <style>
        /* Fond dégradé doux */
        body, html, [class*="css"] {
            height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #ff7e5f, #feb47b);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #fff;
        }

        /* Conteneur glassmorphism */
        .glass-container {
            background: rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            padding: 3rem 4rem;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.18);
            max-width: 480px;
            text-align: center;
        }

        /* Titre clignotant en couleur */
        h1 {
            font-size: 3.4rem;
            margin-bottom: 0.3rem;
            font-weight: 800;
            letter-spacing: 0.06em;
            color: #00d4ff;
            animation: blinkColor 1.8s ease-in-out infinite;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
        }

        @keyframes blinkColor {
            0%, 100% {
                color: #00d4ff;
                text-shadow: 0 0 10px rgba(0, 212, 255, 0.8);
            }
            50% {
                color: #ffffff;
                text-shadow: 0 0 18px rgba(255, 255, 255, 1);
            }
        }

        p {
            font-size: 1.3rem;
            margin-bottom: 2rem;
            font-weight: 500;
            letter-spacing: 0.03em;
            line-height: 1.5;
            text-shadow: 0 1px 5px rgba(0,0,0,0.15);
        }

        .loader {
            border: 6px solid rgba(255, 255, 255, 0.3);
            border-top: 6px solid #fff;
            border-radius: 50%;
            width: 56px;
            height: 56px;
            margin: 0 auto;
            animation: spin 1.4s linear infinite;
            box-shadow: 0 0 12px rgba(255, 255, 255, 0.5);
        }

        @keyframes spin {
            0% { transform: rotate(0deg);}
            100% { transform: rotate(360deg);}
        }

        @media (max-width: 480px) {
            .glass-container {
                padding: 2rem 2.5rem;
                max-width: 90vw;
            }
            h1 {
                font-size: 2.6rem;
            }
            p {
                font-size: 1.1rem;
            }
            .loader {
                width: 48px;
                height: 48px;
            }
        }
    </style>

    <div class="glass-container">
        <h1>🛠️ Maintenance en cours</h1>
        <p>Merci de revenir bientôt.<br>Nous préparons quelque chose d’exceptionnel pour vous !</p>
        <div class="loader"></div>
    </div>
    """,
    unsafe_allow_html=True
)
