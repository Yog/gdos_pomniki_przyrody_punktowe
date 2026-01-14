# How to use:
1. load `gdos_pomniki_przyrody_punktowe-minified.geojson` into JOSM
2. select natural monuments on an area you're interested with, invert selection and remove everything else
3. confirm the location is good enough as CRFOP accuracy of geolocalized features may vary
4. confirm that your natural monument is not mapped already and if it is, update its properties
5. remove `podtyp=*` property or rename it

## properties of a feature:
```
crfop:inscription_date=2004-12-26                / adoption date of this natural monument
denotation=natural_monument
genus=Quercus
leaf_cycle=deciduous
leaf_type=broadleaved
natural=tree
protected=yes
ref:CRFOP=114952                                 / ID of monuments group
ref:gid=159172                                   / ID of this specific monument
ref:inspire=PL.ZIPOP.1393.PP.1061011.5064        / ZIPOP object identifier
link=https://crfop.gdos.gov.pl/CRFOP/widok/viewpomnikprzyrody.jsf?fop=PL.ZIPOP.1393.PP.1061011.5064
species=Quercus robur
species:pl=Dąb szypułkowy
species:wikidata=Q165145
species:wikipedia=pl:Dąb szypułkowy
```
## good to add properties:
```
height=23.6               / in meters, usually listed on CRFOP
circumference=2.92        / in meters, also usually listed on CRFOP
diameter=920              / that's in millimeters
diameter_crown=16.2       / in meters
description=              / description can be sometimes found on CRFOP
start_date=1888           / date when the tree was planted, usually approximate
```

Use `gdos_pomniki_przyrody_punktowe-JOSM.geojson` only to control possible data corruption as it has many features in its original format is not minified. 
