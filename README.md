# Spaghetti Master
Tämän pelin idea on yhdistää Python ohjelmointia visuaalisiin puzzleihin.

## Pelaaminen
Pelin ensimmäistä tasoa voi pelata muokkaamalla 'level_1.py" tiedoston koodia. Ideana on liikuttaa hahmoa oikealla tavalla. Pelin voi avata komennolla 'poetry run invoke start'.

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)

## Komentorivitoiminnot

### Pelin pelaaminen

## Level 1

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

Tason tehtävä on seuraava:
    * liikuta pelaaja oven päälle
    * laita pelaaja avaamaan ovi

### Testaus

Testit ei vielä harmillisesti toimi kunnolla. Olen ollut hieman jäljessä aikataulusta, mutta tulevan viikon aikana pitää ottaa kiinni missatut asiat!