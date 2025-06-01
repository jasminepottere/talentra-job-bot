def run_bot(keywords, location, salary, remote_only):
    # TODO: Replace this mock with Selenium logic

    # Simulated response for now
    return [
        {
            "title": "Software Engineer",
            "company": "Meta",
            "location": location or "Remote",
            "salary": salary or "$120k+"
        },
        {
            "title": "UX Researcher",
            "company": "Amazon",
            "location": location or "Remote",
            "salary": salary or "$130k+"
        }
    ]
