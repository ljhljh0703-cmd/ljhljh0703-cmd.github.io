# 직무 주소(/platform/ /ai/ /fde/ /game/ /agent/)와 전체 목록(/all/), 첫 페이지의 역량 지도를 curation.json 하나로 만든다.
"""
사용: cd 저장소 && python3 tools/build_views.py && python3 tools/check.py
맞춤 이력서·지원 메일에는 직무 주소 하나만 붙인다. 지원처마다 페이지를 새로 만들지 않는다.
"""
import json, pathlib, html, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
D = json.loads((ROOT / "curation.json").read_text(encoding="utf-8"))
P, ITEMS, VIEWS, AXES = D["person"], D["items"], D["views"], D["axes"]
e = html.escape

FONTS = """<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/wanted-sans@1.0.3/fonts/webfonts/variable/split/WantedSansVariable.css">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap">
<link rel="stylesheet" href="../assets/view.css">"""


def link(u):
    if not u: return None
    return u if u.startswith("http") else "../" + u


def nav(current):
    tabs = [(k, v["title"]) for k, v in VIEWS.items()] + [("all", "전체 목록")]
    a = []
    for k, t in tabs:
        cur = ' aria-current="page"' if k == current else ""
        a.append(f'<a href="../{k}/"{cur}>{e(t)}</a>')
    return f'<nav class="v-nav" aria-label="직무별 보기"><a href="../">작품 모음 처음</a>{"".join(a)}</nav>'


def head(title, desc, path):
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="https://ljhljh0703-cmd.github.io/{path}/">
<meta property="og:image" content="https://ljhljh0703-cmd.github.io/assets/og.jpg">
{FONTS}
</head>"""


def person_block(lead):
    return f"""<header class="v-head">
  <p class="v-name">{e(P['name'])}</p>
  <h1>{e(P['line'])}</h1>
  <p class="v-lead">{e(lead)}</p>
  <p class="v-contact"><a href="mailto:{e(P['email'])}">{e(P['email'])}</a><a href="{e(P['github'])}">GitHub</a></p>
</header>"""


def item_block(key, n):
    it = ITEMS[key]
    links = []
    if it.get("url"): links.append(f'<a class="go" href="{e(link(it["url"]))}">사례 보기</a>')
    if it.get("play"): links.append(f'<a href="{e(it["play"])}">바로 플레이</a>')
    if it.get("repo"): links.append(f'<a href="{e(it["repo"])}">코드</a>')
    second = ("AI가 짠 것", it["ai"]) if it.get("ai") else ("팀원이 맡은 것", it["team"]) if it.get("team") else None
    return f"""<article class="v-item" id="{e(key)}">
  <div class="v-body">
    <h2>{e(it['name'])}</h2>
    <p class="v-kind">{e(it['kind'])}<span>{e(it['stage'])}</span></p>
    <p class="v-problem">{e(it['problem'])}</p>
    <p class="v-result">{e(it['result'])}</p>
    <dl class="v-who">
      <div><dt>내가 정한 것</dt><dd>{e(it['decided'])}</dd></div>
{f'      <div><dt>{second[0]}</dt><dd>{e(second[1])}</dd></div>{chr(10)}' if second else ''}      <div><dt>내가 확인한 것</dt><dd>{e(it['checked'])}</dd></div>
    </dl>
    <p class="v-links">{''.join(links)}</p>
  </div>
</article>"""


def view_page(key, v):
    items = "\n".join(item_block(k, i + 1) for i, k in enumerate(v["items"]))
    desc = f"{P['name']} · {v['title']} 지원용 대표 작업 {len(v['items'])}개"
    return f"""{head(f"{P['name']} · {v['title']}", desc, key)}
