# 작품 모음 올리기 전 검사 — 데이터 파일과 그림·링크·금지 표현을 확인한다. 하나라도 실패하면 올리지 않는다.
"""
사용: cd 저장소 && python3 tools/check.py            # 파일만 검사
      python3 tools/check.py --online                 # 바깥 링크 응답까지 검사
"""
import json, re, sys, pathlib, urllib.request, urllib.error

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://ljhljh0703-cmd.github.io/"
BANNED = ["19.1%", "19.1 %", "200판", "출시 완료", "상용 출시", "실사용자", "TOP 3", "TOP3", "1위", "2위", "3위",
          "서류 면제", "서류 전형 면제", "개입 5회", "API 36개"]
errors = []

def load_data():
    src = (ROOT / "works.js").read_text(encoding="utf-8")
    body = src[src.index("window.PORTFOLIO =") + len("window.PORTFOLIO ="):].strip().rstrip(";")
    return json.loads(body)

def local_ok(url):
    p = ROOT / url.split("#")[0].split("?")[0]
    return p.is_file() or (p.is_dir() and (p / "index.html").is_file())

warnings = []

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 portfolio-check"})
    return urllib.request.urlopen(req, timeout=20).status

def check_url(url, where, online):
    if url is None:
        return
    if url.startswith(SITE):
        url = url[len(SITE):]
    if not url.startswith("http"):
        first = url.split("/")[0]
        if (ROOT / first).exists():                     # 이 저장소 안의 페이지
            if not local_ok(url): errors.append(f"{where}: 사이트 안에 없는 경로 {url}")
            return
        url = SITE + url                                 # 같은 주소의 다른 작품 저장소
    if not online:
        return
    try:
        code = fetch(url)
        if code >= 400: errors.append(f"{where}: 링크 응답 {code} {url}")
    except urllib.error.HTTPError as e:
        if e.code == 403: warnings.append(f"{where}: 이 환경에서 확인 불가(403) {url}")
        else: errors.append(f"{where}: 링크 응답 {e.code} {url}")
    except Exception as e:
        warnings.append(f"{where}: 이 환경에서 확인 불가({e.__class__.__name__}) {url}")

def main():
    online = "--online" in sys.argv
    d = load_data()
    works, kinds = d["works"], d["kinds"]
    ids = [w["id"] for w in works]
    if len(ids) != len(set(ids)): errors.append("works: id 가 겹침")
    for w in works:
        for k in ("id", "name", "line", "stage", "url", "ink"):
            if not w.get(k): errors.append(f"카드 {w.get('id')}: {k} 비어 있음")
        for f in (f"card-{w['id']}.webp", f"sticker-{w['id']}.webp"):
            if not (ROOT / "assets/collage" / f).is_file(): errors.append(f"카드 {w['id']}: 그림 없음 assets/collage/{f}")
        check_url(w["url"], f"카드 {w['id']}", online)
    for c in kinds:
        for k in ("ico", "k", "name", "en", "desc", "meta", "items"):
            if not c.get(k): errors.append(f"묶음 {c.get('name')}: {k} 비어 있음")
        for it in c["items"]:
            if not it.get("name") or not it.get("desc"): errors.append(f"묶음 {c['name']}: 항목 이름·설명 빠짐")
            check_url(it.get("url"), f"묶음 {c['name']} · {it.get('name')}", online)
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    for n in re.findall(r"작품 (\d+)개", html):
        if int(n) != len(works): errors.append(f"index.html: 「작품 {n}개」 문구와 실제 카드 {len(works)}개가 다름")
    pages = [ROOT / "index.html", ROOT / "works.js"] + sorted(ROOT.glob("*/index.html"))
    for p in pages:
        t = p.read_text(encoding="utf-8", errors="ignore")
        t = re.sub(r"<style.*?</style>", "", t, flags=re.S)
        for b in BANNED:
            if b in t: errors.append(f"{p.relative_to(ROOT)}: 금지 표현 「{b}」")
    for w in warnings: print(" ⚠", w)
    if errors:
        print("❌ 실패", len(errors), "건"); [print(" -", e) for e in errors]; sys.exit(1)
    print(f"✅ 통과 · 카드 {len(works)}개 · 묶음 {len(kinds)}개 · 검사한 페이지 {len(pages)}개" + (" · 바깥 링크 포함" if online else ""))

if __name__ == "__main__":
    main()
