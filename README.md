# 알고리즘 스터디 (삼성 SW 역량테스트 A·B형 대비)
(2026.8.13.(목) 최신화)

📖 **처음 오셨나요?** → [깃허브 사용 가이드](https://github.com/SSAFY-Algorithm-Team/Team-3/blob/main/GITHUB_GUIDE.md) *(출처: 알고리즘-3팀장 임규영)*

---

## 🎯 목표

1. **필수 목표**
   - 가. 삼성 SW 역량테스트 **A형** 취득
2. **도전 목표**
   - 나. 삼성 SW 역량테스트 **B형** 취득
     1) B형은 4시간 동안 1문제를 풀며, Main 함수는 수정하지 않고 주어진 함수 내용만 구현하는 형식입니다.
     2) 단순 구현보다 **"완전탐색을 어떻게 최적화할 것인가"** 를 묻는 문제가 주로 나옵니다.

**사용 언어**: Python, Java

---

## 🔄 진행 방식

```text
1. (스터디 전) 각자 문제 풀이 → 브랜치에 커밋 & push
2. 스터디 (약 2시간 내외)
3. (스터디 후) 팀장이 PR 일괄 머지
```

---

---

## 🔄 개념(레퍼런스) 자료

**해당 자료들은 REFERENCE 폴더에서 확인 가능합니다**

📖 **그래프** → [그래프](./REFERENCE/그래프.pdf)

📖 **BFS** → [BFS](./REFERENCE/BFS.pdf)

📖 **BFS 레퍼런스 코드** → [BFS 레퍼런스 코드](./REFERENCE/bfs.py)

📖 **DFS** → [DFS](./REFERENCE/DFS.pdf)

📖 **DFS 레퍼런스 코드** → [DFS 레퍼런스 코드](./REFERENCE/dfs.py)

---

## 📅 1주차 문제 (11문제)

- **주제**: 완전탐색 & 백트래킹
- **출처**: SWEA / 프로그래머스

<details>
<summary><b>기본 문제 (6문제)</b></summary>

| 출처 | 문제 등급 | 번호 | 제목 | 링크 |
|:---:|:---:|:---:|---|:---:|
| SWEA | D1 | 21936 | 길이가 M인 회문 찾기 | [바로가기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZFkKmLa1zEDFAQW&categoryId=AZFkKmLa1zEDFAQW&categoryType=CODE) |
| SWEA | D1 | 22375 | 스위치 조작 | [바로가기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZHA7Cn6ZgsDFAQP&categoryId=AZHA7Cn6ZgsDFAQP&categoryType=CODE) |
| SWEA | D1 | 23975 | 우주 괴물 | [바로가기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZU7flp6n8XHBIRK&categoryId=AZU7flp6n8XHBIRK&categoryType=CODE) |
| SWEA | D2 | 12712 | 파리퇴치3 | [바로가기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXuARWAqDkQDFARa) |
| SWEA | D2 | 26059 | 과일 등급 분류 | [바로가기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZwl9ifa3dLHBIT3) |
| SWEA | D3 | 10761 | 신뢰 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXSVc1TqEAYDFAQT) |

</details>

<details>
<summary><b>도전 문제 (5문제)</b></summary>

| 출처 | 문제 등급 | 번호 | 제목 | 링크 |
|:---:|:---:|:---:|---|:---:|
| 프로그래머스 | LEVEL1 | 86491 | 최소 직사각형 | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/86491) |
| SWEA | D4 | 1767 | 프로세서 연결하기 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf&categoryId=AV4suNtaXFEDFAUf&categoryType=CODE&problemTitle=%ED%94%84%EB%A1%9C%EC%84%B8%EC%84%9C&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) |
| SWEA | D4 | 23975 | 벽돌 깨기 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo&categoryId=AWXRQm6qfL0DFAUo&categoryType=CODE&problemTitle=%EB%B2%BD%EB%8F%8C&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) |
| 프로그래머스 | LEVEL2 | 42839 | 소수 찾기 | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42839) |
| 프로그래머스 | LEVEL2 | 87946 | 피로도 | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/87946) |

</details>

---

## 📅 2주차 문제 (15문제)

- **주제**: BFS & DFS
- **출처**: SWEA / 프로그래머스 / 코더스패스

