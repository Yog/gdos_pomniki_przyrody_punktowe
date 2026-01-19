- 🇬🇧 [English instructions](README.en.md)

# Jak używać:
1. wczytaj `gdos_pomniki_przyrody_punktowe-minified.geojson` do JOSM
2. zaznacz pomniki przyrody na obszarze, który Cię interesuje, odwróć zaznaczenie i usuń wszystko pozostałe
3. sprawdź, czy dany pomnik przyrody nie jest już zmapowany, a jeśli jest — zaktualizuj jego właściwości
4. upewnij się, że lokalizacja jest wystarczająco dobra, ponieważ dokładność geolokalizacji obiektów w CRFOP może być wątpliwa  
   * ~88 obiektów ma przypisane 2 lub więcej gatunków, ponieważ ich lokalizacja była taka sama, choć w rzeczywistości jest różna — może to zostać poprawione przy użyciu dobrej fotomapy lub w terenie
5. usuń właściwość `podtyp=*` lub zmień jej nazwę
6. występują również inne obiekty chronione z właściwością `obiekt=*`, które nie są drzewami. Można je mapować, ale **przed wysłaniem dokładnie sprawdź wszystkie tagi**:
   * `głaz narzutowy` — głaz narzutowy
   * `jaskinia` — wejście do jaskini
   * `skałka` — formacja skalna / skałka
   * `wodospad` — wodospad
   * `źródło` — źródło
   * `inne` — zazwyczaj chronione pnącze, ale może to być cokolwiek innego z powyższych

## właściwości obiektu:
```
crfop:inscription_date=1994-06-01                   / data ustanowienia pomnika przyrody
denotation=natural_monument
genus=Tilia
leaf_cycle=deciduous
leaf_type=broadleaved
name=Dagmara
natural=tree
protected=yes
ref:CRFOP=75950                                     / ID grupy pomników
ref:gid=30484                                       / ID konkretnego pomnika
ref:inspire=PL.ZIPOP.1393.PP.0201011.70             / identyfikator obiektu ZIPOP
website=https://crfop.gdos.gov.pl/CRFOP/widok/viewpomnikprzyrody.jsf?fop=PL.ZIPOP.1393.PP.0201011.70
species=Tilia platyphyllos
species:pl=Lipa szerokolistna
species:wikidata=Q156831
species:wikipedia=pl:Lipa szerokolistna
```

## warto dodać właściwości:
```
height=23.6
circumference=2.92
diameter=920
diameter_crown=16.2
description=
start_date=1888
```

Używaj pliku `gdos_pomniki_przyrody_punktowe-init-ref.geojson` **wyłącznie** do kontroli ewentualnych uszkodzeń danych — zawiera on wiele obiektów w oryginalnym (niezminifikowanym) formacie.

## Q-kody `species:wikidata` i lista `species:wikipedia`:

