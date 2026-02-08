
def search_pole_emploi(job, location, contract):
    return [
        {
            "source": "Pôle Emploi",
            "title": f"{job} - Pôle Emploi",
            "location": location,
            "contract": contract,
            "url": "https://pole-emploi.fr"
        }
    ]
