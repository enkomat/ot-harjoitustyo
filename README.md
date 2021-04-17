# Spaghetti Master
Tämän pelin idea on yhdistää Python ohjelmointia visuaalisiin puzzleihin.

## Pelaaminen
Pelin ensimmäistä tasoa voi pelata muokkaamalla 'level_1.py" tiedoston koodia. Pelin voi avata komennolla 'poetry run invoke start'.

## Dokumentaatio

- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)

## Komentorivitoiminnot

### Pelin suorittaminen

Pelin pystyy aloittamaan seuraavalla komennolla:

```bash
poetry run invoke start
```

Pelin ensimmäisen tason pelaajan liikettä voit kontrolloida Python koodilla. Tätä koodia voit lähteä muokkaamaan suorittamalla seuraavan komennon, joka avaa sen oletuseditorissa:

```bash
open src/level_1.py
```

Koodia voi myös toki tarkastella ja editoida suoraan komentoriviltä Nanon avulla:

```bash
nano src/level_1.py
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```