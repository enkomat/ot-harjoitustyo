# Spaghetti Master
Tämän pelin idea on yhdistää Python ohjelmointia visuaalisiin puzzleihin.

## Pelaaminen
Pelin ensimmäistä tasoa voi pelata muokkaamalla 'level_1.py" tiedoston koodia. Ideana on liikuttaa hahmoa oikealla tavalla. Pelin voi avata komennolla 'poetry run invoke start'.

## Dokumentaatio

- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)

## Komentorivitoiminnot

### Pelin suorittaminen

Seuraava komento avaa pelin ensimmäisen tason:

```bash
poetry run invoke start
```

Tason voi myös vaihtoehtoisesti avata seruaavalla komennolla:

```bash
poetry run invoke level1
```

Pelin ensimmäisen tason pelaajan liikettä voit kontrolloida Python koodilla. Tätä koodia voit lähteä muokkaamaan suorittamalla seuraavan komennon, joka avaa sen oletuseditorissa:

```bash
open src/level_1.py
```

Koodia voi myös toki tarkastella ja editoida suoraan komentoriviltä Nanon avulla:

```bash
nano src/level_1.py
```

Pelissä on tällä hetkellä kolme tasoa, joiden kaikkien pitäisi toimia. Kun taso on suoritettu, ilmestyy peliruudulle "level solved" teksti.

Toisen tason voi avata seuraavilla komennoilla:

```bash
poetry run invoke level2
```

```bash
open src/level_2.py
```

Ja kolmannen seuraavilla:

```bash
poetry run invoke level3
```

```bash
open src/level_3.py
```

### Testaus

Testit ei vielä harmillisesti toimi kunnolla. Olen ollut hieman jäljessä aikataulusta, mutta tulevan viikon aikana pitää ottaa kiinni missatut asiat!