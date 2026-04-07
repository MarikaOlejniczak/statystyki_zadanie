Zadanie rekrutacyjne -Statystyki
Aplikacja w Pythonie polegająca na pobraniu i analizie danych z serwisu JSONPlaceholder.

![Dashboard Screenshot](https://github.com/MarikaOlejniczak/statystyki_zadanie/blob/main/screenshot.png?raw=true)

## O projekcie
To mój pierwszy projekt, w którym połączyłam pobieranie danych z API z prostą analityką w Pandas. Celem było stworzenie czytelnego dashboardu, który:
- Pokazuje podstawowe metryki o użytkownikach i postach.
- Wizualizuje na wykresach aktywność użytkowników (komentarze) i postępy w zadaniach (TODOs).
- Prezentuje tabelę 5 najpopularniejszych postów.

## Nauka i wykorzystanie AI
Przy pracy nad tym projektem wspierałam się modelem AI (Gemini). Było to dla mnie świetne narzędzie naukowe, które pomogło mi:
- Poprawnie napisać logikę `merge`** w Pandas, aby połączyć tabelę użytkowników z ich postami i komentarzami i sprawdzić moje błędy.
- **Dopracować stylizację CSS** dla metryk w Streamlit, żeby uzyskać ładny "Dark Mode".
- **Wyjaśnić błędy** i poprowadzić przez proces wdrażania aplikacji na Streamlit Cloud.

## Technologie
- **Python** (Pandas, Requests)
- **Streamlit** (Interfejs i Dashboard)
- **Plotly** (Wykresy interaktywne)

## Jak uruchomić lokalnie
1. Zainstaluj biblioteki: `pip install -r requirements.txt`
2. Uruchom: `streamlit run app.py`
