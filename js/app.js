/**
 * TOEIC WRITING TASK 01 - INTERACTIVE APPLICATION CONTROLLER
 * Presented by Miss Nguyet - TOEIC 2026
 */

// Application State
const state = {
    currentTab: 'home',
    currentChapterId: 1,
    currentTestId: 1,
    studentName: localStorage.getItem('toeic_student_name') || 'Học Viên',
    theme: localStorage.getItem('toeic_writing_theme') || 'dark', // Dark mode default as flagship
    unscrambleIndex: 0,
    unscrambleWordsSelected: [],
    unscrambleScore: 0,
    exam: {
        active: false,
        testId: 1,
        currentQuestionIndex: 0,
        answers: ["", "", "", "", ""],
        timeLeft: 480, // 8 minutes = 480 seconds
        timerInterval: null
    }
};

// DOM Ready Initialization
document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initProfile();
    initNavigation();
    renderView('home');
});

// Theme Toggle (Default Dark Galaxy Theme)
function initTheme() {
    if (state.theme === 'light') {
        document.body.classList.add('light-theme');
        updateThemeBtnText('BẬT ĐÈN', 'fa-sun');
    } else {
        document.body.classList.remove('light-theme');
        updateThemeBtnText('TẮT ĐÈN', 'fa-moon');
    }

    const themeToggleBtn = document.getElementById('themeToggleBtn');
    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', toggleTheme);
    }
}

function toggleTheme() {
    document.body.classList.toggle('light-theme');
    const isLight = document.body.classList.contains('light-theme');
    state.theme = isLight ? 'light' : 'dark';
    localStorage.setItem('toeic_writing_theme', state.theme);
    updateThemeBtnText(isLight ? 'BẬT ĐÈN' : 'TẮT ĐÈN', isLight ? 'fa-sun' : 'fa-moon');
}

function updateThemeBtnText(text, iconClass) {
    const themeIcon = document.getElementById('themeIcon');
    const themeText = document.getElementById('themeText');
    if (themeIcon) themeIcon.className = `fa-solid ${iconClass}`;
    if (themeText) themeText.textContent = text;
}

// Student Profile
function initProfile() {
    const studentNameEl = document.getElementById('sidebarStudentName');
    const avatarEl = document.getElementById('profileAvatar');
    if (studentNameEl) studentNameEl.textContent = state.studentName;
    if (avatarEl) avatarEl.textContent = state.studentName.charAt(0).toUpperCase() || 'H';

    const changeNameBtn = document.getElementById('changeNameBtn');
    if (changeNameBtn) {
        changeNameBtn.addEventListener('click', () => {
            const newName = prompt('Nhập tên của bạn để lưu tiến độ học tập:', state.studentName);
            if (newName && newName.trim()) {
                state.studentName = newName.trim();
                localStorage.setItem('toeic_student_name', state.studentName);
                if (studentNameEl) studentNameEl.textContent = state.studentName;
                if (avatarEl) avatarEl.textContent = state.studentName.charAt(0).toUpperCase();
            }
        });
    }
}

// Navigation & Sidebar
function initNavigation() {
    const sidebar = document.getElementById('sidebar');
    const menuToggleBtn = document.getElementById('menuToggleBtn');
    const toggleSidebarBtn = document.getElementById('toggleSidebarBtn');
    const toggleIcon = document.getElementById('toggleIcon');

    if (menuToggleBtn && sidebar) {
        menuToggleBtn.addEventListener('click', () => {
            sidebar.classList.toggle('open');
        });
    }

    if (toggleSidebarBtn && sidebar) {
        toggleSidebarBtn.addEventListener('click', () => {
            sidebar.classList.toggle('collapsed');
            if (toggleIcon) {
                toggleIcon.className = sidebar.classList.contains('collapsed') 
                    ? 'fa-solid fa-angles-right' 
                    : 'fa-solid fa-angles-left';
            }
        });
    }

    // Sidebar items click
    document.querySelectorAll('.nav-item, .submenu-item').forEach(item => {
        item.addEventListener('click', (e) => {
            if (item.classList.contains('locked-item') || item.getAttribute('data-locked') === 'true') {
                e.preventDefault();
                e.stopPropagation();
                const title = item.getAttribute('data-title') || 'Chuyên mục này';
                showLockedAlert(title);
                return;
            }

            const navTarget = item.getAttribute('data-nav');
            const chapterId = item.getAttribute('data-chapter');
            const testId = item.getAttribute('data-test');

            // Remove active classes
            document.querySelectorAll('.nav-item, .submenu-item').forEach(el => el.classList.remove('active'));
            item.classList.add('active');

            if (navTarget === 'home') {
                renderView('home');
            } else if (navTarget === 'overview') {
                renderView('overview');
            } else if (navTarget === 'unscramble') {
                renderView('unscramble');
            } else if (navTarget === 'upgrader') {
                renderView('upgrader');
            } else if (chapterId) {
                state.currentChapterId = parseInt(chapterId);
                renderView('chapter', state.currentChapterId);
            } else if (testId) {
                state.currentTestId = parseInt(testId);
                renderView('test', state.currentTestId);
            }

            if (window.innerWidth <= 1024 && sidebar) {
                sidebar.classList.remove('open');
            }
        });
    });
}

// Toast notification for locked sections
function showLockedAlert(title = 'Chuyên mục này') {
    showToast(`🔒 ${title} hiện đang tạm khoá. Hiện tại hệ thống chỉ mở học tập tại CHỦ ĐIỂM 01!`, 'warning');
}

function showToast(message, type = 'warning') {
    let container = document.getElementById('appToastContainer');
    if (!container) {
        container = document.createElement('div');
        container.id = 'appToastContainer';
        container.className = 'app-toast-container';
        document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = `app-toast ${type}`;
    toast.innerHTML = `
        <i class="fa-solid fa-lock" style="color: #f59e0b; font-size: 1.15rem; flex-shrink: 0;"></i>
        <div style="flex: 1; font-size: 0.95rem; line-height: 1.5; color: #fff;">${message}</div>
    `;

    container.appendChild(toast);

    setTimeout(() => {
        toast.classList.add('fade-out');
        setTimeout(() => {
            if (toast.parentNode) toast.parentNode.removeChild(toast);
        }, 300);
    }, 3200);
}

// Main View Router
function renderView(viewName, param = null) {
    const contentArea = document.getElementById('mainContentArea');
    if (!contentArea) return;

    // Check if view is locked (only home, overview, and chapter 1 are open)
    if (viewName === 'chapter' && param !== 1) {
        showLockedAlert(`Chủ điểm 0${param}`);
        return;
    }
    if (viewName === 'unscramble' || viewName === 'upgrader' || viewName === 'test') {
        showLockedAlert(viewName === 'test' ? 'Phòng thi thực chiến' : 'Phần luyện tập tương tác');
        return;
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });

    if (viewName === 'home') {
        contentArea.innerHTML = getHomeHTML();
    } else if (viewName === 'overview') {
        contentArea.innerHTML = getOverviewHTML();
    } else if (viewName === 'chapter') {
        state.activeLessonId = null; // Only show cards initially!
        const chapter = GRAMMAR_CHAPTERS.find(c => c.id === param) || GRAMMAR_CHAPTERS[0];
        contentArea.innerHTML = getChapterHTML(chapter);
    } else if (viewName === 'unscramble') {
        contentArea.innerHTML = getUnscrambleHTML();
        initUnscrambleGame();
    } else if (viewName === 'upgrader') {
        contentArea.innerHTML = getUpgraderHTML();
    } else if (viewName === 'test') {
        const test = ETS_MOCK_TESTS.find(t => t.testId === param) || ETS_MOCK_TESTS[0];
        contentArea.innerHTML = getTestSimulatorHTML(test);
        initTestSimulator(test);
    }
}

