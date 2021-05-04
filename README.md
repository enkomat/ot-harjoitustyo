# Spaghetti Master
Tämän pelin idea on yhdistää Python ohjelmointia visuaalisiin puzzleihin.

## Pelaaminen
Pelin ensimmäistä tasoa voi pelata muokkaamalla 'level_1.py" tiedoston koodia. Ideana on liikuttaa hahmoa oikealla tavalla. Pelin voi avata komennolla 'poetry run invoke start'.

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuurikuvaus.md)

## Pelin pelaaminen

### Level 1

Seuraava komento avaa pelin ensimmäisen tason:

```bash
poetry run invoke level1
```

Tason muokattava koodi löytyy osoitteesta /spaghetti/src/level_1.py

Tasolla ovat käytettävisä seuraavat metodikutsut:
* move_player_down() - liikuttaa pelaaja yhden ruudun alaspäin
* move_player_up() - liikuttaa pelaajaa yhden ruudun ylöspäin
* move_player_left() - liikuttaa pelaajaa yhden ruudun vasemmalle
* move_player_right() - liikuttaa pelaajaa yhden ruudun oikealle
* player_interact() - laita pelaaja tekemään jotain pelimaailmassa
* run() - käynnistää pelin

Tason tehtävä on seuraava:
* liikuta pelaaja oven päälle
* laita pelaaja avaamaan ovi

### Level 2

Seuraava komento avaa tason:

```bash
poetry run invoke level2
```

Tason muokattava koodi löytyy osoitteesta /spaghetti/src/level_2.py

Tasolla ovat käytettävisä seuraavat metodikutsut:
* 'players' listan sisällä ovat alla olevat metodikutsut. jokainen elementti listassa on yksittäinen Player olio.
    * move_player_down() - liikuttaa pelaaja yhden ruudun alaspäin
    * move_player_up() - liikuttaa pelaajaa yhden ruudun ylöspäin
    * move_player_left() - liikuttaa pelaajaa yhden ruudun vasemmalle
    * move_player_right() - liikuttaa pelaajaa yhden ruudun oikealle
    * interact() - laita pelaaja tekemään jotain pelimaailmassa
* run() - käynnistää pelin


Tason tehtävä on seuraava:
  * liikuta pelaajat ovien päälle
  * laita pelaajat avaamaan ovet

### Level 3

Seuraava komento avaa tason:

```bash
poetry run invoke level3
```

Tason muokattava koodi löytyy osoitteesta /spaghetti/src/level_3.py

Tasolla ovat käytettävisä seuraavat metodikutsut:
* 'players' listan sisällä ovat alla olevat metodikutsut. jokainen elementti listassa on yksittäinen Player olio.
    * move_player_down() - liikuttaa pelaaja yhden ruudun alaspäin
    * move_player_up() - liikuttaa pelaajaa yhden ruudun ylöspäin
    * move_player_left() - liikuttaa pelaajaa yhden ruudun vasemmalle
    * move_player_right() - liikuttaa pelaajaa yhden ruudun oikealle
    * interact() - laita pelaaja tekemään jotain pelimaailmassa
* run() - käynnistää pelin


Tason tehtävä on seuraava:
  * liikuta kaikki pelaajat ovien päälle
  * laita pelaajat avaamaan ovet

### Level 4

Seuraava komento avaa tason:

```bash
poetry run invoke level4
```

Tason muokattava koodi löytyy osoitteesta /spaghetti/src/level_4.py

Tasolla ovat käytettävisä seuraavat metodikutsut:
* 'players' listan sisällä ovat alla olevat metodikutsut. jokainen elementti listassa on yksittäinen Player olio.
    * move_player_down() - liikuttaa pelaaja yhden ruudun alaspäin
    * move_player_up() - liikuttaa pelaajaa yhden ruudun ylöspäin
    * move_player_left() - liikuttaa pelaajaa yhden ruudun vasemmalle
    * move_player_right() - liikuttaa pelaajaa yhden ruudun oikealle
    * interact() - laita pelaaja tekemään jotain pelimaailmassa
* run() - käynnistää pelin


Tason tehtävä on seuraava:
  * liikuta kaikki pelaajat oven päälle
  * laita pelaajat avaamaan ovi

### Level 5

Tämä taso hieman aikaisempia vaikeampi. Pidä mielessä, että kaikki komennot suoritetaan ennen pelin aloittamista.

Seuraava komento avaa tason:

```bash
poetry run invoke level6
```

Tason muokattava koodi löytyy osoitteesta /spaghetti/src/level_6.py

Tasolla ovat käytettävisä seuraavat metodikutsut:
* 'players' listan sisällä ovat alla olevat metodikutsut. jokainen elementti listassa on yksittäinen Player_2 olio.
    * move_down() - liikuttaa pelaaja yhden ruudun alaspäin
    * move_up() - liikuttaa pelaajaa yhden ruudun ylöspäin
    * move_left() - liikuttaa pelaajaa yhden ruudun vasemmalle
    * move_right() - liikuttaa pelaajaa yhden ruudun oikealle 
    * get_position_x - palauttaa pelaajan paikan x. x on sivuttainen suunta, vasemmalta oikealle.
    * get_position_y - palauttaa pelaajan paikan y. y on vertikaalinen suunta, ylhäältä alas.
    * interact() - laita pelaaja tekemään jotain pelimaailmassa
