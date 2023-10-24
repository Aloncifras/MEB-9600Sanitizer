import os

def ler_arquivo(arquivo):
    lista = []

    arq = open(arquivo, "r")

    for linha in arq:
        lista.append(linha)

    arq.close()

    return lista

path = __file__[:__file__.rfind('\ '[:1])+1] #diretorio do arquivo
print('Path: '+path)
files = os.listdir(path)
nihon = []
print('Arquivos na pasta: ',files,'\n')
for v in files:
    if v[-3:].upper() == 'TXT':
        while '-' in v: #Verificando se tem "-" e trocando por "_" para nao dar erro no mat lab
            os.rename(v,v.replace('-','_'))
            v=v.replace('-','_')
        nihon.append(v)

for name in nihon: #Separando cada bloco de dados de cada arquivo txt na pasta
    escreve = 0  # variavel para parar de escrever
    n = 0  # bloco de dados
    with open(name,'r',encoding='utf-8') as arquivo:
        text = arquivo.readlines()
        with open(name[:-4] + '_' + "sense"+ '.bin', 'w') as calib:
            print('\nBin sendo escrito:  ' + (name[:-4] + '_' + "sense" + '.bin'))
            calib.write(text[32])
        for linha in text:
            if linha[:3] == "\"1\"":
                escreve = 1 # parametro para anotar em outro arquivo
                n+=1
                print('\nBin sendo escrito:  '+(name[:-4] + '_' + str(n) + '.bin'))
                if (name[:-4] + '_' + str(n) + '.bin') in files:  # limpando antigos .bin
                    os.remove(path + name[:-4] + '_' + str(n) + '.bin')
                    #print('diretorio pos limpesa: ',os.listdir(path))
            elif linha == "\"*Wave End\"\n":
                escreve = 0  # parametro parar de anotar e salvar em outro arquivo

                #################### VERIFICANDO O ARQUIVO ##############
                #print('bin sendo lido: '+name[:-4]+'_'+str(n) + '.bin')
                #with open(name[:-4]+'_'+str(n) + '.bin') as sanitised:
                #    print(sanitised.read())
                #print()
                #print()
                ################################################################

            if escreve == 1:
                with open(name[:-4]+'_'+str(n) + '.bin', 'a') as sanitised:
                    sanitised.write(linha[linha.find(',')+1:].replace(',','	')) #escrevendo as linhas e trocando a virgula por tab
                    #sanitised.write(linha) # utilizado para ver a indexação


        #juntando os arquivos 2 e 3
        dois = ler_arquivo(name[:-4]+'_'+'2' + '.bin')
        tres = ler_arquivo(name[:-4]+'_'+'3' + '.bin')
        m=len(dois[-1].split())
        slash=['-45000 '*m+'\n','45000 '*m+'\n','-45000 '*m+'\n','45000 '*m+'\n','-45000 '*m+'\n','45000 '*m+'\n','-45000 '*m+'\n','45000 '*m+'\n'] # separador dos graficos
        merged = dois.copy()
        merged.extend(slash)
        merged.extend(tres)
        merged_file = open(name[:-4]+'_'+'merg' + '.bin', 'w')
        merged_file.writelines(merged)
        merged_file.close()




