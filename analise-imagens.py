from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import json

#configuracoes

endpoint = 'https://csantosimagens.cognitiveservices.azure.com/'
key = '35933288d9c945acbd27c04b23e55c4f'
credentials = CognitiveServicesCredentials(key)
client = ComputerVisionClient(endpoint, credentials)


def analisa_image(url):
    language = "pt"
    max_descriptions = 3
    descricao =[]

    analise = client.describe_image(url, max_descriptions, language)

    for item in analise.captions:
         descricao.extend((item.text, round(item.confidence,2)))
    
    json_data = {
            'descricao' : descricao
        }
    print(json.dumps(json_data))
        
url = "https://blog.bemmaisseguro.com/wp-content/uploads/2014/12/seguro-viagem-bemmaisseguro.com_.jpg"
analisa_image(url)