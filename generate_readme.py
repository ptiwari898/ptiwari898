import requests
import os
from datetime import datetime
from urllib.parse import quote

USERNAME = "ptiwari898"
GITHUB_TOKEN = os.environ.get("GH_TOKEN", "")

headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

def get_repos():
    url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&sort=updated"
    response = requests.get(url, headers=headers)
    repos = response.json()
    # Filter out forked repos, private repos, and the profile repo itself
    return [
        r for r in repos
        if not r.get("fork") and not r.get("private") and r["name"] != USERNAME
    ]

def lang_badge_color(lang):
    colors = {
        "JavaScript": "F7DF1E",
        "TypeScript": "3178C6",
        "Python": "3776AB",
        "HTML": "E34F26",
        "CSS": "1572B6",
        "Java": "ED8B00",
        "C++": "00599C",
        "C": "A8B9CC",
        "Dart": "0175C2",
        "Shell": "89E051",
        "Makefile": "427819",
        "ASL": "6E4C13",
    }
    return colors.get(lang, "57cc99")

def build_repo_table(repos):
    if not repos:
        return "_No public repositories yet._\n"

    rows = []
    for repo in repos:
        name = repo["name"]
        url = repo["html_url"]
        desc = repo.get("description") or "No description"
        lang = repo.get("language") or "—"
        stars = repo.get("stargazers_count", 0)
        updated = repo.get("updated_at", "")[:10]

        if lang != "—":
            color = lang_badge_color(lang)
            lang_badge = f"![](https://img.shields.io/badge/{quote(lang, safe='')}-{color}?style=flat-square&logoColor=white)"
        else:
            lang_badge = "—"

        star_badge = f"![](https://img.shields.io/badge/%E2%AD%90-{stars}-FFD700?style=flat-square)"
        rows.append(f"| [**{name}**]({url}) | {desc[:55]}{'...' if len(desc) > 55 else ''} | {lang_badge} | {star_badge} | `{updated}` |")

    header = "| 📦 Repository | 📜 Description | 🗣️ Language | ⭐ Stars | 🕐 Updated |\n"
    header += "|:---|:---|:---:|:---:|:---:|\n"
    return header + "\n".join(rows)

