import paralleldots
# Setting your API key

class API:

    def __init__(self):
        paralleldots.set_api_key('h8bJrhEBt9h4g2HuDB0MR0kzi9aUtqkNCB1YSUzRY5g')

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def ner(self,text):
        response=paralleldots.ner(text)
        return response

    def emotion_prediction(self,text):
        response= paralleldots.emotion(text)
        return response
    

# obj=API()
# print(obj.ner('India'))
    

