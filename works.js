/* 작품 모음 정본 데이터 — 카드(works)와 종류별 묶음(kinds)은 이 파일만 고치면 페이지에 반영된다.
   url: 이 사이트 안이면 상대 경로, 바깥이면 https 전체 주소, 공개 페이지가 없으면 null.
   works.id = assets/collage/card-<id>.webp · sticker-<id>.webp 파일 이름과 같아야 한다.
   kinds.sticker(선택) = 카드 작품이 없는 묶음에 붙일 스티커, assets/collage/sticker-<sticker>.webp. 고친 뒤 python3 tools/check.py */
window.PORTFOLIO = {
  "works": [
    {
      "id": "08-cofathon",
      "name": "Cofathon 2026",
      "line": "비개발자 담당자에게 받은 판단 기준을 4시간 만에 코드가 검사하게 만든 인터뷰 연습 도구",
      "stage": "최우수 수상 · 개인 참가",
      "url": "cofathon/",
      "ink": "#c0412a"
    },
    {
      "id": "10-game-ops",
      "name": "게임 운영 플랫폼",
      "line": "직접 만든 게임의 디스코드 버그 제보를 분류해 깃허브 이슈로 넘기고, 고친 PR이 합쳐지면 제보자에게 답장까지 보내는 서버",
      "stage": "작동 데모 · 개인",
      "url": "game-ops/",
      "ink": "#207878"
    },
    {
      "id": "01-bookemon",
      "name": "북켓몬",
      "line": "18개 질의 오프라인 평가에서 순위 규칙으로 부적합 추천을 15.56%에서 2.22%로 줄인 도서 추천 서비스",
      "stage": "데모 · 오프라인 평가 완료",
      "url": "AI-Book-Curation/portfolio.html",
      "ink": "#4b4ad1",
      "role": "팀 프로젝트 · 팀장 · 기획 리드 · AI 추천 설계·평가",
      "flow": [
        "질문 입력",
        "후보 검색",
        "순위 조정",
        "책 선택"
      ]
    },
    {
      "id": "09-jelly-panic",
      "name": "지켜줘! 젤리 패닉",
      "line": "피할 수 없는 위협이 한 판도 안 나오는지 500판을 돌려 확인한 수읽기 퍼즐 디펜스",
      "stage": "웹에서 바로 플레이",
      "url": "jelly-panic-case/",
      "ink": "#207878"
    },
    {
      "id": "07-hwigi-tower",
      "name": "회귀자는 탑을 오른다",
      "line": "죽어도 끝나지 않는 탑, 동료 AI와 함께 오르는 로그라이크",
      "stage": "플레이 가능 · Android",
      "url": "hwigi-tower-portfolio/Docs/Portfolio/hwigi-tower-steam-portfolio.html",
      "ink": "#c0412a"
    },
    {
      "id": "13-penelope",
      "name": "Penelope",
      "line": "이야기가 무너지는 조건을 정하고, 그 조건을 규칙과 시험으로 옮긴 이야기 세계 엔진",
      "stage": "공개 라이브 데모 · OpenAI Build Week 제출",
      "url": "penelope/",
      "ink": "#4b4ad1"
    }
  ],
  "kinds": [
    {
      "ico": "game",
      "k": "#c0412a",
      "name": "게임",
      "en": "Games",
      "desc": "AI와 같이 만들고, 규칙을 먼저 정해 검증한 게임들",
      "meta": "웹·안드로이드에서 바로 실행",
      "items": [
        {
          "name": "지켜줘! 젤리 패닉",
          "url": "jelly-panic-case/",
          "desc": "수읽기 퍼즐 디펜스 · 스토어 심사 제출"
        },
        {
          "name": "회귀자는 탑을 오른다",
          "url": "hwigi-tower-portfolio/Docs/Portfolio/hwigi-tower-steam-portfolio.html",
          "desc": "동료 AI와 오르는 로그라이크 · Android"
        },
        {
          "name": "Bone Trail",
          "url": "bone-trail/",
          "desc": "libGDX 로그라이크"
        },
        {
          "name": "BackRoom Level 0",
          "url": "backroom-level-0-godot/portfolio.html",
          "desc": "Godot 탐험 게임"
        },
        {
          "name": "해골 짐꾼의 탑",
          "url": null,
          "desc": "로그라이크 개조판 · 진행 중"
        },
        {
          "name": "턴제 퍼즐",
          "url": null,
          "desc": "솔버가 풀이 가능 여부를 판정 · 진행 중"
        }
      ]
    },
    {
      "ico": "ai",
      "k": "#4b4ad1",
      "name": "AI 서비스",
      "en": "AI services",
      "desc": "추천·상담·통역·매매처럼 실제 쓰임을 두고 만든 AI 서비스",
      "meta": "전부 공개 페이지로 연결",
      "items": [
        {
          "name": "북켓몬",
          "url": "AI-Book-Curation/portfolio.html",
          "desc": "AI 도서 추천"
        },
        {
          "name": "알려줄고양",
          "url": "Medical-Chatbot/portfolio.html",
          "desc": "내과 자문 챗봇"
        },
        {
          "name": "StarLink",
          "url": "StarLink/portfolio.html",
          "desc": "실시간 통역 iOS 앱"
        },
        {
          "name": "QuantLeap",
          "url": "hyunsoo-bot/portfolio.html",
          "desc": "자동매매 에이전트 · 모의 실행"
        },
        {
          "name": "로켓단",
          "url": "ai-npc-social-reasoning-harness/",
          "desc": "늑대인간 게임 사회추론 실험"
        }
      ]
    },
    {
      "ico": "sys",
      "k": "#207878",
      "name": "시스템·운영체계",
      "en": "Systems",
      "desc": "여러 AI가 같은 기준으로 일하게 만드는 도구와 작업 체계",
      "meta": "매일 직접 운영 중",
      "items": [
        {
          "name": "게임 운영 플랫폼",
          "url": "game-ops/",
          "desc": "게임 버그 제보를 분류해 이슈와 답장까지 잇는 서버"
        },
        {
          "name": "Sub brain",
          "url": null,
          "desc": "여러 AI가 함께 쓰는 지식·작업 운영 체계 · 매일 운영"
        },
        {
          "name": "Agent Forge",
          "url": "agent-forge/portfolio.html",
          "desc": "아이디어 한 줄로 게임을 만드는 파이프라인"
        },
        {
          "name": "Vibe Design Studio",
          "url": "VDS/case.html",
          "desc": "바이브 코더용 디자인 시스템"
        },
        {
          "name": "Learning Atlas",
          "url": "learning-atlas/",
          "desc": "학습 기록 지도"
        }
      ]
    },
    {
      "ico": "cup",
      "k": "#c99a1a",
      "name": "대회·해커톤",
      "en": "Competitions",
      "desc": "정해진 시간 안에 문제를 다시 정하고 끝까지 낸 기록",
      "meta": "수상 1 · 제출 3",
      "items": [
        {
          "name": "Cofathon 2026 최우수 수상",
          "url": "cofathon/",
          "desc": "KRAFTON Forward Deployed Engineer 트랙 · 개인 참가"
        },
        {
          "name": "카투사 해커톤",
          "url": "https://github.com/ljhljh0703-cmd/katousa-agent-harness",
          "desc": "투자 에이전트 안전 기준 · 제출"
        },
        {
          "name": "OpenAI Build Week",
          "url": "penelope/",
          "desc": "Penelope · 이야기 세계 엔진 · 제출"
        },
        {
          "name": "SKT 모두의 promp.T",
          "url": null,
          "desc": "업무 AI 활용 · 제출"
        }
      ]
    },
    {
      "ico": "work",
      "sticker": "kind-work",
      "k": "#1b1a17",
      "name": "실무 경력",
      "en": "Work",
      "desc": "제안 PM으로 시작해 지금은 AI 엔지니어로 일하는 중",
      "meta": "2022 ~ 현재",
      "items": [
        {
          "name": "위메이드엑스알",
          "url": "doc-search/",
          "desc": "AI 엔지니어 인턴 · 기획 문서 탐색 AI 스킬 · 재직 중"
        },
        {
          "name": "AX 전환",
          "url": "ax-case/",
          "desc": "인증 사회적기업 · LLM 위키 구축 · AI 직원 8명"
        },
        {
          "name": "트루빈스",
          "url": null,
          "desc": "제안 PM · 참여한 제안의 누적 매출 17억 · 2022~2024"
        },
        {
          "name": "기업 홍보 영상 기획",
          "url": null,
          "desc": "외주 · 진행 중"
        }
      ]
    },
    {
      "ico": "pen",
      "sticker": "kind-pen",
      "k": "#8a5a2b",
      "name": "창작·글",
      "en": "Writing",
      "desc": "소설·게임 시나리오·수기까지, 기획의 바탕이 되는 글",
      "meta": "출판 1",
      "items": [
        {
          "name": "초파리",
          "url": null,
          "desc": "장편소설 · 2024 출판"
        },
        {
          "name": "TRPG 시나리오",
          "url": null,
          "desc": "크툴루의 부름"
        },
        {
          "name": "공모전 수기·에세이",
          "url": null,
          "desc": "여러 편"
        }
      ]
    }
  ]
};
