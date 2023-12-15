import json
import urllib.parse
import urllib.request

import api_keys

api_key = api_keys.PROXYCURL_KEY

# Returns a JSON-formatted dictionary
def get_linkedin_company_recruiters(linkedin_company_profile_url: str):
    base_url = "https://nubela.co/proxycurl/api/linkedin/company/employee/search/"

    params = {
        'linkedin_company_profile_url': linkedin_company_profile_url,
        'keyword_regex': 'recruiter',
        'page_size': 2,
        'country': 'us',
        'enrich_profiles': 'enrich',
        'resolve_numeric_id': False
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"

    headers = {
        'Authorization': f'Bearer {api_key}',
    }

    try:
        # Make the API request
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        data = json.load(response)

        return data
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")

# Returns the company's LinkedIn url as a string
def get_linkedin_company_url(company_name: str):
    base_url = "https://nubela.co/proxycurl/api/linkedin/company/resolve"

    params = {
        'company_name': company_name,
        'enrich_profile': 'skip'
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"

    headers = {
        'Authorization': f'Bearer {api_key}',
    }

    try:
        # Make the API request
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        data = json.load(response)

        return data['url']
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")

def get_credit_balance():
    base_url = "https://nubela.co/proxycurl/api/credit-balance"
    
    url = f"{base_url}?{urllib.parse.urlencode({})}"

    headers = {
        'Authorization': f'Bearer {api_key}',
    }

    try:
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        data = json.load(response)

        return data
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")

def print_credit_balance():
    credit_balance_dict = get_credit_balance()
    print(f"Credit Balance: {credit_balance_dict['credit_balance']}")

# For testing purposes
if __name__ == "__main__":
    # company_name = "Apple"
    # company_url = get_linkedin_company_url(company_name)
    # print(company_url)

    # if company_url:
    #     recruiters_data = get_linkedin_company_recruiters(company_url)
    #     recruiters = []
    #     print(recruiters_data)

        # for employee in recruiters_data.get("employees", []):
            # recruiter = {
            #     "name": employee.get("profile", {}).get("full_name"),
            #     "position_title": employee.get("profile", {}).get("occupation"),
            #     # "company": employee.get("company"),
            #     "profile_url": employee.get("profile_url"),
            # }
            # recruiters.append(recruiter)
    print_credit_balance()
