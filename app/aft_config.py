import africastalking

from django.conf import settings

aft_config : dict = settings.AFRICASTALKING

def check_config(): 
    if(aft_config.get("USERNAME", None) == None):
        raise Exception(
            """Africa's Talking username has not been configured 
            consider adding 
            
            AFRICASTALKING = {
                "USERNAME": <your_username>,
            }
            """
        )
        
    if(aft_config.get("API_KEY", None) == None):
        raise Exception(
            """Africa's Talking api_key has not been configured 
            consider adding 
            
            AFRICASTALKING = {
                "API_KEY": <your_api_key>,
            }
            """
        )
    

check_config()

def configure_aft():
    africastalking.initialize(
        aft_config['USERNAME'],
        aft_config['API_KEY']
    )