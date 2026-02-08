def search_linkedin(job, location, contract):
    return [
        {
            "source": "LinkedIn",
            "title": f"{job} - LinkedIn",
            "location": location,
            "contract": contract,
            "url": "https://linkedin.com"
        }
    ]

