import json
from ipmom import mostra_ipmon
from ModoBatalha import ModoBatalha
import pickle
import pygame
#musica
from pygame.locals import *
pygame.init()
janela= pygame.display.set_mode((470,300),0,32)
pygame.display.set_caption("Modulo Music")
pygame.mixer.music.load("PokemonMusica1.wav")
pygame.mixer.music.play(1)


    

#dados iniciais dos inspermons e de jogadores que estão jogando pela primeira vez

with open('inspermons.json') as arquivo:
    inspermons = json.load(arquivo)
    meus_bichinhos=[{"Nome":"Aluno",
                     "Ataque":50,
                     "Vida":800,
                     "Nome Ataque":"Mendigando nota!",
                     "Defesa":10,
                     "Experiência":1000 }]
    insperbolas = 2

#Início do jogo    
print("Inspermon!")
print("")
print("Desenvido por: Samara e Ana")
print("")
recuperar_salvamento=input("Você possui jogo salvo(Sim ou Não)?")    
a = input("Qual é o seu nome? ")                 
input("Olá, "+a+", seja bem-vindo(a) ao Inspèrmon!")
print("")
import random

while True:
    b = input(a+", o que você deseja fazer: Passear, Dormir ou Ver insperdex?? ")
    print("")
    
    if recuperar_salvamento=="Sim": #Se o jogador ja tem um jogo salvo
        print("Histórico de jogo recuperado com sucesso!")
        with open(a+'.py','rb') as f:        #Salva Dados
            meus_bichinhos,insperbolas= pickle.load(f)

    if b=="Ver insperdex": #ver inspermon que conseguiu capturando ou batalhando
        print("")
        print("Você tem {} insperbolas".format(insperbolas))
        print("")
        for i in range(len(meus_bichinhos)):
            dados_insper_capturado=mostra_ipmon(meus_bichinhos[i])
            print(dados_insper_capturado.dados(meus_bichinhos[i]))
            print("")

    if b=="Dormir": #finaliza o jogo
        print("Bom descanso! Até a próxima...Seu jogo será salvo no seu nome.")
        break    

        print("Seu Insperdéx:")
        print(meus_bichinhos)

    if b=="Passear":
        print()
        print("Ótima escolha!")
        print()
        c = input("Escolha um ginásio: Fab Lab, Lab de Física ou Lab de Química: ")
        print("Esses são os seus inspermons disponíveis:")
        for i in range(len(meus_bichinhos)):  #Mostra inspermons disponíveis para batalhar 
            dados_insper_capturado=mostra_ipmon(meus_bichinhos[i])
            print(dados_insper_capturado.dados(meus_bichinhos[i]))
        jogador_escolhe=input("Digite o nome do inspermon com o qual deseja jogar:")# escolha do inspermon disponivel pra jogar
        for i in range(len(meus_bichinhos)):
            if meus_bichinhos[i]["Nome"]==jogador_escolhe:
                jogador_escolhido=meus_bichinhos[i]
                posicao_escolhida=i
        print("")
        #possibilidade de encontrar insperstops e inspermons para captura no caminho:
        print("No caminho...")
        print("")
        f = random.randint(1,2)
        if f==2: #sorte:possibilidade de encontrar um insperstop e conseguir insperbolas
            print("Você encontrou um Insperstop! O que será que vai ganhar?")
            print("")
            g = random.randint(2,4) #Número de Insperbolas
            insperbolas = insperbolas + g
            print("{0} Insperbolas foram adicionadas ao seu inventário!".format(g))
            print("")
        e = random.randint(1,3) #chance de encontrar um inpersmon
        k = random.randint(0,2) #numero do inspermon encontrado
        l = inspermons[k]       #informações do inspermon encontrado
        if e==2:#sorte:possiblidade de capturar um inspermon no caminho (neste caso é necessário que o jogado tenha insperbolas)
            h = input("Você encontrou um Inspermon, {}! Deseja capturá-lo(sim ou não)?".format(l["Nome"]))
            print()
            if insperbolas<=0:
                print("Você não tem insperbolas para captura-lo")
            while h == "sim" and insperbolas>0:
                i = random.randint(1,2) #captura será bem sucedida ou não
                if i==2:
                    print("Inspermon escapou!")
                    print("")
                    j = input("Deseja tentar novamente?(sim ou não)")
                    print()
                    if j=="sim":
                        continue
                    else:
                        break
                else:
                    print("Você capturou {0}! Parabéns!".format(l["Nome"]))
                    print()
                    insper_novo=inspermons[k]
                    for i in range(len(meus_bichinhos)):
                        if meus_bichinhos[i]["Nome"]== inspermons[k]["Nome"]: #impede que no inspedex existam 2 inspermons com mesmo nome
                            novo_nome=input("Esse nome de inspermon ja existe no seu insperdex.Dê outro nome:")
                            insper_novo["Nome"]=novo_nome
                    meus_bichinhos.append(insper_novo)
                    with open(a+'.py','wb') as f:                             #Salva Dados 
                        pickle.dump([meus_bichinhos,insperbolas], f, protocol=2)
                    print("Adicionando {0} em seu Insperdéx!".format(l["Nome"]))
                    print()
                    break
        #Chegada ao ginásio                   
        print("Você chegou no "+c+"! Boa sorte!")
        print()
        print("Sua batalha começará agora, a sorte está lançada!")
        print()
        with open('inspermons.json') as arquivo:
            inspermons = json.load(arquivo)
            num_inspermon = random.randint(0,2)
            inspermon_sorteado=inspermons[num_inspermon]
            print("Dados do adversário:")
            dados_adver=mostra_ipmon(inspermon_sorteado)
            print(dados_adver.dados(inspermon_sorteado))
            print("Seus dados:")
            dados_jog=mostra_ipmon(jogador_escolhido)
            print(dados_jog.dados(jogador_escolhido))
            d=(random.randint(1,2))

      #Fab Lab (sorte:aumento do ataque em 30%)
        #Com sorte    
        if c=="Fab Lab" and d==2:
            print("A sorte parece estar com você, seu ataque aumentou 30%!")
            print("")
            jogo_fablab=ModoBatalha(inspermon_sorteado,jogador_escolhido,num_inspermon)
            jogo_fablab.loopbatalha(a,inspermon_sorteado,jogador_escolhido,1.3,1,1,1)
            if jogo_fablab.resultado=="vitoria":
                insper_novo=inspermons[num_inspermon]
                for i in range(len(meus_bichinhos)):
                    if meus_bichinhos[i]["Nome"]== inspermons[num_inspermon]["Nome"]:
                        novo_nome=input("Esse nome de inspermon ja existe no seu insperdex.Dê outro nome:")
                        insper_novo["Nome"]=novo_nome
                meus_bichinhos.append(insper_novo)
                x=meus_bichinhos[posicao_escolhida]["Experiência"] #Em caso de vitória adiciona-se experiencia ao inspermon que lutou pelo jogador
                meus_bichinhos[posicao_escolhida]["Experiência"]=x+500
                with open(a+'.py','wb') as f:                             #Salva Dados 
                        pickle.dump([meus_bichinhos,insperbolas], f, protocol=2)
                        
                if meus_bichinhos[posicao_escolhida]["Experiência"]>1400 and x<1400:
                    print("")
                    print("Parabéns,o inspermon {0} evoluiu para o nivel dois!".format(meus_bichinhos[posicao_escolhida]["Nome"]))#Evolução
                    print("")
                    h=meus_bichinhos[posicao_escolhida]["Vida"] 
                    meus_bichinhos[posicao_escolhida]["Vida"]=h+50
                    p=meus_bichinhos[posicao_escolhida]["Defesa"] 
                    meus_bichinhos[posicao_escolhida]["Defesa"]=p+50
                    u=meus_bichinhos[posicao_escolhida]["Ataque"] 
                    meus_bichinhos[posicao_escolhida]["Ataque"]=u+50  #Salva Dados
                    with open(a+'.py','wb') as f:
                        pickle.dump([meus_bichinhos,insperbolas], f, protocol=2)
                if meus_bichinhos[posicao_escolhida]["Experiência"]>1900 and x<1900:
                    print("Parabéns,o inspermon {0} evoluiu para o nivel Três!".format(meus_bichinhos[posicao_escolhida]["Nome"]))#Evolução 2
                    print("")
                    h=meus_bichinhos[posicao_escolhida]["Vida"] 
                    meus_bichinhos[posicao_escolhida]["Vida"]=h+50
                    p=meus_bichinhos[posicao_escolhida]["Defesa"] 
                    meus_bichinhos[posicao_escolhida]["Defesa"]=p+50
                    u=meus_bichinhos[posicao_escolhida]["Ataque"] 
                    meus_bichinhos[posicao_escolhida]["Ataque"]=u+50
                    with open(a+'.py','wb') as f:                   #Salva Dados
                        pickle.dump([meus_bichinhos,insperbolas], f, protocol=2)
        #Sem sorte                
        elif c=="Fab Lab" and d!=2:
            print("Você está sem sorte, tenha uma boa batalha!")
            print("")
            jogo_fablab=ModoBatalha(inspermon_sorteado,jogador_escolhido,num_inspermon)
            jogo_fablab.loopbatalha(a,inspermon_sorteado,jogador_escolhido,1,1,1,1)
            if jogo_fablab.resultado=="vitoria":
                insper_novo=inspermons[num_inspermon]
                for i in range(len(meus_bichinhos)):
                    if meus_bichinhos[i]["Nome"]== inspermons[num_inspermon]["Nome"]: #Impede que no insperdex existam 2 inspermons com mesmo nome
                        novo_nome=input("Esse nome de inspermon ja existe no seu insperdex.Dê outro nome:")
                        insper_novo["Nome"]=novo_nome
                meus_bichinhos.append(insper_novo)
                x=meus_bichinhos[posicao_escolhida]["Experiência"] #Em caso de vitória adiciona-se experiencia ao inspermon que lutou pelo jogador
                meus_bichinhos[posicao_escolhida]["Experiência"]=x+500
                with open(a+'.py','wb') as f:
                    pickle.dump([meus_bichinhos,insperbolas], f, protocol=2)
                if meus_bichinhos[posicao_escolhida]["Experiência"]>1400 and x<1400:
                    print("Parabéns,o inspermon {0} evoluiu para o nivel Dois!".format(meus_bichinhos[posicao_escolhida]["Nome"]))#Evolução
                    print("")
                    h=meus_bichinhos[posicao_escolhida]["Vida"] 
                    meus_bichinhos[posicao_escolhida]["Vida"]=h+50
                    p=meus_bichinhos[posicao_escolhida]["Defesa"] 
                    meus_bichinhos[posicao_escolhida]["Defesa"]=p+50
                    u=meus_bichinhos[posicao_escolhida]["Ataque"] 
                    meus_bichinhos[posicao_escolhida]["Ataque"]=u+50
                    with open(a+'.py','wb') as f:                               #Salva Dados
                        pickle.dump([meus_bichinhos,insperbolas], f, protocol=2)
                if meus_bichinhos[posicao_escolhida]["Experiência"]>1900 and x<1900:
                    print("Parabéns,o inspermon {0} evoluiu para o nivel Três!".format(meus_bichinhos[posicao_escolhida]["Nome"]))#Evolução 2
                    print("")
                    h=meus_bichinhos[posicao_escolhida]["Vida"] 
                    meus_bichinhos[posicao_escolhida]["Vida"]=h+50
                    p=meus_bichinhos[posicao_escolhida]["Defesa"] 
                    meus_bichinhos[posicao_escolhida]["Defesa"]=p+50
                    u=meus_bichinhos[posicao_escolhida]["Ataque"] 
                    meus_bichinhos[posicao_escolhida]["Ataque"]=u+50
                    with open(a+'.py','wb') as f:                             #Salva Dados 
                        pickle.dump([meus_bichinhos,insperbolas], f, protocol=2)
                        

        #Lab Física (sorte:Defesa aumenta 40%)
        #Com Sorte                
        if c=="Lab de Física" and d==2:
            print("A sorte parece estar com você, sua defesa aumentou 40%!")
            print("")
            jogo_labf=ModoBatalha(inspermon_sorteado,jogador_escolhido,num_inspermon)
            jogo_labf.loopbatalha(a,inspermon_sorteado,jogador_escolhido,1,1,1.4,1)
            if jogo_labf.resultado=="vitoria":
                insper_novo=inspermons[num_inspermon]
                for i in range(len(meus_bichinhos)):
                    if meus_bichinhos[i]["Nome"]== inspermons[num_inspermon]["Nome"]:
                        novo_nome=input("Esse nome de inspermon ja existe no seu insperdex.Dê outro nome:")
                        insper_novo["Nome"]=novo_nome
                meus_bichinhos.append(insper_novo)
                x=meus_bichinhos[posicao_escolhida]["Experiência"] #Em caso de vitória adiciona-se experiencia ao inspermon que lutou pelo jogador
                meus_bichinhos[posicao_escolhida]["Experiência"]=x+500
                with open(a+'.py','wb') as f:                             #Salva Dados 
                        pickle.dump([meus_bichinhos,insperbolas], f, protocol=2)
                        
                if meus_bichinhos[posicao_escolhida]["Experiência"]>1400 and x<1400:
                    print("")
                    print("Parabéns,o inspermon {0} evoluiu para o nivel dois!".format(meus_bichinhos[posicao_escolhida]["Nome"]))#Evolução
                    print("")
                    h=meus_bichinhos[posicao_escolhida]["Vida"] 
                    meus_bichinhos[posicao_escolhida]["Vida"]=h+50
                    p=meus_bichinhos[posicao_escolhida]["Defesa"] 
                    meus_bichinhos[posicao_escolhida]["Defesa"]=p+50
                    u=meus_bichinhos[posicao_escolhida]["Ataque"] 
                    meus_bichinhos[posicao_escolhida]["Ataque"]=u+50
                    with open(a+'.py','wb') as f:
                        pickle.dump([meus_bichinhos,insperbolas], f, protocol=2)     #Salva Dados
                if meus_bichinhos[posicao_escolhida]["Experiência"]>1900 and x<1900:
                    print("Parabéns,o inspermon {0} evoluiu para o nivel Três!".format(meus_bichinhos[posicao_escolhida]["Nome"]))#Evolução 2
                    print("")
                    h=meus_bichinhos[posicao_escolhida]["Vida"] 
                    meus_bichinhos[posicao_escolhida]["Vida"]=h+50
                    p=meus_bichinhos[posicao_escolhida]["Defesa"] 
                    meus_bichinhos[posicao_escolhida]["Defesa"]=p+50
                    u=meus_bichinhos[posicao_escolhida]["Ataque"] 
                    meus_bichinhos[posicao_escolhida]["Ataque"]=u+50 
                    with open(a+'.py','wb') as f:                                    #Salva Dados
                        pickle.dump([meus_bichinhos,insperbolas], f, protocol=2)
                
        #Sem Sorte        
        elif c=="Lab de Física" and d!=2:
            print("Você está sem sorte, tenha uma boa batalha!")
            print("")
            jogo_labf=ModoBatalha(inspermon_sorteado,jogador_escolhido,num_inspermon)
            jogo_labf.loopbatalha(a,inspermon_sorteado,jogador_escolhido,1,1,1,1)
            if jogo_labf.resultado=="vitoria":
                insper_novo=inspermons[num_inspermon]
                for i in range(len(meus_bichinhos)):
                    if meus_bichinhos[i]["Nome"]== inspermons[num_inspermon]["Nome"]:
                        novo_nome=input("Esse nome de inspermon ja existe no seu insperdex.Dê outro nome:")
                        insper_novo["Nome"]=novo_nome
                meus_bichinhos.append(insper_novo)
                x=meus_bichinhos[posicao_escolhida]["Experiência"] #Em caso de vitória adiciona-se experiencia ao inspermon que lutou pelo jogador
                meus_bichinhos[posicao_escolhida]["Experiência"]=x+500
                with open(a+'.py','wb') as f:                             #Salva Dados 
                        pickle.dump([meus_bichinhos,insperbolas], f, protocol=2)
                if meus_bichinhos[posicao_escolhida]["Experiência"]>1400 and x<1400:
                    print("Parabéns,o inspermon {0} evoluiu para o nivel Dois!".format(meus_bichinhos[posicao_escolhida]["Nome"]))#Evolução
                    print("")
                    h=meus_bichinhos[posicao_escolhida]["Vida"] 
                    meus_bichinhos[posicao_escolhida]["Vida"]=h+50
                    p=meus_bichinhos[posicao_escolhida]["Defesa"] 
                    meus_bichinhos[posicao_escolhida]["Defesa"]=p+50
                    u=meus_bichinhos[posicao_escolhida]["Ataque"] 
                    meus_bichinhos[posicao_escolhida]["Ataque"]=u+50
                    with open(a+'.py','wb') as f:                               #Salva Dados
                        pickle.dump([meus_bichinhos,insperbolas], f, protocol=2)
                if meus_bichinhos[posicao_escolhida]["Experiência"]>1900 and x<1900:
                    print("Parabéns,o inspermon {0} evoluiu para o nivel Três!".format(meus_bichinhos[posicao_escolhida]["Nome"]))#Evolução 2
                    print("")
                    h=meus_bichinhos[posicao_escolhida]["Vida"] 
                    meus_bichinhos[posicao_escolhida]["Vida"]=h+50
                    p=meus_bichinhos[posicao_escolhida]["Defesa"] 
                    meus_bichinhos[posicao_escolhida]["Defesa"]=p+50
                    u=meus_bichinhos[posicao_escolhida]["Ataque"] 
                    meus_bichinhos[posicao_escolhida]["Ataque"]=u+50
                    with open(a+'.py','wb') as f:
                        pickle.dump([meus_bichinhos,insperbolas], f, protocol=2)
                        
        #Lab Química (sorte: defesa adversária diminui pela metade)
        #Com Sorte                
        if c=="Lab de Química" and d==2:
            print("A sorte parece estar com você, defesa adversária diminuiu pela metade")
            print("")
            jogo_labq=ModoBatalha(inspermon_sorteado,jogador_escolhido,num_inspermon)
            jogo_labq.loopbatalha(a,inspermon_sorteado,jogador_escolhido,1,1,1,2)
            if jogo_labq.resultado=="vitoria":
                insper_novo=inspermons[num_inspermon]
                for i in range(len(meus_bichinhos)):
                    if meus_bichinhos[i]["Nome"]== inspermons[num_inspermon]["Nome"]:
                        novo_nome=input("Esse nome de inspermon ja existe no seu insperdex.Dê outro nome:")
                        insper_novo["Nome"]=novo_nome
                meus_bichinhos.append(insper_novo)
                x=meus_bichinhos[posicao_escolhida]["Experiência"] #Em caso de vitória adiciona-se experiencia ao inspermon que lutou pelo jogador
                meus_bichinhos[posicao_escolhida]["Experiência"]=x+500
                with open(a+'.py','wb') as f:                             #Salva Dados 
                        pickle.dump([meus_bichinhos,insperbolas], f, protocol=2)
                        
                if meus_bichinhos[posicao_escolhida]["Experiência"]>1400 and x<1400:
                    print("")
                    print("Parabéns,o inspermon {0} evoluiu para o nivel dois!".format(meus_bichinhos[posicao_escolhida]["Nome"]))#Evolução
                    print("")
                    h=meus_bichinhos[posicao_escolhida]["Vida"] 
                    meus_bichinhos[posicao_escolhida]["Vida"]=h+50
                    p=meus_bichinhos[posicao_escolhida]["Defesa"] 
                    meus_bichinhos[posicao_escolhida]["Defesa"]=p+50
                    u=meus_bichinhos[posicao_escolhida]["Ataque"] 
                    meus_bichinhos[posicao_escolhida]["Ataque"]=u+50
                    with open(a+'.py','wb') as f:
                        pickle.dump([meus_bichinhos,insperbolas], f, protocol=2)
                if meus_bichinhos[posicao_escolhida]["Experiência"]>1900 and x<1900:
                    print("Parabéns,o inspermon {0} evoluiu para o nivel Três!".format(meus_bichinhos[posicao_escolhida]["Nome"]))#Evolução 2
                    print("")
                    h=meus_bichinhos[posicao_escolhida]["Vida"] 
                    meus_bichinhos[posicao_escolhida]["Vida"]=h+50
                    p=meus_bichinhos[posicao_escolhida]["Defesa"] 
                    meus_bichinhos[posicao_escolhida]["Defesa"]=p+50
                    u=meus_bichinhos[posicao_escolhida]["Ataque"] 
                    meus_bichinhos[posicao_escolhida]["Ataque"]=u+50
                    with open(a+'.py','wb') as f:
                        pickle.dump([meus_bichinhos,insperbolas], f, protocol=2)
            
                               
        #Sem Sorte        
        elif c=="Lab de Química" and d!=2:
            print("Você está sem sorte, tenha uma boa batalha!")
            print("")
            jogo_labq=ModoBatalha(inspermon_sorteado,jogador_escolhido,num_inspermon)
            jogo_labq.loopbatalha(a,inspermon_sorteado,jogador_escolhido,1,1,1,1)
            if jogo_labq.resultado=="vitoria":
                insper_novo=inspermons[num_inspermon]
                for i in range(len(meus_bichinhos)):
                    if meus_bichinhos[i]["Nome"]== inspermons[num_inspermon]["Nome"]:
                        novo_nome=input("Esse nome de inspermon ja existe no seu insperdex.Dê outro nome:")
                        insper_novo["Nome"]=novo_nome
                meus_bichinhos.append(insper_novo)
                x=meus_bichinhos[posicao_escolhida]["Experiência"] #Em caso de vitória adiciona-se experiencia ao inspermon que lutou pelo jogador
                meus_bichinhos[posicao_escolhida]["Experiência"]=x+500
                with open(a+'.py','wb') as f:
                    pickle.dump([meus_bichinhos,insperbolas], f, protocol=2)
                if meus_bichinhos[posicao_escolhida]["Experiência"]>1400 and x<1400:
                    print("Parabéns,o inspermon {0} evoluiu para o nivel Dois!".format(meus_bichinhos[posicao_escolhida]["Nome"]))#Evolução
                    print("")
                    h=meus_bichinhos[posicao_escolhida]["Vida"] 
                    meus_bichinhos[posicao_escolhida]["Vida"]=h+50
                    p=meus_bichinhos[posicao_escolhida]["Defesa"] 
                    meus_bichinhos[posicao_escolhida]["Defesa"]=p+50
                    u=meus_bichinhos[posicao_escolhida]["Ataque"] 
                    meus_bichinhos[posicao_escolhida]["Ataque"]=u+50
                    with open(a+'.py','wb') as f:                               #Salva Dados
                        pickle.dump([meus_bichinhos,insperbolas], f, protocol=2)
                if meus_bichinhos[posicao_escolhida]["Experiência"]>1900 and x<1900:
                    print("Parabéns,o inspermon {0} evoluiu para o nivel Três!".format(meus_bichinhos[posicao_escolhida]["Nome"]))#Evolução 2
                    print("")
                    h=meus_bichinhos[posicao_escolhida]["Vida"] 
                    meus_bichinhos[posicao_escolhida]["Vida"]=h+50
                    p=meus_bichinhos[posicao_escolhida]["Defesa"] 
                    meus_bichinhos[posicao_escolhida]["Defesa"]=p+50
                    u=meus_bichinhos[posicao_escolhida]["Ataque"] 
                    meus_bichinhos[posicao_escolhida]["Ataque"]=u+50
                    with open(a+'.py','wb') as f:                                #Salva Dados
                        pickle.dump([meus_bichinhos,insperbolas], f, protocol=2)
         
                
          
            
                    
                                                          
                                                          
                     
                     
                 

            

