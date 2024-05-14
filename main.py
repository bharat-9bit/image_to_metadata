import json
from paddleocr import PaddleOCR
import ollama

def ocr_with_paddle(img):
    finaltext = ''
    ocr = PaddleOCR(lang='en', use_angle_cls=True)
    result = ocr.ocr(img)
    
    for i in range(len(result[0])):
        text = result[0][i][1][0]
        finaltext += ' '+ text
    print(finaltext)    
    return finaltext
    
def main(finaltext):
    prompt = f"Please provide the following details:name: ,person_job_postion: ,company_name: ,phone_numbers: ,email: ,address: ,website_url: ,services_provided: ,description: {finaltext}"

    response = ollama.chat(
        model="llama3",
        format="json",
        stream=False,
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    # Parse the nested JSON within the "content" field
    nested_json = json.loads(response["message"]["content"])
    print(nested_json)
    # Combine the nested JSON with the main JSON output
    json_output = json.dumps({"Contact Information": nested_json}, indent=4)
    print(json_output)
    return {"answer": json_output}

img = 'images/uttam.jpg'
finaltext = ocr_with_paddle(img)
main(finaltext)