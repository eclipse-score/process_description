/* S-CORE Requirements Engineering Training Portal — Progress & Quiz Logic */

const MODULES = [
  { id: 'index',    label: 'Course Overview',                    url: 'index.html' },
  { id: 'module-1', label: 'Why Requirements Engineering?',      url: 'module-1.html' },
  { id: 'module-2', label: 'Requirement Levels and Types',       url: 'module-2.html' },
  { id: 'module-3', label: 'Requirement Attributes and Quality', url: 'module-3.html' },
  { id: 'module-4', label: 'Workflows and Work Products',        url: 'module-4.html' },
  { id: 'quiz-1',   label: 'Checkpoint Quiz',                    url: 'quiz-1.html', isQuiz: true },
];

function getProgress() {
  const raw = localStorage.getItem('score-re-progress');
  return raw ? JSON.parse(raw) : {};
}
function markComplete(id) {
  const p = getProgress(); p[id] = true; localStorage.setItem('score-re-progress', JSON.stringify(p));
  updateProgressBar();
}
function isComplete(id) { return !!getProgress()[id]; }

function updateProgressBar() {
  const p = getProgress();
  const total = MODULES.filter(m => m.id !== 'index').length;
  const done  = MODULES.filter(m => m.id !== 'index' && p[m.id]).length;
  const pct   = Math.round((done / total) * 100);
  document.querySelectorAll('.progress-bar-inner').forEach(el => el.style.width = pct + '%');
  document.querySelectorAll('.progress-pct').forEach(el => el.textContent = pct + '%');
  document.querySelectorAll('.progress-count').forEach(el => el.textContent = done + ' / ' + total + ' complete');
  MODULES.forEach(m => {
    const a = document.querySelector(`#sidebar nav a[data-id="${m.id}"]`);
    if (!a) return;
    const icon = a.querySelector('.nav-icon');
    if (p[m.id]) { a.classList.add('completed'); icon.textContent = '✓'; }
  });
}

function buildSidebar(activeId) {
  const p = getProgress();
  const sb = document.getElementById('sidebar');
  if (!sb) return;

  const total = MODULES.filter(m => m.id !== 'index').length;
  const done  = MODULES.filter(m => m.id !== 'index' && p[m.id]).length;
  const pct   = Math.round((done / total) * 100);

  const modules = MODULES.filter(m => m.id !== 'index');
  const navGroup = (label, items, startIdx) => `
    <div class="nav-section-label">${label}</div>
    <nav>
      ${items.map((m, i) => {
        const done_m = p[m.id];
        const active = m.id === activeId;
        const num = m.isQuiz ? '?' : (startIdx + i);
        return `<a href="${m.url}" class="${active ? 'active' : ''} ${done_m ? 'completed' : ''}" data-id="${m.id}">
          <span class="nav-icon">${done_m ? '✓' : num}</span>
          <span>${m.label}</span>
        </a>`;
      }).join('')}
    </nav>
  `;

  sb.innerHTML = `
    <div class="brand">
      <h1>S-CORE<br>Requirements<br>Engineering</h1>
      <p>Eclipse Foundation</p>
    </div>
    <div class="progress-area">
      <div class="progress-label">
        <span class="progress-count">${done} / ${total} complete</span>
        <span class="progress-pct">${pct}%</span>
      </div>
      <div class="progress-bar-outer"><div class="progress-bar-inner" style="width:${pct}%"></div></div>
    </div>
    <a href="index.html" style="display:flex;align-items:center;gap:10px;padding:10px 20px;text-decoration:none;color:#c8d6e5;font-size:.84rem;border-left:3px solid transparent;" data-id="index">
      <span class="nav-icon">⌂</span><span>Course Overview</span>
    </a>
    <hr class="nav-sep">
    ${navGroup('Modules', modules, 1)}
  `;
}

/* ── Collapsible Sections ─────────────────────── */
function initCollapsibles() {
  document.querySelectorAll('.collapsible-header').forEach(header => {
    header.addEventListener('click', () => {
      header.classList.toggle('open');
      const body = header.nextElementSibling;
      body.classList.toggle('open');
    });
  });
}

/* ── Quiz Engine ──────────────────────────────── */
function initQuiz(quizId, passMark, onPass) {
  const form = document.getElementById(quizId);
  if (!form) return;

  const submitBtn = form.querySelector('.quiz-submit');
  const resultEl  = form.querySelector('.quiz-result');

  form.querySelectorAll('.options li').forEach(opt => {
    opt.addEventListener('click', () => {
      const questionBlock = opt.closest('.question-block');
      if (questionBlock.dataset.answered) return;
      questionBlock.querySelectorAll('.options li').forEach(o => o.classList.remove('selected'));
      opt.classList.add('selected');
    });
  });

  if (submitBtn) {
    submitBtn.addEventListener('click', () => {
      let correct = 0;
      let total   = 0;
      let unanswered = false;

      form.querySelectorAll('.question-block').forEach(qb => {
        total++;
        const selected = qb.querySelector('.options li.selected');
        if (!selected) { unanswered = true; return; }
        qb.dataset.answered = '1';
        const isCorrect = selected.dataset.correct === 'true';
        if (isCorrect) {
          correct++;
          selected.classList.replace('selected', 'correct');
        } else {
          selected.classList.replace('selected', 'wrong');
          qb.querySelectorAll('.options li').forEach(o => {
            if (o.dataset.correct === 'true') o.classList.add('reveal-correct');
          });
        }
        const fb = qb.querySelector('.feedback');
        if (fb) {
          fb.style.display = 'block';
          fb.classList.add(isCorrect ? 'correct-fb' : 'wrong-fb');
        }
      });

      if (unanswered) { alert('Please answer all questions before submitting.'); return; }

      submitBtn.disabled = true;
      const pct = Math.round((correct / total) * 100);
      resultEl.style.display = 'block';
      if (pct >= passMark) {
        resultEl.className = 'quiz-result pass';
        resultEl.innerHTML = `✓ Passed! You scored ${correct}/${total} (${pct}%). ${onPass ? 'Module marked as complete.' : ''}`;
        if (onPass) { markComplete(onPass); }
      } else {
        resultEl.className = 'quiz-result fail';
        resultEl.innerHTML = `✗ Score: ${correct}/${total} (${pct}%). Pass mark is ${passMark}%. Review the sections above and try again.`;
      }
    });
  }
}

/* ── Auto-mark module visited ─────────────────── */
function autoMarkVisited(id) {
  if (id && id !== 'index' && !id.startsWith('quiz')) {
    markComplete(id);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const pageId = document.body.dataset.page;
  autoMarkVisited(pageId);
  buildSidebar(pageId);
  initCollapsibles();
});
