
def search_pole_emploi(job, location, contract):
    return [
        {
            "source": "France Travail",
            "title": f"{job} - France Travail",
            "location": location,
            "contract": contract,
            "url": "https://francetravail.fr.fr"
        }
    ]
CLIENT_ID = "PAR_itjobfinder2026_9e348be54947551c54dcb05b0c802b95848270cb80f662d9f6cd4226927b8dbd"
CLIENT_SECRET = "74ab1b5fa26760ab13042b7eff027bb21e4b55fd18f93e832f461de69743c88a"
