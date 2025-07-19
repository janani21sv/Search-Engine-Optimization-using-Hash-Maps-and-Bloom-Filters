import tkinter as tk
from bloom_filter import BloomFilter
from hashmap import HashMap
from trie_spellcheck import Trie


bloom_filter = BloomFilter(100000, 0.01)  

hash_map = HashMap()


grp = {
    "Computer": ["Computer", "Comp", "Compute", "Com", "Computers", "Computing", "Compuetr", "Compouter", "Comptuer", "Comupter", "Compurer", "Compter", "PC", "Workstation", "Laptop", "Desktop", "Server", "Hardware", "Software", "Network", "Programming"],
    "python": ["Python", "Py", "Pyth", "Pytho", "Pyt", "python", "Pythn", "py", "Ptyhon", "Pytohn", "Pyython", "Pthon", "Puthon", "Programming Language", "Scripting Language", "Data Analysis", "Machine Learning", "Web Development", "AI", "Data Visualization"],
    "Operating Systems": ["OS", "Operating Systems", "operating", "systems", "oprt", "Operating System", "Os", "operatin", "sytems", "Operting Systems", "Oprating Systems", "Operating Systemms", "Windows", "Linux", "macOS", "Unix", "Android", "iOS"],
    "web development": ["Web", "webdev", "wrb dev", "web dev", "web develop", "Web Development", "wb developmnt", "wep development", "wrb develoment", "wev developmnet", "web develpoment", "wbe developement", "HTML", "CSS", "JavaScript", "Front-end", "Back-end", "Full Stack", "UI/UX Design", "Responsive Design", "Mobile Development"],
    "data science": ["Data", "datasc", "dat", "data scence", "data sc", "Data Science", "dta science", "daat scince", "datta scieence", "data sciennce", "data sciense", "Machine Learning", "Data Analysis", "Data Mining", "Statistical Modeling", "Big Data", "AI", "Deep Learning", "Natural Language Processing", "Data Visualization", "Predictive Analytics"],
    "Computer Science Engineering": ["CSE", "Comp Sci Eng", "Computing Engineering", "Computer Engg", "CS Engineering", "Computer Science", "CSEng", "Comp Science Eng", "Computers and Engineering", "CS Engg", "Computer Sci Engg", "Computing Science Engineering", "Algorithms", "Data Structures", "Database Systems", "Network Security", "Artificial Intelligence", "Computer Architecture"],
    "Cricket": ["Cricket", "Crickit", "Crickett", "Crickete", "Crket", "Crcket", "Crkit", "Criket", "Batsman", "Batsmn", "Batsmen", "Bowler", "Bowller", "Bolewr", "Wicketkeeper", "Wicketkeper", "Wicket-keeper", "All-rounder", "All-rounder", "Allrrounder", "IPL", "Test Match", "Test Metch", "Test Matche", "ODI", "T20", "Run", "Runs", "Wicket", "Wickets", "Boundary", "Boundry", "Boundery", "Six", "Catch", "Ctch", "Cach", "Fielding", "Stumps"],
    "Anime": ["Anime", "Anme", "Anima", "Manga", "Mnga", "Mannga", "Cosplay", "Cospl", "Cospay", "Otaku", "Otak", "Otku", "Shonen", "Shounen", "Shounn", "Shonen", "Seinen", "Shonen Jump", "Mecha", "Slice of Life", "Isekai", "Shojo", "Josei", "Moe", "Fan Service"],
    "Series": ["Series", "Sereis", "Seris", "Tv Show", "TV Series", "Drama", "Comedy", "Action", "Adventure", "Science Fiction", "Fantasy", "Thriller", "Mystery", "Crime", "Romance", "Historical", "Period Drama", "Animation", "Cartoon", "Sitcom", "Reality Show", "Soap Opera", "Documentary"],
    "Career": ["Career", "Carrer", "Carreer", "Job", "Profession", "Employment", "Work", "Resume", "Interview", "Networking", "Job Search", "Job Application", "Career Development", "Career Growth", "Professional Skills", "Leadership", "Work-Life Balance", "Goal Setting", "Entrepreneurship", "Success", "Promotion", "Salary", "Workplace", "Teamwork"],
    "Education": ["Education", "Edcation", "Educatin", "Educaton", "School", "Schol", "Collge", "Unversity", "Corses", "Online Learning", "E-lerning", "Degree", "Study Abroad", "Studnt Life", "Exams", "Homework", "Resarch", "Study Tips", "Student Organizations", "Scholarships"],
    "Sports": ["Sports", "Sprots", "Spors", "Footbal", "Basketball", "Tenns", "Golf", "Cricket", "Basebal", "Hocky", "Volleyball", "Athletics", "Swiming", "Soccr", "Rugby", "Boxing", "Martial Arts", "Fitness"],
    "University": ["University", "Universty", "Collge", "Campus", "Admissions", "Courses", "Research", "Facity", "Studnt Life", "Alumni", "Graduation", "Scholarships", "Internships", "Student Organizations", "Career Services"],
    "Silicon Valley": ["Silicon Valley", "Silcon Valey", "Technology", "Innovation", "Startups", "Entreprenurship", "Tech Companies", "Software", "Hardware", "Venture Capital", "Networking", "Investment", "Incubators", "Artificial Intelligence", "Internet of Things"],
    "MAANG": ["MAANG", "MANG", "Microsoft", "Amazn", "Appl", "Netfli", "Gogle", "Sofware Enginer", "Product Manager", "Technical Interview", "Ladership Principles", "Career Growth", "Internship", "Full-time Job", "Coding Challnge"],
    "Software developer": ["Software Developer", "Software Developr", "Sofware Develoer", "Coding", "Programing", "Web Developmnt", "Mobile App Development", "Sofware Engineering", "Agile Methodology", "Version Control", "Debugging", "Code Review", "Sofware Testing"],
    "Artificial Intelligence": ["Artificial Intelligence", "Artifical Inteligence", "Machine Learning", "Machine Lerning", "Deep Learning", "Neural Networks", "Computer Vision", "Natural Langage Processing", "Robotics", "AI Research", "Data Mining", "Pattern Recognition"],
    "Cybersecurity": ["Cybersecurity", "Cyber Security", "Information Security", "Network Security", "Data Protection", "Hacking", "Ethical Hacking", "Penetration Testing", "Vulnerability Assessment", "Security Audit", "Firewalls", "Intrusion Detection System", "Encryption"],
    "Internet of Things": ["Internet of Things", "IOT", "Smart Home", "Connected Devices", "Sensors", "Cloud Computing", "Data Analytics", "Automation", "Smart Cities", "Industrial IoT", "Wearable Devices", "IoT Security", "IoT Applications"]
}



