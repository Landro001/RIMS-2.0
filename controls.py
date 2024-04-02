# Mapeia e anota as instâncias da classe, para permitir acesso fácil a cada instância caso haja necessidade de mudança

global control_reference
control_reference = {}

def add_to_control_reference(key, value):
    ''' 
    Função que emparelha um par chave:valor ao dicionário global
    '''
    global control_reference
    try:
        control_reference[key] = value
    except KeyError as e:
        print(e)
    finally:
        pass

def return_control_reference():
    '''
    Função que retornar o dicionário
    '''
    global control_reference
    return control_reference
    