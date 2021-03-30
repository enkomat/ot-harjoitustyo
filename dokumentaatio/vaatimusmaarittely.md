# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on auttaa käyttäjiä visualisoimaan heidän Pythonilla luomiaan algoritmeja ja ohjelmia. Prosessi ei kuitenkaan ole täysin automatisoitu, vaan käyttäjä asettaa kutsut haluamiinsa kohtiin.

## Sovellulsen toiminta

Tämän jälkeen käyttäjä näkee algoritminsa toiminnan reaaliajassa ja voi käyttöliittymän kautta katsoa visualisaation alusta loppuun uudestaan, taikka selata lläpi luotuja freimejä. Tässä esimerkki siitä, miten ohjelmaa kutsutaan:

    def DFS(self,s):           
        visited = [False for i in range(self.V)]
        stack = []
        stack.append(s)
 
        while (len(stack)):
            s = stack[-1]
            stack.pop()
            visulog.node(s)
 
            if (not visited[s]):
                visited[s] = True
                visulog.node(s, red)
 
            for node in self.adj[s]:
                if (not visited[node]):
                    stack.append(node)
                    visulog.node(node)
                    visulog.link(s, node)

Tämä alkuperäinen DFS koodi on [GeeksforGeeks](https://www.geeksforgeeks.org/iterative-depth-first-traversal/) sivustolta, mutta olen lisännyt siihen neljään kohtaan kutsun sovellukseeni. Node metodin parametrit ovat seuraavat: Node, name, color, size, position. Metodi on ylikuormitettu niin, että siitä voi käyttää mitä tahansa variaatioita. Lyhyin mahdollinen kutsu sisältää pelkän referenssin haluttuun solmuun. Link metodin parametrit ovat taas seuraavat: node1, node2, name, color, width. Lyhyin metodikutsu on vain yksinkertainen kahden solmun linkitys.

Oletetaan, että meillä olisi seuraavanlainen simppeli verkko kyseessä:
    
    A : [B,C,E]
    B : [A,C]
    C : [A,B]
    D : [B]

Tällöin sovellus tulostaa annetuilla neljällä kutsulla seuraavat kuvat annetussa järjestyksessä, kun haulle annetaan ensimmäisenä solmuna A:

Tässä on siis lähtökohtana, että sovellus tekee kaiken raskaamman työn taustalla ja käyttäjä voi kohtuu suoraviivaisesti asettaa kutsuja mihin tahansa kohtaan metodin koodia. Tällöin siis ohjelma automaattisesti piirtää käyttäjän kutsumat muodot ruudulle, asettelee muodot sopiviin kohtiin ja antaa muodoille tunnisteen. Myös käyttäjä voi määritellä minkä tahansa muodon kohdan (x+y parametreilla) sekä tunnisteen manuaalisesti. Jos tämän joutuisi tekemään aina käsin, olisi sovelluksen käyttäminen koodin seassa liian monimutkaista, joten lähtökohtaisesti nämä asiat tehdään automaattisesti. Ideana on, että esim. metodikutsulla 'visulog.node(myNode, blue)' luodaan taustalle lista, joka pitää mielessään kaikki spesifit solmut joita on luotu ja listätään 'myNode' siihen. (Tämä tietorakenne on täysin erillinen mistään, mitä käyttäjän omaan solmuja pyörittävään tietorakenteeseen liittyy. Niiden ei ole tarkoitus kommunikoida keskenään.) Tällöin jos kutsut myöhemmin 'visulog.node(myNode, red)', osaa taustalla pyörivä sovellus hakea oikean solmun ja uudelleenvärittää sen sinisestä punaiseksi.

Vielä yksi esimerkki ohjelmistotekniikan materiaalista:
   
    class Kassapaate:
        def __init__(self):
            visulog.table(2)
            self.kassassa_rahaa = 100000
            self.edulliset = 0
            self.maukkaat = 0
            visulog.table(1, self.kassassa_rahaa)
            visulog.table(0, self.edulliset)
            visulog.table(0, self.maukkaat)

        def syo_edullisesti_kateisella(self, maksu):
            if maksu >= 240:
                self.kassassa_rahaa = self.kassassa_rahaa + 240
                self.edulliset += 1
                visulog.table.update()
                return maksu - 240
            else:
                return maksu

        def syo_maukkaasti_kateisella(self, maksu):
            if maksu >= 400:
                self.kassassa_rahaa = self.kassassa_rahaa + 400
                self.maukkaat += 1
                visulog.table.update()
                return maksu - 400
            else:
                return maksu

        def syo_edullisesti_kortilla(self, kortti):
            if kortti.saldo >= 240:
                kortti.ota_rahaa(240)
                self.edulliset += 1
                visulog.table.update()
                return True
            else:
                return False

        def syo_maukkaasti_kortilla(self, kortti):
            if kortti.saldo >= 400:
                kortti.ota_rahaa(400)
                self.maukkaat += 1
                visulog.table.update()
                return True
            else:
                return False

        def lataa_rahaa_kortille(self, kortti, summa):
            if summa >= 0:
                kortti.lataa_rahaa(summa)
                self.kassassa_rahaa += summa
            else:
                return
    
    class Maksukortti:
        def __init__(self, saldo):
            self.saldo = saldo
            visulog.table(1, self.saldo)

        def lataa_rahaa(self, lisays):
            self.saldo += lisays
            visulog.table.update()

        def ota_rahaa(self, maara):
            if self.saldo < maara:
                visulog.table(self, red)
                return False

            self.saldo = self.saldo - maara
            visulog.table.update()
            return True

        def __str__(self):
            saldo_euroissa = round(self.saldo / 100, 2)
        
            return f"saldo: {saldo_euroissa}"

Tässä käytetään vähän monimutkaisemmalla tavalla sovelluksen table luokkaa. Jos käyttäjä kutsuu pelkästään kolumnia eikä riviä kuten esimerkissä on tehty, lisätään uusi tulokas aina viimeisen paikan jälkeen seuraavalle. Tällöin voidaan helpommin handlata tilanteita joissa ei ole varmuutta monta riviä lopulliseen taulukkoon tulee. Jos tietyn taulun kohta halutaan löytää ja sitä muokata, voidaan se tehdä esimerkissä metodikutsulla 'visulog.table(self, red)'. Tällöin tuo spesifi olio haetaan sovelluksen hallinnoimasta listasta ja sitä vastaavaan ruutuun tehdään muutos. Kyseisessä tilanteessa siis ruutu maalataan punaiseksi jos kortilta loppuu saldo.

## Käyttäjät

Sovelluksella on vain yksi käyttäjä, joka on sitä koodissaan käyttävä ohjelmoija.

## Käyttöliittymäluonnos

![](https://raw.githubusercontent.com/enkomat/ot-harjoitustyo/master/dokumentaatio/UI.jpeg)

## Perusversion tarjoama toiminnallisuus

* Neljä metodikutsua: node(), link(), box(), table(). 
    * Node piirtää solmun joka visualisoidaan ympyränä. Sisäänrakennettuna on kuitenkin myös ominaisuus yhdistää solmuja link metodilla, joka automaattisesti piirtää näiden välille viivan. Node ja link ovat siis parivaljakko, jota käytetään visualisoimaan verkkoihin liittyviä algoritmeja.
    * Box luo neliön ruudun keskelle kun sitä kutsutaan. Kaikkia luotuja neliötä voi liikuttaa, skaalata, pyörittää, nimetä ja värittää uudelleen miten haluaa. Jokainen neliö tällöin sisältää siis referenssin niihin alkuperäisiin muuttujiin joihon se on liitetty.
    * Table luo halutun kokoisen taulukon. Se voi perusversiossa olla maksimissaan 255*255 kokoinen. Tästä taulukosta voi kutsua mitä tahansa kohtaa tyyliin 'table(2, 10, color, string)'. Ensimmäinen parametri on rivi, toinen parametri kolumni, kolmas parametri kohdan väri ja neljäs parametri siinä lukeva teksti. Tauluja voi olla olemassa vain yksi. 
* Tilanteessa, jossa käyttäjä kutsuu päällekkäin metodeja node, box tai table, piirtyvät ne toistensa päälle.
* Käyttöliittymä on perusversiossa tulisi olemaaan todella askeettinen. Sovelluksen piirtämät freimit piirtyvät reaaliajassa niille kuuluvaan ikkunaan ja toiston jälkeen nämä freimit jäävät pyörimään luuppina kyseiseen ikkunaan.

## Jatkokehitys

* Sovellukselle luonnoksen kaltainen käyttöliittymän. Tämän avulla käyttäjä voi käydä freimejä paremin yksi kerrallaan läpi tai valita kuinka nopeaan tahtiin ne toistuvat. 
* Toiminnallisuus, jolla käyttäjä voisi exportata visualisoinnin png taikka gif muodossa olisi kätevä lisä. Näin voisi luoda vaikkapa GitHubiin tai muualle dokumentaatioon graafisia avauksia siitä, miten tietyt metodit toimii.