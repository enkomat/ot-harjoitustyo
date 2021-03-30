# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on peli nimeltä Spaghetti Master. Pelin ydinidea on puzzlepeli jota voi kontrolloida pelkästään kutsuilla koodista. Tarkoitus on lähtökohtaisesti viihdyttää ja mahdollisesti opettaa jotain uutta ohjelmoinnista samalla. Peli ei todennäköisesti sovellu kenellekkään, jolla ei aikaisempaa koodauskokemusta. Eli ideana on tehdä ongelmista kohtuu kinkkisiä.

## Pelin toiminta

Peli toimii kirjastona joka sinun pitää liittää luomaasi Python tiedostoon / tiedostoihin. Osa pulmista saattaa tarvita useampaa luokkaa, jotta pystyt suorittamaan ne toivotulla tavalla. Pelaajan pitää kutsua pelin tarjoamia metodeja oikealla tavalla ja modifioida pelin sisäisiä elementtejä (joita kutsutaan nodeiksi) Pythonin tarjoamilla tietorakenteilla.

Käytän [tätä](https://www.kenney.nl/assets/micro-roguelike) public domain grafiikka assettia.

## Käyttäjät

Sovelluksella on vain yksi käyttäjä, joka on sitä koodissaan käyttävä ohjelmoija.

## Käyttöliittymäluonnos

![](https://raw.githubusercontent.com/enkomat/ot-harjoitustyo/master/dokumentaatio/level1.png)

## Perusversion tarjoama toiminnallisuus

* Seuraavat metodikutsut: start_game(level_name), move_up(amt), move_down(amt), move_left(amt), move_right(amt), interact(), get_position(), create_node(), remove_node(), link_nodes(node_a, node_b), cut_link(node_a, node_b), get_node(index).
* Arvio siitä, kuinka monta kutsua pelille koodisi joutui tekemään. Tätä verrataan tavoiteaikaan.
* Mahdollisuus aloittaa viimeksi pelatusta tasosta. Jos sinulla on tallessa viimeksi pelaaman levelin nimi. Voit syöttää tämän koodiisi kun kutsut 'start_game' metodia. (Todennäköisesti tämä jo tallessa luomassasi tiedostossa jos olet kirjoittanut koodia kyseiselle tasolle.)

## Jatkokehitys

* Karttaeditori jonka avulla kuka tahansa voi tehdä oman pulmansa ja jakaa sen kavereille.