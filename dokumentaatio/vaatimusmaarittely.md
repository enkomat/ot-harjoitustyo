# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on peli nimeltä Spaghetti Master. Pelin ydinidea on puzzlepeli jota voi kontrolloida pelkästään kutsuilla koodista. Tarkoitus on lähtökohtaisesti viihdyttää ja mahdollisesti opettaa jotain uutta ohjelmoinnista samalla. Peli ei todennäköisesti sovellu kenellekkään, jolla ei aikaisempaa koodauskokemusta. Eli ideana on tehdä ongelmista kohtuu kinkkisiä.

## Pelin toiminta

Peli toimii kirjastona joka sinun pitää liittää annettuihin Python tiedostoihin. Pelaajan pitää kutsua pelin tarjoamia metodeja oikealla tavalla ja modifioida pelin sisäisiä elementtejä (rakentaa seiniä seiniä pelaajien liikkumista) Pythonin tarjoamilla tietorakenteilla.

Käytän [tätä](https://www.kenney.nl/assets/micro-roguelike) public domain grafiikka assettia.

## Käyttäjät

Pelillä on vain yksi käyttäjä, eli pelaaja.

## Käyttöliittymäluonnos (projektin alku)

![](https://raw.githubusercontent.com/enkomat/ot-harjoitustyo/master/dokumentaatio/level1.png)

## Lopullinen käyttöliittymä

Peli koostuu kahdesta näkymästä, tasovalikosta ja tasonäkymästä. Tasonäkymät muuttuvat jokaisen tason mukaan, mutta perusilme on samanlainen.

![](https://raw.githubusercontent.com/enkomat/ot-harjoitustyo/master/dokumentaatio/main_menu_screenshot.png)

![](https://raw.githubusercontent.com/enkomat/ot-harjoitustyo/master/dokumentaatio/level_1_screenshot.png)

## Perusversion tarjoama toiminnallisuus

* Kuusi tasoa, joista neljä perustuu pelaajien liikuttamiseen ja kaksi vikaa lisää talojen rakentamismekaniikan.
* Seuraavat metodikutsut: move_up(), move_down(), move_left(), move_right(), interact(), get_position_x(), get_position_y(), build_wall(), build_door()
* Tasonäkymä josta pelaaja voi klikkaamalla hypätä pelaamaan haluamaansa tasoa.
* Automaattinen koodinpäivitys klikatessa reset+play nappeja, jonka avulla jokaisen tason voi pelata läpi sulkematta peli-ikkunaa vaikka pelaaja tekisi useammankin koodimuutoksen pelatessaan joka tasoa.
* Tason siirtojen pyyhkiminen painamalla reset näppäintä.
* Play / pause ominaisuus pelatessa, joka mahdollistaa pelin pysäyttämisen.

## Jatkokehitys

* Karttaeditori jonka avulla kuka tahansa voi tehdä oman pulmansa ja jakaa sen kavereille.
* Mahdollisuus tallettaa edistystä.
* Eri pistemääriä paremmasta versus huonommasta ratkaisusta.
* Useampia tasoja, rutkasti enemmän haastetta myöhempiin tasoihin. Talojen ratkaiseminen mahdollistaa esim. convex hulling tyyppisten algoritmien käyttämisen ongelmanratkonnassa.
* Raiteita joille saa liikkuvia vaunuja. Nämä voivat mennä pisteiden läpi, jotka vastavaavat funktioita koodissa. Pelaaja voi muokata näitä funktioita tai luoda täysin uusia.
