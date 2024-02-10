"""Ülesanne 2. Ülesandes peab tekst minema jutumulli sisse keskele. Õppematerjalis on olemas tee, kuidas saada teksti
täpselt pildi keskele. Aga kuna selle jutumulli keskkoht on küsitava väärtusega, siis jätsin programmi silmajärgi leitud
keskkoha, kuid tegin ka eraldi funktsiooni teksti asetamisest jutumulli pildifaili keskkohta"""

import pygame       # impordime pygame mooduli
pygame.init()       # initialiseerime Pygame mooduli

'''def keskel():       # funktsioon, mis paneb teksti täpselt jutumulli pildi keskele, Kahjuks aga pole pilt sümmeetriline ja see ei jää ilus
    chat = pygame.image.load("chat.png")  # muutuja chat saab väärtuseks järgmise pildi failist chat.png
    font = pygame.font.SysFont('Calibri', 25)  # määrame teksti fondi ja suuruse
    text = font.render("Tere, olen Anders", True, [255, 255, 255])  # renderdame sisestatud teksti,määrame teksti servad siledaks ja määrame värvi
    laius = text.get_rect().width       # määrame muutujale laius tekstikasti laiuse
    korgus = text.get_rect().height     # määrame muutujale korgus tekstikasti kõrguse
    chat.blit(text, [150 - laius/2, 119 - korgus/2])        # lisame teksti cahat pildi keskele
    chat = pygame.transform.scale(chat, [258, 202])  # muudame pildi suurust,et pilt ära mahuks
    return chat     # tagastame pildi, mis on nüüd koos tekstiga ja õige suurusega'''


screen = pygame.display.set_mode([640, 480])  # Teeme ekraani
pygame.display.set_caption("Ülesanne 2")  # Paneme ekraanile nime

bg = pygame.image.load("bg_shop.png")  # muutuja bg saab väärtuseks pildi failist bg_shop.png
screen.blit(bg, [0, 0])  # lisame pildi ekraanile antud alguskoha koordinaatidega

seller = pygame.image.load("seller.png")  # muutuja seller saab väärtuseks järgmise pildi failist seller.png
seller = pygame.transform.scale(seller, [254, 305])  # muudame pildi suurust,et pilt mahuks ära
screen.blit(seller, [105, 159])  # lisame pildi ekraanile, määrates alguskoordinaatideks antud väärtused

# Järgnevad read panevad teksti jutumulli pildi tektsiala keskele silmajärgi mõõdetult
chat = pygame.image.load("chat.png")  # muutuja chat saab väärtuseks järgmise pildi failist chat.png
chat = pygame.transform.scale(chat, [258, 202])  # muudame pildi suurust,et pilt ära mahuks
screen.blit(chat, [245, 66])  # lisame pildi ekraanile antud alguskohast
font = pygame.font.SysFont('Calibri', 25)  # määrame teksti fondi ja suuruse
text = font.render("Tere, olen Anders", True, [255, 255, 255])  # renderdame sisestatud teksti,määrame teksti servad siledaks ja määrame värvi
screen.blit(text, [285, 140])  # lisame teksti ekraanile antud alguskohast

'''screen.blit(keskel(), [245, 66])       #funktsiooni, mis paneb teksti täpselt jutumulli pildi keskele väljakutsumine'''

running = True          # Anname muutujale running väärtuseks True, mida kasutame tsükli kontrollimiseks
while running:          # käivitame tsükli pildi ekraanil hoidmiseks, ehk niikaua, kuni muutuja running on True
    for event in pygame.event.get():    # kordame tsüklit niikaua, kuni Pygame sündmuse tüüp on sisestus
        if event.type == pygame.QUIT:   # Kui Pygame sündmuse tüüp on akna sulgemisnupu vajutus, siis
            running = False             # muudame muutuja running väärtuseks False, mis lõpetab tsükli

    pygame.display.flip()               # toome ekraanile tehtud pildi nähtavale

pygame.quit()                   # sulgeme pygame-i
