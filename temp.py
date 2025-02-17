from llm.Gemini import Gemini,t

while 1:
    prompt=input(">>> ")

    C=t()
    result=Gemini(prompt)
    print(t()-C)

    print(result)