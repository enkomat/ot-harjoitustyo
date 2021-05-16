# Testausdokumentti

Ohjelmaa on testattu sekä automatisoiduin unittest testein ja sen lisäksi manuaalisesti.

### Testauskattavuus

Sovelluksen testikattavuus on 78% käyttöliittymä ja sen kaikki interaktiot mukaanluettuna.

![](https://raw.githubusercontent.com/enkomat/ot-harjoitustyo/master/dokumentaatio/testikattavuus.png)

Testaamatta jäivät iso osa Util luokassa sijaitsevat käyttöliittymään liittyvistä hiirenklikkaus interaktioista. Testit tällä hetkellä testaa pystyykö kunkin tason suorittaa onnistuneella ratkaisulla sekä sitä, että jääkö taso suorittamatta jos antaa puutteellisen ratkaisun.