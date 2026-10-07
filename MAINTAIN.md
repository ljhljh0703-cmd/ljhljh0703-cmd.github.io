# 작품 모음 관리

이 저장소가 작품 모음 첫 페이지(https://ljhljh0703-cmd.github.io/)의 정본이다. 다른 곳에 있는 사본은 이 저장소를 받아 맞춘다.

## 고치는 곳
- 카드 9장과 종류별 묶음: `works.js` 하나만 고친다.
- 카드 그림: `assets/collage/card-<id>.webp`, `assets/collage/sticker-<id>.webp` (id는 `works.js`의 id와 같게)
- 작품 상세 페이지: 작품별 폴더 (`cofathon/`, `jelly-panic-case/`)
- 화면 모양·움직임: `index.html`

## 새 작품을 카드로 올릴 때
1. 근거 기록을 먼저 만들고, 페이지 문장은 그 기록에 있는 것만 쓴다.
2. 대표 물건 그림 1장을 웹 ChatGPT로 만들고, 기존 카드와 같은 가공을 거쳐 스티커로 만든다.
3. 작품 페이지 첫 화면을 600×800으로 캡처해 인쇄 카드로 만든다.
4. `works.js`의 `works`에 한 줄 추가하고, 맞는 묶음의 `items`에도 넣는다.
5. 첫 페이지의 「작품 N개」 문구 3곳을 실제 개수로 맞춘다.
6. `python3 tools/check.py --online` 통과 확인 후 올린다.

## 올리기 전 검사 (`tools/check.py`)
- 카드마다 그림 두 장이 있는지
- 링크가 실제로 열리는지 (`--online`)
- 「작품 N개」 문구와 실제 카드 수가 같은지
- 쓰면 안 되는 표현(등수·출시 완료·검수에서 막힌 숫자 등)이 없는지
