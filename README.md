# 🌌 COSMOS 과학 동아리 물리 & 천체 인터랙티브 시뮬레이터 모음집

COSMOS 과학 동아리에서 자체 제작한 고정밀 물리 및 천체 인터랙티브 시뮬레이션 웹 애플리케이션 모음입니다. 별도의 설치 없이 순수 웹 브라우저(Canvas API & Web Audio) 환경에서 60 FPS로 부드럽게 구동됩니다.

---

## 🚀 온라인 실시간 체험 링크 (GitHub Pages)

| 시뮬레이션 명칭 | 설명 | 바로가기 |
| :--- | :--- | :---: |
| **⏳ 이중/다중진자 & 블랙번 진자** | Runge-Kutta 4차(RK4) 혼돈 역학 진자 및 3D 하모노그래프 리사주(Lissajous) 곡선 시뮬레이션 | [체험하기](https://lilyd1879-svg.github.io/cosmos-simulations/index.html) |
| **🪐 정밀 N-체 다체 중력 & 행성 시뮬레이션** | 태양계 행성 궤도, 라그랑주 점, 3체 이상 다체 중력 섭동 및 충돌 역학 시뮬레이션 | [체험하기](https://lilyd1879-svg.github.io/cosmos-simulations/gravity.html) |
| **🌌 실시간 천구 별자리 & 행성 지도** | 사용자 위치 기반 실시간 별자리, 행성 남중고도 계산 및 인공위성(ISS 등) 실시간 궤도 추적 | [체험하기](https://lilyd1879-svg.github.io/cosmos-simulations/sky.html) |
| **🌫️ 행성 대기 & 유체 역학 시뮬레이션** | 행성별 대기 구성비, 밀도, 유체 점성 및 난류 유동(Navier-Stokes) 환경 시뮬레이션 | [체험하기](https://lilyd1879-svg.github.io/cosmos-simulations/air.html) |
| **📊 동아리 활동 발표 프레젠테이션** | 과학 동아리 활동 경과 및 물리 시뮬레이션 원리 발표 슬라이드 | [보러가기](https://lilyd1879-svg.github.io/cosmos-simulations/presentation.html) |

---

## 🛠️ 주요 기술 스택
- **Engine**: Pure Vanilla JavaScript (No Heavy External Frameworks, 100% Client-Side)
- **Rendering**: HTML5 Canvas 2D / 3D Projection Context
- **Physics**: 
  - 4th-Order Runge-Kutta (RK4) Numerical Integration
  - N-Body Newton Gravitational Dynamics
  - Navier-Stokes Grid-based Fluid Mechanics
- **Audio**: Web Audio API Procedural Synthesizer & Spatial Ambient Sound

---

## 📂 파일 구조
- `index.html` / `pendulum.html`: 이중/다중진자 및 블랙번 진자 (리사주 곡선)
- `gravity.html`: N-체 다체 중력 및 행성 궤도 시뮬레이션
- `sky.html`: 실시간 천구 별자리 지도 및 행성 궤적
- `air.html`: 대기 유체 역학 시뮬레이션
- `presentation.html`: 동아리 발표 슬라이드
