#!/usr/bin/env python3

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "Templates" / "content"
BASE_TEMPLATE = ROOT / "Templates" / "layout" / "base.html"
TIMEZONE = ZoneInfo("America/New_York")

PAGES = {
    "index": {
        "output": ROOT / "index.html",
        "title": "Department of Economics | University of South Carolina",
        "description": "Department of Economics at the University of South Carolina: faculty, research, degree programs, seminars, and Ph.D. student information.",
        "nav": "home",
    },
    "faculty": {
        "output": ROOT / "faculty.html",
        "title": "Faculty | Department of Economics | University of South Carolina",
        "description": "Meet the faculty of the Department of Economics at the University of South Carolina and explore their research interests and recent work.",
        "nav": "faculty",
    },
    "research": {
        "output": ROOT / "research.html",
        "title": "Research | Department of Economics | University of South Carolina",
        "description": "Explore research, publications, and working papers from the Department of Economics at the University of South Carolina.",
        "nav": "research",
    },
    "events": {
        "output": ROOT / "events.html",
        "title": "Seminars and Events | Department of Economics | University of South Carolina",
        "description": "View seminars, events, and important department dates for the Department of Economics at the University of South Carolina.",
        "nav": "events",
    },
    "phd_students": {
        "output": ROOT / "phd_students.html",
        "title": "Ph.D. Students | Department of Economics | University of South Carolina",
        "description": "Directory of Ph.D. students in the Department of Economics at the University of South Carolina.",
        "nav": "phd_students",
    },
    "job_market_candidates": {
        "output": ROOT / "job_market_candidates.html",
        "title": "Job Market Candidates | Department of Economics | University of South Carolina",
        "description": "Meet the current job market candidates from the Department of Economics at the University of South Carolina.",
        "nav": "job_market_candidates",
    },
}


def nav_class(active: bool) -> str:
    return "open" if active else "closed"


def build_navigation(active_page: str) -> str:
    faculty_open = active_page in {"faculty", "research"}
    phd_open = active_page in {"phd_students", "job_market_candidates"}
    events_open = active_page == "events"

    faculty_items = """
      <ul class='no-bullet'>
      <li class=""><a class='level_2' href='faculty.html'>Faculty</a></li>
      <li class=""><a class='level_2' href='research.html'>Research</a></li>
     </ul>"""

    phd_items = """
      <ul class='no-bullet'>
      <li class=""><a class='level_2' href='phd_students.html'>Ph.D. Directory</a></li>
      <li class=""><a class='level_2' href='job_market_candidates.html'>Job Market Candidates</a></li>
      <li class=""><a class='level_2' href='https://sc.edu/study/colleges_schools/moore/study/economics/degree_programs/phd_in_economics/'>Ph.D. Program</a></li>
      </ul>"""

    undergraduate_items = """
      <ul class='no-bullet'>
      <li class=""><a class='level_2' href='https://sc.edu/study/colleges_schools/moore/study/economics/degree_programs/bachelors/index.php'>BBA Economics</a></li>
      <li class=""><a class='level_2' href='https://sc.edu/study/majors_and_degrees/economics.php'>BS and BA in Economics</a></li>
      </ul>"""

    return f"""<ul class="side-nav">
        <li class="closed"><a class='level_1' href='index.html'>Department of Economics</a></li>
        <li class="{nav_class(faculty_open)}"><a class='level_1' href='faculty.html'>Faculty &amp; Research</a>{faculty_items}
        </li>
        <li class="{nav_class(phd_open)}"><a class='level_1' href='phd_students.html'>Ph.D. Program</a>{phd_items}
        </li>
        <li class="closed"><a class='level_1' href='https://sc.edu/study/colleges_schools/moore/study/economics/degree_programs/master_of_arts_in_economics/'>Master’s Program</a></li>
        <li class="closed"><a class='level_1' href='https://sc.edu/study/colleges_schools/moore/study/economics/degree_programs/bachelors/index.php'>Undergraduate Program</a>{undergraduate_items}
        </li>
        <li class="{nav_class(events_open)}"><a class='level_1' href='events.html'>Seminars &amp; Events</a></li>
      </ul>"""


