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

Seuraava komento avaa pelin toisen tason:

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

Seuraava komento avaa pelin toisen tason:

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

Seuraava komento avaa pelin toisen tason:

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