// ==========================================
// 1. HOME VIEW
// ==========================================
function getHomeHTML() {
    return `
        <div class="glass-panel welcome-card" style="padding: 40px; margin-bottom: 30px;">
            <div class="welcome-hero">
                <div class="badge-tag ets-badge mb-2"><i class="fa-solid fa-sparkles"></i> TOEIC WRITING TASK 01 • ETS 2026</div>
                <h1 class="welcome-title" style="font-size: 2.2rem; font-family: var(--font-heading); margin-bottom: 12px;">TOEIC WRITING TASK 01</h1>
                <p class="welcome-subtitle" style="font-size: 1.05rem; line-height: 1.75; color: var(--text-secondary); max-width: 860px; margin-bottom: 24px;">
                    Chào mừng bạn đến với hệ thống học tập tương tác <strong>TOEIC WRITING TASK 01 (Write a Sentence Based on a Picture)</strong> cùng Miss Nguyệt.
                    Chương trình được biên soạn kỹ lưỡng kết hợp chuẩn khảo thí chính thức từ <strong>ETS & IIG Việt Nam</strong> giúp bạn nắm vững cấu trúc câu và bứt phá Band 3 tối đa!
                </p>
            </div>
            
            <div class="welcome-stats" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 26px 0;">
                <div class="stat-card" style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-color); border-radius: 16px; padding: 22px; text-align: center;">
                    <div class="stat-value" style="font-size: 2.2rem; font-weight: 800; color: var(--color-cyan); font-family: var(--font-heading);">06</div>
                    <div class="stat-label" style="font-size: 0.9rem; color: var(--text-muted); margin-top: 4px;">Chủ Điểm Trọng Tâm</div>
                </div>
            <div class="welcome-stats" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 26px 0;">
                <div class="stat-card" style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-color); border-radius: 16px; padding: 22px; text-align: center;">
                    <div class="stat-value" style="font-size: 2.2rem; font-weight: 800; color: var(--color-cyan); font-family: var(--font-heading);">01</div>
                    <div class="stat-label" style="font-size: 0.9rem; color: var(--text-muted); margin-top: 4px;">Chủ Điểm Đang Mở</div>
                </div>
                <div class="stat-card" style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-color); border-radius: 16px; padding: 22px; text-align: center;">
                    <div class="stat-value" style="font-size: 2.2rem; font-weight: 800; color: var(--color-purple); font-family: var(--font-heading);">05</div>
                    <div class="stat-label" style="font-size: 0.9rem; color: var(--text-muted); margin-top: 4px;">Bài Học Chuyên Sâu (S, V, O, C, M)</div>
                </div>
                <div class="stat-card" style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-color); border-radius: 16px; padding: 22px; text-align: center;">
                    <div class="stat-value" style="font-size: 2.2rem; font-weight: 800; color: var(--color-success); font-family: var(--font-heading);">50</div>
                    <div class="stat-label" style="font-size: 0.9rem; color: var(--text-muted); margin-top: 4px;">Tranh Thực Hành Sắc Nét</div>
                </div>
                <div class="stat-card" style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-color); border-radius: 16px; padding: 22px; text-align: center;">
                    <div class="stat-value" style="font-size: 2.2rem; font-weight: 800; color: var(--color-gold); font-family: var(--font-heading);">150</div>
                    <div class="stat-label" style="font-size: 0.9rem; color: var(--text-muted); margin-top: 4px;">Câu Mẫu Chuẩn Score 3</div>
                </div>
            </div>
            
            <div class="cta-group" style="display: flex; gap: 14px; flex-wrap: wrap; margin-top: 20px;">
                <button class="btn btn-primary" onclick="renderView('overview')" style="background: linear-gradient(135deg, var(--color-cyan), var(--color-purple)); color: white; border: none; padding: 13px 28px; border-radius: 12px; font-weight: 700; cursor: pointer; display: inline-flex; align-items: center; gap: 8px;">
                    <i class="fa-solid fa-landmark"></i> TỔNG QUAN IIG / ETS
                </button>
                <button class="btn btn-secondary" onclick="renderView('chapter', 1)" style="background: rgba(0, 242, 254, 0.15); color: var(--color-cyan); border: 1px solid var(--color-cyan); padding: 13px 26px; border-radius: 12px; font-weight: 700; cursor: pointer; display: inline-flex; align-items: center; gap: 8px; box-shadow: 0 0 20px rgba(0, 242, 254, 0.2);">
                    <i class="fa-solid fa-graduation-cap"></i> BẮT ĐẦU HỌC CHỦ ĐIỂM 01
                </button>
            </div>
        </div>

        <h2 style="font-size: 1.55rem; margin-bottom: 20px; color: var(--text-primary); font-family: var(--font-heading);">
            <i class="fa-solid fa-compass" style="color: var(--color-cyan);"></i> Khám Phá Các Chuyên Mục
        </h2>

        <div class="patterns-grid" style="grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 20px;">
            <div class="pattern-card highlight-card" onclick="renderView('overview')" style="cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <div class="pattern-num">TỔNG QUAN</div>
                    <span class="badge-tag" style="background: rgba(2, 132, 199, 0.15); color: #0284c7; font-weight: 800; font-size: 0.75rem;"><i class="fa-solid fa-circle-check"></i> ĐANG MỞ</span>
                </div>
                <div class="pattern-formula" style="font-size: 1.25rem;">Tổng Quan Bài Thi & Task 01</div>
                <div class="pattern-desc">Cấu trúc bài thi TOEIC Writing, thang điểm 0-3 điểm/câu, tiêu chí giám khảo và ví dụ đề thi thực tế.</div>
            </div>

            <div class="pattern-card highlight-card" onclick="renderView('chapter', 1)" style="cursor: pointer; border-color: var(--color-cyan); box-shadow: 0 0 25px rgba(0, 242, 254, 0.12);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <div class="pattern-num" style="color: var(--color-cyan);">CHỦ ĐIỂM 01</div>
                    <span class="badge-tag" style="background: rgba(16, 185, 129, 0.18); color: #10b981; font-weight: 800; font-size: 0.75rem;"><i class="fa-solid fa-circle-check"></i> ĐANG MỞ</span>
                </div>
                <div class="pattern-formula" style="font-size: 1.25rem; color: var(--color-cyan);">Thành Phần Câu Cơ Bản</div>
                <div class="pattern-desc">5 bài học chuyên sâu: Chủ ngữ (S), Động từ (V), Tân ngữ (O), Bổ ngữ (C), Trạng ngữ (M) kèm 50 tranh thực hành và 150 câu mẫu.</div>
            </div>

            <div class="pattern-card locked-card" onclick="showLockedAlert('Chủ điểm 02: Cấu trúc mô tả tranh cơ bản')" style="cursor: not-allowed;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <div class="pattern-num" style="color: var(--text-muted);">CHỦ ĐIỂM 02</div>
                    <span class="badge-tag" style="background: rgba(239, 68, 68, 0.12); color: #ef4444; font-weight: 700; font-size: 0.75rem;"><i class="fa-solid fa-lock"></i> TẠM KHOÁ</span>
                </div>
                <div class="pattern-formula" style="font-size: 1.25rem; color: var(--text-muted);">Cấu Trúc Mô Tả Tranh Cơ Bản</div>
                <div class="pattern-desc" style="color: var(--text-muted);">Tranh tả người, Tranh tả vật & các cấu trúc chủ đạo (Nội dung đang hoàn thiện).</div>
            </div>

            <div class="pattern-card locked-card" onclick="showLockedAlert('Chủ điểm 03: Cấu trúc mô tả tranh nâng cao')" style="cursor: not-allowed;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <div class="pattern-num" style="color: var(--text-muted);">CHỦ ĐIỂM 03</div>
                    <span class="badge-tag" style="background: rgba(239, 68, 68, 0.12); color: #ef4444; font-weight: 700; font-size: 0.75rem;"><i class="fa-solid fa-lock"></i> TẠM KHOÁ</span>
                </div>
                <div class="pattern-formula" style="font-size: 1.25rem; color: var(--text-muted);">Cấu Trúc Mô Tả Tranh Nâng Cao</div>
                <div class="pattern-desc" style="color: var(--text-muted);">Kỹ thuật nâng cấp Band 3, ghép câu phức & 5 cạm bẫy cấm kỵ (Nội dung đang hoàn thiện).</div>
            </div>

            <div class="pattern-card locked-card" onclick="showLockedAlert('Game Sắp Xếp Câu (Unscramble)')" style="cursor: not-allowed;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <div class="pattern-num" style="color: var(--text-muted);">LUYỆN TẬP</div>
                    <span class="badge-tag" style="background: rgba(239, 68, 68, 0.12); color: #ef4444; font-weight: 700; font-size: 0.75rem;"><i class="fa-solid fa-lock"></i> TẠM KHOÁ</span>
                </div>
                <div class="pattern-formula" style="font-size: 1.25rem; color: var(--text-muted);">Game Sắp Xếp Câu & Nâng Cấp</div>
                <div class="pattern-desc" style="color: var(--text-muted);">Rèn luyện phản xạ ngữ pháp và nâng cấp câu Band 3 (Nội dung đang hoàn thiện).</div>
            </div>

            <div class="pattern-card locked-card" onclick="showLockedAlert('Phòng thi thực chiến')" style="cursor: not-allowed;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <div class="pattern-num" style="color: var(--text-muted);">THỰC CHIẾN</div>
                    <span class="badge-tag" style="background: rgba(239, 68, 68, 0.12); color: #ef4444; font-weight: 700; font-size: 0.75rem;"><i class="fa-solid fa-lock"></i> TẠM KHOÁ</span>
                </div>
                <div class="pattern-formula" style="font-size: 1.25rem; color: var(--text-muted);">ETS Test 01 - 05 (8:00 Phút)</div>
                <div class="pattern-desc" style="color: var(--text-muted);">Phòng thi thực tế với đồng hồ 8 phút và chấm điểm tự động (Nội dung đang hoàn thiện).</div>
            </div>
        </div>
    `;
}