def build_mobile_nav(active_page: str) -> str:
    return f"""          <ul class="off-canvas-list">
            <li class="college closed">
              <a class="off-canvas-submenu-call" href="#">
                <img alt="The University of South Carolina - Darla Moore School of Business" onerror="this.onerror=null;this.src='https://sc.edu/study/colleges_schools/moore/index.php/_internal/images/images/USC_MooreSchool_logo_horizontal_RGB_G_rev.png'" src="Images/USC_MooreSchool_logo_horizontal_RGB_G_rev.png"/>
              </a>
              <ul class="no-bullet off-canvas-submenu">
                <li class="underline"><a href="https://sc.edu/study/colleges_schools/moore/index.php/">Darla Moore School of Business</a></li>
                <li><a href="http://www.sc.edu/">University of South Carolina</a></li>
                <hr/>
                <li class="underline"><a href="https://sc.edu/study/colleges_schools/moore/index.php/offices/departments/">Departments</a></li>
                <li class="underline"><a href="https://sc.edu/study/colleges_schools/moore/index.php/research/graduate-studies/prospective">Graduate Resources</a></li>
                <li class="underline"><a href="https://sc.edu/study/colleges_schools/moore/index.php/student-affairs/Prospective/">Undergraduate Resources</a></li>
                <li class="underline"><a href="https://sc.edu/study/colleges_schools/moore/index.php/courses/">Courses</a></li>
                <hr/>
                <li class="underline"><a href="https://sc.edu/study/colleges_schools/moore/index.php/office-of-the-dean/college-leadership.php">Dean's Office</a></li>
                <li class="underline"><a href="https://sc.edu/study/colleges_schools/moore/index.php/alumni-and-giving/">Alumni &amp; Giving</a></li>
                <li><a href="https://sc.edu/study/colleges_schools/moore/index.php/public-affairs/resources/faculty-by-department.php">Faculty by Department</a></li>
                <li>
                  <form action="//sc.edu/study/colleges_schools/moore/search/" id="search-small">
                    <input name="cx" type="hidden" value="002688418440466237416:ilehtu0wbts"/>
                    <input name="cof" type="hidden" value="FORID:10"/>
                    <input name="ie" type="hidden" value="UTF-8"/>
                    <label class="hidden-for-small-only" for="searchSmallOnlyInput">Search The Darla Moore School of Business</label>
                    <input id="searchSmallOnlyInput" name="q" placeholder="Search The Darla Moore School of Business..." type="search"/>
                  </form>
                </li>
              </ul>
            </li>
{build_navigation(active_page)}
            <ul class="side-nav">
              <li><label>Office</label></li>
              <li><a href="contact.html">Contact Us</a></li>
            </ul>
            <ul class="side-nav">
              <li><label>Address</label><span class="map-link"><a href="https://sc.edu/visit/map/?id=744#!m/223307" rel="noopener noreferrer" target="_blank"><i class="fa fa-map-marker">&#160;</i> Map</a></span></li>
              <li class="phone-address"><h6>Department of Economics</h6><p>The University of South Carolina<br/>Darla Moore School of Business<br/>1014 Greene Street<br/>Columbia, South Carolina 29208<br/></p></li>
            </ul>
            <ul class="side-nav">
              <li><label>Department of Economics Social Media</label></li>
              <li class="unit-social"><a data-gtm-event="nav-unit-twitter" href="https://twitter.com/UofSC_Econ" title="twitter"><i class="fa fa-twitter-square fa-2x">&#160;</i><span class="hide">Twitter</span></a></li>
            </ul>
          </ul>"""


def build_desktop_nav(active_page: str) -> str:
    return f"""  <div class="hide-for-small-only medium-3 medium-pull-9 columns content-unit-page-navigation">
      <hr class="show-for-small-only"/>
{build_navigation(active_page)}
      <ul class="side-nav">
        <li><label>Address</label><span class="map-link"><a href="https://sc.edu/visit/map/?id=744#!m/223307" rel="noopener noreferrer" target="_blank"><i class="fa fa-map-marker">&#160;</i> Map</a></span></li>
        <li class="phone-address"><h6>Department of Economics</h6><p>The University of South Carolina<br/>Darla Moore School of Business<br/>1014 Greene Street<br/>Columbia, South Carolina 29208<br/></p></li>
      </ul>
      <ul class="side-nav">
        <li><label>Department of Economics Social Media</label></li>
        <li class="unit-social"><a data-gtm-event="nav-unit-twitter" href="https://twitter.com/UofSC_Econ" title="twitter"><i class="fa fa-twitter-square fa-2x">&#160;</i><span class="hide">Twitter</span></a></li>
      </ul>
    </div>
  </div>"""


