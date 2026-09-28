import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# ==========================================
# CONFIGURATION
# ==========================================

BASE_URL = "https://www.moteur.ma/fr/voiture/achat-voiture-occasion"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


# ==========================================
# RÉCUPÉRER LE HTML D'UNE PAGE
# ==========================================

def get_html(page):

    url = f"{BASE_URL}?page={page}"

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print("Erreur :", response.status_code)
        return None

    return BeautifulSoup(response.text, "html.parser")


# ==========================================
# EXTRAIRE LES DONNÉES
# ==========================================

def extract_cars(soup):

    cars_data = []

    cars = soup.find_all(
        "div",
        class_="card mb-0 overflow-hidden h-100 ads-index-card"
    )

    print(f"{len(cars)} annonces trouvées.")

    for car in cars:

        title = car.find("h5", class_="ads-index-title")
        title = title.get_text(strip=True) if title else "N/A"

        price = car.find("h4", class_="ad-price-grid")
        price = price.get_text(strip=True) if price else "N/A"

        city = "N/A"

        desc = car.find("div", class_="item-card9-desc")

        if desc:
            links = desc.find_all("a")

            if len(links) > 0:
                city = links[0].get_text(strip=True)

        year = gearbox = fuel = mileage = "N/A"

        meta = car.find("div", class_="ad-meta")

        if meta:

            spans = meta.find_all("span")

            if len(spans) >= 4:

                year = spans[0].get_text(strip=True)

                gearbox = spans[1].get_text(strip=True)

                fuel = spans[2].get_text(strip=True)

                mileage = spans[3].get_text(strip=True)

        link = car.find("a", href=True)
        link = link["href"] if link else "N/A"

        cars_data.append({

            "Marque_Modele": title,
            "Prix": price,
            "Ville": city,
            "Annee": year,
            "Boite": gearbox,
            "Carburant": fuel,
            "Kilometrage": mileage,
            "Lien": link

        })

    return cars_data


# ==========================================
# SAUVEGARDER CSV
# ==========================================

def save_csv(data):

    df = pd.DataFrame(data)

    df.to_csv(

        "../data/cars.csv",

        index=False,

        encoding="utf-8-sig"

    )

    print("\nDataset enregistré.")
    print(df.head())


# ==========================================
# PROGRAMME PRINCIPAL
# ==========================================
def main():

    all_cars = []

    TOTAL_PAGES = 35

    for page in range(1, TOTAL_PAGES + 1):

        print(f"\n==============================")
        print(f"Scraping de la page {page}/{TOTAL_PAGES}")
        print(f"==============================")

        soup = get_html(page)

        if soup:

            cars = extract_cars(soup)

            all_cars.extend(cars)

            print(f"Total actuel : {len(all_cars)} annonces")

        else:

            print(f"Impossible de récupérer la page {page}")

        # Petite pause pour ne pas surcharger le serveur
        time.sleep(2)

    save_csv(all_cars)

    print("\n===================================")
    print("SCRAPING TERMINÉ")
    print(f"Nombre total d'annonces : {len(all_cars)}")
    print("Fichier enregistré : data/cars.csv")
    print("===================================")


if __name__ == "__main__":
    main()