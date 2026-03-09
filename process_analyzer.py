print("Program started")
import requests

url = "http://localhost:1234/v1/chat/completions"

headers = {
    "Content-Type": "application/json"
}

process = input("Describe a business process: ")

data = {
 "model": "local-model",
 "messages": [
   {"role": "system", "content": "You are an expert in business process improvement and automation."},
   {"role": "user", "content": f"Analyze this process and suggest improvements and automation opportunities: {process}"}
 ]
}

response = requests.post(url, headers=headers, json=data)

result = response.json()

print("\nAI analysis:\n")
print(result["choices"][0]["message"]["content"])