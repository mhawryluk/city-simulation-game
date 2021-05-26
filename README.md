# city-simulation-game
Project for Python programming class

## Plan pracy:
#### (15.03 - 28.03):
- [x] zarys implementacji klas (deklaracja nazw i dziedziczenia)
- [x] game engine - funkcje do zarządzania grą (game loop, obsługa menu, interakcji gracza z programem)
- [x] mapa (grid: pola to działki do budowy budynków, krawędzie to drogi), wraz z wizualizacją
- [x] główne menu i okno gry (mapa i menu jej dotyczące)
- [x] ulice (budowanie)

#### (29.03 - 18.04):
- [x] implementacja budynków (wraz z mechanizmami budowania i wizualizacją)
- [x] implementacja obszarów zabudowania (ich wyznaczanie i wizualizacja)
- [x] mechanika budowy i zakupów (odpowiednie menu oraz mechanizm zapisu mapy)
- [x] menu opcji (in-game - dotyczy budowy i zarządzania miastem przez gracza)

#### (19.04 - 16.05):
- [x] symulacja procesów miejskich (odpowiednie funkcje programu symulujące zdarzenia jak ruch uliczny itp)
- [x] zdarzenia losowe
- [x] opcje zarządzania miastem i budynkami
- [x] ulepszenia budynków
- [x] system potrzeb i zadowolenia mieszkańców
- [x] komunikaty dotyczące stanu miasta, 
- [x] statystyki oraz mechanizmy symulujące ekonomię


## more TODO:
- [x] ustawianie strefy klikając, na razie jest tylko przeciągając
- [x] dom jest za duży
- [x] mechanizm pieniędzy - okienko przedstawiające stan konta, sprawdzanie czy można zbudować budynek, wydawanie pieniędzy
- [x] dźwięki gry
- [ ] menu opcji - więcej opcji wpływających na symulator
- [ ] chowanie wszystkich paneli przy przyciśnięciu escape
- [ ] zoom nie działa prawidłowo?
- [ ] wizualizacja poziomów zanieczyszczenia, dostępu do zasobów
- [x] okienko z pieniędzmi i satysfakcją 
- [x] upgrade
- [x] bulldoze - wyłączyć przy zmianie trybu
- [x] okienko upgrade'u pojawia się np. przy wyburzaniu
- [x] zapisywanie stref

## poprawki:
- [x] rozdzielić GUI od logiki gry
- [x] zoptymalizować kod highlight_roads
- [x] zastąpić import *
- [x] GameEngine - stałe w konstruktorze
- [x] WINDOW -> window
- [x] MEASUREMENTS -> usunąłem to pole
- [x] __init__.py
- [x] road_width_ratio -> zmienić w stałą
- [ ] przenieść wszystko związane z assetami do wspólnej klasy
- [x] pg.image.load...
- [x] CityImages - singleton?
- [ ] pickle
- [x] snake_case nazw plików

## TODO M:
- [ ] animacja samochodów
- [ ] zoom
- [ ] rozmiar obrazków

