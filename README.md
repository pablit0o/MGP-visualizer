# MGP-visualization - A visualization of mathematical genealogy
## Context
I created this repository to simulate visualizations with academic (or doctoral) advisors instead of biological descendance. Part of this was inspired by the "Wikipedia game" whereby you try to find the fastest route from one Wikipedia page to another! One of the fields seen in many scientists is the "Academic Advisor" and "Doctoral Students" fields, where you can access a gigantic scientific pedigree of Advisor-Advisee relationships.

I've noted that there is quite the extensive lineage from any one mathematician to another. I remember Weierstrass in particular had dozens of doctoral advisees. Chances are, if you ever talk to a math professor, you likely talked to someone who talked to someone who...talked to Weierstrass. 

I initially wanted to use Wikidata for accessing this data, but I stumbled upon an even greater resource while researching. The Mathematics Genealogy Project [1] (hence the repo name) gives you a rich source of information for each of their documented mathematicians. Additionally, I also found a repo that did similar functionality to my goal [2], but I feel like they did not capitalize on the MGP dataset as they provided a rather static pedigree. 

As it turns out, most of the functionality is direct applications of graph theory—a must know for any competitive programmer. As such, I enjoyed making this project, and I hope you enjoy using it!

## Dependencies
...

## Usage
...

The IEEE-style references are denoted as [X], while footnotes are denoted [X*].

## Footnotes
[1*] The MGP API can obscurely be accessed through [1] and going over to the 'Contact Us' page. By selecting 'Request access to data for research purposes', you will be redirected to their API. The code can be found when creating an account and downloading
their sample python script.\n
[2*] The mgp_data.json has data queried from the MGP API on 22/06/2026. It contains xxx,xxx entries and took roughly [started at 4:20 am] ~X hours.\n

## References
[1] Mathematics Genealogy Project, "Mathematics Genealogy Project" [Online]. Available: https://www.genealogy.math.ndsu.nodak.edu/. [Accessed: Jun. 22, 2026].\n
[2] J. Kun, _math-genealogy-scraper_. Github. [Online]. Available https://github.com/j2kun/math-genealogy-scraper. [Accessed: Jun. 22, 2026].\n