// ==========================================
// 2. OVERVIEW VIEW
// ==========================================
function getOverviewHTML() {
    let sectionsHTML = OVERVIEW_DATA.sections.map(sec => `
        <div class="glass-panel mb-4" style="padding: 36px 40px; margin-bottom: 26px;">
            <div class="overview-header" style="display: flex; align-items: center; gap: 14px; margin-bottom: 20px;">
                <i class="${sec.icon}" style="font-size: 1.5rem; color: var(--color-cyan);"></i>
                <h2 style="font-family: var(--font-heading); font-size: 1.6rem; color: var(--text-primary);">${sec.title}</h2>
            </div>
            ${sec.content}
        </div>
    `).join('');

    return `
        <div class="overview-container">
            <div class="glass-panel mb-4" style="padding: 36px 40px; margin-bottom: 26px;">
                <div class="badge-tag ets-badge mb-2"><i class="fa-solid fa-award"></i> TỔNG QUAN KHẢO THÍ CHÍNH THỨC</div>
                <h1 style="font-family: var(--font-heading); font-size: 2.1rem; color: var(--text-primary); margin-bottom: 10px;">TOEIC WRITING TASK 01 (ETS & IIG)</h1>
                <p style="font-size: 1.05rem; line-height: 1.75; color: var(--text-secondary); margin-bottom: 0;">Nắm chắc toàn bộ quy cách đề thi, thang điểm chấm 0 - 3 điểm/câu, 3 tiêu chí cốt lõi và chiến lược quản lý 8:00 phút làm bài đỉnh cao.</p>
            </div>
            ${sectionsHTML}
        </div>
    `;
}

// ==========================================
// 3. GRAMMAR CHAPTER VIEW WITH INTERACTIVE COMPONENT TABS
// ==========================================
const COMPONENT_TABS_META = {
    // Chủ điểm 01: Thành phần câu cơ bản (Exact Match to User Mockup)
    "1-1": { title: "CHỦ NGỮ", subtitle: "(SUBJECT)", icon: "fa-solid fa-user", theme: "tab-theme-subject" },
    "1-2": { title: "ĐỘNG TỪ", subtitle: "(VERB)", icon: "fa-solid fa-bolt", theme: "tab-theme-verb" },
    "1-3": { title: "TÂN NGỮ", subtitle: "(OBJECT)", icon: "fa-solid fa-bullseye", theme: "tab-theme-object" },
    "1-4": { title: "BỔ NGỮ", subtitle: "(COMPLEMENT)", icon: "fa-solid fa-wand-magic-sparkles", theme: "tab-theme-complement" },
    "1-5": { title: "TRẠNG NGỮ", subtitle: "(ADVERB)", icon: "fa-solid fa-stopwatch", theme: "tab-theme-modifier" },

    // Chủ điểm 02: Cấu trúc mô tả tranh cơ bản
    "2-1": { title: "TRANH TẢ NGƯỜI", subtitle: "(PEOPLE)", icon: "fa-solid fa-person-walking", theme: "tab-theme-subject" },
    "2-2": { title: "TRANH TẢ VẬT", subtitle: "(OBJECTS & SCENES)", icon: "fa-solid fa-cube", theme: "tab-theme-object" },

    // Chủ điểm 03: Cấu trúc mô tả tranh nâng cao
    "3-1": { title: "NÂNG CẤP S - V - O", subtitle: "(LEVEL 8 - 9)", icon: "fa-solid fa-rocket", theme: "tab-theme-subject" },
    "3-2": { title: "CÂU PHỨC LIÊN TỪ", subtitle: "(WHEN / BECAUSE)", icon: "fa-solid fa-diagram-project", theme: "tab-theme-verb" },
    "3-3": { title: "CHECKLIST BẪY ETS", subtitle: "(DOS & DON'TS)", icon: "fa-solid fa-shield-halved", theme: "tab-theme-modifier" }
};

