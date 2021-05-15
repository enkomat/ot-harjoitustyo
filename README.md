# Spaghetti Master
Tämän pelin idea on yhdistää Python ohjelmointia visuaalisiin puzzleihin.

## Pelaaminen
Pelin ensimmäistä tasoa voi pelata muokkaamalla 'level_1.py" tiedoston koodia. Ideana on liikuttaa hahmoa oikealla tavalla. Pelin voi avata komennolla 'poetry run invoke start'.

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuurikuvaus.md)

## Pelin pelaaminen

### Pelin käynnistäminen

Seuraava komento avaa pelin tasovalikon:

```bash
poetry run invoke start
```

### Level 1

Tason muokattava koodi löytyy osoitteesta /spaghetti/src/level_solutions/level_1_solution.py

Tasolla on yksi pelaaja, johon voi viitata `level.player` kutsulla. Player luokasta tulee tason ratkaisemiseen vähintään osaa alla olevista metodikutsuista:
* move_down() - liikuttaa pelaaja yhden ruudun alaspäin
* move_up() - liikuttaa pelaajaa yhden ruudun ylöspäin
* move_left() - liikuttaa pelaajaa yhden ruudun vasemmalle
* move_right() - liikuttaa pelaajaa yhden ruudun oikealle
* interact() - laita pelaaja tekemään jotain pelimaailmassa

Tason tehtävä on seuraava:
* liikuta pelaaja oven päälle
* laita pelaaja avaamaan ovi

### Level 2

Tason muokattava koodi löytyy osoitteesta /spaghetti/src/level_solutions/level_2_solution.py

Tasolla ovat käytettävisä seuraavat metodikutsut:
* 'players' listan sisällä ovat alla olevat metodikutsut. jokainen elementti listassa on yksittäinen Player olio.
    * move_player_down() - liikuttaa pelaaja yhden ruudun alaspäin
    * move_player_up() - liikuttaa pelaajaa yhden ruudun ylöspäin
    * move_player_left() - liikuttaa pelaajaa yhden ruudun vasemmalle
    * move_player_right() - liikuttaa pelaajaa yhden ruudun oikealle
    * interact() - laita pelaaja tekemään jotain pelimaailmassa

Tason tehtävä on seuraava:
  * liikuta pelaajat ovien päälle
  * laita pelaajat avaamaan ovet

### Level 3

Tason muokattava koodi löytyy osoitteesta /spaghetti/src/level_solutions/level_3_solution.py

Tasolla ovat käytettävisä seuraavat metodikutsut:
* 'players' listan sisällä ovat alla olevat metodikutsut. jokainen elementti listassa on yksittäinen Player olio.
    * move_player_down() - liikuttaa pelaaja yhden ruudun alaspäin
    * move_player_up() - liikuttaa pelaajaa yhden ruudun ylöspäin
    * move_player_left() - liikuttaa pelaajaa yhden ruudun vasemmalle
    * move_player_right() - liikuttaa pelaajaa yhden ruudun oikealle
    * interact() - laita pelaaja tekemään jotain pelimaailmassa

Tason tehtävä on seuraava:
  * liikuta kaikki pelaajat ovien päälle
  * laita pelaajat avaamaan ovet

### Level 4

Tason muokattava koodi löytyy osoitteesta /spaghetti/src/level_solutions/level_4_solution.py

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

Tällä tasolla aletaan rakentamaan taloja.

Tason muokattava koodi löytyy osoitteesta /spaghetti/src/level_solutions/level_5 _solution.py

Tasolla on yksi pelaaja, ja sillä ovat käytettävisä seuraavat metodikutsut:
  * move_down() - liikuttaa pelaaja yhden ruudun alaspäin
  * move_up() - liikuttaa pelaajaa yhden ruudun ylöspäin
  * move_left() - liikuttaa pelaajaa yhden ruudun vasemmalle
  * move_right() - liikuttaa pelaajaa yhden ruudun oikealle 
  * get_position_x() - palauttaa pelaajan paikan x. x on sivuttainen suunta, vasemmalta oikealle.
  * get_position_y() - palauttaa pelaajan paikan y. y on vertikaalinen suunta, ylhäältä alas.
  * build_wall() - rakentaa seinän siihen kohtaan missä pelaaja sillä hetkellä on.
  * build_door() - rakentaa oven siihen kohtan missä pelaaja sillä hetkellä on.

Tason tehtävä on seuraava:
  * ohjaa pelaajaa merkattuja viivoja ja pilareita pitkin, rakentaen jokaisen viivan ja pilarin päälle seinät.
  * rakenna ovet koordinaatteihin (19, 22) ja (19, 18).

Huomaa, että seinien läpi ei voi kävellä!

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