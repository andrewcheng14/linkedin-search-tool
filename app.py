from flask import Flask, render_template, request
from proxycurl_api import get_linkedin_company_url, get_linkedin_company_recruiters

# # test data for testing employee parsing
# test_recruiters_data = {
#     "employees": [
#         {
#             "last_updated": "2023-10-26T11:34:30Z",
#             "profile": {
#                 "accomplishment_courses": [],
#                 "accomplishment_honors_awards": [],
#                 "accomplishment_organisations": [],
#                 "accomplishment_patents": [],
#                 "accomplishment_projects": [],
#                 "accomplishment_publications": [],
#                 "accomplishment_test_scores": [],
#                 "activities": [],
#                 "articles": [],
#                 "background_cover_image_url": None,
#                 "certifications": [],
#                 "city": "Seattle",
#                 "connections": None,
#                 "country": "US",
#                 "country_full_name": "United States of America",
#                 "education": [
#                     {
#                         "degree_name": None,
#                         "description": None,
#                         "ends_at": {
#                             "day": 31,
#                             "month": 12,
#                             "year": 1975
#                         },
#                         "field_of_study": None,
#                         "logo_url": "https://media-exp1.licdn.com/dms/image/C4E0BAQF5t62bcL0e9g/company-logo_400_400/0/1519855919126?e=1672876800\u0026v=beta\u0026t=9twXof1JlnNHfFprrDMi-C1Kp55HTT4ahINKHRflUHw",
#                         "school": "Harvard University",
#                         "school_linkedin_profile_url": None,
#                         "starts_at": {
#                             "day": 1,
#                             "month": 1,
#                             "year": 1973
#                         }
#                     },
#                     {
#                         "degree_name": None,
#                         "description": None,
#                         "ends_at": None,
#                         "field_of_study": None,
#                         "logo_url": "https://media-exp1.licdn.com/dms/image/C4D0BAQENlfOPKBEk3Q/company-logo_400_400/0/1519856497259?e=1672876800\u0026v=beta\u0026t=v7nJTPaJMfH7WOBjb22dyvNKxAgdPdVd8uLCUkMB1LQ",
#                         "school": "Lakeside School",
#                         "school_linkedin_profile_url": None,
#                         "starts_at": None
#                     }
#                 ],
#                 "experiences": [
#                     {
#                         "company": "Breakthrough Energy ",
#                         "company_linkedin_profile_url": "https://www.linkedin.com/company/breakthrough-energy/",
#                         "description": None,
#                         "ends_at": None,
#                         "location": None,
#                         "logo_url": "https://media-exp1.licdn.com/dms/image/C4D0BAQGwD9vNu044FA/company-logo_400_400/0/1601560874941?e=1672876800\u0026v=beta\u0026t=VKb6OAHEwlnazKYKm4fc9go-y4zkUv2BT6tosOdQ54Y",
#                         "starts_at": {
#                             "day": 1,
#                             "month": 1,
#                             "year": 2015
#                         },
#                         "title": "Founder"
#                     },
#                     {
#                         "company": "Bill \u0026 Melinda Gates Foundation",
#                         "company_linkedin_profile_url": "https://www.linkedin.com/company/bill-\u0026-melinda-gates-foundation/",
#                         "description": None,
#                         "ends_at": None,
#                         "location": None,
#                         "logo_url": "https://media-exp1.licdn.com/dms/image/C4E0BAQE7Na_mKQhIJg/company-logo_400_400/0/1633731810932?e=1672876800\u0026v=beta\u0026t=Mz_ntwD4meCMcgo1L3JqDxBQRabFLIesd0Yz2ciAXNs",
#                         "starts_at": {
#                             "day": 1,
#                             "month": 1,
#                             "year": 2000
#                         },
#                         "title": "Co-chair"
#                     }
#                 ],
#                 "first_name": "Bill",
#                 "full_name": "Bill Gates",
#                 "groups": [],
#                 "headline": "Co-chair, Bill \u0026 Melinda Gates Foundation",
#                 "languages": [],
#                 "last_name": "Gates",
#                 "occupation": "Co-chair at Bill \u0026 Melinda Gates Foundation",
#                 "people_also_viewed": [],
#                 "profile_pic_url": "https://media.licdn.com/dms/image/C5616AQH9tkBTUhHfng/profile-displaybackgroundimage-shrink_200_800/0/1614530499015?e=2147483647\u0026v=beta\u0026t=VEoCyedtZulnAVYWT9BXfKHi5OFp8avElNjiz8kjSTU",
#                 "public_identifier": "williamhgates",
#                 "recommendations": [],
#                 "similarly_named_profiles": [],
#                 "state": "Washington",
#                 "summary": "Co-chair of the Bill \u0026 Melinda Gates Foundation. Founder of Breakthrough Energy. Co-founder of Microsoft. Voracious reader. Avid traveler. Active blogger.",
#                 "volunteer_work": []
#             },
#             "profile_url": "https://www.linkedin.com/in/satyanadella"
#         }
#     ],
#     "next_page": ""
# }

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search_recruiters", methods=["POST"])
def search_recruiters():
    company_name = request.form.get("company")
    company_url = get_linkedin_company_url(company_name)

    # Get user inputs from the form
    target_role = request.form.get("target_role")
    university = request.form.get("university")
    major = request.form.get("major")

    # Create the message template based on user selections
    message_template = f"Hi [Recruiter Name], I study {major} at {university} and I'm a big fan of {company_name}. I'm interested in {target_role} roles at {company_name} and believe I would be a great fit given my background. If you have the time, I’d love to discuss how my experience matches the position."

    if company_url:
        recruiters_data = get_linkedin_company_recruiters(company_url)
        # recruiters_data = test_recruiters_data
        recruiters = []

        for employee in recruiters_data.get("employees", []):

            recruiter = {
                "name": employee.get("profile", {}).get("full_name"),
                "position_title": employee.get("profile", {}).get("occupation"),
                "profile_url": employee.get("profile_url"),
            }
            recruiters.append(recruiter)

        return render_template('results.html', recruiters=recruiters, message_template=message_template, target_role=target_role, university=university, company=company_name, major=major)
    else:
        return render_template("results.html", recruiters=[])

if __name__ == "__main__":
    app.run(debug=True)
