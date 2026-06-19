def main():
    text= input()
    result= convert(text)
    print(result)

def convert(text):
    text= text.replace(":)","😊")
    text= text.replace(":(","😒")
    return text

main()