<details>
<summary><b>개념 문제 (3문제)</b></summary>

| 출처 | 문제 등급 | 번호 | 제목 | 링크 |
|:---:|:---:|:---:|---|:---:|
| 코더스패스 | LEVEL3 | 1397 | 간선의 배열과 인접행렬 | [바로가기](https://codersit.co.kr/pass/oj/1397?pass=cote@step1) |
| 코더스패스 | LEVEL4 | 1145 | 너비 우선 탐색 (BFS) | [바로가기](https://codersit.co.kr/pass/oj/1145?pass=cote@step1) |
| 코더스패스 | LEVEL4 | 1732 | 깊이 우선 탐색 (DFS) | [바로가기](https://codersit.co.kr/pass/oj/1732?pass=cote@step1) |

</details>

<details>
<summary><b>기본 문제 (6문제)</b></summary>

| 출처 | 문제 등급 | 번호 | 제목 | 링크 |
|:---:|:---:|:---:|---|:---:|
| 코더스패스 | LEVEL4 | 1146 | 연결 요소의 개수 | [바로가기](https://codersit.co.kr/pass/oj/1146?pass=cote@step1) |
| SWEA | D2 | 5102 | 노드의 거리 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTVmxDKb1oDFAVT&categoryId=AWTVmxDKb1oDFAVT&categoryType=CODE&problemTitle=%EB%85%B8%EB%93%9C%EC%9D%98+%EA%B1%B0%EB%A6%AC&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) |
| SWEA | D3 | 5105 | 미로의 거리 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTVoHTab5gDFAVT&categoryId=AWTVoHTab5gDFAVT&categoryType=CODE&problemTitle=5105&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) |
| SWEA | D3 | 5188 | 최소합 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTtlrlKeDcDFAVT&categoryId=AWTtlrlKeDcDFAVT&categoryType=CODE&problemTitle=%EC%B5%9C%EC%86%8C%ED%95%A9&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) |
| SWEA | D3 | 5215 | 햄버거 다이어트 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWT-lPB6dHUDFAVT&categoryId=AWT-lPB6dHUDFAVT&categoryType=CODE&problemTitle=%ED%96%84%EB%B2%84%EA%B1%B0&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) |
| SWEA | D4 | 1249 | 보급로 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD&categoryId=AV15QRX6APsCFAYD&categoryType=CODE&problemTitle=%EB%B3%B4%EA%B8%89%EB%A1%9C&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) |

</details>

<details>
<summary><b>도전 문제 (6문제)</b></summary>

| 출처 | 문제 등급 | 번호 | 제목 | 링크 |
|:---:|:---:|:---:|---|:---:|
| SWEA | D4 | 2117 | 홈 방범 서비스 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V61LqAf8DFAWu&categoryId=AV5V61LqAf8DFAWu&categoryType=CODE&problemTitle=%ED%99%88&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) |
| SWEA | D5 | 1247 | 최적 경로 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15OZ4qAPICFAYD&categoryId=AV15OZ4qAPICFAYD&categoryType=CODE&problemTitle=1247&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) |
| SWEA | D5 | 2382 | 미생물 격리 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV597vbqAH0DFAVl&categoryId=AV597vbqAH0DFAVl&categoryType=CODE&problemTitle=%EB%AF%B8%EC%83%9D%EB%AC%BC&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) |
| SWEA | D5 | 5644 | 무선 충전 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRDL1aeugDFAUo&categoryId=AWXRDL1aeugDFAUo&categoryType=CODE&problemTitle=%EB%AC%B4%EC%84%A0&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) |
| SWEA | D5 | 2115 | 벌꿀채취 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V4A46AdIDFAWu&categoryId=AV5V4A46AdIDFAWu&categoryType=CODE&problemTitle=%EB%B2%8C%EA%BF%80&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) |
| SWEA | D6 | 1855 | 영준이의 진짜 BFS | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LnipaDvwDFAXc&categoryId=AV5LnipaDvwDFAXc&categoryType=CODE&problemTitle=BFS&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) |

</details>

---

## 📤 제출 방법 요약

```bash
git switch master
git pull
git switch -c {깃허브 닉네임}/week-01
# 문제 풀고 커밋
git push -u origin {깃허브 닉네임}/week-01
```