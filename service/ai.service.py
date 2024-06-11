#AIzaSyABDszSxCMbD_Fhn0JViUj1GnjQafHWpDg  APIKEY AI STUDIO

# import os
# import google.generativeai as genai

# # Configurar la API Key de Google Generative AI
# genai.configure(api_key=os.environ['AIzaSyABDszSxCMbD_Fhn0JViUj1GnjQafHWpDg'])

# # Configuración del modelo
# generation_config = {
#   "temperature": 0.9,
#   "top_p": 1,
#   "top_k": 0,
#   "max_output_tokens": 2048,
#   "response_mime_type": "text/plain",
# }

# model = genai.GenerativeModel(
#   model_name="gemini-1.0-pro",
#   generation_config=generation_config,
# )

# def generate_recommendations(resultados):
#     prompt = f"Based on the following results: {resultados}, provide personalized study recommendations."
#     response = model.generate_content([
#         "input: " + prompt,
#         "output: ",
#     ])
#     recommendations = response.text.strip()
#     return recommendations.split('\n')  # Suponiendo que las recomendaciones se proporcionan como una lista