function getChapterHTML(chapter) {
    const isFiveItems = chapter.lessons.length === 5;
    const gridClass = isFiveItems ? 'component-tabs-grid component-tabs-grid-5' : 'component-tabs-grid';

    let tabsHTML = `
        <div class="${gridClass}">
            ${chapter.lessons.map(lesson => {
                const meta = COMPONENT_TABS_META[lesson.lessonId] || { 
                    title: lesson.title, 
                    subtitle: '', 
                    icon: 'fa-solid fa-bookmark', 
                    theme: 'tab-theme-subject' 
                };
                const isActive = lesson.lessonId === state.activeLessonId ? 'active' : '';
                return `
                    <div class="component-tab-card ${meta.theme} ${isActive}" onclick="toggleLessonView('${lesson.lessonId}')">
                        <div class="tab-icon-circle">
                            <i class="${meta.icon}"></i>
                        </div>
                        <div class="tab-title-group">
                            <div class="tab-title">${meta.title}</div>
                            <div class="tab-subtitle">${meta.subtitle}</div>
                        </div>
                    </div>
                `;
            }).join('')}
        </div>
    `;

    let lessonsHTML = chapter.lessons.map(lesson => {
        let lessonContentHTML = '';
        if (lesson.sections && lesson.sections.length > 0) {
            const subTabsHTML = `
                <div class="sub-tabs-container" id="subtabs-${lesson.lessonId}">
                    ${lesson.sections.map((sec, sIdx) => `
                        <button class="sub-tab-btn ${sIdx === 0 ? 'active' : ''}" data-lesson="${lesson.lessonId}" data-key="${sec.key}" onclick="switchSubSection('${lesson.lessonId}', '${sec.key}')">
                            <i class="${sec.icon || 'fa-solid fa-book'}"></i> ${sec.tabTitle || sec.title}
                        </button>
                    `).join('')}
                </div>
            `;
            const subPanesHTML = lesson.sections.map((sec, sIdx) => `
                <div id="subpane-${lesson.lessonId}-${sec.key}" class="sub-section-pane ${sIdx === 0 ? 'active' : ''}">
                    ${sec.content}
                </div>
            `).join('');

            lessonContentHTML = `
                <div class="lesson-inner-container">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; padding-bottom: 14px; border-bottom: 1px dashed var(--border-color);">
                        <div style="font-family: var(--font-heading); font-size: 1.45rem; font-weight: 800; color: var(--color-cyan);">
                            <i class="fa-solid fa-book-open-reader"></i> ${lesson.title}
                        </div>
                        <button class="btn-back-to-hub" onclick="closeLessonView()"><i class="fa-solid fa-angles-up"></i> Thu gọn</button>
                    </div>
                    ${subTabsHTML}
                    <div class="sub-panes-container">
                        ${subPanesHTML}
                    </div>
                </div>
            `;
        } else {
            lessonContentHTML = `
                <div class="lesson-section mb-4">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; padding-bottom: 14px; border-bottom: 1px dashed var(--border-color);">
                        <div style="font-family: var(--font-heading); font-size: 1.45rem; font-weight: 800; color: var(--color-cyan);">
                            <i class="fa-solid fa-book-open-reader"></i> ${lesson.title}
                        </div>
                        <button class="btn-back-to-hub" onclick="closeLessonView()"><i class="fa-solid fa-angles-up"></i> Thu gọn</button>
                    </div>
                    ${lesson.content || ''}
                </div>
            `;
        }

        return `
            <div id="pane-${lesson.lessonId}" class="lesson-pane ${lesson.lessonId === state.activeLessonId ? 'active' : ''}">
                ${lessonContentHTML}
            </div>
        `;
    }).join('');

    return `
        <div class="glass-panel" style="padding: 40px; margin-bottom: 30px;">
            <div class="badge-tag ets-badge mb-2">${chapter.badge}</div>
            <h1 style="font-family: var(--font-heading); font-size: 2rem; margin-bottom: 24px; color: var(--text-primary);">${chapter.title}</h1>
            <hr style="border: none; border-top: 1px solid var(--border-color); margin-bottom: 24px;">
            ${tabsHTML}
            <div id="lessonPanesContainer">
                ${lessonsHTML}
            </div>
        </div>
    `;
}

window.toggleLessonView = function(lessonId) {
    if (state.activeLessonId === lessonId) {
        closeLessonView();
    } else {
        switchLesson(lessonId);
    }
};

window.closeLessonView = function() {
    state.activeLessonId = null;
    document.querySelectorAll('.component-tab-card').forEach(card => {
        card.classList.remove('active');
    });
    document.querySelectorAll('.lesson-pane').forEach(pane => {
        pane.classList.remove('active');
    });
};