trie = Trie()
trie.buildtrie(grp)


def populate_index():
    keywords_urls = {
    "python": [
        "https://www.python.org/",
        "https://docs.python.org/",
        "https://www.learnpython.org/",
        "https://realpython.com/",
    ],
    "web development": [
        "https://developer.mozilla.org/en-US/docs/Learn",
        "https://www.w3schools.com/",
        "https://www.freecodecamp.org/",
        "https://www.udemy.com/topic/web-development/",
    ],
    "data science": [
        "https://www.kaggle.com/",
        "https://www.datacamp.com/",
        "https://towardsdatascience.com/",
        "https://www.analyticsvidhya.com/",
    ],
    "Operating Systems": [
        "https://www.os.com/",
        "https://www.osamrita.edu"
    ],
    "Computer": [
        "https://www.computerhope.com/",
        "https://www.computerworld.com/",
        "https://www.computer.org/"
    ],
    "Computer Science Engineering": [
        "https://www.acm.org/",
        "https://www.ieee.org/",
        "https://www.computer.org/"
    ],
    "Cricket": [
        "https://www.espncricinfo.com/",
        "https://www.icc-cricket.com/",
        "https://www.cricbuzz.com/"
    ],
    "Anime": [
        "https://www.crunchyroll.com/",
        "https://myanimelist.net/",
        "https://www.funimation.com/"
    ],
    "Series": [
        "https://www.imdb.com/",
        "https://www.netflix.com/",
        "https://www.amazon.com/Prime-Video/b/?node=2676882011"
    ],
    "Career": [
        "https://www.indeed.com/",
        "https://www.linkedin.com/jobs",
        "https://www.glassdoor.com/index.htm"
    ],
    "Education": [
        "https://www.edx.org/",
        "https://www.coursera.org/",
        "https://www.udemy.com/"
    ],
    "Sports": [
        "https://www.espn.com/",
        "https://www.sportingnews.com/",
        "https://www.olympics.com/"
    ],
    "Silicon Valley": [
        "https://siliconvalley.center/",
        "https://www.siliconvalley.com/",
        "https://www.svcdc.org/"
    ],
    "MAANG": [
        "https://www.maangtikka.com/",
        "https://www.maangtikka.in/",
        "https://www.maangtikkas.com/"
    ],
    "Software developer": [
        "https://stackoverflow.com/",
        "https://github.com/",
        "https://dev.to/"
    ],
    "Artificial Intelligence": [
        "https://ai.google/",
        "https://www.ibm.com/watson",
        "https://www.aaai.org/"
    ],
    "Internet of Things": [
        "https://www.iotforall.com/",
        "https://www.iot-inc.com/",
        "https://www.postscapes.com/"
    ],
    "Movies": [
        "https://www.imdb.com/",
        "https://www.rottentomatoes.com/",
        "https://www.netflix.com/",
        "https://www.amazon.com/Movies/b?node=2858905011"
    ],
    "Cybersecurity": [
        "https://www.cybrary.it/",
        "https://www.sans.org/",
        "https://www.securitymagazine.com/",
        "https://www.cisecurity.org/"
    ],
    "Embedded Systems": [
        "https://www.embedded.com/",
        "https://www.eetimes.com/",
        "https://www.renesas.com/us/en/",
        "https://www.embeddedrelated.com/"
    ],
    "Student Clubs": [
        "https://www.campusgroups.com/",
        "https://www.studentlife.org/",
        "https://www.nsls.org/",
        "https://www.leosclub.com/"
    ],
    "College": [
        "https://www.collegeboard.org/",
        "https://www.petersons.com/",
        "https://www.unigo.com/",
        "https://www.niche.com/colleges/"
    ],
    "University": [
        "https://www.timeshighereducation.com/world-university-rankings",
        "https://www.usnews.com/education/best-global-universities",
        "https://www.topuniversities.com/university-rankings/world-university-rankings/2022",
        "https://www.qs.com/world-university-rankings/"
    ],
    "Entrance Exams": [
        "https://www.ets.org/",
        "https://www.mba.com/",
        "https://www.act.org/",
        "https://www.collegeboard.org/"
    ],
    "GitHub": [
        "https://github.com/",
        "https://docs.github.com/",
        "https://github.blog/",
        "https://github.com/explore"
    ],
    "HackerRank": [
        "https://www.hackerrank.com/",
        "https://www.hackerrank.com/domains/tutorials/10-days-of-javascript",
        "https://www.hackerrank.com/domains/tutorials/10-days-of-statistics",
        "https://www.hackerrank.com/domains/tutorials/10-days-of-data-structures"
    ],
    "Google": [
        "https://www.google.com/",
        "https://careers.google.com/",
        "https://developers.google.com/"
    ],
    "Microsoft": [
        "https://www.microsoft.com/",
        "https://careers.microsoft.com/",
        "https://docs.microsoft.com/",
        "https://www.microsoft.com/en-us/education"
    ],
    "Competitive Programming": [
        "https://www.codechef.com/",
        "https://www.topcoder.com/",
        "https://codeforces.com/",
        "https://leetcode.com/"
    ]
}



    for keyword, urls in keywords_urls.items():
        bloom_filter.add(keyword)
        hash_map.set(keyword, urls)
        trie.insertele(keyword)
    return keywords_urls


