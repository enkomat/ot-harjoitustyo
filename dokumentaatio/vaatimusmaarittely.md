# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on auttaa käyttäjiä visualisoimaan heidän Pythonilla luomiaan algoritmeja. Prosessi ei kuitenkaan ole täysin automatisoitu, vaan käyttäjä asettaa kutsut haluamiinsa kohtiin.

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
                print(s,end=' ')
                visited[s] = True
                visulog.node(s, red)
 
            for node in self.adj[s]:
                if (not visited[node]):
                    stack.append(node)
                    visulog.node(node)
                    visulog.link(s, node)

Tämä alkuperäinen DFS koodi on [GeeksforGeeks](https://www.geeksforgeeks.org/iterative-depth-first-traversal/) sivustolta, mutta olen lisännyt siihen neljään kohtaan kutsun sovellukseeni.

Oletetaan, että meillä olisi seuraavanlainen simppeli verkko kyseessä:
    A : [B,C,E]
    B : [A,C]
    C : [A,B]
    D : [B]

Tällöin sovellus tulostaisi annetuilla neljällä kutsulla seuraavat kuvat annetussa järjestyksessä, kun haulle annetaan ensimmäisenä solmuna A:


Tässä on siis oletuksena, että sovellus tekee kaiken raskaamman työn taustalla ja käyttäjä voi kohtuu suoraviivaisesti asettaa kutsuja mihin tahansa kohtaan metodin koodia. Tällöin siis ohjelma automaattisesti piirtää käyttäjän kutsumat muodot ruudulle, asettelee muodot sopiviin kohtiin ja antaa muodoille tunnisteen. Myös käyttäjä voi määritellä minkä tahansa muodon kohdan (x+y parametreilla) sekä tunnisteen manuaalisesti. Jos tämän joutuisi tekemään aina käsin, olisi sovelluksen käyttäminen koodin seassa liian monimutkaista, joten lähtökohtaisesti nämä asiat tehdään automaattisesti.

## Käyttöliittymäluonnos



## Perusversion tarjoama toiminnallisuus

Neljä automatisoitua metodikutsua: node(), link(), box(), table(). Node piirtää solmun joka visualisoidaan ympyränä. Sisäänrakennettuna on kuitenkin myös ominaisuus yhdistää solmuja link metodilla, joka automaattisesti piirtää näiden välille viivan. Box luo neliön ruudun keskelle kun sitä kutsutaan. Kaikkia luotuja neliötä voi liikuttaa, skaalata, pyörittää, nimetä ja värittää uudelleen miten haluaa. Jokainen neliö tällöin sisältää siis referenssin niihin alkuperäisiin muuttujiin joihon se on liitetty. Table luo halutun kokoisen taulukon. Se voi perusversiossa olla maksimissaan 64*64 kokoinen. Tästä taulukosta voi kutsua mitä tahansa kohtaa tyyliin 'table(2, 10, color, string)'. Ensimmäinen parametri on rivi, toinen parametri kolumni, kolmas parametri kohdan väri ja neljäs parametri siinä lukeva teksti. Tauluja voi olla olemassa vain yksi. Tilanteessa, jossa käyttäjä kutsuu päällekkäin metodeja node, box ja table, piirtyvät ne toistensa päälle.

Käyttöliittymä on perusversiossa tulisi olemaaan todella askeettinen. Sovelluksen piirtämät freimit piirtyvät reaaliajassa niille kuuluvaan ikkunaan ja toiston jälkeen nämä freimit jäävät pyörimään luuppina kyseiseen ikkunaan.

## Jatkokehitys

Jos aikaa, niin luon sovellukselle luonnoksen kaltaisen käyttöliittymän. Tämän avulla käyttäjä voi käydä freimejä paremin yksi kerrallaan läpi tai valita kuinka nopeaan tahtiin ne toistuvat.