window.switchLesson = function(lessonId) {
    state.activeLessonId = lessonId;
    
    // Update active tab card
    document.querySelectorAll('.component-tab-card').forEach(card => {
        card.classList.remove('active');
    });
    
    // Find the matching card
    const targetCard = Array.from(document.querySelectorAll('.component-tab-card')).find(c => {
        return c.getAttribute('onclick') && c.getAttribute('onclick').includes(lessonId);
    });
    if (targetCard) targetCard.classList.add('active');

    // Update active pane
    document.querySelectorAll('.lesson-pane').forEach(pane => {
        pane.classList.remove('active');
    });
    const targetPane = document.getElementById(`pane-${lessonId}`);
    if (targetPane) {
        targetPane.classList.add('active');
        // Smoothly scroll to the opened lesson
        setTimeout(() => {
            targetPane.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 100);
    }
};

window.switchSubSection = function(lessonId, key) {
    // Update subtab buttons
    const subtabsContainer = document.getElementById(`subtabs-${lessonId}`);
    if (subtabsContainer) {
        subtabsContainer.querySelectorAll('.sub-tab-btn').forEach(btn => {
            btn.classList.remove('active');
            if (btn.getAttribute('data-key') === key) {
                btn.classList.add('active');
            }
        });
    }

    // Update subpanes
    const lessonPane = document.getElementById(`pane-${lessonId}`);
    if (lessonPane) {
        lessonPane.querySelectorAll('.sub-section-pane').forEach(pane => {
            pane.classList.remove('active');
        });
        const targetSubpane = document.getElementById(`subpane-${lessonId}-${key}`);
        if (targetSubpane) {
            targetSubpane.classList.add('active');
        }
    }
};

// ==========================================
// 4. UNSCRAMBLE GAME ENGINE
// ==========================================
function getUnscrambleHTML() {
    return `
        <div class="game-container">
            <div class="game-header">
                <div class="game-title"><i class="fa-solid fa-puzzle-piece" style="color: var(--color-cyan);"></i> Sắp Xếp Câu Chuẩn Trật Tự (S - V - O)</div>
                <div class="game-progress-badge" id="unscrambleProgress">Câu 1 / ${UNSCRAMBLE_EXERCISES.length}</div>
            </div>

            <div class="vietnamese-hint-box">
                <i class="fa-solid fa-lightbulb" style="color: var(--color-gold);"></i>
                <div><strong>Nghĩa tiếng Việt gợi ý:</strong> <span id="unscrambleVietnamese"></span></div>
            </div>

            <p style="font-size: 0.95rem; font-weight: 700; color: var(--text-muted); margin-bottom: 10px;">Nhấp vào các từ để ghép thành câu hoàn chỉnh:</p>
            <div class="word-drop-area" id="wordDropArea">
                <span style="color: var(--text-muted); font-size: 1rem;" id="dropPlaceholder">Nhấp từ ở bên dưới để đưa vào đây...</span>
            </div>

            <p style="font-size: 0.95rem; font-weight: 700; color: var(--text-muted); margin-bottom: 10px;">Ngân hàng từ:</p>
            <div class="word-pool-area" id="wordPoolArea"></div>

            <div class="game-controls">
                <button class="btn btn-secondary" id="unscrambleResetBtn" style="background: rgba(255, 255, 255, 0.06); color: var(--text-primary); border: 1px solid var(--border-color); padding: 11px 22px; border-radius: 12px; font-weight: 700; cursor: pointer;"><i class="fa-solid fa-arrow-rotate-left"></i> Làm lại</button>
                <button class="btn btn-primary" id="unscrambleCheckBtn" style="background: linear-gradient(135deg, var(--color-cyan), var(--color-purple)); color: white; border: none; padding: 11px 24px; border-radius: 12px; font-weight: 700; cursor: pointer;"><i class="fa-solid fa-check"></i> Kiểm tra</button>
                <button class="btn btn-primary" id="unscrambleNextBtn" style="display: none; background: linear-gradient(135deg, var(--color-success), var(--color-cyan)); color: white; border: none; padding: 11px 24px; border-radius: 12px; font-weight: 700; cursor: pointer;"><i class="fa-solid fa-forward"></i> Câu tiếp theo</button>
            </div>

            <div class="game-feedback-box" id="unscrambleFeedback"></div>
        </div>
    `;
}

function initUnscrambleGame() {
    loadUnscramblePuzzle(state.unscrambleIndex);

    document.getElementById('unscrambleResetBtn').addEventListener('click', () => {
        loadUnscramblePuzzle(state.unscrambleIndex);
    });

    document.getElementById('unscrambleCheckBtn').addEventListener('click', checkUnscrambleAnswer);
    document.getElementById('unscrambleNextBtn').addEventListener('click', () => {
        state.unscrambleIndex = (state.unscrambleIndex + 1) % UNSCRAMBLE_EXERCISES.length;
        loadUnscramblePuzzle(state.unscrambleIndex);
    });
}

function loadUnscramblePuzzle(index) {
    const puzzle = UNSCRAMBLE_EXERCISES[index];
    state.unscrambleWordsSelected = [];

    document.getElementById('unscrambleProgress').textContent = `Câu ${index + 1} / ${UNSCRAMBLE_EXERCISES.length}`;
    document.getElementById('unscrambleVietnamese').textContent = puzzle.vietnameseHint;
    document.getElementById('unscrambleFeedback').style.display = 'none';
    document.getElementById('unscrambleCheckBtn').style.display = 'inline-flex';
    document.getElementById('unscrambleNextBtn').style.display = 'none';

    renderUnscrambleAreas(puzzle);
}

function renderUnscrambleAreas(puzzle) {
    const dropArea = document.getElementById('wordDropArea');
    const poolArea = document.getElementById('wordPoolArea');

    dropArea.innerHTML = '';
    poolArea.innerHTML = '';

    if (state.unscrambleWordsSelected.length === 0) {
        dropArea.innerHTML = '<span style="color: var(--text-muted); font-size: 1rem;" id="dropPlaceholder">Nhấp từ ở bên dưới để đưa vào đây...</span>';
    } else {
        state.unscrambleWordsSelected.forEach((word, idx) => {
            const chip = document.createElement('div');
            chip.className = 'word-chip in-drop-area';
            chip.textContent = word;
            chip.addEventListener('click', () => {
                state.unscrambleWordsSelected.splice(idx, 1);
                renderUnscrambleAreas(puzzle);
            });
            dropArea.appendChild(chip);
        });
    }

    // Unselected words
    const remainingWords = [...puzzle.words];
    state.unscrambleWordsSelected.forEach(selectedWord => {
        const foundIdx = remainingWords.indexOf(selectedWord);
        if (foundIdx > -1) remainingWords.splice(foundIdx, 1);
    });

    remainingWords.forEach(word => {
        const chip = document.createElement('div');
        chip.className = 'word-chip';
        chip.textContent = word;
        chip.addEventListener('click', () => {
            state.unscrambleWordsSelected.push(word);
            renderUnscrambleAreas(puzzle);
        });
        poolArea.appendChild(chip);
    });
}

function checkUnscrambleAnswer() {
    const puzzle = UNSCRAMBLE_EXERCISES[state.unscrambleIndex];
    const feedbackBox = document.getElementById('unscrambleFeedback');
    const isCorrect = state.unscrambleWordsSelected.join(' ') === puzzle.correctOrder.join(' ');

    feedbackBox.style.display = 'block';
    if (isCorrect) {
        feedbackBox.className = 'game-feedback-box correct';
        feedbackBox.innerHTML = `
            <div style="font-weight: 800; font-size: 1.15rem; color: var(--color-success); margin-bottom: 8px;">
                <i class="fa-solid fa-circle-check"></i> Chính xác tuyệt đối!
            </div>
            <p style="margin-bottom: 8px;"><strong>Giải thích ngữ pháp:</strong> ${puzzle.explanation}</p>
        `;
        document.getElementById('unscrambleCheckBtn').style.display = 'none';
        document.getElementById('unscrambleNextBtn').style.display = 'inline-flex';
        triggerConfetti();
    } else {
        feedbackBox.className = 'game-feedback-box wrong';
        feedbackBox.innerHTML = `
            <div style="font-weight: 800; font-size: 1.15rem; color: var(--color-error); margin-bottom: 8px;">
                <i class="fa-solid fa-circle-xmark"></i> Chưa chính xác!
            </div>
            <p>Hãy chú ý trật tự Chủ ngữ &rarr; Động từ &rarr; Tân ngữ hoặc vị trí của cụm giới từ.</p>
        `;
    }
}

// ==========================================
// 5. SENTENCE UPGRADER VIEW
// ==========================================
function getUpgraderHTML() {
    let challengesHTML = UPGRADER_CHALLENGES.map(ch => `
        <div class="glass-panel mb-4" style="padding: 36px 40px; margin-bottom: 26px;">
            <h2 style="font-size: 1.45rem; margin-bottom: 20px; color: var(--color-cyan); font-family: var(--font-heading);">
                <i class="fa-solid fa-arrow-up-right-dots"></i> ${ch.title}
            </h2>
            <div class="upgrade-case-study">
                <div class="img-preview-box">
                    <img src="${ch.image}" alt="${ch.imageAlt}" class="lesson-img">
                    <div class="ets-keyword-tags mt-3" style="margin-top: 14px;">
                        <span class="ets-keyword-tag">${ch.keywords[0]}</span>
                        <span class="ets-keyword-tag">${ch.keywords[1]}</span>
                    </div>
                </div>
                <div class="upgrade-steps">
                    <div class="step-card" style="border-left: 4px solid #ef4444;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span class="level-tag l1">${ch.levels.level1.band}</span>
                        </div>
                        <div style="font-size: 1.15rem; font-weight: 700; color: var(--text-primary); margin: 8px 0; font-family: var(--font-heading);">"${ch.levels.level1.sentence}"</div>
                        <p style="font-size: 0.95rem; color: var(--text-muted); margin-bottom: 0;">${ch.levels.level1.analysis}</p>
                    </div>

                    <div class="step-card" style="border-left: 4px solid var(--color-cyan);">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span class="level-tag l2">${ch.levels.level2.band}</span>
                        </div>
                        <div style="font-size: 1.15rem; font-weight: 700; color: var(--text-primary); margin: 8px 0; font-family: var(--font-heading);">"${ch.levels.level2.sentence}"</div>
                        <p style="font-size: 0.95rem; color: var(--text-muted); margin-bottom: 0;">${ch.levels.level2.analysis}</p>
                    </div>

                    <div class="step-card" style="border-left: 4px solid var(--color-success); background: rgba(16, 185, 129, 0.08);">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span class="level-tag l3">${ch.levels.level3.band}</span>
                        </div>
                        <div style="font-size: 1.25rem; font-weight: 800; color: var(--color-success); margin: 8px 0; font-family: var(--font-heading);">"${ch.levels.level3.sentence}"</div>
                        <p style="font-size: 0.98rem; color: var(--text-primary); margin-bottom: 0;">${ch.levels.level3.analysis}</p>
                    </div>
                </div>
            </div>
        </div>
    `).join('');

    return `
        <div class="upgrader-container">
            <div class="glass-panel mb-4" style="padding: 36px 40px; margin-bottom: 26px;">
                <div class="badge-tag ets-badge mb-2"><i class="fa-solid fa-chart-line"></i> THỬ THÁCH NÂNG CẤP CÂU</div>
                <h1 style="font-family: var(--font-heading); font-size: 2.1rem; color: var(--text-primary); margin-bottom: 10px;">Bí Quyết Chuyển Đổi Từ Band 1 Lên Band 3</h1>
                <p style="font-size: 1.05rem; line-height: 1.75; color: var(--text-secondary); margin-bottom: 0;">Học cách quan sát chi tiết bức tranh để thêm công cụ, vị trí, đặc điểm trực tiếp và đạt điểm số tối đa từ giám khảo ETS!</p>
            </div>
            ${challengesHTML}
        </div>
    `;
}

// ==========================================
// 6. ETS REAL SIMULATOR ENGINE (8:00 MINUTES)
// ==========================================
function getTestSimulatorHTML(test) {
    return `
        <div class="ets-simulator-container">
            <div class="ets-header-bar">
                <div class="ets-exam-title">
                    <i class="fa-solid fa-desktop" style="color: var(--color-cyan);"></i> ${test.title} (Questions 1 - 5)
                </div>
                <div class="ets-timer-box" id="etsTimerDisplay">
                    <i class="fa-solid fa-stopwatch"></i> 08:00
                </div>
            </div>

            <div class="ets-nav-tabs" id="etsQuestionTabs">
                ${test.questions.map((q, idx) => `
                    <button class="ets-tab-btn ${idx === 0 ? 'active' : ''}" data-qidx="${idx}">
                        Question ${idx + 1}
                    </button>
                `).join('')}
            </div>

            <div class="ets-body">
                <div class="ets-picture-column">
                    <div class="ets-img-wrapper">
                        <img id="etsCurrentImg" src="${test.questions[0].image}" alt="TOEIC Writing Question Picture" class="ets-img">
                    </div>
                    <div class="ets-keywords-box">
                        <div class="ets-keywords-title">Given Keywords (02 từ gợi ý):</div>
                        <div class="ets-keyword-tags" id="etsKeywordsList">
                            <span class="ets-keyword-tag">${test.questions[0].keywords[0]}</span>
                            <span class="ets-keyword-tag">${test.questions[0].keywords[1]}</span>
                        </div>
                    </div>
                </div>

                <div class="ets-writing-column">
                    <div class="ets-instruction-note">
                        <strong>Directions:</strong> Write ONE sentence based on the picture using the TWO words or phrases provided. You may change the forms of the words and you may use the words in any order.
                    </div>

                    <div class="ets-textarea-wrap">
                        <textarea id="etsAnswerInput" class="ets-textarea" placeholder="Type your sentence here... (e.g. The woman in a red uniform is scanning...)"></textarea>
                        <div class="ets-char-count" id="etsCharCount">0 words | 0 chars</div>
                    </div>

                    <div class="teacher-tip-box" style="margin-top: 0; padding: 14px 18px; font-size: 0.95rem;">
                        <i class="fa-solid fa-circle-exclamation"></i>
                        <div><strong>Quy định:</strong> Viết đúng 01 câu duy nhất, viết hoa chữ cái đầu và kết thúc bằng dấu chấm (<code>.</code>).</div>
                    </div>
                </div>
            </div>

            <div class="ets-footer-actions">
                <div>
                    <button class="btn btn-secondary" id="etsPrevBtn" style="visibility: hidden; background: rgba(255, 255, 255, 0.06); color: var(--text-primary); border: 1px solid var(--border-color); padding: 10px 20px; border-radius: 10px; font-weight: 700; cursor: pointer;"><i class="fa-solid fa-chevron-left"></i> Previous</button>
                </div>
                <div style="display: flex; gap: 12px;">
                    <button class="btn btn-secondary" id="etsNextBtn" style="background: rgba(255, 255, 255, 0.06); color: var(--text-primary); border: 1px solid var(--border-color); padding: 10px 20px; border-radius: 10px; font-weight: 700; cursor: pointer;">Next <i class="fa-solid fa-chevron-right"></i></button>
                    <button class="btn btn-primary" id="etsSubmitBtn" style="background: linear-gradient(135deg, var(--color-success), var(--color-cyan)); color: white; border: none; padding: 10px 24px; border-radius: 10px; font-weight: 700; cursor: pointer;"><i class="fa-solid fa-paper-plane"></i> Submit Test</button>
                </div>
            </div>
        </div>

        <!-- Results Modal -->
        <div class="results-modal" id="etsResultsModal">
            <div class="results-card">
                <div class="results-header">
                    <div class="badge-tag ets-badge mb-2">ETS WRITING SCORING REPORT</div>
                    <h2 style="font-family: var(--font-heading); font-size: 2.1rem; color: var(--text-primary); margin: 10px 0;">Báo Cáo Điểm Số & Đánh Giá Chi Tiết</h2>
                    <div class="score-summary-circle">
                        <div class="score-val" id="totalScoreVal">15</div>
                        <div class="score-label">/ 15 Điểm</div>
                    </div>
                    <p style="color: var(--text-muted); font-size: 1.05rem;">Đánh giá TOEIC Writing Task 1: <strong id="scaledBandScore" style="color: var(--color-cyan);">Band Tối Đa (Level 8-9)</strong></p>
                </div>
                <div id="resultsDetailList"></div>
                <div style="text-align: center; margin-top: 30px;">
                    <button class="btn btn-primary" id="closeResultsBtn" style="background: linear-gradient(135deg, var(--color-cyan), var(--color-purple)); color: white; border: none; padding: 12px 28px; border-radius: 12px; font-weight: 700; cursor: pointer;"><i class="fa-solid fa-check"></i> Đóng & Tiếp Tục Luyện Tập</button>
                </div>
            </div>
        </div>
    `;
}

function initTestSimulator(test) {
    state.exam.active = true;
    state.exam.testId = test.testId;
    state.exam.currentQuestionIndex = 0;
    state.exam.answers = ["", "", "", "", ""];
    state.exam.timeLeft = 480;

    if (state.exam.timerInterval) clearInterval(state.exam.timerInterval);

    // Timer Interval
    state.exam.timerInterval = setInterval(() => {
        if (state.exam.timeLeft > 0) {
            state.exam.timeLeft--;
            updateTimerDisplay();
        } else {
            clearInterval(state.exam.timerInterval);
            alert('Hết giờ làm bài 8:00 phút! Hệ thống đang tự động chấm điểm bài thi của bạn.');
            gradeAndShowResults(test);
        }
    }, 1000);

    updateTimerDisplay();
    loadQuestionView(test, 0);

    // Events
    const textarea = document.getElementById('etsAnswerInput');
    textarea.addEventListener('input', (e) => {
        state.exam.answers[state.exam.currentQuestionIndex] = e.target.value;
        updateCharCount(e.target.value);
        updateQuestionTabsStatus(test);
    });

    document.querySelectorAll('.ets-tab-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const idx = parseInt(btn.getAttribute('data-qidx'));
            loadQuestionView(test, idx);
        });
    });

    document.getElementById('etsPrevBtn').addEventListener('click', () => {
        if (state.exam.currentQuestionIndex > 0) {
            loadQuestionView(test, state.exam.currentQuestionIndex - 1);
        }
    });

    document.getElementById('etsNextBtn').addEventListener('click', () => {
        if (state.exam.currentQuestionIndex < 4) {
            loadQuestionView(test, state.exam.currentQuestionIndex + 1);
        }
    });

    document.getElementById('etsSubmitBtn').addEventListener('click', () => {
        if (confirm('Bạn có chắc chắn muốn nộp bài thi TOEIC Writing Task 1 ngay bây giờ?')) {
            clearInterval(state.exam.timerInterval);
            gradeAndShowResults(test);
        }
    });

    document.getElementById('closeResultsBtn').addEventListener('click', () => {
        document.getElementById('etsResultsModal').classList.remove('show');
    });
}

