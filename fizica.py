import os
from dotenv import load_dotenv 
import openai    #   bilbioteca/modulul  *openai* ,componenta software care oferă funcționalitățile necesare pentru a interacționa cu serviciile OpenAI.
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
messages = [ {"role": "system", "content":" Esti profesor de fizica. Ajuta elevul cu ce te intreaba numai despre fizica, nu altceva. Raspunde in romana."} ]
while True:        # Acesta este un ciclu while care rulează în mod continuu, până când este oprit explicit prin utilizarea unei instrucțiuni "break"              
	message = input("Intrebarea dumneavoastra despre fizica: ")   # variabila caruia ii atribuim intrebarea elevului/userului
	if message:     #cat timp a scris useru/elevu
		messages.append(      #ce ii este scris lui gpt, o sa fie lipita si partea pe care o va scrie useru in output
			{"role": "user", "content": message},
		)
		chat = openai.ChatCompletion.create(                      #se creeaza chatu pt gpt, iar linia messages=messages se refera ca baga in chat parametrul messages care contine messages vechi si message scris de user
			model="gpt-3.5-turbo", messages=messages
		)
	reply = chat.choices[0].message.content         #Aici se extrage răspunsul generat de ChatGPT din obiectul "chat". Se obține conținutul mesajului de la prima opțiune de răspuns și se stochează în variabila "reply".
	print(f"Prof virtual: {reply}")                      # Acesta este un afișaj simplu care printează răspunsul generat de ChatGPT.
	messages.append({"role": "assistant", "content": reply})         # joacă un rol important în actualizarea listei messages cu răspunsul asistentului generat de modelul GPT-3.5 Turbo, asigurând continuitatea și coerența conversației.
