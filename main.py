import gradio as gr
import os
import google.generativeai as genai
from dotenv import load_dotenv

class ChatBot_gemi:
    def __init__(self) -> None:
        load_dotenv()  
        self.init_gemini_chat()  

    def init_gemini_chat(self): #inicializacion de gemini
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("La variable de entorno GOOGLE_API_KEY no está configurada.")
        genai.configure(api_key=api_key)
        gemini = genai.GenerativeModel("gemini-pro")
        self.chatbot = gemini.start_chat()
        
    def get_respuesta(self, question: str, conversation: list): #obtencion de respuestas
        response=self.chatbot.send_message(question)
        conversation.append((question,response.text))
        
        return "", conversation
    
    def l_gradio(self): #gradio para interfaz visual
        with gr.Blocks() as demo:
            
            chatbot=gr.Chatbot()
            question=gr.Textbox(label="Hable ahora o calle para siempre")
            clear=gr.ClearButton([question, chatbot])
            
            question.submit(self.get_respuesta, [question, chatbot], [question, chatbot])
            
        demo.launch()
        
        
if __name__ == "__main__":
    a=ChatBot_gemi()
    a.l_gradio()
            
    
            

        