function updateTimerDisplay() {
    const timerDisplay = document.getElementById('etsTimerDisplay');
    if (!timerDisplay) return;

    const mins = Math.floor(state.exam.timeLeft / 60);
    const secs = state.exam.timeLeft % 60;
    const formatted = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;

    timerDisplay.innerHTML = `<i class="fa-solid fa-stopwatch"></i> ${formatted}`;

    if (state.exam.timeLeft <= 120) {
        timerDisplay.classList.add('warning-time');
    } else {
        timerDisplay.classList.remove('warning-time');
    }
}

function loadQuestionView(test, qIdx) {
    state.exam.currentQuestionIndex = qIdx;
    const q = test.questions[qIdx];

    document.getElementById('etsCurrentImg').src = q.image;
    document.getElementById('etsKeywordsList').innerHTML = `
        <span class="ets-keyword-tag">${q.keywords[0]}</span>
        <span class="ets-keyword-tag">${q.keywords[1]}</span>
    `;

    const textarea = document.getElementById('etsAnswerInput');
    textarea.value = state.exam.answers[qIdx] || '';
    updateCharCount(textarea.value);

    // Update Tab styling
    document.querySelectorAll('.ets-tab-btn').forEach((btn, idx) => {
        if (idx === qIdx) btn.classList.add('active');
        else btn.classList.remove('active');
    });

    // Update buttons
    const prevBtn = document.getElementById('etsPrevBtn');
    const nextBtn = document.getElementById('etsNextBtn');
    prevBtn.style.visibility = qIdx === 0 ? 'hidden' : 'visible';
    nextBtn.style.visibility = qIdx === 4 ? 'hidden' : 'visible';
}

