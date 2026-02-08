def search_indeed(job, location, contract):
    return [
        {
            "source": "Indeed",
            "title": f"{job} - Indeed",
            "location": location,
            "contract": contract,
            "url": "https://indeed.com"
        }
    ]

