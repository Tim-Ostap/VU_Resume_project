def collect_personal_info():
    user_name = input("Full name: ")
    user_email = input("Email: ")
    user_phone = input("Phone: ")
    user_linkedin = input("LinkedIn: ")
    user_github = input("GitHub: ")

    return user_name, user_email, user_phone, user_linkedin, user_github

def collect_work_experience():
    experiences = []
    add_another_job = True

    while add_another_job:
        add_another_role = True
        roles = []
        
        company = input("Company name: ")
        job_title = input("Job title: ")
        start_date = input("Start date: ")
        end_date = input("End date: ")
        
        while add_another_role:
            roles.append(input("What did you do in this role? (one role at a time): "))

            choice = input("Add another role? (y/n): ")
            if choice == "y" or choice == "Y":
                pass
            elif choice == "n" or choice == "N":
                add_another_role = False
            choice = ""

        experiences.append({
            "company": company,
            "job_title": job_title,
            "start_date": start_date,
            "end_date": end_date,
            "roles": roles

        })

        choice = input("Add another job? (y/n): ")
        if choice == "y" or choice == "Y":
            pass
        elif choice == "n" or choice == "N":
            add_another_job = False
        choice = ""

    return experiences