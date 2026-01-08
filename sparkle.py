import vlc
import time 

input('Olá, deseja 1 benção? ✨️ ')
print('Você ganhou a benção dos sparkles ✨️ (É obrigatorio) ')
input('Quer Falar Algo pros Dev do Sparkle? ✨️💻 ')

player = vlc.MediaPlayer("sparkle.mp3")
player.play()
player.set_repeat(True)

print('Por falar, vai ganhar mais 5 minutos')
print('Você vai ficar por 5 minutos, agora fica o som')
time.sleep(300)

player.stop()
print('Obrigado por usar esse script, espero que sua vida fique melhor e que sempre lembre-se desse script (: ')
