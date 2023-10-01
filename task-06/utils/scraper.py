from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

class MatchData:
    def __init__(self, status, description , match_details, tournament_info, team1_name, team1_score, team1_over, team2_name, team2_score, team2_over, additional_info , scorecard_link):
        self.status = status
        self.description = description
        self.match_details = match_details
        self.tournament_info = tournament_info
        self.team1_name = team1_name
        self.team1_score = team1_score
        self.team1_over = team1_over
        self.team2_name = team2_name
        self.team2_score = team2_score
        self.team2_over = team2_over
        self.additional_info = additional_info
        self.scorecard_link = scorecard_link


def extract_data(html_snippet):
    soup = BeautifulSoup(html_snippet, 'html.parser')

    first_match_div = soup.find('div', class_='ds-px-4 ds-py-3')
    if first_match_div:
        match_status_element = first_match_div.find(class_='ds-text-tight-xs ds-font-bold ds-uppercase ds-leading-5')
        match_status = match_status_element.text.strip() if match_status_element else None
        if match_status.startswith('Today'):
            match_schedule = first_match_div.find('span', class_='ds-text-tight-xs ds-font-bold ds-uppercase ds-leading-5').text
            match_details = first_match_div.find('div', class_='ds-text-tight-xs ds-truncate ds-text-typo-mid3').text
            tournament_info = first_match_div.find('span', class_='ds-text-tight-xs ds-text-typo ds-underline ds-decoration-ui-stroke hover:ds-text-typo-primary hover:ds-decoration-ui-stroke-primary ds-block !ds-inline').text
            team1_name = first_match_div.find_all('p', class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate')[0].text
            team2_name = first_match_div.find_all('p', class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate')[1].text
            starts_in = first_match_div.find("p", class_="ds-text-tight-s ds-font-regular ds-truncate ds-text-typo").text
            url = first_match_div.find('a', class_='ds-no-tap-higlight')['href']
            return {
                'state' : "scheduled",
                'match_schedule' : match_schedule,
                'match_details' : match_details,
                'tournament_info' : tournament_info,
                'team1_name' : team1_name,
                'team2_name' : team2_name,
                'starts_in' : starts_in,
                'url' : url
            }

        elif match_status == 'RESULT':
            match_details = first_match_div.find('div', class_='ds-text-tight-xs ds-truncate ds-text-typo-mid3').text
            tournament_info = first_match_div.find('span', class_='ds-text-tight-xs ds-text-typo ds-underline ds-decoration-ui-stroke hover:ds-text-typo-primary hover:ds-decoration-ui-stroke-primary ds-block !ds-inline').text
            team1_name = first_match_div.find_all('p', class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate')[0].text
            team2_name = first_match_div.find_all('p', class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate')[1].text
            team1_score = first_match_div.find_all('strong', class_='')[0].text
            team2_score = first_match_div.find_all('strong', class_='')[1].text
            over_info = first_match_div.find_all('div', class_='ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap')
            match_result = first_match_div.find('p', class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo').text
            url = first_match_div.find('a', class_='ds-no-tap-higlight')['href']
            return {
                'state': 'result',
                'match_details' : match_details,
                'tournament_info' : tournament_info,
                'team1_name' : team1_name,
                'team2_name' : team2_name,
                'team1_score' : team1_score,
                'team2_score' : team2_score,
                'team1_over': over_info[0].text,
                'team2_over': over_info[1].text,
                'match_result' : match_result,
                'url' : url
            }

        elif match_status == 'Live':
            team1_element = first_match_div.select_one('.ci-team-score:nth-child(1)')
            team1_name = team1_score = team1_over = "N/A"  # Default values

            if team1_element:
                team1_name = team1_element.select_one('.ds-capitalize').text.strip()
                team1_score_element = team1_element.select_one('.ds-text-compact-s strong')
                team1_over_element = team1_element.select_one('.ds-text-compact-xs')
                if team1_score_element:
                    team1_score = team1_score_element.text.strip()
                if team1_over_element:
                    team1_over = team1_over_element.text.strip()

            team2_element = first_match_div.select_one('.ci-team-score:nth-child(2)')
            team2_name = team2_score = team2_over = "N/A"  # Default values

            if team2_element:
                team2_name = team2_element.select_one('.ds-capitalize').text.strip()
                team2_score_element = team2_element.select_one('.ds-text-compact-s strong')
                team2_over_element = team2_element.select_one('.ds-text-compact-xs')
                if team2_score_element:
                    team2_score = team2_score_element.text.strip()
                if team2_over_element:
                    team2_over = team2_over_element.text.strip()

            description = first_match_div.select_one('p.ds-text-tight-s').text.strip() #commentary
            tournament_info = first_match_div.select_one('.ds-truncate > span > div > a > span').text.strip()
            url = first_match_div.select_one('a.ds-no-tap-higlight')['href']

            return {
                'state' :"live",
                'tournament_info' : tournament_info,
                'team1_name' : team1_name,
                'team1_score': team1_score,
                'team1_over':team1_over,
                'team2_name' : team2_name,
                'team2_score' : team2_score,
                'team2_over':team2_over,
                'match_comment' : description,
                'url' : url
            }
            
        else:
            return None
        

def save_to_csv(data):
    data['timestamp'] = datetime.now().strftime('%H:%M:%S %d-%m-%Y') 
    with open('cricket_data.csv', mode='a', newline='') as file:
        fieldnames = data.keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(data)


def scraper():
    url = 'https://www.espncricinfo.com/live-cricket-score'
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    data = extract_data(html_content)
    save_to_csv(data)
    return data;