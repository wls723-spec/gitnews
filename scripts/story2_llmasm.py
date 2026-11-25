# -*- coding: utf-8 -*-
# Story 2: alesha-pro/llm.asm (100% Pure x86-64 NASM Assembly LLM Trilogy)

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 2] alesha-pro/llm.asm : Pure Assembly LLM Trilogy   -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_llmasm.jpg" alt="llm.asm Pure x86-64 Assembly LLM Inference and Bare-Metal OS Editorial Illustration" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="cpu" style="width:12px;height:12px;"></i> BARE-METAL ENGINEERING</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">⚡ 14.7KB 바이너리 · llama.cpp 대비 최대 +35.6% 빠름 · OS 없는 베어메탈 AI</span>
              <span class="platform-tag">GitHub New Rocket &amp; x86-64 ASM</span>
              <span class="platform-tag">alesha-pro / llm.asm</span>
            </div>

            <h2 class="article-headline">
              "C도, Rust도, libc도 없다" — 14.7KB 순수 어셈블리로 llama.cpp를 꺾은 'llm.asm'
            </h2>

            <div class="article-subheadline">
              17,252줄의 순수 x86-64 NASM 어셈블리만으로 Qwen3-0.6B 추론기(14,712 B · 126.8 tok/s), 리눅스 없이 부팅되는 베어메탈 AI OS(24,252 B · 74ms 부팅), 그리고 브라유 점자 TUI를 갖춘 Mini-GPT 학습기(32,944 B)까지 3부작을 구현 (★152 · MIT)
            </div>
            <p class="article-snippet">
              거대한 PyTorch와 수백 MB짜리 CUDA·C++ 런타임이 당연하게 여겨지는 시대에, 단 <strong>14,712바이트</strong>짜리 정적 리눅스 ELF 파일이 그 벽을 비웃듯 치고 나왔습니다. 공개 15시간 만에 ★152를 기록한 <strong>alesha-pro/llm.asm</strong>은 C 컴파일러, <code>libc</code>, <code>libm</code>, 외부 라이브러리 의존성이 모두 <strong>0개</strong>인 순수 x86-64 NASM 어셈블리 3부작입니다. <code>Qwen3-0.6B(Q8_0)</code> 추론에서는 4스레드 기준 <code>69.24 tok/s</code>, 40스레드 기준 <code>126.81 tok/s</code>를 찍어 <strong><code>llama.cpp</code> CPU 모드를 +18%~+35.6% 앞질렀고</strong>, 운영체제 없이 74ms 만에 바로 LLM 챗봇으로 부팅되는 24KB 베어메탈 OS까지 구현해 시스템 해커들을 열광시키고 있습니다.
            </p>
            <div class="article-action">
              <span>메모 펼치기</span>
              <i data-lucide="chevron-down" class="chevron-icon"></i>
            </div>
          </div>
        </div>

        <div class="article-detail" onclick="event.stopPropagation()">
          <div class="editorial-content">

            <h3 class="editorial-section-title">
              <i data-lucide="flame"></i> 1. 리드: 15KB 플로피에도 들어가는 6억 파라미터 AI 엔진
            </h3>
            <p>
              현대 AI 추론 스택을 열어보면 겹겹이 쌓인 추상화의 탑이 끝도 없이 이어진다. Python 인터프리터 아래 C++ 바인딩이 있고, 그 아래 <code>glibc</code>, <code>libstdc++</code>, 동적 링커, 스레드 런타임, 수많은 백엔드 셰이더가 얽혀 있다. 가볍다는 C/C++ 엔진조차 바이너리와 공유 라이브러리를 합치면 수십 MB를 훌쩍 넘긴다. 그런데 <code>alesha-pro/llm.asm</code> 저장소의 <code>Makefile</code>을 실행하면 눈을 의심하게 되는 결과물이 떨어져 나온다. <code>build/asm-llm</code>, 크기 정확히 <strong>14,712바이트</strong>. 이메일 첨부파일 아이콘 하나보다 가벼운 파일이 Qwen3-0.6B 모델을 통째로 구동한다.
            </p>
            <p>
              더 놀라운 건 이 프로젝트가 단순한 "되기는 되는(Toy) 장난감"이 아니라는 사실이다. AMD EPYC 7642(CPU 전용) 환경에서 동일한 Qwen3-0.6B Q8_0 모델을 놓고 <code>llama.cpp</code>와 정면 대결을 벌인 벤치마크에서, <code>llm.asm</code>은 1스레드 <code>20.70 tok/s</code>(+24.5%), 4스레드 <code>69.24 tok/s</code>(+35.6%), 40스레드 <code>125.86 tok/s</code>(최고 <code>126.81 tok/s</code>, +19.8%)를 기록하며 전 구간에서 C++ 표준 엔진을 따돌렸다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 추상화 오버헤드를 걷어내면 드러나는 실리콘의 민낯
            </h3>
            <p>
              <code>llm.asm</code>은 단순히 "어셈블리로 짰다"는 기행이 아니라, <strong>컴파일러의 범용 추상화와 OS 스케줄러 계층을 제거했을 때 CPU 메모리 대역폭과 AVX2 명령어 파이프라인이 어디까지 빨라질 수 있는지</strong>를 증명하는 실전 교과서다. 추론(14.7 KB)에 더해 리눅스 커널조차 없이 하드웨어 위에서 바로 부팅되는 <strong>24.2 KB 베어메탈 AI OS</strong>와 역전파·AdamW까지 어셈블리로 짠 <strong>32.9 KB 학습기</strong>까지 3부작으로 완성되면서, 에지 임베디드·보안 감사·저수준 AI 런타임 설계자들에게 강렬한 충격을 던졌다.
            </p>

            <div class="editorial-quote">
              <p>
                "C도, C++도, Rust도, libc도, libm도, 런타임 의존성도 없다. <strong>expf·sincosf·RMSNorm·RoPE·SwiGLU부터 BPE 토크나이저, futex 스레드 풀, 베어메탈 ACPI/APIC SMP 커널, 해석적 역전파와 실시간 점자(Braille) TUI까지 17,252줄 전부를 손수 x86-64 어셈블리로 작성했다.</strong>"
              </p>
              <small>— alesha-pro/llm.asm 공식 저장소 아키텍처 명세</small>
            </div>

            <p>
              특히 두 번째 프로젝트인 <code>02-baremetal-os</code>(<code>build/asm-llm-os.elf</code>, 24,252 바이트)는 QEMU KVM(16 vCPU)과 실제 Proxmox Xeon 서버에서 <strong>0 GB 디스크·OS 없음</strong> 상태로 전원 인가 후 <strong>74~94ms</strong> 만에 부팅해 <code>134.94 tok/s</code>로 Qwen3 대화를 시작한다. 2 MiB 휴지 페이지(Huge-Page) 항등 매핑 덕분에 리눅스 위에서 돌릴 때보다 오히려 약 10% 더 높은 처리량을 뽑아냈다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: INT8×INT8 AVX2 커널과 0-의존성 시스템 호출 파이프라인
            </h3>
            <p>
              14.7 KB에서 32.9 KB 사이의 극소 바이너리가 PyTorch FP32 기준 코사인 유사도 <code>0.99965</code>(탐욕 디코딩 64/64 토큰 일치)와 학습기 역전파 21개 그래디언트 텐서 코사인 <code>1.0000000000</code>을 달성한 핵심 기술은 세 가지로 압축된다:
            </p>
            <ul>
              <li><strong><code>FAST_Q8=1</code> AVX2+F16C 하이브리드 GEMV 커널:</strong> 일반 디코드 루프에서 <code>llama.cpp</code>와 경쟁하기 위해 INT8 활성값×INT8 가중치 내적을 AVX2 정수 명령(<code>vpmaddubsw</code> / <code>vpmaddwd</code>)으로 처리하고, <code>.asmbin</code> v2 포맷의 FP16 블록 스케일은 <code>F16C vcvtph2ps</code>로 즉시 복원한다. 여기에 다음 행(Next-Row) 단조 프리페치와 Head-Major 연속 KV 캐시, 병렬 GQA(Grouped-Query Attention)를 결합해 메모리 대역폭 병목을 극소화했다.</li>
              <li><strong><code>libc</code> 없는 Linux Syscall &amp; <code>clone()</code>/<code>futex()</code> 스레드 풀:</strong> 리눅스 ELF 버전은 <code>nasm</code>으로 어셈블한 뒤 <code>ld</code>로만 링크하여 <code>mmap</code>, <code>read</code>, <code>write</code>, <code>clone</code>, <code>futex</code> 시스템 콜을 커널 ABI에 직접 꽂는다. 모든 스레드 수(1~40T)에서 비트 단위까지 동일한 결정론적(Deterministic) 출력을 보장한다.</li>
              <li><strong>Multiboot 1 베어메탈 OS &amp; <code>6x16</code> 레지스터 블록 SGEMM 학습기:</strong> <code>02-baremetal-os</code>는 32비트 보호 모드에서 64비트 롱 모드로 전환한 뒤 2 MiB 페이징·ACPI MADT 파싱·APIC SMP 코어 깨우기를 거쳐 VGA/PS2/COM1 인터페이스로 부팅한다. <code>03-minigpt-train</code>은 YMM 레지스터를 <code>6×16</code>으로 타일링한 FP32 SGEMM과 AdamW, 80×24 UTF-8 점자 손실 그래프 TUI를 32.9 KB 안에 구겨 넣었다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">llm.asm 순수 x86-64 어셈블리 3부작 계층 구조</span>
                <span class="schematic-badge">17,252 Lines NASM · Zero Dependencies · MIT</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Inference ELF (14.7 KB)</div>
                  <div class="schematic-desc">
                    <code>asm-llm</code>: Qwen3-0.6B Q8_0 추론<br>
                    내장 BPE 토크나이저 &amp; GQA/QK-Norm/RoPE<br>
                    AVX2 <code>vpmaddubsw</code> + <code>vcvtph2ps</code> GEMV<br>
                    <code>clone()</code>/<code>futex()</code> 풀 · 126.8 tok/s
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Bare-Metal OS (24.2 KB)</div>
                  <div class="schematic-desc">
                    <code>asm-llm-os.elf</code>: OS 없는 BIOS/UEFI 부팅<br>
                    Multiboot 1 → Long Mode → 2 MiB HugePage<br>
                    ACPI/APIC SMP 멀티코어 활성화<br>
                    74ms 부팅 · VGA/COM1 챗 · 134.9 tok/s
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Mini-GPT Trainer (32.9 KB)</div>
                  <div class="schematic-desc">
                    <code>asm-gpt-train</code>: 순수 FP32 학습·샘플링<br>
                    <code>6×16</code> 레지스터 블록 AVX2+FMA SGEMM<br>
                    전 21개 텐서 PyTorch 대비 1.000 코사인 일치<br>
                    Decoupled AdamW + 80×24 점자 Loss TUI
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">alesha-pro/llm.asm 저장소 실화면 — 3부작 바이너리 스펙 및 llama.cpp 대비 스레드별 디코드 벤치마크</span>
              </div>
              <img src="../assets/images/demo_llmasm.png" alt="alesha-pro llm.asm Repository Benchmarks and Trilogy Specs" class="showcase-img">
              <p class="showcase-caption">
                ▲ github.com/alesha-pro/llm.asm 실화면: 14.7 KB 추론 ELF, 24.2 KB 베어메탈 OS, 32.9 KB 학습기의 바이너리 크기 및 AMD EPYC 7642 환경 llama.cpp 대비 실측 속도표.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 소프트웨어 공학적 시사점: 비대화(Bloat)에 대한 역습과 신뢰할 수 있는 TCB
            </h3>
            <p>
              오늘날 수백 GB 모델 가중치와 수십 GB 컨테이너 이미지가 표준이 된 AI 인프라에서, <code>llm.asm</code>이 던지는 질문은 묵직하다. 왜 가중치 613 MiB를 읽어 들이는 실행 파일과 런타임 생태계가 수 GB씩 필요해야 하는가?
            </p>
            <ul>
              <li><strong>극한으로 줄어든 신뢰 컴퓨팅 기반(TCB):</strong> 국방·항공·금융·보안 에어갭 환경에서 거대한 Python/C++ 의존성 트리를 감사(Audit)하는 비용은 천문학적이다. 반면 MIT 라이선스의 <code>llm.asm</code>은 외부 라이브러리 공급망 공격 표면이 정확히 '0'이며, 전체 코드가 17,252줄에 불과해 실행 바이너리의 모든 명령어를 정적으로 검증하는 것이 가능하다.</li>
              <li><strong>어셈블리 장벽과 AI 보조 최적화의 미래:</strong> 물론 단일 아키텍처(x86-64 AVX2+FMA+F16C)에 종속되며 배치 프리필(Prefill) GEMM 대신 토큰 단위 GEMV에 특화돼 있다는 한계는 분명하다. 하지만 이 극단적 사례는 AI 시대에 "컴파일러가 못 짜는 하드웨어 밀착형 마이크로커널"의 가치가 오히려 다시 상승하고 있음을 보여준다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: OS가 부팅되는 시간에, 이미 모델이 대답을 마친다
            </h3>
            <p>
              서버의 전원을 켜고 리눅스 커널이 <code>systemd</code> 서비스를 하나씩 띄우는 동안, <code>llm.asm</code>의 베어메탈 OS는 이미 74밀리초 만에 16개 코어를 깨워 첫 문장을 생성하고 있다.
            </p>
            <p>
              AI의 크기가 커질수록, 그 아래에서 가중치를 실제로 굴리는 소프트웨어 계층은 거꾸로 이토록 얇고 날카로워질 수 있다. 14,712바이트의 어셈블리 바이너리는 거대 프레임워크에 길들여진 우리에게 '컴퓨터가 원래 얼마나 빠른 기계였는지'를 새삼 일깨운다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=llm+asm+x86-64+assembly+qwen3+bare+metal" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/alesha-pro/llm.asm" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
