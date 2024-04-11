from calculadora import soma,media
#Nome do arquivo deve iniciar ou terminar com "_test"..
#No terminal uso o comando "pytest"



def teste_soma():
 assert soma(1,2)== 3

def teste_neg():
     assert soma(-1,-2)== -3

def teste_errada():
            assert soma(3,4)== 10
def teste_media():
    assert media([1,2,3,4]) == 2.5

    
  

