from langchain_groq import ChatGroq
from langchain.schema import HumanMessage

def donner_conseil(symptomes: str, analyse: str, diagnostic: str, llm: ChatGroq) -> str:
    prompt = f"""
    Tu es un conseiller médical bienveillant.
    
    Symptômes du patient : "{symptomes}"
    Analyse des symptômes : "{analyse}"
    Diagnostic possible : "{diagnostic}"
    
    Donne des conseils pratiques :
    1. Ce que le patient peut faire immédiatement
    2. Les médicaments sans ordonnance possibles
    3. Quand consulter un médecin en urgence
    4. Les habitudes à adopter pour aller mieux
    
    Réponds en français avec bienveillance.
    Rappelle toujours de consulter un médecin pour un vrai diagnostic.
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content