* run() - käynnistää pelin


Tason tehtävä on seuraava:
  * ohjaa kaikki pelaajat ovelle. pelaajien paikka muuttuu satunnaisesti joka kerta kun tason avaa.
  * avaa yhellä pelaajalla ovi ja kävele muilla sen läpi. ovi on aina samassa paikassa.

### Level 6

Seuraava komento avaa tason:

```bash
poetry run invoke level6
```

Tason muokattava koodi löytyy osoitteesta /spaghetti/src/level_6.py

Tasolla ovat käytettävisä seuraavat metodikutsut:
* 'players' listan sisällä ovat alla olevat metodikutsut. jokainen elementti listassa on yksittäinen Player_2 olio.
    * move_down() - liikuttaa pelaaja yhden ruudun alaspäin
    * move_up() - liikuttaa pelaajaa yhden ruudun ylöspäin
    * move_left() - liikuttaa pelaajaa yhden ruudun vasemmalle
    * move_right() - liikuttaa pelaajaa yhden ruudun oikealle 
    * get_position_x - palauttaa pelaajan paikan x. x on sivuttainen suunta, vasemmalta oikealle.
    * get_position_y - palauttaa pelaajan paikan y. y on vertikaalinen suunta, ylhäältä alas.
    * interact() - laita pelaaja tekemään jotain pelimaailmassa
* 'door' olion sisällä ovat alla olevat muuttujat.
    * get_position_x - palauttaa oven paikan x. x on sivuttainen suunta, vasemmalta oikealle.
    * get_position_y - palauttaa oven paikan y. y on vertikaalinen suunta, ylhäältä alas.
* run() - käynnistää pelin

Tason tehtävä on seuraava:
  * pelaajia on yhteensä 16. niiden paikka muuttuu satunnaisesti joka kerta kun avaat pelin uudestaan. hae ne 8 pelaajaa jotka ovat lähimpänä ovea.
  * kuljeta nämä kahdeksan pelaajaa oven läpi. jos yksikin pelaaja joka on liian kaukana ovesta menee siitä läpi, taso epäonnistuu. oven paikka muuttuu satunnaisesti.

### Level 7

Tämä taso on haastava. Pelin lähdekoodia ei ikinä tarvitse - eikä saa - muuttaa ratkaistaakseen tehtävää. Myöskään yksityisiin tai suojattuihin muuttujiin ei saa koskea. Tasot pystyy aina selvittämään kyseisen tason julkisilla metodeilla. Voit tosin lisätä mitä tahansa Pipin taikka Pythonin tarjoamia kirjastoja koodiin.

Seuraava komento avaa tason:

```bash
poetry run invoke level7
```

Tason muokattava koodi löytyy osoitteesta /spaghetti/src/level_7.py

Tasolla ovat käytettävisä seuraavat metodikutsut:
* 'players' listan sisällä ovat alla olevat metodikutsut. jokainen elementti listassa on yksittäinen Player_2 olio.
    * move_down() - liikuttaa pelaaja yhden ruudun alaspäin
    * move_up() - liikuttaa pelaajaa yhden ruudun ylöspäin
    * move_left() - liikuttaa pelaajaa yhden ruudun vasemmalle
    * move_right() - liikuttaa pelaajaa yhden ruudun oikealle 
    * get_position_x - palauttaa pelaajan paikan x. x on sivuttainen suunta, vasemmalta oikealle.
    * get_position_y - palauttaa pelaajan paikan y. y on vertikaalinen suunta, ylhäältä alas.
    * interact() - laita pelaaja tekemään jotain pelimaailmassa
* run() - käynnistää pelin

Tason tehtävä on seuraava:
  * jaa pelaajat kahteen tasan kahdeksan hengen ryhmään.
  * seuraavaksi vaikea osuus: ryhmät tulee jakaa sillä perusteella, että molemmat vievät mahdollisimman pienen alueen. eli molempien aluuet summattuna yhteen muodostavat pienimmäan mahdollisen numeron. alla vielä pari havainnollistavaa kuvaa oikein jaetuista ryhmistä:
    * ![](https://raw.githubusercontent.com/enkomat/ot-harjoitustyo/master/dokumentaatio/level7_3.png)
    * ![](https://raw.githubusercontent.com/enkomat/ot-harjoitustyo/master/dokumentaatio/level7_4.png)
  * kuljeta kumpikin ryhmä jommasta kummasta ovesta läpi. ovi liittää kunkin sen läpi pelaajan siihen liitettyyn ryhmänumeroon. eli vain saman ryhmän jäseniä saa mennä yhdestä annetusta ovesta läpi, sen jälkeen kun ovi on kertaalleen avattu. taso epäonnistuu jos väärän ryhmän pelaaja menee toiselle ryhmälle varatusta ovesta läpi. (ovien koordinaatit ovat (10, 15) ja (20, 15).)

## Testaus

Testit voi suorittaa seuraavalla kutsulla:

```bash
poetry run invoke test
```

Coverage sovelluksen voi suorittaa seuraavalla komennolla:

```bash
poetry run invoke coverage
```

Coverage raportin voi luoda seuraavalla komennolla:

```bash
poetry run invoke coveragereport
```