def search_keyword():
    query = keyword_entry.get()

    if bloom_filter.exists(query):
        urls = hash_map.get(query)
        result_text.delete(1.0, tk.END)

        if urls:
            result_text.insert(tk.END, "Search Results:\n")
            for url in urls:
                result_text.insert(tk.END, f"- {url}\n")
        else:
            result_text.insert(tk.END, "No results found.")
    else:
        suggestion=trie.search_keyword(query, grp)
        suggestions=trie.spellchk(query)
        result_text.delete(1.0, tk.END)

        if suggestion:
            result_text.insert(tk.END, "Did you mean:")
            result_text.insert(tk.END, f"- {suggestion}\n")
            urls = hash_map.get(suggestion)
            if urls:
                result_text.insert(tk.END, "Search Results:\n")
                for url in urls:
                    result_text.insert(tk.END, f"- {url}\n")
            else:
                result_text.insert(tk.END, "No results found.")
        elif suggestions:
            valid_suggestions = []
            for suggestion in suggestions:
                if bloom_filter.exists(suggestion) and trie.search(suggestion):
                    valid_suggestions.append(suggestion)
            
            if len(valid_suggestions)!=len(keywords_urls):
                result_text.insert(tk.END, "Did you mean:\n")
                for suggestion in valid_suggestions:
                    result_text.insert(tk.END, f"- {suggestion}\n")
                    urls = hash_map.get(suggestion)
                    if urls:
                        result_text.insert(tk.END, "Search Results:\n")
                        for url in urls:
                            result_text.insert(tk.END, f"- {url}\n")
            else:
                result_text.insert(tk.END, "No valid suggestions found.")
        else:
            result_text.insert(tk.END, "Keyword not found in index.")


def add_keyword():
    keyword = add_entry.get()
    urls = url_entry.get().split(",")  

    if bloom_filter.exists(keyword):
        existing_urls = hash_map.get(keyword)
        updated_urls = existing_urls + urls
        hash_map.set(keyword, updated_urls)
    else:
        bloom_filter.add(keyword)
        hash_map.set(keyword, urls)

    add_entry.delete(0, tk.END)
    url_entry.delete(0, tk.END)
    status_text.config(text="Keyword added/updated successfully.")


root = tk.Tk()
root.title("SEO Tool")


keyword_label = tk.Label(root, text="Enter a keyword to search:")
keyword_label.pack()
keyword_entry = tk.Entry(root)
keyword_entry.pack()


search_button = tk.Button(root, text="Search", command=search_keyword)
search_button.pack()


result_text = tk.Text(root, height=10, width=50)
result_text.pack()


separator = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, padx=5, pady=5)


add_label = tk.Label(root, text="Add or update a keyword:")
add_label.pack()
add_entry = tk.Entry(root)
add_entry.pack()


url_label = tk.Label(root, text="Enter URL(s) (comma-separated if multiple):")
url_label.pack()
url_entry = tk.Entry(root)
url_entry.pack()


add_button = tk.Button(root, text="Add/Update Keyword", command=add_keyword)
add_button.pack()


status_text = tk.Label(root, text="")
status_text.pack()


keywords_urls=populate_index()

root.mainloop()


