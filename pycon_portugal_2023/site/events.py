W1 = "Workshop I"
W2 = "Workshop II"
A = "Auditorium"

events = [
    {
        "image": "",
        "day": 7,
        "start_time": "08:00",
        "duration": 60,
        "title": "Registration",
        "room": "",
        "speaker": "",
        "description": "",
    },
    {
        "image": "",
        "day": 7,
        "start_time": "09:00",
        "duration": 15,
        "title": "Welcoming Session",
        "room": A,
        "speaker": "",
        "description": "Welcoming Session",
    },
    {
        "image": "images/speakers/tom-forbes.png",
        "day": 7,
        "start_time": "09:15",
        "duration": 60,
        "title": "Optimising for joy",
        "room": A,
        "speaker": "Tom Forbes",
        "description": "The good feeling new developers get when they begin to"
        " program for the first time fades as we get more experience and"
        " learn more. Is it possible to recapture that feeling?",
    },
    {
        "image": "images/speakers/darya_petrashka.png",
        "day": 7,
        "start_time": "10:15",
        "duration": 35,
        "title": "Amazon CodeWhisperer, ChatGPT, and GitHub Copilot: "
        "Choosing the Best Python AI Code Assistant ",
        "room": A,
        "speaker": "Darya Petrashka",
        "description": "Discover the right helper for your Python coding needs."
        " Explore security, code readability, cut-off limitations,"
        " creativity, ability to generate tests, and troubleshooting "
        "capabilities. Find survey results for programmers.",
    },
    {
        "image": "",
        "day": 7,
        "start_time": "10:50",
        "duration": 30,
        "title": "Coffee break",
        "room": "",
        "speaker": "",
        "description": "",
    },
    {
        "image": "images/speakers/riccardo_magliocchetti.png",
        "day": 7,
        "start_time": "11:20",
        "duration": 35,
        "title": "A simples serverless data pipeline",
        "room": A,
        "speaker": "Riccardo Magliocchetti",
        "description": "Building and maintaining data pipelines when it’s not "
        "your full time job is a pain! So better keep things simple"
        " without the need to manage the system yourself. In this "
        "talk I’ll show a data pipeline architecture built leveraging"
        " some cloud offerings by AWS and Preset.",
    },
    {
        "image": "images/speakers/avneet_kaur.png",
        "day": 7,
        "start_time": "11:55",
        "duration": 35,
        "title": "Building Dainty Dashboards in Plotly Dash for health data science.",
        "room": A,
        "speaker": "Avneet Kaur",
        "description": "Data science projects are often characterized by "
        "visualizations which enhances the creative storytelling "
        "process and allow us to derive actionable insights from data.",
    },
    {
        "image": "images/speakers/duarte_pompeu.png",
        "day": 7,
        "start_time": "12:30",
        "duration": 35,
        "title": "Tools to setup great python projects",
        "room": A,
        "speaker": "Duarte Pompeu",
        "description": "In a professional python project, there are many steps"
        " one can take to improve its quality. In this talk, I "
        "will review some tools that have been useful to me",
    },
    {
        "image": "",
        "day": 7,
        "start_time": "13:05",
        "duration": 60,
        "title": "Lunch break",
        "room": "",
        "speaker": "",
        "description": "",
    },
    {
        "image": "images/speakers/joao_ferreira.png",
        "day": 7,
        "start_time": "14:05",
        "duration": 35,
        "title": "Legacy apps, deadlines and project pragmatism - Delivering"
        " thousands of messages every night in primary healthcare ",
        "room": A,
        "speaker": "João Ferreira",
        "description": "In my talk I will go over the story of how I set up"
        " the service that sends text message reminders to"
        " patients of the Portuguese primary care health"
        " system. I will explain the constraints of working"
        " with a distributed silo legacy application and other"
        " proprietary projects in a large company, and the"
        " impact of that and short deadlines on application"
        " design. Python shines through the project for its "
        "vast amazing libraries, ease of design and speed of iteration.",
    },
    {
        "image": "images/speakers/lucas.png",
        "day": 7,
        "start_time": "14:40",
        "duration": 35,
        "title": "Artificial Intelligence running on the Blockchain",
        "room": A,
        "speaker": "Lucas Roitman",
        "description": "New technology now allows machine learning models to"
        " be uploaded to the blockchain, enhancing decentralized"
        " applications' (dapps) functionality and competitiveness"
        " against centralized apps. In this talk, we will discuss"
        " how anyone can easily deploy a simple machine learning"
        " model to the blockchain.",
    },
    {
        "image": "images/speakers/rashmi_nagpal.png",
        "day": 7,
        "start_time": "15:15",
        "duration": 35,
        "title": " The Aesthetics of Unbiased Machine Learning Systems:"
        " Crafting Fairness in Practice",
        "room": A,
        "speaker": "Rashmi Nagpal",
        "description": "In Artificial Intelligence systems, a renaissance has"
        " unfolded in recent years, captivating the imagination"
        " of many! However, a startling statistic emerges amidst"
        " the enthusiasm: merely 13% of machine learning models"
        " are deployed into production!",
    },
    {
        "image": "",
        "day": 7,
        "start_time": "15:50",
        "duration": 30,
        "title": "Coffee Break",
        "room": "",
        "speaker": "",
        "description": "",
    },
    {
        "image": "images/speakers/quazi_nafiul_islam.png",
        "day": 7,
        "start_time": "16:20",
        "duration": 35,
        "title": "Weird Python: A few ways in which Python can misbehave",
        "room": A,
        "speaker": "Quazi Nafiul Islam",
        "description": "Python usually works the way we expect to, but "
        "sometimes it doesn't. This talk is about when"
        " to expect the unexpected.",
    },
    {
        "image": "images/speakers/jorge_miranda.png",
        "day": 7,
        "start_time": "16:55",
        "duration": 35,
        "title": "Tavern Crawler: a tool to enable fast and easy development"
        " of automated API tests",
        "room": A,
        "speaker": "Jorge Miranda",
        "description": "Tavern is an open source pytest plugin aimed to write"
        " automated integration tests for HTTP and MQTT APIs. "
        "Currently, there isn’t any UI support for it. This talk"
        " presents a Visual Studio Code extension that enables"
        " easy and fast writing of Tavern tests .",
    },
    {
        "image": "images/speakers/anastasiia_kostiv.png",
        "day": 7,
        "start_time": "17:30",
        "duration": 35,
        "title": "Revealing Perspectives: The Art of Data Insight Communication"
        " in the Data-Driven Projects",
        "room": A,
        "speaker": "Anastasiia Kostiv",
        "description": '"Unveiling Perspectives: The Art of Data Insight'
        ' Communication in the Data-Driven Projects" is an'
        " engaging presentation that emphasizes the criticality"
        " of effectively communicating findings and insights"
        " in the field of Data Science. Often overlooked, the"
        " final stage of a data-driven project involves"
        " presenting results to stakeholders. This talk sheds"
        " light on the importance of this stage and explores"
        " the art of presenting findings, storytelling, and"
        " employing interactive methods to convey complex"
        " information in an intuitive manner. By leveraging"
        " powerful Python tools such as PyShiny, FastAPI,"
        " Streamlit, Flask, and ReactPy, participants will"
        " gain insights into how to effectively utilize these "
        "tools to enhance their data analysis and ensure "
        "understandability and memorability. In addition,"
        " the session will touch upon color science principles"
        " and other intriguing elements. The speaker will "
        "showcase a real-life data-driven project and demonstrate"
        " their innovative solution for result communication,"
        " providing practical examples and valuable takeaways.",
    },
    {
        "image": "",
        "day": 7,
        "start_time": "18:05",
        "duration": 30,
        "title": "Lightning Talks",
        "room": A,
        "speaker": "",
        "description": "",
    },
    {
        "image": "",
        "day": 8,
        "start_time": "09:00",
        "duration": 15,
        "title": "Morning Announcements",
        "room": A,
        "speaker": "",
        "description": "",
    },
    {
        "image": "images/speakers/cristian_maureira_fredes.png",
        "day": 8,
        "start_time": "9:15",
        "duration": 35,
        "title": "CPython Survival Kit: basic C concepts to understand Python better",
        "room": A,
        "speaker": "Cristián Maureira-Fredes",
        "description": "The newest Python versions are including many changes "
        "that improve the performance and functionality, but "
        "what's going on under the hood? In this talk, you will "
        "learn the necessary topics to start discovering how "
        "CPython internals work, and how to create a new module"
        " based in C or C++.",
    },
    {
        "image": "images/speakers/claudia_mendes_silva.png",
        "day": 8,
        "start_time": "9:50",
        "duration": 60,
        "title": "Breaking Bias: PyWomen = 0 #ErrorAlert",
        "room": A,
        "speaker": "Cláudia Mendes",
        "description": "In this keynote we are going to talk about how unconscious"
        " bias can impact on business and real world IT "
        "products and learn the importance of understanding"
        " the inclusion of diverse teams.",
    },
    {
        "image": "",
        "day": 8,
        "start_time": "10:50",
        "duration": 30,
        "title": "Coffee Break",
        "room": "",
        "speaker": "",
        "description": "",
    },
    {
        "image": "",
        "day": 8,
        "start_time": "11:20",
        "duration": 35,
        "title": "Living and breathing backwards compatible changes",
        "room": A,
        "speaker": "Leandro Damascena, Henrique Graça",
        "description": "From the team behind AWS Lambda Powertools for Python,"
        " we will explore trade-offs in API design and UX when"
        " your project is used by thousands of customers in production.",
    },
    {
        "image": "images/speakers/efe_oge.png",
        "day": 8,
        "start_time": "11:55",
        "duration": 35,
        "title": "Practical Guide to Database Locks with Django",
        "room": A,
        "speaker": "Efe Öge",
        "description": "Race conditions? No problem! Dive into the world of "
        "database locks with Django and gain hands-on knowledge"
        " on how to eliminate race conditions, maintain order,"
        " and boost your application's performance.",
    },
    {
        "image": "images/speakers/francisco_lavrador_pires.png",
        "day": 8,
        "start_time": "12:30",
        "duration": 35,
        "title": "Python in Qiskit Enviroments for Quantum Computing",
        "room": A,
        "speaker": "Francisco Lavrador Pires",
        "description": "Python's presence in Qiskit environments for quantum"
        " computing is vital for several reasons. Its simplicity,"
        " extensive libraries, and integration with scientific"
        " computing tools make it an ideal language for expressing"
        " quantum algorithms and designing quantum circuits. "
        "Python's versatility allows researchers to combine quantum"
        " computing with machine learning techniques, opening "
        "new possibilities for advancements in the field. Furthermore,"
        " Python's emphasis on readability and the support of a"
        " vibrant community fosters collaboration and knowledge-sharing,"
        " propelling the growth and adoption of quantum computing.",
    },
    {
        "image": "",
        "day": 8,
        "start_time": "13:05",
        "duration": 60,
        "title": "Lunch Break",
        "room": "",
        "speaker": "",
        "description": "",
    },
    {
        "image": "images/speakers/luca_baggi.png",
        "day": 8,
        "start_time": "14:05",
        "duration": 35,
        "title": "I know Polars is fast, but my data pipelines are written in pandas!",
        "room": A,
        "speaker": "Luca Baggi",
        "description": "We all know it by now: Polars is blazingly fast™️."
        " Yet my pipelines are all written in pandas, and it "
        "will just take too much time to rewrite them in Polars..."
        " won't it? Turns out, it takes less than thirty minutes "
        "to tame this new arctic beast!",
    },
    {
        "image": "images/speakers/murilo_cunha.png",
        "day": 8,
        "start_time": "14:40",
        "duration": 35,
        "title": "Faster Python with friends",
        "room": A,
        "speaker": "Murilo Cunha",
        "description": "Python's flexible and intuitive syntax enables"
        " developers to quickly build applications. But on the"
        " other hand, it may be slow during runtime. Luckily, "
        "there are different ways we can speed up a Python program."
        " In this talk, we'll explore different alternatives to"
        " make Python programs faster.",
    },
    {
        "image": "images/speakers/rodrigo_girao_serrao.png",
        "day": 8,
        "start_time": "15:15",
        "duration": 35,
        "title": "Comprehending Comprehensions",
        "room": A,
        "speaker": "Rodrigo Girão Serrão",
        "description": "Discover the immense potential of Python's list "
        "comprehensions, dictionary comprehensions, set comprehensions,"
        " and generator expressions, as we present them as an idiom "
        "that focuses on data transformations. Using real-world "
        "examples, we'll demonstrate how these tools can streamline"
        " data manipulation and transformation tasks while"
        " enhancing code readability. We'll also provide insights "
        "on best practices and use cases to maximize their "
        "effectiveness. By the end of this talk, you will be equipped"
        " to confidently harness the full potential of comprehensions"
        " and generator expressions, empowering you to create more"
        " expressive and elegant Python code. Join us on this exciting"
        " journey and level up your Python programming!",
    },
    {
        "image": "",
        "day": 8,
        "start_time": "15:50",
        "duration": 30,
        "title": "Coffee Break",
        "room": "",
        "speaker": "",
        "description": "",
    },
    {
        "image": "images/speakers/lucas_pires.png",
        "day": 8,
        "start_time": "16:20",
        "duration": 35,
        "title": "Building advanced back-office interfaces using Django & HTMX",
        "room": A,
        "speaker": "Lucas Pires",
        "description": "Explore a pragmatic approach to enhancing Django's "
        "back-office interfaces. Delve into the practical"
        " integration of lightweight frameworks like HTMX and "
        "AlpineJS to introduce interactivity with minimal"
        " JavaScript. This talk focuses on custom generic"
        " class-based views, offering insights into CRUD"
        " operations, formsets, and advanced techniques for "
        "managing Django models. Join me for a comprehensive "
        "overview of these techniques, from read-only forms to "
        "patching HTMX into the Django Admin, as we redefine"
        " Django development practices.",
    },
    {
        "image": "images/speakers/tiago-silva.png",
        "day": 8,
        "start_time": "16:55",
        "duration": 35,
        "title": "Esmerald and Saffier - Complex Python made it easy with async",
        "room": A,
        "speaker": "Tiago Silva, Pedro Correia",
        "description": "Python in the context of data for python developers, "
        "non python engineers and businesses using Esmerald and"
        " Saffier with the power of async python.",
    },
    {
        "image": "images/speakers/filipe_lains.png",
        "day": 8,
        "start_time": "17:30",
        "duration": 35,
        "title": "Getting started with (modern) Python packaging",
        "room": A,
        "speaker": "Filipe Laíns",
        "description": "Let's make sense of modern Python packaging tooling.",
    },
    {
        "image": "",
        "day": 8,
        "start_time": "18:05",
        "duration": 30,
        "title": "Lightning Talks",
        "room": A,
        "speaker": "",
        "description": "",
    },
    {
        "image": "images/speakers/stefanie_molin.png",
        "day": 9,
        "start_time": "9:00",
        "duration": 120,
        "title": "Beyond the Basics: Data Visualization in Python",
        "room": W1,
        "speaker": "Stefanie Molin",
        "description": "The human brain excels at finding patterns in visual"
        " representations, which is why data visualizations "
        "are essential to any analysis. Done right, they bridge"
        " the gap between those analyzing the data and those"
        " consuming the analysis. However, learning to create"
        " impactful, aesthetically-pleasing visualizations can "
        "often be challenging. This session will equip you with "
        "the skills to make customized visualizations using Python.",
    },
    {
        "image": "images/speakers/maxim-danilov.png",
        "day": 9,
        "start_time": "9:00",
        "duration": 120,
        "title": "Django and ReportLab: create PDF Like A Boss",
        "room": W2,
        "speaker": "Maxim Danilov",
        "description": "PDF document guarantees 100% delivery of content to "
        "the customers as planned. The workshop shows how to "
        "use the REPORTLab library to create PDF generator, "
        "based on Django Models and Templates to allow complex"
        " document layout for auto-generated catalogs or "
        "reports in PDF format.",
    },
    {
        "image": "",
        "day": 9,
        "start_time": "11:00",
        "duration": 30,
        "title": "Coffee Break",
        "room": "",
        "speaker": "",
        "description": "",
    },
    {
        "image": "images/speakers/olaniyan_adewale_hafeez.png",
        "day": 9,
        "start_time": "11:30",
        "duration": 120,
        "title": "MicroPython and time series analysis: Forecasting and trend analysis",
        "room": W1,
        "speaker": "Olaniyan Adewale, Sulaiman Adisa Adigun",
        "description": 'The workshop on "MicroPython and time series analysis:'
        ' Forecasting and trend analysis" is designed to help'
        " attendees learn how to perform time series analysis,"
        " forecasting, and trend analysis using MicroPython."
        " This workshop is ideal for anyone interested in learning"
        " how to analyze data collected over time, and how to "
        "use MicroPython to implement these analyses on "
        "microcontrollers.",
    },
    {
        "image": "images/speakers/shahriyar_rzayev.png",
        "day": 9,
        "start_time": "11:30",
        "duration": 120,
        "title": "Learn Flask the hard way: Introduce Architecture Patterns",
        "room": W2,
        "speaker": "Shahriyar Rzayev",
        "description": "Level up your Flask skills in this workshop!"
        " Learn Flask the hard way by diving into"
        " architectural patterns. Discover how to build"
        " scalable and maintainable applications using "
        "Repository, Unit of Work, and Use Cases. Don't "
        "miss this opportunity to become a Flask pro!",
    },
    {
        "image": "",
        "day": 9,
        "start_time": "13:30",
        "duration": 30,
        "title": "Lunch Break",
        "room": "",
        "speaker": "",
        "description": "",
    },
    {
        "image": "images/speakers/goncalo_marques.png",
        "day": 9,
        "start_time": "14:30",
        "duration": 120,
        "title": "From WebSites to Datasets: Unleashing the Power "
        "of Data Harvesting with Python",
        "room": W1,
        "speaker": "Gonçalo Marques",
        "description": "Learn how to develop multiparadigm web scrapers "
        "and crawlers leveraging an async model. Discover"
        " how to extract valuable information from websites"
        " using Python's environment and powerful tools. Master"
        " the art of collecting data at scale. Join this "
        "exhilarating journey of web exploration.",
    },
    {
        "image": "images/speakers/jayesh_kothari.png",
        "day": 9,
        "start_time": "14:30",
        "duration": 120,
        "title": "Data Storytelling using Python",
        "room": W2,
        "speaker": "Jayesh Kothari",
        "description": "In this captivating workshop, participants will embark"
        " on an exciting journey to explore the art of data "
        "storytelling with the power of Python. Led by Jayesh"
        " Kothari, a Python enthusiast and data storytelling"
        " expert, this session promises to be both informative"
        " and engaging.",
    },
    {
        "image": "",
        "day": 9,
        "start_time": "16:30",
        "duration": 30,
        "title": "Coffee Break",
        "room": "",
        "speaker": "",
        "description": "",
    },
    {
        "image": "images/speakers/felix-mino.png",
        "day": 9,
        "start_time": "17:00",
        "duration": 120,
        "title": "Boosting up your tests: property-based testing workshop",
        "room": W1,
        "speaker": "Felix Mino",
        "description": "Have you introduced bugs to your project when "
        "refactoring or making a “small” change to your "
        "code? Do you want to make your code base bulletproof?"
        " Learn how and when to write property-based tests,"
        " with little effort but significant benefits",
    },
    {
        "image": "images/speakers/rodrigo_girao_serrao.png",
        "day": 9,
        "start_time": "17:00",
        "duration": 120,
        "title": "Mastering comprehensions",
        "room": W2,
        "speaker": "Rodrigo Girão Sirrão",
        "description": "Practice how to write elegant comprehensions"
        " to make your code more idiomatic and easier to"
        " follow. With dozens of exercises, this tutorial"
        " will be perfect for you to finally get to grips "
        "with: list comprehensions, dictionary comprehensions,"
        " set comprehensions, generator expressions. Among other"
        " things, you will learn to identify situations where you"
        " should be using these powerful and elegant Python "
        "constructs. You will also learn how to use them to "
        "level up your Python skills. By the end of the tutorial,"
        " you will learn all of the ins and outs of comprehensions,"
        " their use cases, best practices and things to avoid, "
        "and some advanced usage patterns as well!",
    },
]
