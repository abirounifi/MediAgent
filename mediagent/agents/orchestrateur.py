from langchain_groq import ChatGroq
from agents.agent_symptomes import analyser_symptomes
from agents.agent_medical import consulter_base_medicale
from agents.agent_conseil import donner_conseil
import os

def lancer_systeme_multi_agent(message_utilisateur: str) -> dict:
    
    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.3-70b-versatile"
    )
    
    # Étape 1 : Agent symptômes analyse le message
    analyse = analyser_symptomes(message_utilisateur, llm)
    
    # Étape 2 : Agent médical consulte la base médicale
    diagnostic = consulter_base_medicale(analyse, llm)
    
    # Étape 3 : Agent conseil génère une recommandation
    conseil = donner_conseil(message_utilisateur, analyse, diagnostic, llm)
    
    return {
        "analyse": analyse,
        "diagnostic": diagnostic,
        "conseil": conseil
    }