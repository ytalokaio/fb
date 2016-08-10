##################################################
#               CUSTOM IMPORTS                   #
##################################################
from .models import Projeto # MODELS
##################################################



def project_media(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    projeto = Projeto.objects.all()
    if projeto:
    	projeto = projeto[0]
    	return {'PROJECT_VALID':True, 'PROJECT_DATA':projeto}
    else:
    	return {'PROJECT_VALID':False}