```
Ailanthus altissima         › Q159570 › pl:Bożodrzew gruczołkowaty
Betula pendula              › Q156895 › pl:Brzoza brodawkowata
Betula pubescens            › Q157624 › pl:Brzoza omszona
Fagus sylvatica             › Q146149 › pl:Buk zwyczajny
Taxus baccata               › Q179729 › pl:Cis pospolity
Taxus × media               › Q6292155 › pl:Cis pośredni
Quercus petraea             › Q158608 › pl:Dąb bezszypułkowy
Quercus rubra               › Q147525 › pl:Dąb czerwony
Quercus robur               › Q165145 › pl:Dąb szypułkowy
Pseudotsuga menziesii       › Q156687 › pl:Daglezja zielona
Gleditsia triacanthos       › Q157650 › pl:Glediczja trójcierniowa
Carpinus betulus            › Q158776 › pl:Grab pospolity
Pyrus communis              › Q146281 › pl:Grusza pospolita
Juniperus communis          › Q26325  › pl:Jałowiec pospolity
Sorbus torminalis           › Q147459 › pl:Jarząb brekinia
Sorbus aucuparia            › Q146198 › pl:Jarząb pospolity
Sorbus intermedia           › Q27980  › pl:Jarząb szwedzki
Fraxinus pennsylvanica      › Q161164 › pl:Jesion pensylwański
Fraxinus angustifolia       › Q518949 › pl:Jesion wąskolistny
Fraxinus excelsior          › Q156907 › pl:Jesion wyniosły
Abies concolor              › Q145939 › pl:Jodła kalifornijska
Abies homolepis             › Q1166864 › pl:Jodła nikko
Abies alba                  › Q146992 › pl:Jodła pospolita
Aesculus × carnea           › Q163779 › pl:Kasztanowiec czerwony
Aesculus hippocastanum      › Q26899  › pl:Kasztanowiec zwyczajny
Acer rubrum                 › Q161364 › pl:Klon czerwony
Acer pseudoplatanus         › Q156944 › pl:Klon jawor
Acer negundo                › Q161166 › pl:Klon jesionolistny
Acer campestre              › Q158785 › pl:Klon polny
Acer saccharinum            › Q158301 › pl:Klon srebrzysty
Acer platanoides            › Q26745  › pl:Klon zwyczajny
Corylus colurna             › Q148939 › pl:Leszczyna turecka
Tilia cordata               › Q158746 › pl:Lipa drobnolistna
Tilia × europaea            › Q163760 › pl:Lipa holenderska
Tilia × euchlora            › Q159657 › pl:Lipa krymska
Tilia tomentosa             › Q161382 › pl:Lipa srebrzysta
Tilia platyphyllos          › Q156831 › pl:Lipa szerokolistna
Magnolia                    › Q157017 › pl:Magnolia
Magnolia × soulangeana      › Q731443 › pl:Magnolia pośrednia
Ginkgo biloba               › Q43284  › pl:Miłorząb dwuklapowy
Larix decidua               › Q146048 › pl:Modrzew europejski
Alnus glutinosa             › Q156904 › pl:Olsza czarna
Platanus × hispanica        › Q161374 › pl:Platan klonolistny
Robinia pseudoacacia        › Q157417 › pl:Robinia akacjowa
Pinus nigra                 › Q145954 › pl:Sosna czarna
Pinus rigida                › Q837410 › pl:Sosna smołowa
Pinus strobus               › Q157230 › pl:Sosna wejmutka
Pinus sylvestris            › Q133128 › pl:Sosna zwyczajna
Picea abies                 › Q145992 › pl:Świerk pospolity
Picea omorika               › Q147824 › pl:Świerk serbski
Populus balsamifera         › Q149471 › pl:Topola balsamiczna
Populus × berolinensis      › Q4460779 › pl:Topola berlińska
Populus alba                › Q146269 › pl:Topola biała
Populus nigra               › Q147064 › pl:Topola czarna
Populus × canadensis        › Q149622 › pl:Topola kanadyjska
Populus tremula             › Q146110 › pl:Topola osika
Populus × canescens         › Q149553 › pl:Topola szara
Liriodendron tulipifera     › Q158783 › pl:Tulipanowiec amerykański
Ulmus glabra                › Q147498 › pl:Wiąz górski
Ulmus minor                 › Q147487 › pl:Wiąz pospolity
Ulmus laevis                › Q147492 › pl:Wiąz szypułkowy
Salix alba                  › Q156918 › pl:Wierzba biała
Salix fragilis              › Q157518 › pl:Wierzba krucha
Prunus avium                › Q165137 › pl:Wiśnia ptasia
Thuja plicata               › Q147417 › pl:Żywotnik olbrzymi
Thuja occidentalis          › Q147468 › pl:Żywotnik zachodni
```
Najczęściej spotykane gatunki bez określonej odmiany *(sp.)*
```
Tilia        › Q127849 › pl:Lipa
Fagus        › Q25403 › pl:Buk
Quercus      › Q12004 › pl:Dąb
Acer         › Q42292 › pl:Klon
Populus      › Q25356 › pl:Topola
Aesculus     › Q158752 › pl:Kasztanowiec
Salix        › Q36050 › pl:Wierzba
Ulmus        › Q131113 › pl:Wiąz
```

## Minifikacja pliku .geojson z JOSM poleceniem Pythona:
```python
$ python -c "import sys
w=sys.stdout.buffer.write
for line in sys.stdin.buffer:
    w(line.lstrip().rstrip(b'\r\n'))" < gdos_pomniki_przyrody_punktowe-JOSMgenerated.geojson > gdos_pomniki_przyrody_punktowe-minified.geojson
```