def generate_readme(repos):
    repo_table = build_repo_table(repos)
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    total = len(repos)

    readme = f"""<div align="center">

<!-- ══════════════════════════════════════════════════ -->
<!--          MINECRAFT ANIMATED HEADER                -->
<!-- ══════════════════════════════════════════════════ -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=venom&color=0:1a472a,50:2d6a4f,100:40916c&height=200&text=Pawan%20Tiwari&fontSize=65&fontColor=ffffff&animation=fadeIn&fontAlignY=50&desc=%E2%9B%8F%20ASSISTANT%20PROF%20%7C%20DEV%20%7C%20AI%20EXPLORER%20%E2%9B%8F&descAlignY=72&descSize=18&descColor=95d5b2"/>
  <source media="(prefers-color-scheme: light)" srcset="https://capsule-render.vercel.app/api?type=venom&color=0:6a994e,50:a7c957,100:d4e09b&height=200&text=Pawan%20Tiwari&fontSize=65&fontColor=1b4332&animation=fadeIn&fontAlignY=50&desc=%E2%9B%8F%20ASSISTANT%20PROF%20%7C%20DEV%20%7C%20AI%20EXPLORER%20%E2%9B%8F&descAlignY=72&descSize=18&descColor=2d6a4f"/>
  <img width="100%" src="https://capsule-render.vercel.app/api?type=venom&color=0:1a472a,50:2d6a4f,100:40916c&height=200&text=Pawan%20Tiwari&fontSize=65&fontColor=ffffff&animation=fadeIn&fontAlignY=50&desc=%E2%9B%8F%20ASSISTANT%20PROF%20%7C%20DEV%20%7C%20AI%20EXPLORER%20%E2%9B%8F&descAlignY=72&descSize=18&descColor=95d5b2" alt="Header"/>
</picture>

<br/>

<!-- ══ MINECRAFT PIXEL TYPING ANIMATION ══ -->
<img src="https://readme-typing-svg.demolab.com?font=Press+Start+2P&size=14&pause=1000&color=55FF55&center=true&vCenter=true&width=700&height=70&lines=%F0%9F%8E%AE+Welcome+Player+ptiwari898!;%F0%9F%8F%AB+Asst+Prof+%40+SIRT+Bhopal;%F0%9F%92%BB+Full+Stack+Dev+%26+AI+Explorer;%F0%9F%93%9A+RGPV+Open+Lab+Manuals+Author;%E2%8C%A8%EF%B8%8F+Custom+Keyboards+%26+On-Device+AI;%E2%98%95+Coffee+%E2%86%92+Code+%E2%86%92+Repeat!" alt="Typing SVG" />

<br/><br/>

[![Profile Views](https://komarev.com/ghpvc/?username=ptiwari898&color=57cc99&style=for-the-badge&label=PROFILE+VIEWS)](https://github.com/ptiwari898)
[![Followers](https://img.shields.io/github/followers/ptiwari898?style=for-the-badge&color=80ed99&labelColor=22333b&label=FOLLOWERS)](https://github.com/ptiwari898?tab=followers)

</div>

---

<div align="center">
  <img src="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg" alt="Snake animation" width="100%"/>
</div>

---

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Press+Start+2P&size=12&pause=9999&color=FFD700&center=true&vCenter=true&width=400&height=40&lines=%F0%9F%93%A6+PLAYER+STATS" alt="section" />
</div>

```
╔════════════════════════════════════════════════════════╗
║  🎮  PLAYER : ptiwari898                              ║
║  📛  NAME   : Pawan Tiwari                            ║
║  🏫  ROLE   : Assistant Professor @ SIRT Bhopal       ║
║  🎓  EDU    : M.Tech in CSE                           ║
║  📍  LOC    : Bhopal, India 🇮🇳                         ║
╠════════════════════════════════════════════════════════╣
║  ⚗️  CRAFTING (Currently Learning)                     ║
║  ├─ 🔭  3D Portfolio & React Projects                 ║
║  ├─ 🌱  Flutter · AI/ML · Full Stack                  ║
║  └─ 👯  Open to Collaborate!                          ║
╠════════════════════════════════════════════════════════╣
║  ⚡  FUN : I turn coffee into code ☕                   ║
╚════════════════════════════════════════════════════════╝
```

---

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Press+Start+2P&size=12&pause=9999&color=FFD700&center=true&vCenter=true&width=500&height=40&lines=%F0%9F%8F%86+ACHIEVEMENTS+UNLOCKED" alt="section" />
</div>

<div align="center">

| 🎖️ Role | 🏰 Organization | ⏳ Duration |
|:---:|:---:|:---:|
| 🏫 Assistant Professor | **SIRT Bhopal** | `2023 → NOW` |
| 🌐 Front-End Developer | **Freelance** | `2021 → 2023` |
| 🎬 Motion Graphic Designer | **Praadis Technologies** | `2019 → 2020` |

</div>

---

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Press+Start+2P&size=12&pause=9999&color=FFD700&center=true&vCenter=true&width=450&height=40&lines=%E2%9A%92%EF%B8%8F+CRAFTING+TABLE" alt="section" />
</div>

<div align="center">

**🗣️ Languages**

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

**🛠️ Frameworks & Tools**

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Express](https://img.shields.io/badge/Express.js-404D59?style=for-the-badge&logo=express&logoColor=61DAFB)
![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![WordPress](https://img.shields.io/badge/WordPress-117AC9?style=for-the-badge&logo=wordpress&logoColor=white)
![NPM](https://img.shields.io/badge/NPM-CB3837?style=for-the-badge&logo=npm&logoColor=white)

**🎨 Design & AI**

![Figma](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)
![Adobe XD](https://img.shields.io/badge/Adobe%20XD-470137?style=for-the-badge&logo=adobexd&logoColor=FF61F6)
![After Effects](https://img.shields.io/badge/After%20Effects-9999FF?style=for-the-badge&logo=adobeaftereffects&logoColor=white)
![Canva](https://img.shields.io/badge/Canva-00C4CC?style=for-the-badge&logo=canva&logoColor=white)
![NVIDIA CUDA](https://img.shields.io/badge/CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white)

</div>

---

<!-- ══════════════════════════════════════════════════ -->
<!--   AUTO-UPDATED REPOS — regenerated by GitHub Actions  -->
<!-- ══════════════════════════════════════════════════ -->

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Press+Start+2P&size=12&pause=9999&color=FFD700&center=true&vCenter=true&width=500&height=40&lines=%F0%9F%97%82%EF%B8%8F+MY+REPOSITORIES+({total}+total)" alt="section" />
</div>

> 🤖 _Auto-updated by GitHub Actions · Last sync: **{now}**_

{repo_table}

---

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Press+Start+2P&size=12&pause=9999&color=FFD700&center=true&vCenter=true&width=400&height=40&lines=%F0%9F%93%8A+SCOREBOARD" alt="section" />
</div>

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=ptiwari898&show_icons=true&theme=chartreuse-dark&hide_border=true&bg_color=0d1117&title_color=57cc99&icon_color=80ed99&text_color=c7f9cc" height="175"/>
&nbsp;
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=ptiwari898&layout=compact&theme=chartreuse-dark&hide_border=true&bg_color=0d1117&title_color=57cc99&text_color=c7f9cc" height="175"/>

</div>

<div align="center">

<img src="https://nirzak-streak-stats.vercel.app/?user=ptiwari898&theme=chartreuse-dark&hide_border=true&background=0d1117&ring=57cc99&fire=80ed99&currStreakLabel=c7f9cc&sideLabels=c7f9cc&dates=888888" width="55%"/>

</div>

<div align="center">
<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=ptiwari898&theme=github_dark" width="98%"/>
</div>

---

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Press+Start+2P&size=12&pause=9999&color=FFD700&center=true&vCenter=true&width=400&height=40&lines=%F0%9F%8F%86+TROPHY+ROOM" alt="section" />
</div>

<div align="center">
<img src="https://github-profile-trophy.vercel.app/?username=ptiwari898&theme=matrix&no-frame=true&no-bg=true&margin-w=8&column=6"/>
</div>

---

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=0:1a472a,50:2d6a4f,100:40916c&height=130&section=footer&text=%E2%9B%8F%20Still%20Crafting...%20%F0%9F%8C%B1&fontSize=22&fontColor=95d5b2&animation=fadeIn&fontAlignY=65"/>
  <source media="(prefers-color-scheme: light)" srcset="https://capsule-render.vercel.app/api?type=waving&color=0:6a994e,50:a7c957,100:d4e09b&height=130&section=footer&text=%E2%9B%8F%20Still%20Crafting...%20%F0%9F%8C%B1&fontSize=22&fontColor=1b4332&animation=fadeIn&fontAlignY=65"/>
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:1a472a,50:2d6a4f,100:40916c&height=130&section=footer&text=%E2%9B%8F%20Still%20Crafting...%20%F0%9F%8C%B1&fontSize=22&fontColor=95d5b2&animation=fadeIn&fontAlignY=65" alt="Footer"/>
</picture>

**⭐ Star my repos if you find them useful! ⭐**

</div>
"""
    return readme

if __name__ == "__main__":
    print("🔍 Fetching repositories...")
    repos = get_repos()
    print(f"✅ Found {len(repos)} repositories")
    readme = generate_readme(repos)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)
    print("✅ README.md generated successfully!")
