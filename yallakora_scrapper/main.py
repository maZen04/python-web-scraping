import requests
from bs4 import BeautifulSoup
import csv
import os


BASE_URL = "https://www.yallakora.com/matches-center"


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/154.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8"
}


def get_page(date):

    url = f"{BASE_URL}?date={date}#days"

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=20
    )

    print("Status:", response.status_code)
    print("URL:", response.url)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("Length:", len(response.text))

    return response


def find_championships(soup):

    selectors = [
        "div.matchCard",
        ".matchCard",
        "div[class*='matchCard']"
    ]

    for selector in selectors:

        championships = soup.select(selector)

        if championships:
            print("Selector used:", selector)
            return championships

    return []


def get_championship_title(championship):

    title = championship.find("h2")

    if title:
        return title.get_text(" ", strip=True)

    return "Unknown Championship"


def get_matches(championship):

    matches = championship.select("div.item")

    if not matches:
        matches = championship.select(".item")

    return matches


def get_team_name(match, class_name):

    team = match.select_one(f".{class_name}")

    if team:
        return team.get_text(" ", strip=True)

    return "Unknown"


def get_score(match):

    score_elements = match.select(
        ".MResult .score"
    )

    if len(score_elements) >= 2:

        team_a_score = score_elements[0].get_text(
            strip=True
        )

        team_b_score = score_elements[1].get_text(
            strip=True
        )

        return f"{team_a_score} - {team_b_score}"

    return "Unknown"


def get_match_time(match):

    time_element = match.select_one(".time")

    if time_element:

        return time_element.get_text(
            " ",
            strip=True
        )

    return "Unknown"


def extract_match_data(championships):

    matches_details = []

    for championship in championships:

        championship_title = get_championship_title(
            championship
        )

        print(
            "\nChampionship:",
            championship_title
        )

        all_matches = get_matches(
            championship
        )

        print(
            "Matches found:",
            len(all_matches)
        )

        for match in all_matches:

            team_a = get_team_name(
                match,
                "teamA"
            )

            team_b = get_team_name(
                match,
                "teamB"
            )

            score = get_score(match)

            match_time = get_match_time(
                match
            )

            print()
            print("Championship:", championship_title)
            print("Team A:", team_a)
            print("Score:", score)
            print("Team B:", team_b)
            print("Time:", match_time)
            print("=" * 50)

            matches_details.append({
                "نوع البطولة": championship_title,
                "الفريق الاول": team_a,
                "النتيجة": score,
                "الفريق الثاني": team_b,
                "الوقت": match_time
            })

    return matches_details


def save_to_csv(matches_details, date):

    if not matches_details:

        print("\nNo matches found.")

        return

    # Get the folder where this Python file is located
    folder = os.path.dirname(
        os.path.abspath(__file__)
    )

    # Convert date from MM/DD/YYYY to MM-DD-YYYY
    safe_date = date.replace("/", "-")

    filename = os.path.join(
        folder,
        f"matches_{safe_date}.csv"
    )

    with open(
        filename,
        "w",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "نوع البطولة",
                "الفريق الاول",
                "النتيجة",
                "الفريق الثاني",
                "الوقت"
            ]
        )

        writer.writeheader()

        writer.writerows(
            matches_details
        )

    print(
        f"\nSaved successfully to: {filename}"
    )


def main():

    date = input(
        "Please enter a date (MM/DD/YYYY): "
    ).strip()

    response = get_page(date)

    if response.status_code != 200:

        print("\nRequest failed.")

        print("\nResponse:")
        print(response.text[:1000])

        return

    soup = BeautifulSoup(
        response.text,
        "lxml"
    )

    championships = find_championships(
        soup
    )

    print(
        "\nChampionships found:",
        len(championships)
    )

    if not championships:

        print(
            "\nNo championship elements found."
        )

        print(
            "\nFirst 2000 characters:"
        )

        print(
            response.text[:2000]
        )

        return

    matches_details = extract_match_data(
        championships
    )

    save_to_csv(
        matches_details,
        date
    )


if __name__ == "__main__":
    main()