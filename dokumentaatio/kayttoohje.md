# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/enkomat/ot-harjoitustyo/releases) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

## Pelin käynnistäminen

Ennen pelin käynnistämistä, asenna riippuvuudet komennolla:

```
poetry install
```

Nyt pelin voi käynnistää komennolla:

```
poetry run invoke start
```

## Pelin pelaaminen

### Tasovalikko
Kun avaat pelin, ensimmäinen näkymä on tasovalikko. Voit valita haluamasi tason klikkaamalla sitä. Tasojen vaikeus nousee, joten on suositeltavaa ratkaista tasot järjestyksessä.

![](https://raw.githubusercontent.com/enkomat/ot-harjoitustyo/master/dokumentaatio/main_menu.png)

### Tason ratkominen
Kun avaat tason, näkyy sinulle staattinen näkymä josta löytyy peliä kontrolloivia nappeja ikkunan alalaidasta:
![](https://raw.githubusercontent.com/enkomat/ot-harjoitustyo/master/dokumentaatio/play_level.png)

Tarkoituksena on koodaamalla Pythonia ratkaista taso. Kuvassa näkyvässä ensimmäisessä tasossa on tarkoitus koodin avulla liikuttaa pelaaja ovella ja kävellä siitä sisään. Jokaiselle tasolle on oma Python tiedosto jota muokkaamalla pystyt aloittamaan tason ratkomisen. Löydät nämä tiedostot kansiosta [src/level_solutions](https://github.com/enkomat/ot-harjoitustyo/tree/master/spaghetti/src/level_solutions). Mitään muita kooditiedostoja ei tarvitse peliä pelatessa muuttaa. Kun avaat tason 'solution' tiedoston, näyttää se aluksi tältä:

![](https://raw.githubusercontent.com/enkomat/ot-harjoitustyo/master/dokumentaatio/solution_code_1.png)

Voit aloittaa poistamalla pass komennon ja lähteä liikuttamaan pelaajaa 'level' olion sisältämän 'player' olion metodien avulla.

Kun koodi mielestäsi vaikuttaa toimivalta, voit painaa play nappia peli-ikkunasta. Ohjelmaa ei tarvitse käynnistää uudestaan. Kun muutat koodiasi, tallennettuasi sen voit painaa reset nappia (joka on play napin oikealla puolella) ja tällöin uusi koodisi automaattisesti peliin. Jos haluat palata takaisin tasovalikkoon, voit painaa valikkonappia joka löytyy ikkunan oikeasta alalaidasta.