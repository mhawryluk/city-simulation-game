# city-simulation-game
project for Python programming class

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
- [ ] symulacja procesów miejskich (odpowiednie funkcje programu symulujące zdarzenia jak ruch uliczny itp)
- [ ] zdarzenia losowe
- [ ] opcje zarządzania miastem i budynkami (w tym ulepszenia)
- [ ] system potrzeb i zadowolenia mieszkańców
- [ ] komunikaty dotyczące stanu miasta, statystyki oraz mechanizmy symulujące ekonomię


## obecne TODO:
- [ ] ustawianie strefy klikając, na razie jest tylko przeciągając
- [ ] dom jest za duży
- [ ] mechanizm pieniędzy - okienko przedstawiające stan konta, sprawdzanie czy można zbudować budynek, wydawanie pieniędzy
- [ ] dźwięki gry
- [ ] menu opcji - więcej opcji wpływających na symulator
- [ ] zonetypes - zmienić ze stringów w enumy/stałe
- [ ] chowanie wszystkich paneli przy przyciśnięciu escape
- [ ] zoom nie działa prawidłowo?
- [ ] wizualizacja poziomów zanieczyszczenia, dostępu do zasobów
- [ ] okienko z pieniędzmi i satysfakcją 
- [ ] upgrade
- [ ] bulldoze
- [ ] zapisywanie stref

## poprawki:
- [ ] rozdzielić GUI od logiki gry
- [x] zoptymalizować kod highlight_roads
- [x] zastąpić import *
- [x] GameEngine - stałe w konstruktorze
- [x] WINDOW -> window
- [x] MEASUREMENTS -> usunąłem to pole
- [x] __init__.py
- [x] road_width_ratio -> zmienić w stałą
- [ ] przenieść wszystko związane z assetami do wspólnej klasy
- [x] pg.image.load...
- [ ] CityImages - singleton?
- [ ] pickle
- [x] snake_case nazw plików

