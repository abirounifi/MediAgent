from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
import os

def analyser_symptomes(symptomes: str, llm: ChatGroq) -> str:
    prompt = f"""
    Tu es un expert médical spécialisé dans l'analyse des symptômes.
    
    Le patient décrit ses symptômes : "{symptomes}"
    
    Analyse ces symptômes et identifie :
    1. Les symptômes principaux
    2. La durée possible
    3. La gravité estimée (légère, modérée, grave)
    
    Réponds en français de manière claire et structurée.
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content