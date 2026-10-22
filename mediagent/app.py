import streamlit as st
from dotenv import load_dotenv
import os
from agents.orchestrateur import lancer_systeme_multi_agent

load_dotenv()

st.set_page_config(
    page_title="MediAgent",
    page_icon="🏥",
    layout="wide"
)

# Barre latérale
with st.sidebar:
    st.image("https://img.icons8.com/color/96/caduceus.png", width=80)
    st.title("MediAgent")
    st.markdown("---")
    st.markdown("### 🤖 Les 3 agents")
    st.success("🔍 Agent Symptômes")
    st.info("🏥 Agent Médical")
    st.warning("💊 Agent Conseil")
    st.markdown("---")
    st.caption("⚠️ Ceci n'est pas un diagnostic médical officiel. Consultez toujours un médecin.")
    if st.button("🗑️ Effacer la conversation"):
        st.session_state.messages = []
        st.rerun()

# Titre principal
st.title("🏥 MediAgent — Assistant Biomédical")
st.caption("Système multi-agent intelligent • Décrivez vos symptômes ci-dessous")
st.markdown("---")

# Historique
if "messages" not in st.session_state:
    st.session_state.messages = []

# Message de bienvenue
if len(st.session_state.messages) == 0:
    st.info("👋 Bonjour ! Décrivez vos symptômes et nos 3 agents vont les analyser ensemble.")

# Affichage des messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Saisie utilisateur
if prompt := st.chat_input("Ex: j'ai mal à la tête et de la fièvre depuis 2 jours..."):

    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("🔄 Les 3 agents analysent votre message..."):
            resultats = lancer_systeme_multi_agent(prompt)

        # Agent 1
        with st.expander("🔍 Agent Symptômes — Analyse", expanded=True):
            st.success(resultats["analyse"])

        # Agent 2
        with st.expander("🏥 Agent Médical — Diagnostic possible", expanded=True):
            st.info(resultats["diagnostic"])

        # Agent 3
        with st.expander("💊 Agent Conseil — Recommandations", expanded=True):
            st.warning(resultats["conseil"])

    reponse_complete = f"""
🔍 **Analyse :** {resultats["analyse"]}

🏥 **Diagnostic :** {resultats["diagnostic"]}

💊 **Conseils :** {resultats["conseil"]}
"""
    st.session_state.messages.append({"role": "assistant", "content": reponse_complete})