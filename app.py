from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nova University</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, Helvetica, sans-serif;
        }

        body {
            background: #f5f7fb;
            color: #172033;
        }

        nav {
            height: 76px;
            background: white;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 7%;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 3px 20px rgba(0,0,0,.06);
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 23px;
            font-weight: 800;
            color: #172b67;
        }

        .logo-icon {
            width: 43px;
            height: 43px;
            border-radius: 12px;
            background: linear-gradient(135deg, #3155d9, #7a5cff);
            color: white;
            display: grid;
            place-items: center;
            font-weight: bold;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 30px;
        }

        nav a {
            text-decoration: none;
            color: #555e70;
            font-weight: 600;
        }

        nav a:hover {
            color: #3155d9;
        }

        .apply {
            background: #3155d9;
            color: white !important;
            padding: 12px 21px;
            border-radius: 10px;
        }

        .hero {
            min-height: 590px;
            padding: 80px 7%;
            display: grid;
            grid-template-columns: 1.1fr .9fr;
            align-items: center;
            gap: 50px;
            background:
                radial-gradient(circle at 90% 20%, #dfe5ff 0, transparent 30%),
                linear-gradient(135deg, #f8faff, #eef2ff);
        }

        .tag {
            display: inline-block;
            background: #e2e8ff;
            color: #3155d9;
            padding: 9px 15px;
            border-radius: 50px;
            font-weight: bold;
            font-size: 13px;
            margin-bottom: 20px;
        }

        h1 {
            font-size: clamp(42px, 6vw, 72px);
            line-height: 1.03;
            color: #15245c;
            margin-bottom: 22px;
        }

        h1 span {
            color: #536ee8;
        }

        .hero p {
            color: #626c80;
            font-size: 18px;
            line-height: 1.7;
            max-width: 600px;
        }

        .buttons {
            display: flex;
            gap: 15px;
            margin-top: 30px;
        }

        .btn {
            padding: 15px 24px;
            border-radius: 11px;
            text-decoration: none;
            font-weight: bold;
            display: inline-block;
        }

        .primary {
            background: #3155d9;
            color: white;
            box-shadow: 0 10px 25px rgba(49,85,217,.25);
        }

        .secondary {
            background: white;
            color: #3155d9;
            border: 1px solid #dbe1ef;
        }

        .hero-card {
            background: white;
            border-radius: 28px;
            padding: 28px;
            box-shadow: 0 25px 60px rgba(35,50,100,.15);
        }

        .campus-img {
            height: 300px;
            border-radius: 20px;
            background:
                linear-gradient(rgba(20,35,90,.1), rgba(20,35,90,.2)),
                linear-gradient(135deg, #667eea, #764ba2);
            display: flex;
            align-items: end;
            padding: 25px;
            color: white;
        }

        .campus-img h3 {
            font-size: 25px;
        }

        .rating {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
        }

        .rating strong {
            font-size: 23px;
        }

        .rating small {
            color: #788194;
        }

        section {
            padding: 85px 7%;
        }

        .section-title {
            text-align: center;
            max-width: 650px;
            margin: auto;
            margin-bottom: 50px;
        }

        .section-title h2 {
            color: #182760;
            font-size: 38px;
            margin-bottom: 12px;
        }

        .section-title p {
            color: #70798a;
            line-height: 1.7;
        }

        .stats {
            background: #172b67;
            color: white;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 25px;
            text-align: center;
        }

        .stat h2 {
            font-size: 38px;
            margin-bottom: 7px;
        }

        .stat p {
            color: #bfc9ed;
        }

        .courses {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 25px;
        }

        .course {
            background: white;
            padding: 30px;
            border-radius: 18px;
            border: 1px solid #e9edf5;
            transition: .25s;
        }

        .course:hover {
            transform: translateY(-7px);
            box-shadow: 0 18px 40px rgba(30,45,90,.1);
        }

        .course-icon {
            width: 52px;
            height: 52px;
            border-radius: 14px;
            background: #e9edff;
            color: #3155d9;
            display: grid;
            place-items: center;
            font-size: 23px;
            margin-bottom: 20px;
        }

        .course h3 {
            margin-bottom: 10px;
            color: #1b2a62;
        }

        .course p {
            color: #70798a;
            line-height: 1.6;
            margin-bottom: 20px;
        }

        .course a {
            color: #3155d9;
            text-decoration: none;
            font-weight: bold;
        }

        .news {
            background: #f0f3fa;
        }

        .news-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 25px;
        }

        .news-card {
            background: white;
            border-radius: 18px;
            padding: 27px;
        }

        .date {
            color: #3155d9;
            font-size: 13px;
            font-weight: bold;
            margin-bottom: 14px;
        }

        .news-card h3 {
            color: #1c2b63;
            margin-bottom: 12px;
        }

        .news-card p {
            color: #70798a;
            line-height: 1.6;
        }

        .cta {
            margin: 70px 7%;
            padding: 60px;
            border-radius: 25px;
            color: white;
            background: linear-gradient(135deg, #3155d9, #684ee8);
            text-align: center;
        }

        .cta h2 {
            font-size: 38px;
            margin-bottom: 15px;
        }

        .cta p {
            color: #e2e6ff;
            margin-bottom: 25px;
        }

        .cta .btn {
            background: white;
            color: #3155d9;
        }

        footer {
            background: #111c42;
            color: white;
            padding: 50px 7%;
            display: grid;
            grid-template-columns: 2fr 1fr 1fr 1fr;
            gap: 35px;
        }

        footer h3 {
            margin-bottom: 15px;
        }

        footer p, footer a {
            color: #aeb9df;
            line-height: 1.8;
            text-decoration: none;
        }

        .mobile {
            display: none;
            font-size: 25px;
        }

        @media(max-width: 850px) {
            nav ul {
                display: none;
            }

            .mobile {
                display: block;
            }

            .hero {
                grid-template-columns: 1fr;
                padding-top: 50px;
            }

            .stats,
            .courses,
            .news-grid,
            footer {
                grid-template-columns: 1fr 1fr;
            }
        }

        @media(max-width: 550px) {
            .stats,
            .courses,
            .news-grid,
            footer {
                grid-template-columns: 1fr;
            }

            .hero-card {
                padding: 15px;
            }

            .campus-img {
                height: 230px;
            }

            .cta {
                margin: 40px 5%;
                padding: 40px 20px;
            }
        }
    </style>
</head>

<body>

<nav>
    <div class="logo">
        <div class="logo-icon">N</div>
        NOVA UNIVERSITY
    </div>

    <ul>
        <li><a href="#home">Home</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#courses">Courses</a></li>
        <li><a href="#news">News</a></li>
        <li><a href="#contact">Contact</a></li>
        <li><a href="#" class="apply">Apply Now</a></li>
    </ul>

    <div class="mobile">☰</div>
</nav>

<section class="hero" id="home">
    <div>
        <div class="tag">🎓 WORLD-CLASS EDUCATION</div>

        <h1>
            Shape Your<br>
            <span>Future Today.</span>
        </h1>

        <p>
            Discover a university where ambitious students,
            inspiring teachers, and innovative ideas come together
            to create a better tomorrow.
        </p>

        <div class="buttons">
            <a href="#courses" class="btn primary">Explore Programs →</a>
            <a href="#about" class="btn secondary">Discover Nova</a>
        </div>
    </div>

    <div class="hero-card">
        <div class="campus-img">
            <div>
                <h3>Our Beautiful Campus</h3>
                <p>Learn. Connect. Grow.</p>
            </div>
        </div>

        <div class="rating">
            <div>
                <strong>4.9/5</strong><br>
                <small>Student Rating</small>
            </div>

            <div>
                <strong>#12</strong><br>
                <small>Global Ranking</small>
            </div>
        </div>
    </div>
</section>

<section class="stats" id="about">
    <div class="stat">
        <h2>25K+</h2>
        <p>Students</p>
    </div>

    <div class="stat">
        <h2>180+</h2>
        <p>Programs</p>
    </div>

    <div class="stat">
        <h2>95%</h2>
        <p>Employment Rate</p>
    </div>

    <div class="stat">
        <h2>120+</h2>
        <p>Countries</p>
    </div>
</section>

<section id="courses">
    <div class="section-title">
        <h2>Explore Our Programs</h2>
        <p>
            Choose from industry-focused programs designed to
            prepare you for the careers of tomorrow.
        </p>
    </div>

    <div class="courses">

        <div class="course">
            <div class="course-icon">💻</div>
            <h3>Computer Science</h3>
            <p>
                Learn software engineering, artificial intelligence,
                cybersecurity and modern computing.
            </p>
            <a href="#">View Program →</a>
        </div>

        <div class="course">
            <div class="course-icon">📊</div>
            <h3>Business & Management</h3>
            <p>
                Develop leadership, entrepreneurship, finance and
                strategic business skills.
            </p>
            <a href="#">View Program →</a>
        </div>

        <div class="course">
            <div class="course-icon">🔬</div>
            <h3>Science & Research</h3>
            <p>
                Explore biology, chemistry, physics and cutting-edge
                scientific research.
            </p>
            <a href="#">View Program →</a>
        </div>

        <div class="course">
            <div class="course-icon">🎨</div>
            <h3>Arts & Design</h3>
            <p>
                Turn creativity into a career through design,
                media, architecture and visual arts.
            </p>
            <a href="#">View Program →</a>
        </div>

        <div class="course">
            <div class="course-icon">⚖️</div>
            <h3>Law & Policy</h3>
            <p>
                Build expertise in law, government, policy and
                international relations.
            </p>
            <a href="#">View Program →</a>
        </div>

        <div class="course">
            <div class="course-icon">🩺</div>
            <h3>Health Sciences</h3>
            <p>
                Prepare for meaningful careers in healthcare,
                medicine and health research.
            </p>
            <a href="#">View Program →</a>
        </div>

    </div>
</section>

<section class="news" id="news">
    <div class="section-title">
        <h2>University News</h2>
        <p>Stay updated with the latest events and achievements.</p>
    </div>

    <div class="news-grid">

        <div class="news-card">
            <div class="date">AUG 18, 2026</div>
            <h3>Admissions Are Now Open</h3>
            <p>
                Applications for the upcoming academic year are
                officially open.
            </p>
        </div>

        <div class="news-card">
            <div class="date">AUG 12, 2026</div>
            <h3>New Research Center</h3>
            <p>
                Nova University announces a new innovation and
                artificial intelligence research center.
            </p>
        </div>

        <div class="news-card">
            <div class="date">AUG 05, 2026</div>
            <h3>Global Student Conference</h3>
            <p>
                Students from more than 40 countries joined our
                annual international conference.
            </p>
        </div>

    </div>
</section>

<div class="cta">
    <h2>Ready to Start Your Journey?</h2>
    <p>Take the first step toward your future at Nova University.</p>
    <a href="#" class="btn">Apply to Nova University →</a>
</div>

<footer id="contact">
    <div>
        <h3>NOVA UNIVERSITY</h3>
        <p>
            Empowering students through knowledge,
            innovation and opportunity.
        </p>
    </div>

    <div>
        <h3>University</h3>
        <p><a href="#">About Us</a></p>
        <p><a href="#">Programs</a></p>
        <p><a href="#">Research</a></p>
    </div>

    <div>
        <h3>Students</h3>
        <p><a href="#">Admissions</a></p>
        <p><a href="#">Scholarships</a></p>
        <p><a href="#">Campus Life</a></p>
    </div>

    <div>
        <h3>Contact</h3>
        <p>📍 University Avenue</p>
        <p>📧 info@nova.edu</p>
        <p>☎ +91 98765 43210</p>
    </div>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)