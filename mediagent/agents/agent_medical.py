from langchain_groq import ChatGroq
from langchain.schema import HumanMessage

def consulter_base_medicale(symptomes: str, llm: ChatGroq) -> str:
    prompt = f"""
    Tu es un médecin généraliste avec accès à une base de données médicale.
    
    Symptômes analysés : "{symptomes}"
    
    Sur la base de ces symptômes, identifie :
    1. Les maladies ou conditions possibles (2 ou 3 maximum)
    2. Les causes les plus probables
    3. Les examens médicaux recommandés
    
    Réponds en français de manière claire.
    Rappelle toujours que ceci n'est pas un diagnostic médical officiel.
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content