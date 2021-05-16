# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne on jaettu seuraavalla tavalla pakkauksiin:

![](https://raw.githubusercontent.com/enkomat/ot-harjoitustyo/master/dokumentaatio/paketit.png)

Pakkaus *utilities* on kaiken pelilogiikan ja interaktiivisuuden pyörittäjä, *levels* sisältää kaiken yksittäisiin tasoihin liittyvän informaation, *game_objects* sisältää kaikki monistettavat pelin tasoihin liittyvät elementit. Pakkaus *enum_types* sisältää pelin tilojen hallintaan käytettävät enumeraattoriluokat.

## Käyttöliittymä

Käyttöliittymä sisältää kaksi näkymää:

- Tasovalikko
- Tasonäkymä

Tasovalikko on näkymä josta pelaaja voi klikkaamalla hypätä mihin tahansa pelin tasoon. Tasonäkymiä on yhtä paljon kun tasoja nyt pelissä on, eli vähän alle kymmenen. Jokainen taso on erinäköinen.

## Sovelluslogiikka

Sovelluksen ytimen muodostaa Util luokka, jonka sisällä on peliä pyörittävä `run()` metodi. Tästä metodista kannattaa aloittaa koodin lukeminen, koska se on oleellisin pelin toiminnan kannalta. Sovellus tarkkaillee tasovalikossa ollessaan jatkuvasti mistä kohdasta ruutua pelaaja hiirellä klikkaa ja jos tietyn tason napin kohdalta painetaan, siirrytään pelaamaan. Tämä tehdään `execute_main_menu()` metodin avulla. 

Pelatessa tiettyä tasoa `execute_gameplay()` metodi taasen tarkkailee joka hetkellä sattuuko pelaaja painamaan jostakin pelinäkymässä olevasta napista. Taso alkaa aina pause tilasta, ja kun pelaaja painaa play nappia lähtee *event_handler* suorittamaan pelaajan sille tason N *level_N_solution* luokan kautta antamia käskyjä.

Tässä sovelluksen luokkien suhteita kuvaileva luokkakaavio:

![](https://raw.githubusercontent.com/enkomat/ot-harjoitustyo/master/dokumentaatio/luokkakaavio.png)

Kaikki yhteydet *enum_types* paketin sisällä oleviin luokkiin ovat katkoviivalla, koska sen sisällä olevat luokat ovat staattisia eikä niistä missään vaiheessa tehdä olioita.

#### Ensimmäisen tason ratkaiseminen (vanha arkkitehtuuri, tämä suoritusjärjestys ei päde nykyisessä)

![](https://raw.githubusercontent.com/enkomat/ot-harjoitustyo/master/dokumentaatio/level1seq.png)