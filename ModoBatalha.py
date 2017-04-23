class ModoBatalha:
    def __init__(self,inspermon_sorteado,jogador_escolhido,num_inspermon):
        self.vida_adversario=inspermon_sorteado["Vida"]
        self.vida_jogador=jogador_escolhido["Vida"]
    def loopbatalha(self,a,inspermon_sorteado,jogador_escolhido,x1,x2,y1,y2):
        import random
        AtaqueJogador=jogador_escolhido["Ataque"]*x1
        AtaqueAdversario=inspermon_sorteado["Ataque"]/x2
        DefesaJogador=jogador_escolhido["Defesa"]*y1
        DefesaAdversario=inspermon_sorteado["Defesa"]/y2
        while self.vida_adversario > 0 and self.vida_jogador> 0:
                print("")
                comando=input("Deseja Atacar ou Fugir? ")
                if comando=="Atacar":
                    print(a+" ataca:{}".format(jogador_escolhido["Nome Ataque"]))
                    if AtaqueJogador>DefesaAdversario:
                        print("Ataque bem sucedido!")
                        
                        self.vida_adversario=self.vida_adversario -( AtaqueJogador-DefesaAdversario )
                        print( "vida de {0} cai para {1}".format(inspermon_sorteado["Nome"],self.vida_adversario))
                        
                        if self.vida_adversario<= 0:
                            print("Parabéns você ganhou, {0} foi adicionado ao seu Insperdéx!".format(inspermon_sorteado["Nome"]))
                            
                            self.resultado="vitoria"
                            break
                        else:  #começa ataque do oponente
                            print("{0} ataca: {1}!".format(inspermon_sorteado["Nome"],inspermon_sorteado["Nome Ataque"]))
            
                            if AtaqueAdversario<=DefesaJogador:
                                print("Ataque adversário mal sucedido!")
                                
                            else:
                                self.vida_jogador=self.vida_jogador-(AtaqueAdversario-DefesaJogador)
                                print( "vida de {0} cai para {1}".format(a,self.vida_jogador))
                                if self.vida_jogador<=0:
                                    print("Você perdeu, que pena! ")
                                    self.resultado="derrota"
                                    break
                    elif AtaqueJogador<DefesaAdversario:
                        print("Ataque mau sucedido,defesa do adversário é superior ao seu ataque")
                        
                        print("{0} ataca: {1}!".format(inspermon_sorteado["Nome"], inspermon_sorteado["Nome Ataque"]))
                    
                        self.vida_jogador=self.vida_jogador-(AtaqueAdversario-DefesaJogador)
                        
                        print( "vida de {0} cai para {1}".format(a,self.vida_jogador))
                        if self.vida_jogador<=0:
                            print("Você perdeu, que pena! ")
                            self.resultado="derrota"
                            break
                        else:
                            continue
                elif comando=="Fugir":
                    e = random.randint(1,2)
                    if e==2:
                        print("Que pena. Treine mais!")
                        
                        self.resultado="derrota"
                        break
                    else:
                        print("Sua fuga foi mal sucedida, continue a batalha,porém perderá sua vez!")
                      
                        if AtaqueAdversario<=DefesaJogador:
                            print("Ataque adversário mal sucedido!")
                           
                        else:
                            print("{0} ataca: {1}!".format(inspermon_sorteado["Nome"], inspermon_sorteado["Nome Ataque"]))
                            print("")
                            self.vida_jogador=self.vida_jogador-(AtaqueAdversario-DefesaJogador)
                            print( "vida de {0} cai para {1}".format(a,self.vida_jogador))
                           
                            if self.vida_jogador<=0:
                                print("Você perdeu, que pena! ")
                                
                                self.resultado="derrota"
                                break
                            else:
                                continue
        
        
