# -*- coding: utf-8 -*-
# Story 1: jingyaogong/minimind (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 1] jingyaogong/minimind : COVER STORY                -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_minimind.jpg" alt="MiniMind Ultra-Lightweight From-Scratch LLM Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">🧠 단돈 600원·2시간 만에 0부터 깎는 64M LLM</span>
              <span class="platform-tag">GitHub Trending &amp; PyTorch Native</span>
              <span class="platform-tag">jingyaogong / minimind</span>
            </div>

            <h2 class="main-lead-headline">
              <span id="hero-title">단돈 600원과 2시간이면 내 GPU에서 LLM을 '0부터' 창조한다: 오픈소스 'MiniMind'의 역습</span>
            </h2>

            <div class="article-subheadline">
              transformers·trl 추상화 없이 순수 PyTorch만으로 사전학습·SFT·DPO·GRPO·MoE·Agentic RL까지 전 과정을 바닥부터 구현한 64M 초경량 언어모델 (+772스타/일, 누적 66,486스타)
            </div>
            <p class="article-snippet">
              수천억 원짜리 H100 클러스터를 가진 빅테크만 파운데이션 모델을 학습할 수 있다는 통념에 균열이 생기고 있습니다. 오늘 하루에만 772스타를 추가하며 GitHub 전체 트렌딩 1위에 오른 <strong>jingyaogong/minimind</strong>는 단 64M(6,400만) 파라미터 크기의 모델을 단일 RTX 3090 GPU에서 2시간(클라우드 대여비 3위안, 약 600원) 만에 바닥부터 직접 학습시켜 토크나이저와 어텐션, 강화학습의 블랙박스를 낱낱이 해체합니다.
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
              <i data-lucide="flame"></i> 1. 리드: "레고로 비행기를 직접 조립하는 게 일등석에 앉아 가는 것보다 짜릿하다"
            </h3>
            <p>
              2026년의 AI 개발자들은 역설적인 소외를 겪고 있다. API 키 한 줄이면 수천억 파라미터 프론티어 모델을 호출할 수 있고, <code>transformers</code>나 <code>trl</code>, <code>peft</code> 같은 고수준 라이브러리를 부르면 단 십여 줄의 코드로 LoRA 미세조정과 추론을 끝낼 수 있다. 하지만 그 편리함이라는 이름의 두꺼운 추상화 장막 뒤에서, 정작 모델이 어떻게 문장을 분절하고 어텐션 행렬을 계산하며 강화학습 보상을 통해 추론 능력을 얻는지는 누구도 직접 만져보지 못하는 '성역'이 되어버렸다.
            </p>
            <p>
              중국 개발자 진야오공(Jingyao Gong)이 Apache-2.0으로 공개해 누적 66,486스타(오늘 +772스타)를 돌파한 <strong>jingyaogong/minimind</strong>는 이 거대한 블랙박스를 책상 위 단일 GPU 한 장으로 끌어내린다. GPT-3의 2,700분의 1 크기인 64M 파라미터 <code>minimind-3</code>(MoE 버전 <code>198M-A64M</code>)을 들고, 고수준 래퍼를 모조리 걷어낸 순수 PyTorch 코드로 "0부터 1까지의 모델 창조"를 증명했기 때문이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 왜 지금 개발자들은 '64M 초소형 백지 모델'에 열광하는가
            </h3>
            <p>
              MiniMind의 폭발적 인기는 단순히 '작은 모델' 때문이 아니다. 프론티어 연구실들이 수조 원대 학습 파이프라인을 비밀에 부치는 사이, MiniMind는 현대 LLM을 지탱하는 모든 핵심 기술—BPE 토크나이저 학습, Pretraining, SFT, DPO, PPO/GRPO/CISPO 강화학습, 멀티턴 Tool-Use Agentic RL, 모델 증류, 심지어 확산 언어모델(dLM)과 선형 어텐션 확장까지—를 누구나 한 파일씩 읽어 내려갈 수 있는 교본으로 열어젖혔다.
            </p>

            <div class="editorial-quote">
              <p>
                "기존 거대 모델에 LoRA를 얹는 것은 뉴턴에게 21세기 스마트폰 사용법을 가르치는 것과 같다. <strong>레고 블록으로 비행기를 직접 조립해 띄우는 경험</strong>만이 물리적 본질을 이해하게 해준다. 단돈 3위안(약 600원)의 GPU 비용이면 0부터 언어모델을 창조할 수 있다."
              </p>
              <small>— jingyaogong/minimind 공식 아키텍처 선언문 (Apache-2.0)</small>
            </div>

            <p>
              더 놀라운 점은 2026년 4월 <code>minimind-3</code> 아키텍처 대개편 이후에도 어제(11월 18일)까지 디코딩 및 FP32 LoRA 병합 수정 커밋이 이어지며 살아 숨 쉬는 표준 코드베이스로 진화하고 있다는 사실이다. <code>Qwen3 / Qwen3-MoE</code> 생태계와 구조를 정렬하고, <code>&lt;tool_call&gt;</code>·<code>&lt;think&gt;</code> 토큰과 <code>open_thinking</code> 적응형 사고 전환까지 64M 모델 안에 그대로 구현해 냈다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 외부 래퍼 제로(0) 순수 PyTorch 풀스택 해부
            </h3>
            <p>
              저장소의 <code>model/</code>과 <code>trainer/</code> 디렉토리를 열어보면, 상용 트레이닝 프레임워크의 거대한 보일러플레이트 대신 놀랄 만큼 명쾌한 직렬 파이프라인이 드러난다:
            </p>
            <ul>
              <li><strong>네이티브 모델 코어 (<code>model/model_minimind.py</code> &amp; <code>model_lora.py</code>):</strong> RoPE(YaRN 장문 확장 지원)와 GQA/MoE 라우팅을 포함한 Dense(64M)·MoE(198M-A64M, 공유 전문가 제거) 아키텍처를 서드파티 추상화 없이 PyTorch 모듈로 직접 정의했다.</li>
              <li><strong>전 주기 10단계 트레이너 (<code>trainer/train_*.py</code>):</strong> 토크나이저 학습(<code>train_tokenizer.py</code>)에서 출발해 <code>train_pretrain.py</code>, <code>train_full_sft.py</code>, <code>train_dpo.py</code>, 그리고 <code>train_ppo.py</code>·<code>train_grpo.py</code>·<code>train_agent.py</code>까지 현대 포스트 트레이닝의 모든 알고리즘을 개별 독립 스크립트로 구현했다.</li>
              <li><strong>분리된 롤아웃 엔진 &amp; 생태계 호환 (<code>trainer/rollout_engine.py</code>):</strong> RLAIF 및 멀티턴 에이전트 강화학습(<code>GRPO / CISPO</code>)에서 생성 백엔드를 유연하게 교체할 수 있도록 롤아웃 엔진을 분리했고, 최종 가중치는 <code>llama.cpp</code>, <code>vllm</code>, <code>ollama</code> 및 OpenAI 호환 API(<code>serve_openai_api.py</code>)로 즉시 서빙된다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">MiniMind-3 순수 PyTorch 제로-투-원(0→1) LLM 학습 파이프라인</span>
                <span class="schematic-badge">Apache-2.0 · 64M Dense / 198M-A64M MoE</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Tokenizer &amp; Pretrain</div>
                  <div class="schematic-desc">
                    BPE + ByteLevel 토크나이저<br>
                    <code>&lt;think&gt;</code> · <code>&lt;tool_call&gt;</code> 특수 토큰<br>
                    <code>pretrain_t2t.jsonl</code> 정제 코퍼스<br>
                    <code>model_minimind.py</code> (RoPE + YaRN)
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. SFT &amp; Post-Training RL</div>
                  <div class="schematic-desc">
                    <code>train_full_sft.py</code> (RTX 3090 2시간)<br>
                    <code>train_dpo.py</code> 선호도 정렬(RLHF)<br>
                    <code>train_grpo.py</code> / <code>train_agent.py</code><br>
                    <code>rollout_engine.py</code> 멀티턴 Tool-Use RL
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Distillation &amp; Serving</div>
                  <div class="schematic-desc">
                    <code>train_distillation.py</code> 지식 증류<br>
                    <code>convert_model.py</code> FP32 LoRA 병합<br>
                    <code>serve_openai_api.py</code> (<code>reasoning_content</code>)<br>
                    <code>llama.cpp</code> · <code>vLLM</code> · <code>Ollama</code> 즉시 배포
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">MiniMind 공식 GitHub 저장소 &amp; 0-to-1 아키텍처 쇼케이스</span>
              </div>
              <img src="../assets/images/demo_minimind.png" alt="MiniMind Official Repository Showcase" class="showcase-img">
              <p class="showcase-caption">
                ▲ jingyaogong/minimind 공식 저장소 실화면: 26M~198M 초경량 Dense/MoE 모델 스펙과 Pretrain→SFT→DPO→Agentic RL 전 과정을 순수 PyTorch로 구현한 전체 로드맵을 확인할 수 있다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 산업·교육 해자 붕괴: 수백만 원 AI 강의를 무력화한 '투명한 코드'
            </h3>
            <p>
              MiniMind가 겨누는 칼날은 빅테크의 데이터센터 독점뿐만 아니라, 거품 낀 AI 교육 시장과 폐쇄형 튜토리얼 산업에도 꽂힌다. 저자는 README에서 "인터넷에 엉터리 설명으로 포장된 유료 AI 강의가 넘쳐난다"고 직격탄을 날리며, 수집·정제·중복 제거까지 마친 전 단계 데이터셋과 학습 코드를 Apache-2.0으로 무료 개방했다.
            </p>
            <ul>
              <li><strong>엣지·특수목적 초소형 모델의 실험실:</strong> 64M 파라미터 모델은 범용 상식 퀴즈에서는 대형 모델과 경쟁하지 않지만, 온디바이스 특화 태스크나 차세대 아키텍처(<code>MiniMind-V</code> 비전, <code>MiniMind-O</code> 옴니, 확산형 <code>dLM</code>)의 빠른 가설 검증에는 수억 원짜리 클러스터보다 압도적인 반복 속도를 제공한다.</li>
              <li><strong>완전한 개방성과 재현성:</strong> 블랙박스 API 호출에만 익숙해진 차세대 엔지니어들에게 "모델 아키텍처와 손실함수 한 줄까지 직접 통제할 수 있는 주권"을 되돌려주었다는 평가가 나온다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 크기가 권력이던 시대의 끝자락에서
            </h3>
            <p>
              프론티어 연구소가 파라미터 수와 데이터센터 전력량을 경쟁할 때, 오픈소스 커뮤니티의 한쪽에서는 단돈 600원으로 지능의 씨앗을 0부터 배양하는 법을 전 세계에 보급하고 있다.
            </p>
            <p>
              남의 거대한 비행기 일등석에 편승해 프롬프트만 깎는 시대는 곧 한계에 부딪힌다. 내 GPU 위에서 직접 엔진을 조립하고 첫 토큰을 숨 쉬게 해본 개발자만이, 다음 AI 패러다임의 진짜 설계자가 될 것이다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=MiniMind+LLM+from+scratch+64M+PyTorch" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://www.modelscope.cn/studios/gongjy/MiniMind" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 온라인 웹 데모 체험
              </a>
              <a href="https://github.com/jingyaogong/minimind" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