FOOTER = """<div class="row footer">
<div class="small-12 medium-5 large-4 columns">
<ul class="small-block-grid-1 logo-footer">
<li><a data-gtm-event="nav-college-footer-cla" href="https://sc.edu/study/colleges_schools/moore/index.php" title="Darla Moore School of Business"> <img alt="Darla Moore School of Business" height="45" src="Images/USC_MooreSchool_logo_horizontal_RGB_G_rev.png" width="280"/> </a></li>
</ul>
</div>
<div class="show-for-small-only small-12 columns social-media"><hr class="show-for-small-only"/>
<ul class="small-block-grid-1">
</ul>
</div>
<div class="show-for-small-only show small-12 columns social-media">
<ul class="small-block-grid-5">
<li><a data-gtm-event="nav-college-footer-twitter" href="https://twitter.com/MooreSchool" title="Moore School Twitter Feed"> <em class="fa fa-twitter-square fa-3x">&#160;</em> <span class="hidden-for-small-only">Twitter</span> </a></li>
</ul>
<hr class="show-for-small-only"/></div>
<div class="show-for-medium-up medium-7 large-8 columns">
<div class="row right">
<div class="small-5 small-centered medium-12 large-12 columns social-media"><a class="donate-button center right" data-gtm-event="nav-college-footer-giving" href="https://sc.edu/giving/" title="Make a Gift">Make a Gift</a> <br class="show-for-medium-only"/> <a data-gtm-event="nav-college-footer-twitter" href="https://twitter.com/MooreSchool" title="Moore School Twitter Account"> <em class="fa fa-twitter-square fa-2x">&#160;</em> <span class="hidden-for-medium-up">Twitter</span> </a></div>
</div>
</div>
</div>"""


def extract_content(page_name: str) -> str:
    page_text = PAGES[page_name]["output"].read_text()
    start = '<div class="row content-secondary-page">'
    end = '<div class="hide-for-small-only medium-3 medium-pull-9 columns content-unit-page-navigation">'
    if start not in page_text or end not in page_text:
        raise ValueError(f"Could not extract content from {PAGES[page_name]['output'].name}")
    return page_text.split(start, 1)[1].split(end, 1)[0]


def bootstrap_content() -> None:
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    for page_name in PAGES:
        fragment = extract_content(page_name).strip()
        content_path = CONTENT_DIR / f"{page_name}.html"
        content_path.write_text(f'<div class="row content-secondary-page">\n{fragment}\n')


def render_pages() -> None:
    template = BASE_TEMPLATE.read_text()
    build_timestamp = datetime.now(TIMEZONE).strftime("%a, %d %b %Y %H:%M:%S %z")

    for page_name, page in PAGES.items():
        content_path = CONTENT_DIR / f"{page_name}.html"
        if not content_path.exists():
            raise FileNotFoundError(f"Missing content fragment: {content_path}")

        html = template
        replacements = {
            "{{TITLE}}": page["title"],
            "{{DESCRIPTION}}": page["description"],
            "{{DATE}}": build_timestamp,
            "{{MOBILE_NAV}}": build_mobile_nav(page["nav"]),
            "{{CONTENT_MAIN}}": content_path.read_text().rstrip(),
            "{{DESKTOP_NAV}}": build_desktop_nav(page["nav"]),
            "{{FOOTER}}": FOOTER,
        }

        for placeholder, value in replacements.items():
            html = html.replace(placeholder, value)

        page["output"].write_text(html + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the Department of Economics site pages from shared templates.")
    parser.add_argument("--bootstrap", action="store_true", help="Extract page-specific content fragments from the current generated HTML files.")
    args = parser.parse_args()

    if args.bootstrap:
        bootstrap_content()

    render_pages()


if __name__ == "__main__":
    main()