<body class="v" data-view="{key}">
{nav(key)}
<main class="v-sheet">
{person_block(v['lead'])}
<p class="v-intro">{e(P['intro'])}</p>
<section class="v-list" aria-label="대표 작업">
{items}
</section>
<p class="v-more">다른 작업은 <a href="../all/">전체 목록</a>에 시기 순으로 있습니다.</p>
</main>
</body>
</html>
"""


def all_page():
    rows = []
    for r in D["all"]:
        name = f'<a href="{e(link(r["url"]))}">{e(r["name"])}</a>' if r.get("url") else e(r["name"])
        rows.append(f"<tr><td>{e(r['when'])}</td><th scope=\"row\">{name}</th><td>{e(r['kind'])}</td><td>{e(r['role'])}</td><td>{e(r['stage'])}</td></tr>")
    desc = f"{P['name']}의 작업 {len(D['all'])}개 전체 목록"
    return f"""{head(f"{P['name']} · 전체 목록", desc, "all")}
<body class="v" data-view="all">
{nav("all")}
<main class="v-sheet wide">
{person_block("지금까지 한 작업을 최근 것부터 모두 적었습니다. 직무별 대표 작업은 위 주소에서 먼저 보실 수 있습니다.")}
<div class="v-table-wrap">
<table class="v-table">
<caption>작업 {len(D['all'])}개 · 최근 순</caption>
<thead><tr><th scope="col">시기</th><th scope="col">작업</th><th scope="col">종류</th><th scope="col">내 역할</th><th scope="col">단계</th></tr></thead>
<tbody>
{chr(10).join(rows)}
</tbody>
</table>
</div>
</main>
</body>
</html>
"""


def axes_html():
    cols = []
    for a in AXES:
        lis = "".join(f'<li><a href="{e(ITEMS[k]["url"])}" data-return-key="axis-{a["id"]}-{k}">{e(ITEMS[k]["name"])}</a></li>' for k in a["items"])
        cols.append(f'<div class="axis"><h3>{e(a["name"])}</h3><p>{e(a["proof"])}</p><ul>{lis}</ul></div>')
    views = "".join(f'<a href="{k}/" data-return-key="view-{k}">{e(v["title"])}</a>' for k, v in VIEWS.items())
    return f"""<!-- axes:start (tools/build_views.py 가 curation.json 으로 만든다. 손으로 고치지 않는다) -->
<section class="axes" aria-labelledby="axes-h">
  <div class="axes-board">
    <h2 id="axes-h">무엇을 할 수 있는지</h2>
    <div class="axes-grid">{''.join(cols)}</div>
    <p class="axes-views"><span>직무별로 보기</span>{views}<a href="all/" data-return-key="view-all">전체 목록</a></p>
  </div>
</section>
<!-- axes:end -->"""


def picks_html():
    lis = "".join(f'<li><a href="{e(ITEMS[k]["url"])}" data-return-key="pick-{k}"><b>{e(ITEMS[k]["name"])}</b><span>{e(ITEMS[k]["short"])}</span></a></li>' for k in D["picks"])
    return f"""<!-- picks:start (tools/build_views.py 가 curation.json 으로 만든다) -->
  <div class="picks piece" style="--rot:.6deg"><h2>대표 작업 {len(D['picks'])}개</h2><ul>{lis}</ul></div>
  <!-- picks:end -->"""


def main():
    for k, v in VIEWS.items():
        for key in v["items"]:
            assert key in ITEMS, f"{k}: 없는 작품 {key}"
        (ROOT / k).mkdir(exist_ok=True)
        (ROOT / k / "index.html").write_text(view_page(k, v), encoding="utf-8")
    (ROOT / "all").mkdir(exist_ok=True)
    (ROOT / "all" / "index.html").write_text(all_page(), encoding="utf-8")
    idx = ROOT / "index.html"
    t = idx.read_text(encoding="utf-8")
    block = axes_html()
    if "<!-- axes:start" in t:
        t = re.sub(r"<!-- axes:start.*?<!-- axes:end -->", lambda m: block, t, flags=re.S)
    else:
        t = t.replace('<section class="kinds"', block + '\n\n<section class="kinds"', 1)
    t = re.sub(r"<!-- picks:start.*?<!-- picks:end -->", lambda m: picks_html(), t, flags=re.S)
    idx.write_text(t, encoding="utf-8")
    print(f"만듦: 직무 주소 {len(VIEWS)}개 · 전체 목록 {len(D['all'])}개 · 역량 지도 {len(AXES)}칸")


if __name__ == "__main__":
    main()
