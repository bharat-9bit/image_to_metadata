# from paddleocr import PaddleOCR 
# import ollama

# def ocr_with_paddle(img):
#     finaltext = ''
#     ocr = PaddleOCR(lang='en', use_angle_cls=True)
#     result = ocr.ocr(img)
    
#     for i in range(len(result[0])):
#         text = result[0][i][1][0]
#         finaltext += ' '+ text
#     print(finaltext)
#     print(type(finaltext))    
#     return finaltext
    


# def main(finaltext):
#     SYSTEM_PROMPT = """You are a helpful reading assistant who answers questions 
#         based on snippets of text provided in context. Answer only using the context provided, 
#         being as concise as possible. If you're unsure, just say that you don't know.
#         Context:
#     """
#     prompt = 'Identify the Name, Email , Number , Company Name ,and if comapany slogan, address and website is presnt so also mention and if not then mention'

#     response = ollama.chat(
#         model= "llama3",
#         messages=[
#             {
#                 "role": "system",
#                 "content": SYSTEM_PROMPT
#                 + "\n".join(finaltext),
#             },
#             {"role": "user", "content": prompt},
#         ],
#     )

#     print(response["message"])
#     return {"answer": response["message"]}

# img = 'airtel.jpg'
# finaltext = ocr_with_paddle(img)
# main(finaltext)

# from paddleocr import PaddleOCR 
# import ollama

# def ocr_with_paddle(img):
#     finaltext = ''
#     ocr = PaddleOCR(lang='en', use_angle_cls=True)
#     result = ocr.ocr(img)
    
#     for i in range(len(result[0])):
#         text = result[0][i][1][0]
#         finaltext += ' '+ text
#     print(finaltext)    
#     return finaltext
    
# def main(finaltext):
#     prompt = f"Given the extracted text from the image, please provide the following details in a structured format.{finaltext}"


#     response = ollama.chat(
#         model="llama3",
#         format="json",
#         stream=False,
#         messages=[
#             {"role": "user", "content": prompt},
#         ],
#     )
#     output = ({"Contact Information": response["message"]})
#     # print(response["message"])
#     print(output)
#     return {"answer": response["message"]}

# img = 'images/teleIt.jpg'
# finaltext = ocr_with_paddle(img)
# main(finaltext)

########################################################################################
# import json
# from paddleocr import PaddleOCR
# import ollama

# def ocr_with_paddle(img):
#     finaltext = ''
#     ocr = PaddleOCR(lang='en', use_angle_cls=True)
#     result = ocr.ocr(img)
    
#     for i in range(len(result[0])):
#         text = result[0][i][1][0]
#         finaltext += ' '+ text
#     print(finaltext)    
#     return finaltext
    
# def main(finaltext):
#     prompt = f"Given the extracted text from the image, please provide the following details in a structured format.{finaltext}"

#     response = ollama.chat(
#         model="dolphin-phi",
#         format="json",
#         stream=False,
#         messages=[
#             {"role": "user", "content": prompt},
#         ],
#     )
#     # Parse the nested JSON within the "content" field
#     nested_json = json.loads(response["message"]["content"])
#     # Combine the nested JSON with the main JSON output
#     json_output = json.dumps({"Contact Information": nested_json}, indent=4)
#     print(json_output)
#     return {"answer": json_output}

# img = 'images/bharti_airtel.jpg'
# finaltext = ocr_with_paddle(img)
# main(finaltext)
############################################################################################