function updateCharCount(text) {
    const charCountEl = document.getElementById('etsCharCount');
    const trimmed = text.trim();
    const words = trimmed ? trimmed.split(/\s+/).length : 0;
    const chars = text.length;
    if (charCountEl) {
        charCountEl.textContent = `${words} words | ${chars} chars`;
    }
}

function updateQuestionTabsStatus(test) {
    document.querySelectorAll('.ets-tab-btn').forEach((btn, idx) => {
        if (state.exam.answers[idx] && state.exam.answers[idx].trim().length > 3) {
            btn.classList.add('completed');
        } else {
            btn.classList.remove('completed');
        }
    });
}

// Intelligent Scoring Algorithm
function gradeAndShowResults(test) {
    let totalScore = 0;
    let detailsHTML = '';

    test.questions.forEach((q, idx) => {
        const userAns = (state.exam.answers[idx] || '').trim();
        const scoreReport = evaluateSingleSentence(userAns, q);
        totalScore += scoreReport.score;

        detailsHTML += `
            <div class="q-review-item">
                <div class="q-review-header">
                    <h4 style="font-family: var(--font-heading); font-size: 1.15rem; color: var(--text-primary);">Question ${idx + 1} (${q.keywords.join(' / ')})</h4>
                    <span class="badge-tag score-badge score-${scoreReport.score}" style="background: rgba(0, 242, 254, 0.15); color: var(--color-cyan); border: 1px solid var(--color-cyan); padding: 4px 12px; border-radius: 20px; font-weight: 700;">Score: ${scoreReport.score} / 3 Điểm</span>
                </div>
                
                <div style="font-size: 0.92rem; color: var(--text-muted); margin-bottom: 4px;">Câu trả lời của bạn:</div>
                <div class="q-user-ans">"${userAns || '(Bỏ trống)'}"</div>
                
                <div class="feedback-analysis" style="font-size: 0.98rem; color: var(--text-primary); margin-bottom: 14px;">
                    <strong>Nhận xét:</strong> ${scoreReport.feedback}
                </div>

                <div class="sample-levels-box">
                    <div class="sample-row">
                        <div>
                            <strong style="color: #f87171;">Level 1 (Band 1):</strong>
                        </div>
                        <div style="margin-top: 4px;">${q.sampleLevel1}</div>
                    </div>
                    <div class="sample-row">
                        <div>
                            <strong style="color: var(--color-cyan);">Level 2 (Band 2):</strong>
                        </div>
                        <div style="margin-top: 4px;">${q.sampleLevel2}</div>
                    </div>
                    <div class="sample-row" style="background: rgba(16, 185, 129, 0.1); border: 1.5px solid var(--color-success);">
                        <div>
                            <strong style="color: var(--color-success);">Level 3 (Band 3 - Tối Đa):</strong>
                        </div>
                        <div style="margin-top: 4px; font-weight: 700; color: var(--text-primary); font-family: var(--font-heading);">${q.sampleLevel3}</div>
                    </div>
                </div>
            </div>
        `;
    });

    document.getElementById('totalScoreVal').textContent = totalScore;
    
    let bandText = 'Band 3 (Xuất Sắc - 180-200 TOEIC)';
    if (totalScore < 7) bandText = 'Band 1 (Cần Cải Thiện - <120 TOEIC)';
    else if (totalScore < 12) bandText = 'Band 2 (Khá - 130-170 TOEIC)';
    
    document.getElementById('scaledBandScore').textContent = bandText;
    document.getElementById('resultsDetailList').innerHTML = detailsHTML;
    document.getElementById('etsResultsModal').classList.add('show');

    if (totalScore >= 12) {
        triggerConfetti();
    }
}

function evaluateSingleSentence(userText, question) {
    if (!userText || userText.length < 5) {
        return { score: 0, feedback: "Câu bị bỏ trống hoặc quá ngắn, chưa đạt tiêu chuẩn chấm điểm của ETS." };
    }

    const lower = userText.toLowerCase();
    const k1 = question.keywords[0].toLowerCase();
    const k2 = question.keywords[1].toLowerCase();

    // Check keyword flexibility presence
    const hasK1 = checkKeywordFlexible(lower, k1);
    const hasK2 = checkKeywordFlexible(lower, k2);

    const hasPeriod = userText.endsWith('.') || userText.endsWith('!');
    const isSingleSentence = (userText.match(/\./g) || []).length <= 1;

    if (!hasK1 && !hasK2) {
        return { score: 0, feedback: `Chưa sử dụng cả 2 từ khóa gợi ý (${k1}, ${k2}).` };
    }

    if (!hasK1 || !hasK2) {
        return { score: 1, feedback: `Chỉ sử dụng 1 trong 2 từ khóa. Bị thiếu từ: <strong>${!hasK1 ? k1 : k2}</strong>.` };
    }

    if (!isSingleSentence) {
        return { score: 1, feedback: "Đề bài yêu cầu viết ĐÚNG 01 câu duy nhất. Bạn đã viết nhiều câu riêng biệt." };
    }

    // Evaluate grammar & sentence length
    const wordsCount = userText.split(/\s+/).length;
    if (wordsCount >= 10 && hasPeriod) {
        return { score: 3, feedback: "Xuất sắc! Câu đủ 2 từ khóa, cấu trúc phong phú, cụ thể hóa chi tiết và hoàn chỉnh ngữ pháp." };
    } else if (wordsCount >= 5) {
        return { score: 2, feedback: "Đạt yêu cầu! Câu sử dụng đúng 2 từ khóa và mô tả đúng tranh. Có thể nâng cấp thêm chi tiết để đạt điểm tối đa." };
    } else {
        return { score: 1, feedback: "Câu quá ngắn hoặc chưa hoàn chỉnh vị ngữ." };
    }
}

function checkKeywordFlexible(text, keyword) {
    if (text.includes(keyword)) return true;
    
    // Stemming checks for verbs & plurals
    const base = keyword.replace(/(ing|ed|s|es)$/, '');
    if (base.length >= 3 && text.includes(base)) return true;

    // Common irregular forms
    const irregulars = {
        'man': ['men'],
        'woman': ['women'],
        'person': ['people'],
        'sit': ['sat', 'sitting'],
        'stand': ['stood', 'standing'],
        'hold': ['held', 'holding'],
        'wear': ['wore', 'wearing', 'worn'],
        'carry': ['carried', 'carrying', 'carries'],
        'scan': ['scanned', 'scanning', 'scans'],
        'stack': ['stacked', 'stacking', 'stacks'],
        'box': ['boxes']
    };

    if (irregulars[keyword]) {
        for (let form of irregulars[keyword]) {
            if (text.includes(form)) return true;
        }
    }

    return false;
}

// Confetti Celebration
function triggerConfetti() {
    const canvas = document.getElementById('confettiCanvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const pieces = [];
    const colors = ['#00f2fe', '#a855f7', '#ec4899', '#3b82f6', '#f59e0b', '#10b981'];

    for (let i = 0; i < 100; i++) {
        pieces.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height - canvas.height,
            size: Math.random() * 8 + 4,
            color: colors[Math.floor(Math.random() * colors.length)],
            speedY: Math.random() * 4 + 2,
            speedX: Math.random() * 4 - 2,
            rotation: Math.random() * 360
        });
    }

    let frames = 0;
    function renderConfetti() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        pieces.forEach(p => {
            p.y += p.speedY;
            p.x += p.speedX;
            p.rotation += 2;
            ctx.fillStyle = p.color;
            ctx.save();
            ctx.translate(p.x, p.y);
            ctx.rotate((p.rotation * Math.PI) / 180);
            ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size);
            ctx.restore();
        });

        frames++;
        if (frames < 180) {
            requestAnimationFrame(renderConfetti);
        } else {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
        }
    }

    renderConfetti();
}
