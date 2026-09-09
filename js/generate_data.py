# -*- coding: utf-8 -*-
import json
import os

data_js_content = """/**
 * TOEIC WRITING TASK 01 - DATA REPOSITORY
 * Presented by Miss Nguyet - TOEIC 2026
 * Authoritative Standards: ETS & IIG Vietnam
 */

const OVERVIEW_DATA = {
    title: "TỔNG QUAN TOEIC WRITING TASK 01",
    subtitle: "Chuẩn Khảo Thí ETS & IIG Việt Nam 2026",
    sections: [
        {
            id: "format",
            title: "1. Cấu Trúc Đề Thi & Vị Trí Task 01",
            icon: "fa-solid fa-layer-group",
            content: `
                <div class="overview-card">
                    <div class="badge-tag ets-badge">Chuẩn ETS & IIG Việt Nam</div>
                    <p class="lead-text">Kỳ thi <strong>TOEIC Writing (Kỹ năng Viết)</strong> là một phần trong bài thi TOEIC Speaking & Writing chính thức của ETS, đánh giá khả năng sử dụng tiếng Anh trong môi trường làm việc quốc tế.</p>
                    
                    <div class="table-responsive my-3">
                        <table class="custom-table">
                            <thead>
                                <tr>
                                    <th>Phần thi (Task)</th>
                                    <th>Số lượng câu</th>
                                    <th>Thời gian</th>
                                    <th>Thang điểm</th>
                                    <th>Mục tiêu đánh giá</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="highlight-row">
                                    <td><strong>Task 01 (Questions 1 - 5)</strong></td>
                                    <td><strong>5 câu</strong></td>
                                    <td><strong>8 phút</strong></td>
                                    <td><strong>0 - 3 điểm / câu</strong></td>
                                    <td><strong>Viết 01 câu dựa trên bức tranh và 02 từ gợi ý (Write a Sentence Based on a Picture)</strong></td>
                                </tr>
                                <tr>
                                    <td>Task 02 (Questions 6 - 7)</td>
                                    <td>2 câu</td>
                                    <td>20 phút (10p/câu)</td>
                                    <td>0 - 4 điểm / câu</td>
                                    <td>Phản hồi yêu cầu bằng văn bản (Respond to a Written Request)</td>
                                </tr>
                                <tr>
                                    <td>Task 03 (Question 8)</td>
                                    <td>1 câu</td>
                                    <td>30 phút</td>
                                    <td>0 - 5 điểm</td>
                                    <td>Viết bài luận trình bày quan điểm (Write an Opinion Essay)</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    
                    <div class="info-alert">
                        <i class="fa-solid fa-circle-info"></i>
                        <div><strong>Tổng điểm TOEIC Writing:</strong> Quy đổi từ 0 đến <strong>200 điểm</strong> chia thành 9 cấp độ năng lực (Proficiency Levels). <strong>Task 01 chiếm tỷ trọng nền tảng cốt lõi</strong> về mặt ngữ pháp và cấu trúc câu!</div>
                    </div>
                </div>
            `
        },
        {
            id: "requirements",
            title: "2. Quy Cách & Yêu Cầu Đề Thi Task 01",
            icon: "fa-solid fa-list-check",
            content: `
                <div class="overview-card">
                    <div class="rules-grid">
                        <div class="rule-box primary">
                            <div class="rule-icon"><i class="fa-solid fa-image"></i></div>
                            <div class="rule-body">
                                <h4>01 Bức Tranh & 02 Từ Khóa</h4>
                                <p>Với mỗi câu hỏi (từ Question 1 đến Question 5), bạn sẽ nhìn thấy 1 bức tranh và <strong>2 từ/cụm từ gợi ý</strong> (ví dụ: <em>man / laptop</em>, <em>cashier / scan</em>, <em>wait / bus</em>).</p>
                            </div>
                        </div>
                        
                        <div class="rule-box warning">
                            <div class="rule-icon"><i class="fa-solid fa-pen-nib"></i></div>
                            <div class="rule-body">
                                <h4>Viết ĐÚNG 01 Câu Duy Nhất</h4>
                                <p>Bạn phải viết <strong>chính xác một câu đơn hoặc một câu phức/ghép hoàn chỉnh</strong>. Không được viết 2 câu riêng biệt (ngăn cách bởi dấu chấm).</p>
                            </div>
                        </div>
                        
                        <div class="rule-box success">
                            <div class="rule-icon"><i class="fa-solid fa-arrows-rotate"></i></div>
                            <div class="rule-body">
                                <h4>Quy Tắc Biến Đổi Từ Khóa (Flexibility)</h4>
                                <ul>
                                    <li>✔ <strong>ĐƯỢC PHÉP</strong> thay đổi hình thái từ: chia thì (<em>use &rarr; is using / used</em>), chuyển số ít/nhiều (<em>box &rarr; boxes</em>), thêm giới từ phù hợp.</li>
                                    <li>✔ <strong>ĐƯỢC PHÉP</strong> thay đổi thứ tự xuất hiện của 2 từ khóa trong câu.</li>
                                    <li>✘ <strong>KHÔNG ĐƯỢC</strong> đổi từ loại (ví dụ: đề cho động từ <em>decide</em> không được tự ý đổi thành danh từ <em>decision</em>).</li>
                                </ul>
                            </div>
                        </div>
                        
                        <div class="rule-box info">
                            <div class="rule-icon"><i class="fa-solid fa-stopwatch"></i></div>
                            <div class="rule-body">
                                <h4>Quản Lý 8 Phút Cho 5 Câu</h4>
                                <p>Bạn có tổng cộng <strong>8:00 phút</strong> cho cả 5 câu. Hệ thống cho phép bấm <strong>Next / Back</strong> tự do chuyển đổi giữa các câu để chỉnh sửa trước khi hết giờ.</p>
                            </div>
                        </div>
                    </div>
                </div>
            `
        },
        {
            id: "scoring",
            title: "3. Thang Điểm 0 – 3 & Tiêu Chí Chấm Của IIG/ETS",
            icon: "fa-solid fa-chart-simple",
            content: `
                <div class="overview-card">
                    <p class="mb-3">Mỗi câu trong Task 01 được chấm độc lập trên thang điểm từ <strong>0 đến 3 điểm</strong> bởi ít nhất 2 giám khảo ETS hoặc hệ thống AI ETS e-rater:</p>
                    
                    <div class="score-cards-container">
                        <div class="score-card score-3">
                            <div class="score-badge">SCORE 3 (Tối Đa)</div>
                            <div class="score-desc">
                                <h5>Xuất sắc & Hoàn hảo</h5>
                                <ul>
                                    <li>✔ Sử dụng <strong>đúng và đủ cả 2 từ khóa</strong> được cho.</li>
                                    <li>✔ Mô tả <strong>chính xác 100%</strong> nội dung và hành động/trạng thái trong tranh.</li>
                                    <li>✔ Ngữ pháp hoàn toàn chính xác: chia thì chuẩn, hòa hợp chủ-vị đúng, mạo từ và giới từ chuẩn xác.</li>
                                </ul>
                            </div>
                        </div>

                        <div class="score-card score-2">
                            <div class="score-badge">SCORE 2 (Đạt yêu cầu)</div>
                            <div class="score-desc">
                                <h5>Khá - Còn lỗi ngữ pháp nhỏ</h5>
                                <ul>
                                    <li>✔ Sử dụng đủ cả 2 từ khóa và câu mô tả đúng tranh.</li>
                                    <li>⚠️ Có <strong>1 hoặc 2 lỗi ngữ pháp nhỏ</strong> (lỗi mạo từ <em>a/an/the</em>, số ít số nhiều nhẹ, hoặc trật tự từ hơi gượng gạo) nhưng người đọc vẫn hiểu đúng ý nghĩa.</li>
                                </ul>
                            </div>
                        </div>

                        <div class="score-card score-1">
                            <div class="score-badge">SCORE 1 (Yếu)</div>
                            <div class="score-desc">
                                <h5>Mắc lỗi nghiêm trọng</h5>
                                <ul>
                                    <li>⚠️ Chỉ sử dụng <strong>1 từ khóa</strong> (bỏ quên 1 từ).</li>
                                    <li>⚠️ Hoặc mắc <strong>lỗi ngữ pháp rất nặng</strong> làm sai lệch ý nghĩa câu (thiếu động từ chính, câu què, chia sai thì hoàn toàn).</li>
                                    <li>⚠️ Hoặc hai từ khóa bị rời rạc, không tạo thành một câu có nghĩa mô tả tranh.</li>
                                </ul>
                            </div>
                        </div>

                        <div class="score-card score-0">
                            <div class="score-badge">SCORE 0 (Không điểm)</div>
                            <div class="score-desc">
                                <h5>Không có điểm</h5>
                                <ul>
                                    <li>✘ Bỏ trống không viết gì.</li>
                                    <li>✘ Lạc đề hoàn toàn, không liên quan đến bức tranh.</li>
                                    <li>✘ Không sử dụng bất kỳ từ khóa nào trong 2 từ gợi ý.</li>
                                    <li>✘ Viết bằng ngôn ngữ khác tiếng Anh.</li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <div class="mt-4">
                        <h4 class="mb-2" style="color: var(--color-cyan);"><i class="fa-solid fa-magnifying-glass-chart"></i> 3 Tiêu Chí Chấm Cốt Lõi Của Giám Khảo:</h4>
                        <div class="criteria-grid">
                            <div class="criteria-pill">
                                <strong>1. Grammar & Syntax:</strong> Đúng thì (hiện tại tiếp diễn / bị động / đơn), đúng S-V agreement, đúng giới từ.
                            </div>
                            <div class="criteria-pill">
                                <strong>2. Picture Relevance:</strong> Mô tả trung thực những gì nhìn thấy trực tiếp, không suy diễn lung tung.
                            </div>
                            <div class="criteria-pill">
                                <strong>3. Keyword Usage:</strong> Ghép 2 từ khóa vào cấu trúc câu tự nhiên, chính xác vị trí.
                            </div>
                        </div>
                    </div>
                </div>
            `
        },
        {
            id: "strategy",
            title: "4. Chiến Lược 8 Phút & Bảng Tự Rà Soát Lỗi (Checklist)",
            icon: "fa-solid fa-shield-halved",
            content: `
                <div class="overview-card">
                    <div class="timeline-strategy">
                        <div class="strategy-step">
                            <div class="step-num">01</div>
                            <div class="step-content">
                                <h4>Bước 1: Quan Sát Tranh & Xác Định Từ Loại (20 giây/câu)</h4>
                                <p>Nhìn nhanh hành động chính hoặc trạng thái đồ vật. Xác định 2 từ khóa thuộc từ loại gì (Danh từ - Động từ? Danh từ - Giới từ? Động từ - Liên từ?).</p>
                            </div>
                        </div>
                        <div class="strategy-step">
                            <div class="step-num">02</div>
                            <div class="step-content">
                                <h4>Bước 2: Xây Dựng Khung Câu Cơ Bản S + V + O (40 giây/câu)</h4>
                                <p>Hình thành ngay bộ khung chuẩn: Ai làm gì? (Hiện tại tiếp diễn: <em>The man is typing on a laptop</em>) hoặc Vật ở đâu? (Bị động/Tồn tại: <em>There are boxes stacked on the floor</em>).</p>
                            </div>
                        </div>
                        <div class="strategy-step">
                            <div class="step-num">03</div>
                            <div class="step-content">
                                <h4>Bước 3: Nâng Cấp Câu Lên Band Điểm Tối Đa (20 giây/câu)</h4>
                                <p>Thêm đặc điểm nhìn thấy (quần áo, công cụ, vị trí cụ thể) để biến câu thông thường thành câu Band 3 sắc sảo.</p>
                            </div>
                        </div>
                        <div class="strategy-step">
                            <div class="step-num">04</div>
                            <div class="step-content">
                                <h4>Bước 4: Rà Soát Nhanh Bằng 5 Điểm Vàng (Checklist)</h4>
                                <p>Dành 30 giây cuối cùng kiểm tra toàn bộ 5 câu theo bảng checklist dưới đây trước khi nộp bài.</p>
                            </div>
                        </div>
                    </div>

                    <div class="checklist-container mt-4">
                        <h4><i class="fa-solid fa-square-check" style="color: var(--color-success);"></i> 5 Điểm Vàng Tự Rà Soát (Self-Checklist)</h4>
                        <div class="checklist-grid">
                            <div class="check-item"><i class="fa-solid fa-check"></i> Đã dùng <strong>đủ cả 2 từ khóa</strong> chưa? (Không bỏ sót từ nào)</div>
                            <div class="check-item"><i class="fa-solid fa-check"></i> Động từ to-be và V-ing đã hòa hợp Chủ - Vị chưa? (<em>The man is... / The workers are...</em>)</div>
                            <div class="check-item"><i class="fa-solid fa-check"></i> Danh từ đếm được đã có mạo từ (<em>a/an/the</em>) hoặc dạng số nhiều (<em>-s/-es</em>) chưa?</div>
                            <div class="check-item"><i class="fa-solid fa-check"></i> Đã có <strong>dấu chấm kết câu (.)</strong> và <strong>viết hoa chữ cái đầu câu</strong> chưa?</div>
                            <div class="check-item"><i class="fa-solid fa-check"></i> Có viết quá 1 câu không? (Phải đảm bảo <strong>chỉ có đúng 1 câu</strong>).</div>
                        </div>
                    </div>
                </div>
            `
        }
    ]
};

const GRAMMAR_CHAPTERS = [
    {
        id: 1,
        title: "Chương 01: Cấu Trúc Câu Đơn & 7 Mẫu Câu Cơ Bản",
        badge: "Nền tảng",
        slidesRange: "Slides 1 - 27",
        summary: "Nắm vững định nghĩa câu trần thuật mô tả tranh, cấu trúc S + V + O và 7 mô hình câu chuẩn trong ngữ pháp tiếng Anh.",
        lessons: [
            {
                lessonId: "1-1",
                title: "1. Định Nghĩa Câu Đơn Mô Tả Tranh",
                content: `
                    <div class="lesson-box">
                        <p class="lead-text">Câu trần thuật mô tả tranh trong <strong>TOEIC Writing Task 1</strong> là câu dùng để <strong>mô tả trực tiếp những gì nhìn thấy trong bức tranh</strong>.</p>
                        <div class="formula-box">
                            <div class="formula-title">Cấu trúc cốt lõi</div>
                            <div class="formula-math">S + V + O .</div>
                        </div>
                        <p><strong>Đặc điểm quan trọng:</strong></p>
                        <ul>
                            <li>Bắt đầu bằng chữ hoa, kết thúc bằng dấu chấm (<code>.</code>).</li>
                            <li>Chủ ngữ (S) luôn <strong>có sẵn và nhìn thấy rõ ràng</strong> trong bức tranh (người hoặc vật), không phải tự tưởng tượng ra.</li>
                            <li>Động từ (V) mô tả trực tiếp hành động hoặc trạng thái đang diễn ra.</li>
                        </ul>
                    </div>
                `
            },
            {
                lessonId: "1-2",
                title: "2. Bảy (07) Cấu Trúc Câu Cơ Bản",
                content: `
                    <div class="lesson-box">
                        <p>Trong tiếng Anh học thuật có 7 cấu trúc câu chuẩn. Trong TOEIC Writing Part 1, bạn sẽ áp dụng linh hoạt các cấu trúc này:</p>
                        <div class="patterns-grid">
                            <div class="pattern-card">
                                <div class="pattern-num">Mẫu 1</div>
                                <div class="pattern-formula">S + V</div>
                                <div class="pattern-desc">Chỉ có Chủ ngữ + Nội động từ (không cần tân ngữ).</div>
                                <div class="pattern-example"><em>The train arrives.</em> / <em>The sun is shining.</em></div>
                            </div>
                            <div class="pattern-card highlight-card">
                                <div class="pattern-num">Mẫu 2 (Trọng tâm)</div>
                                <div class="pattern-formula">S + V + O</div>
                                <div class="pattern-desc">Chủ ngữ + Ngoại động từ + Tân ngữ trực tiếp.</div>
                                <div class="pattern-example"><em>The man is using a laptop.</em></div>
                            </div>
                            <div class="pattern-card">
                                <div class="pattern-num">Mẫu 3</div>
                                <div class="pattern-formula">S + V + C</div>
                                <div class="pattern-desc">Chủ ngữ + Động từ liên kết (Linking verb) + Bổ ngữ cho chủ ngữ (SC).</div>
                                <div class="pattern-example"><em>The customer looks satisfied.</em> / <em>She is a doctor.</em></div>
                            </div>
                            <div class="pattern-card">
                                <div class="pattern-num">Mẫu 4</div>
                                <div class="pattern-formula">S + V + O + O</div>
                                <div class="pattern-desc">Chủ ngữ + Động từ + Tân ngữ gián tiếp (IO) + Tân ngữ trực tiếp (DO).</div>
                                <div class="pattern-example"><em>The cashier gives the customer the receipt.</em></div>
                            </div>
                            <div class="pattern-card">
                                <div class="pattern-num">Mẫu 5</div>
                                <div class="pattern-formula">S + V + O + C</div>
                                <div class="pattern-desc">Chủ ngữ + Động từ + Tân ngữ + Bổ ngữ cho tân ngữ (OC).</div>
                                <div class="pattern-example"><em>They painted the wall white.</em></div>
                            </div>
                            <div class="pattern-card">
                                <div class="pattern-num">Mẫu 6</div>
                                <div class="pattern-formula">S + V + Adv</div>
                                <div class="pattern-desc">Chủ ngữ + Động từ + Trạng từ / Cụm giới từ chỉ nơi chốn.</div>
                                <div class="pattern-example"><em>The woman is standing near the counter.</em></div>
                            </div>
                            <div class="pattern-card highlight-card">
                                <div class="pattern-num">Mẫu 7 (Trọng tâm)</div>
                                <div class="pattern-formula">S + V + O + Adv</div>
                                <div class="pattern-desc">Chủ ngữ + Động từ + Tân ngữ + Cụm trạng ngữ / giới từ chỉ nơi chốn.</div>
                                <div class="pattern-example"><em>The man is typing an email on his computer.</em></div>
                            </div>
                        </div>
                    </div>
                `
            }
        ]
    },
    {
        id: 2,
        title: "Chương 02: Các Thành Phần Câu Cốt Lõi (S - V - O - C)",
        badge: "Ngữ pháp chi tiết",
        slidesRange: "Slides 28 - 41",
        summary: "Phân loại chuyên sâu Chủ ngữ, Động từ, Tân ngữ trực tiếp / gián tiếp / giới từ và phân biệt rõ Tân ngữ vs Bổ ngữ.",
        lessons: [
            {
                lessonId: "2-1",
                title: "1. Chủ Ngữ (Subject - S)",
                content: `
                    <div class="lesson-box">
                        <h4>Phân loại Chủ ngữ:</h4>
                        <div class="two-col-grid">
                            <div class="col-box">
                                <h5>1. Danh từ (Nouns)</h5>
                                <p><strong>Chỉ người:</strong> <em>the man, the woman, workers, customers, passengers, students, two men...</em></p>
                                <p><strong>Chỉ vật:</strong> <em>the table, the car, boxes, documents, the presentation screen...</em></p>
                            </div>
                            <div class="col-box">
                                <h5>2. Đại từ (Pronouns)</h5>
                                <p><strong>Đại từ nhân xưng:</strong> <em>he, she, they</em> (Dùng khi thấy rõ giới tính / số lượng người).</p>
                                <p><strong>Đại từ bất định:</strong> <em>someone</em> (Dùng khi không thấy rõ mặt hoặc góc chụp từ sau lưng).</p>
                            </div>
                        </div>
                    </div>
                `
            },
            {
                lessonId: "2-2",
                title: "2. Tân Ngữ (Object - O) & 2 Vị Trí Đặt Tân Ngữ",
                content: `
                    <div class="lesson-box">
                        <p>Tân ngữ là thành phần đứng sau động từ hoặc giới từ, nhận sự tác động của hành động.</p>
                        <div class="table-responsive">
                            <table class="custom-table">
                                <thead>
                                    <tr>
                                        <th>Loại Tân Ngữ</th>
                                        <th>Câu Hỏi Xác Định</th>
                                        <th>Ví Dụ Thực Tế</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td><strong>Tân ngữ trực tiếp (DO)</strong></td>
                                        <td><em>What? (Cái gì?) / Who? (Ai?)</em></td>
                                        <td>The man is using <strong>a laptop</strong>.</td>
                                    </tr>
                                    <tr>
                                        <td><strong>Tân ngữ gián tiếp (IO)</strong></td>
                                        <td><em>To whom? / For whom? (Cho ai?)</em></td>
                                        <td>The doctor is handing <strong>the patient</strong> a prescription.</td>
                                    </tr>
                                    <tr>
                                        <td><strong>Tân ngữ của giới từ (OP)</strong></td>
                                        <td>Đứng sau Preposition</td>
                                        <td>The woman is looking at <strong>the screen</strong>.</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        
                        <div class="formula-box mt-3">
                            <div class="formula-title">2 Cách Viết Khi Động Từ Có 2 Tân Ngữ (Give, Hand, Send, Offer...)</div>
                            <div class="comparison-row">
                                <div class="comp-box">
                                    <strong>Cách 1: Người trước – Vật sau (KHÔNG giới từ)</strong><br>
                                    <code>S + V + Người (IO) + Vật (DO)</code><br>
                                    <em>The doctor hands the patient the medicine.</em>
                                </div>
                                <div class="comp-box">
                                    <strong>Cách 2: Vật trước – Người sau (CÓ giới từ TO/FOR)</strong><br>
                                    <code>S + V + Vật (DO) + to/for + Người (IO)</code><br>
                                    <em>The doctor hands the medicine to the patient.</em>
                                </div>
                            </div>
                        </div>
                    </div>
                `
            },
            {
                lessonId: "2-3",
                title: "3. Phân Biệt Tân Ngữ (Object) và Bổ Ngữ (Complement)",
                content: `
                    <div class="lesson-box">
                        <div class="table-responsive">
                            <table class="custom-table">
                                <thead>
                                    <tr>
                                        <th>Đặc Điểm</th>
                                        <th>TÂN NGỮ (OBJECT)</th>
                                        <th>BỔ NGỮ (COMPLEMENT)</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td><strong>Bản chất</strong></td>
                                        <td>Là đối tượng <strong>bị tác động</strong> bởi hành động.</td>
                                        <td>Là thành phần <strong>bổ sung ý nghĩa, mô tả bản chất</strong> cho S hoặc O.</td>
                                    </tr>
                                    <tr>
                                        <td><strong>Mối quan hệ</strong></td>
                                        <td>Khác đối tượng với Chủ ngữ ($S \neq O$).</td>
                                        <td>Cùng chỉ một đối tượng với S hoặc O ($S = C$).</td>
                                    </tr>
                                    <tr>
                                        <td><strong>Ví dụ</strong></td>
                                        <td><em>She met <strong>the manager</strong>.</em> (Cô ấy $\neq$ người quản lý)</td>
                                        <td><em>She is <strong>a manager</strong>.</em> (Cô ấy chính là người quản lý)</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                `
            }
        ]
    },
    {
        id: 3,
        title: "Chương 03: 5 Cấu Trúc Then Chốt Trong TOEIC Writing Task 1",
        badge: "Chiến thuật làm bài",
        slidesRange: "Slides 42 - 46",
        summary: "Bộ 5 cấu trúc câu quyền năng nhất bao quát 100% các dạng tranh xuất hiện trong đề thi thật.",
        lessons: [
            {
                lessonId: "3-1",
                title: "Top 5 Cấu Trúc Chuẩn Điểm Tuyệt Đối",
                content: `
                    <div class="lesson-box">
                        <div class="key-structures-list">
                            <div class="struct-card">
                                <div class="struct-header">
                                    <span class="struct-badge">Cấu trúc 1</span>
                                    <h4>Thì Hiện Tại Tiếp Diễn (Mô tả hành động đang diễn ra)</h4>
                                </div>
                                <div class="struct-formula">S + is / are + V-ing + O .</div>
                                <p class="struct-desc">Cấu trúc phổ biến nhất khi tranh có người đang thực hiện một hành động cụ thể.</p>
                                <div class="struct-eg"><strong>Ví dụ:</strong> <em>The mechanic is repairing a car in the garage.</em></div>
                            </div>

                            <div class="struct-card">
                                <div class="struct-header">
                                    <span class="struct-badge">Cấu trúc 2</span>
                                    <h4>Bị Động Hiện Tại Tiếp Diễn (Hành động đang được thực hiện lên vật)</h4>
                                </div>
                                <div class="struct-formula">S (Vật) + is / are + being + V3/ed + (by O) .</div>
                                <p class="struct-desc">Dùng khi muốn nhấn mạnh vào vật đang chịu tác động trực tiếp của hành động.</p>
                                <div class="struct-eg"><strong>Ví dụ:</strong> <em>The groceries are being scanned at the counter.</em></div>
                            </div>

                            <div class="struct-card">
                                <div class="struct-header">
                                    <span class="struct-badge">Cấu trúc 3</span>
                                    <h4>Bị Động Hiện Tại Đơn (Mô tả kết quả sắp đặt / bố trí của đồ vật)</h4>
                                </div>
                                <div class="struct-formula">S (Vật) + is / are + V3/ed + Prepositional Phrase .</div>
                                <p class="struct-desc">Dùng khi mô tả đồ vật đã được sắp xếp sẵn (không có người tác động tại thời điểm chụp).</p>
                                <div class="struct-eg"><strong>Ví dụ:</strong> <em>Cardboard boxes are stacked on the warehouse floor.</em></div>
                            </div>

                            <div class="struct-card">
                                <div class="struct-header">
                                    <span class="struct-badge">Cấu trúc 4</span>
                                    <h4>Cấu Trúc Trạng Thái (Mô tả tính chất / trạng thái của người hoặc vật)</h4>
                                </div>
                                <div class="struct-formula">S + is / are + Adjective .</div>
                                <p class="struct-desc">Dùng khi keyword cho sẵn là một tính từ mô tả trạng thái.</p>
                                <div class="struct-eg"><strong>Ví dụ:</strong> <em>The conference room is empty and quiet.</em></div>
                            </div>

                            <div class="struct-card">
                                <div class="struct-header">
                                    <span class="struct-badge">Cấu trúc 5</span>
                                    <h4>Cấu Trúc Tồn Tại (Mô tả những thứ sẵn có trong bức tranh)</h4>
                                </div>
                                <div class="struct-formula">There is / There are + Noun Phrase + Prepositional Phrase / V-ing / V3 .</div>
                                <p class="struct-desc">Dùng khi tranh mô tả bối cảnh chung hoặc sự hiện diện của người/vật.</p>
                                <div class="struct-eg"><strong>Ví dụ:</strong> <em>There are several passengers waiting on the train platform.</em></div>
                            </div>
                        </div>
                    </div>
                `
            }
        ]
    },
    {
        id: 4,
        title: "Chương 04: Kỹ Thuật Nâng Cấp Câu - Tranh Mô Tả Người",
        badge: "Bí quyết Band 3",
        slidesRange: "Slides 47 - 60",
        summary: "Công thức nâng cấp toàn diện 3 thành phần Chủ ngữ (S), Hành động (V) và Tân ngữ (O) dựa trên hình ảnh thực tế.",
        lessons: [
            {
                lessonId: "4-1",
                title: "1. Kỹ Thuật Cụ Thể Hóa Chủ Ngữ (S)",
                content: `
                    <div class="lesson-box">
                        <div class="upgrade-case-study">
                            <div class="img-preview-box">
                                <img src="images/image12.png" alt="Cashier scanning groceries" class="lesson-img">
                                <span class="img-caption">Tranh minh họa: Nữ nhân viên tại quầy thu ngân</span>
                            </div>
                            <div class="upgrade-steps">
                                <div class="base-sentence">
                                    <span class="level-tag l1">Câu cơ bản (Band 1):</span>
                                    <code>The woman is scanning some items.</code>
                                    <p class="note-muted">Câu đúng ngữ pháp nhưng "The woman" còn quá chung chung.</p>
                                </div>
                                
                                <div class="step-card">
                                    <div class="step-tag">Bước 1: Thêm đặc điểm nhìn thấy rõ (Visible Features)</div>
                                    <p>Thêm cụm giới từ mô tả trang phục: <code>in a red uniform</code> hoặc phụ kiện: <code>with a red cap on</code></p>
                                    <div class="improved-code">&rarr; <strong>The woman in a red uniform</strong> is scanning some items.</div>
                                    <div class="rule-tip">
                                        <strong>Mẹo giới từ:</strong><br>
                                        • <strong>IN + quần áo</strong> đang mặc (<em>in a blue suit, in a uniform</em>)<br>
                                        • <strong>WITH ... ON</strong>: phụ kiện đội/đeo trên người (<em>with a cap on, with glasses on</em>)<br>
                                        • <strong>WITH</strong>: phụ kiện mang theo (<em>with an umbrella, with a briefcase</em>)
                                    </div>
                                </div>

                                <div class="step-card">
                                    <div class="step-tag">Bước 2: Thêm vị trí của người (Location of Subject)</div>
                                    <p>Thêm cụm phân từ hoặc cụm giới từ chỉ vị trí: <code>standing at the checkout counter</code></p>
                                    <div class="improved-code">&rarr; <strong>The woman standing at the checkout counter</strong> is scanning some items.</div>
                                </div>
                            </div>
                        </div>
                    </div>
                `
            },
            {
                lessonId: "4-2",
                title: "2. Kỹ Thuật Cụ Thể Hóa Hành Động (V) & Tân Ngữ (O)",
                content: `
                    <div class="lesson-box">
                        <div class="two-col-grid">
                            <div class="col-box">
                                <h5>Cụ thể hóa Hành Động (V)</h5>
                                <p><strong>Thêm công cụ thực hiện:</strong></p>
                                <div class="code-pill">with a barcode scanner</div>
                                <p>&rarr; <em>The woman is scanning some items <strong>with a barcode scanner</strong>.</em></p>
                                <p><strong>Thêm vị trí hành động:</strong></p>
                                <div class="code-pill">at the checkout counter</div>
                                <p>&rarr; <em>The woman is scanning some items <strong>at the checkout counter</strong>.</em></p>
                            </div>

                            <div class="col-box">
                                <h5>Cụ thể hóa Tân Ngữ (O)</h5>
                                <p><strong>1. Thay danh từ chung bằng từ cụ thể:</strong></p>
                                <p><code>items</code> &rarr; <code>grocery items</code></p>
                                <p><strong>2. Thêm số lượng tương đối:</strong></p>
                                <p><code>some</code> &rarr; <code>several</code> (rõ ràng hơn 2)</p>
                                <p><strong>3. Thêm đặc điểm nhìn thấy:</strong></p>
                                <p><code>packaged grocery items</code> (đóng gói sẵn)</p>
                                <div class="master-sentence mt-2">
                                    <span class="level-tag l3">Câu nâng cấp Band 3 Tối Đa:</span><br>
                                    <strong>The woman in a red uniform is scanning several packaged grocery items with a barcode scanner.</strong>
                                </div>
                            </div>
                        </div>
                    </div>
                `
            }
        ]
    },
    {
        id: 5,
        title: "Chương 05: Kỹ Thuật Nâng Cấp Câu - Tranh Mô Tả Vật",
        badge: "Bí quyết Band 3",
        slidesRange: "Slides 61 - 70",
        summary: "Kỹ thuật biến câu mô tả vật khô khan thành câu chuẩn ngữ cảnh bằng cách cụ thể hóa danh từ và trạng thái vật lý.",
        lessons: [
            {
                lessonId: "5-1",
                title: "Kỹ Thuật Cụ Thể Hóa Danh Từ & Trạng Thái Thực Tế",
                content: `
                    <div class="lesson-box">
                        <div class="upgrade-case-study">
                            <div class="img-preview-box">
                                <img src="images/image13.jpeg" alt="Cardboard boxes stacked on floor" class="lesson-img">
                                <span class="img-caption">Tranh minh họa: Các thùng hàng trong kho</span>
                            </div>
                            <div class="upgrade-steps">
                                <div class="base-sentence">
                                    <span class="level-tag l1">Câu cơ bản (Band 1):</span>
                                    <code>There are some boxes on the floor.</code>
                                    <p class="note-muted">Câu đúng ngữ pháp nhưng chỉ nêu sự tồn tại chung chung, chưa nêu trạng thái vật lý.</p>
                                </div>

                                <div class="step-card">
                                    <div class="step-tag">Bước 1: Nâng cấp Danh Từ (Noun Specificity)</div>
                                    <ul>
                                        <li>Thay danh từ chung: <code>boxes</code> &rarr; <code>cardboard boxes</code> (thùng carton).</li>
                                        <li>Thêm số lượng: <code>some</code> &rarr; <code>several</code></li>
                                        <li>Thêm kích thước quan sát được: <code>large cardboard boxes</code></li>
                                    </ul>
                                </div>

                                <div class="step-card">
                                    <div class="step-tag">Bước 2: Cụ thể hóa Trạng Thái Thực Tế (Physical State)</div>
                                    <div class="two-ways-box">
                                        <div class="way-item">
                                            <strong>Cách 1: Đổi sang cấu trúc trạng thái bị động</strong><br>
                                            <code>The + Noun + is/are + V3/ed + Preposition</code><br>
                                            &rarr; <em>The large cardboard boxes <strong>are stacked</strong> on the warehouse floor.</em>
                                        </div>
                                        <div class="way-item mt-2">
                                            <strong>Cách 2: Thêm cụm phân từ V3/ed</strong><br>
                                            <code>There are + Noun + V3/ed + Preposition</code><br>
                                            &rarr; <em>There are several large cardboard boxes <strong>stacked</strong> on the floor.</em>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                `
            }
        ]
    },
    {
        id: 6,
        title: "Chương 06: Bảng Quy Tắc Vàng & Cảnh Báo Lỗi Sai Cấm Kỵ",
        badge: "Tránh mất điểm",
        slidesRange: "Quy tắc cốt tử",
        summary: "Những cạm bẫy suy diễn chủ quan khiến thí sinh bị trừ điểm nặng nề trong Task 1.",
        lessons: [
            {
                lessonId: "6-1",
                title: "Bảng Đối Chiếu: Những Điều NÊN Làm và CẤM KỴ",
                content: `
                    <div class="lesson-box">
                        <div class="dos-donts-grid">
                            <div class="donts-column">
                                <div class="column-header"><i class="fa-solid fa-circle-xmark"></i> CÁC LỖI CẤM KỴ (DON'TS)</div>
                                <div class="item-list">
                                    <div class="item-bad">
                                        <strong>✘ Không suy đoán nghề nghiệp:</strong> Không viết <em>"The doctor / The manager"</em> nếu chỉ nhìn thấy người mặc thường phục hoặc không có phù hiệu rõ ràng.
                                    </div>
                                    <div class="item-bad">
                                        <strong>✘ Không suy đoán cảm xúc & tính cách:</strong> Tuyệt đối không thêm <em>"tired, busy, happy, hardworking, smart"</em> vì không có căn cứ khách quan.
                                    </div>
                                    <div class="item-bad">
                                        <strong>✘ Không thêm mục đích suy diễn:</strong> Không thêm <em>"for moving house, in order to buy food"</em> nếu tranh không thể hiện.
                                    </div>
                                    <div class="item-bad">
                                        <strong>✘ Không dùng trạng từ đánh giá chủ quan:</strong> Tránh các từ như <em>"neatly, carefully, skillfully, professionally"</em>.
                                    </div>
                                    <div class="item-bad">
                                        <strong>✘ Không dùng bị động tiếp diễn 'is being V3':</strong> Tuyệt đối KHÔNG dùng nếu trong hình không có người đang thực hiện hành động lên vật!
                                    </div>
                                </div>
                            </div>

                            <div class="dos-column">
                                <div class="column-header"><i class="fa-solid fa-circle-check"></i> NGUYÊN TẮC VÀNG (DOS)</div>
                                <div class="item-list">
                                    <div class="item-good">
                                        <strong>✔ Chỉ mô tả sự thật mắt thấy:</strong> Mô tả trang phục thực tế (<em>in a blue shirt</em>), vị trí thực tế (<em>at the desk</em>), vật dụng cầm trên tay.
                                    </div>
                                    <div class="item-good">
                                        <strong>✔ Ưu tiên câu đúng ngữ pháp tuyệt đối:</strong> Thà viết một câu đơn giản nhưng chuẩn 100% ngữ pháp hơn là viết câu phức tạp mà sai chia thì.
                                    </div>
                                    <div class="item-good">
                                        <strong>✔ Luôn kiểm tra 2 từ khóa:</strong> Đảm bảo cả hai từ khóa đã được đưa vào câu và có biến đổi đuôi từ (tense/plural) phù hợp.
                                    </div>
                                    <div class="item-good">
                                        <strong>✔ Viết đúng 01 câu hoàn chỉnh:</strong> Đảm bảo câu có đủ Chủ ngữ, Động từ chính, viết hoa đầu câu và kết thúc bằng dấu chấm.
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                `
            }
        ]
    }
];

const UNSCRAMBLE_EXERCISES = [
    {
        id: 1,
        title: "Bài tập 01: Sắp xếp câu S + V + O cơ bản",
        words: ["is", "a laptop", "The man", "using", "."],
        correctOrder: ["The man", "is", "using", "a laptop", "."],
        vietnameseHint: "Người đàn ông đang sử dụng máy tính xách tay.",
        explanation: "Cấu trúc S (The man) + is + V-ing (using) + O (a laptop)."
    },
    {
        id: 2,
        title: "Bài tập 02: Sắp xếp câu với chủ ngữ số nhiều",
        words: ["boxes", "The workers", "carrying", "are", "heavy", "."],
        correctOrder: ["The workers", "are", "carrying", "heavy", "boxes", "."],
        vietnameseHint: "Những người công nhân đang khiêng những chiếc thùng nặng.",
        explanation: "Chủ ngữ số nhiều 'The workers' đi với to-be 'are', động từ 'carrying', cụm tân ngữ 'heavy boxes'."
    },
    {
        id: 3,
        title: "Bài tập 03: Câu có 2 Tân ngữ (Người trước - Vật sau)",
        words: ["a prescription", "hands", "The doctor", "the patient", "."],
        correctOrder: ["The doctor", "hands", "the patient", "a prescription", "."],
        vietnameseHint: "Bác sĩ trao đơn thuốc cho bệnh nhân.",
        explanation: "Cấu trúc S + V + Tân ngữ gián tiếp (the patient) + Tân ngữ trực tiếp (a prescription) không dùng giới từ."
    },
    {
        id: 4,
        title: "Bài tập 04: Câu có 2 Tân ngữ với giới từ TO",
        words: ["to the patient", "hands", "a prescription", "The doctor", "."],
        correctOrder: ["The doctor", "hands", "a prescription", "to the patient", "."],
        vietnameseHint: "Bác sĩ trao đơn thuốc cho bệnh nhân (dùng giới từ to).",
        explanation: "Cấu trúc S + V + Vật (a prescription) + to + Người (the patient)."
    },
    {
        id: 5,
        title: "Bài tập 05: Cấu trúc Bị động Hiện tại tiếp diễn",
        words: ["being", "Some groceries", "scanned", "are", "at the counter", "."],
        correctOrder: ["Some groceries", "are", "being", "scanned", "at the counter", "."],
        vietnameseHint: "Một số món hàng tạp hóa đang được quét tại quầy.",
        explanation: "Cấu trúc bị động tiếp diễn: S (Some groceries) + are + being + V3 (scanned) + cụm giới từ nơi chốn."
    },
    {
        id: 6,
        title: "Bài tập 06: Cấu trúc Tồn tại There are + Phân từ V3",
        words: ["several boxes", "stacked", "There are", "on the floor", "."],
        correctOrder: ["There are", "several boxes", "stacked", "on the floor", "."],
        vietnameseHint: "Có vài chiếc hộp được xếp chồng trên sàn.",
        explanation: "Cấu trúc There are + Noun phrase (several boxes) + Quá khứ phân từ rút gọn (stacked) + Prep phrase."
    },
    {
        id: 7,
        title: "Bài tập 07: Câu nâng cấp với cụm giới từ trang phục",
        words: ["in a red uniform", "several items", "is scanning", "The woman", "."],
        correctOrder: ["The woman", "in a red uniform", "is scanning", "several items", "."],
        vietnameseHint: "Người phụ nữ mặc đồng phục đỏ đang quét vài món đồ.",
        explanation: "Cụm 'in a red uniform' bổ nghĩa trực tiếp cho chủ ngữ 'The woman'."
    },
    {
        id: 8,
        title: "Bài tập 08: Câu nâng cấp với công cụ thực hiện",
        words: ["is scanning", "with a barcode scanner", "The cashier", "the products", "."],
        correctOrder: ["The cashier", "is scanning", "the products", "with a barcode scanner", "."],
        vietnameseHint: "Nhân viên thu ngân đang quét sản phẩm bằng máy quét mã vạch.",
        explanation: "Cụm 'with a barcode scanner' bổ nghĩa công cụ cho động từ 'is scanning'."
    }
];

const UPGRADER_CHALLENGES = [
    {
        id: 1,
        title: "Thử Thách 01: Nâng Cấp Câu Mô Tả Thu Ngân",
        image: "images/image12.png",
        imageAlt: "Cashier scanning items",
        keywords: ["cashier", "scan"],
        levels: {
            level1: {
                band: "Band 1 (Cơ bản - 1 điểm)",
                sentence: "The woman is scanning some items.",
                analysis: "Câu đúng ngữ pháp nhưng từ ngữ còn chung chung, chưa làm nổi bật chi tiết quan sát."
            },
            level2: {
                band: "Band 2 (Khá - 2 điểm)",
                sentence: "The woman in a red uniform is scanning items at the counter.",
                analysis: "Đã cụ thể hóa trang phục 'in a red uniform' và địa điểm 'at the counter'."
            },
            level3: {
                band: "Band 3 (Xuất sắc - 3 điểm tối đa)",
                sentence: "The cashier in a red uniform is scanning packaged grocery items with a barcode scanner.",
                analysis: "Cụ thể hóa hoàn hảo: nghề nghiệp rõ ràng (cashier), trang phục (in a red uniform), tân ngữ chi tiết (packaged grocery items) và công cụ (with a barcode scanner)."
            }
        }
    },
    {
        id: 2,
        title: "Thử Thách 02: Nâng Cấp Câu Mô Tả Hàng Hóa Trong Kho",
        image: "images/image13.jpeg",
        imageAlt: "Cardboard boxes stacked on warehouse floor",
        keywords: ["box", "stack"],
        levels: {
            level1: {
                band: "Band 1 (Cơ bản - 1 điểm)",
                sentence: "There are some boxes on the floor.",
                analysis: "Chỉ nêu sự tồn tại chung chung, chưa sử dụng đúng từ khóa 'stack'."
            },
            level2: {
                band: "Band 2 (Khá - 2 điểm)",
                sentence: "The cardboard boxes are stacked on the floor.",
                analysis: "Đã sử dụng cấu trúc bị động mô tả trạng thái 'are stacked' và xác định rõ 'cardboard boxes'."
            },
            level3: {
                band: "Band 3 (Xuất sắc - 3 điểm tối đa)",
                sentence: "Several large cardboard boxes are stacked neatly on the warehouse floor.",
                analysis: "Cụ thể hóa số lượng (several), kích thước (large), chủng loại (cardboard boxes), trạng thái (are stacked) và bối cảnh (warehouse floor)."
            }
        }
    }
];

const ETS_MOCK_TESTS = [
    {
        testId: 1,
        title: "ETS 2026 - FULL TEST 01",
        description: "Đề thi mô phỏng chuẩn ETS Writing Task 1 - Questions 1 to 5 (Thời gian: 8 phút)",
        durationMinutes: 8,
        questions: [
            {
                qNum: 1,
                image: "images/image12.png",
                keywords: ["woman", "scan"],
                vietnameseContext: "Người phụ nữ mặc đồng phục đang quét mã vạch sản phẩm tại quầy thanh toán.",
                keyRules: ["woman/cashier", "scan/scanning/scans"],
                sampleLevel1: "The woman is scanning some items.",
                sampleLevel2: "The woman in a red uniform is scanning items at the checkout counter.",
                sampleLevel3: "The woman in a red uniform is scanning packaged grocery items with a handheld barcode scanner.",
                explanation: "Keyword 1 là 'woman', keyword 2 là 'scan'. Thì thích hợp nhất là Hiện tại tiếp diễn (is scanning)."
            },
            {
                qNum: 2,
                image: "images/image13.jpeg",
                keywords: ["box", "stack"],
                vietnameseContext: "Nhiều thùng carton được xếp chồng lên nhau trên sàn kho.",
                keyRules: ["box/boxes", "stack/stacked/are stacked/is stacked"],
                sampleLevel1: "The boxes are stacked on the floor.",
                sampleLevel2: "There are several cardboard boxes stacked on the warehouse floor.",
                sampleLevel3: "Several large cardboard boxes are stacked on top of each other on the floor.",
                explanation: "Keyword 1 là 'box' (dạng số nhiều 'boxes'), keyword 2 là 'stack' (chia bị động 'are stacked' hoặc cụm phân từ 'stacked')."
            },
            {
                qNum: 3,
                image: "images/image3.png",
                keywords: ["man", "laptop"],
                vietnameseContext: "Người đàn ông đang ngồi làm việc và sử dụng máy tính xách tay tại bàn làm việc.",
                keyRules: ["man/men", "laptop/laptops"],
                sampleLevel1: "The man is using a laptop.",
                sampleLevel2: "The man is typing on his laptop at the desk.",
                sampleLevel3: "The man sitting at the wooden desk is actively working on his laptop computer.",
                explanation: "Sử dụng 'man' làm chủ ngữ và 'laptop' làm tân ngữ với động từ chia tiếp diễn (is using / is typing on / is working on)."
            },
            {
                qNum: 4,
                image: "images/image9.png",
                keywords: ["people", "discuss"],
                vietnameseContext: "Một nhóm đồng nghiệp đang ngồi quanh bàn họp thảo luận công việc.",
                keyRules: ["people", "discuss/discussing/are discussing"],
                sampleLevel1: "People are discussing a project.",
                sampleLevel2: "A group of people are discussing some documents around the table.",
                sampleLevel3: "Several business professionals are discussing work documents during a meeting in the conference room.",
                explanation: "Keyword 'people' là danh từ số nhiều, động từ 'discuss' chia thì tiếp diễn 'are discussing'."
            },
            {
                qNum: 5,
                image: "images/image10.png",
                keywords: ["passenger", "wait"],
                vietnameseContext: "Các hành khách đang đứng đợi tàu/xe buýt tại sân ga.",
                keyRules: ["passenger/passengers", "wait/waiting/are waiting"],
                sampleLevel1: "Passengers are waiting for the train.",
                sampleLevel2: "Several passengers are waiting on the platform with their luggage.",
                sampleLevel3: "A few passengers carrying their luggage are patiently waiting for the arriving train on the platform.",
                explanation: "Keyword 'passenger' (chuyển sang số nhiều 'passengers'), keyword 'wait' chia 'are waiting for...'."
            }
        ]
    },
    {
        testId: 2,
        title: "ETS 2026 - FULL TEST 02",
        description: "Đề thi mô phỏng chuẩn ETS Writing Task 1 - Questions 1 to 5 (Thời gian: 8 phút)",
        durationMinutes: 8,
        questions: [
            {
                qNum: 1,
                image: "images/image12.png",
                keywords: ["cashier", "customer"],
                vietnameseContext: "Nhân viên thu ngân đang phục vụ khách hàng tại quầy.",
                keyRules: ["cashier/cashiers", "customer/customers"],
                sampleLevel1: "The cashier is helping a customer.",
                sampleLevel2: "The cashier in a uniform is serving a customer at the checkout counter.",
                sampleLevel3: "The friendly cashier is handing the purchase receipt to the customer at the checkout counter.",
                explanation: "Kết hợp 2 danh từ 'cashier' và 'customer' trong cùng một câu hành động tương tác."
            },
            {
                qNum: 2,
                image: "images/image13.jpeg",
                keywords: ["warehouse", "floor"],
                vietnameseContext: "Các kiện hàng được bố trí trên sàn nhà kho.",
                keyRules: ["warehouse", "floor/floors"],
                sampleLevel1: "There are boxes on the warehouse floor.",
                sampleLevel2: "Cardboard packages are placed across the warehouse floor.",
                sampleLevel3: "Multiple storage boxes are organized systematically on the warehouse floor.",
                explanation: "Sử dụng 'warehouse floor' hoặc liên kết 2 danh từ qua cấu trúc tồn tại / bị động."
            },
            {
                qNum: 3,
                image: "images/image3.png",
                keywords: ["type", "keyboard"],
                vietnameseContext: "Người nhân viên đang gõ bàn phím máy tính.",
                keyRules: ["type/typing/types/is typing", "keyboard/keyboards"],
                sampleLevel1: "He is typing on a keyboard.",
                sampleLevel2: "The man is typing an email on the laptop keyboard.",
                sampleLevel3: "The office worker is rapidly typing information on his computer keyboard at his desk.",
                explanation: "Động từ 'type' chia tiếp diễn (is typing) đi với giới từ 'on' và tân ngữ 'the keyboard'."
            },
            {
                qNum: 4,
                image: "images/image9.png",
                keywords: ["meeting", "document"],
                vietnameseContext: "Cuộc họp có các tài liệu được đặt trên bàn.",
                keyRules: ["meeting/meetings", "document/documents"],
                sampleLevel1: "They review documents in the meeting.",
                sampleLevel2: "Colleagues are examining important documents during the team meeting.",
                sampleLevel3: "Several business partners are reviewing printed documents during a scheduled meeting around the table.",
                explanation: "Sử dụng 'documents' làm tân ngữ cho hành động xem xét và 'meeting' làm trạng ngữ thời gian/ngữ cảnh."
            },
            {
                qNum: 5,
                image: "images/image10.png",
                keywords: ["luggage", "carry"],
                vietnameseContext: "Người đi du lịch đang kéo/xách hành lý.",
                keyRules: ["luggage", "carry/carrying/carries/is carrying/are carrying"],
                sampleLevel1: "A traveler is carrying luggage.",
                sampleLevel2: "The passenger is carrying heavy luggage through the terminal.",
                sampleLevel3: "A woman dressed in casual clothes is carrying her travel luggage across the station platform.",
                explanation: "Lưu ý 'luggage' là danh từ không đếm được (không thêm -s). 'carry' chia 'is carrying'."
            }
        ]
    },
    {
        testId: 3,
        title: "ETS 2026 - FULL TEST 03",
        description: "Đề thi mô phỏng chuẩn ETS Writing Task 1 - Questions 1 to 5 (Thời gian: 8 phút)",
        durationMinutes: 8,
        questions: [
            {
                qNum: 1,
                image: "images/image12.png",
                keywords: ["uniform", "item"],
                vietnameseContext: "Người phụ nữ mặc đồng phục đang xử lý các món hàng.",
                keyRules: ["uniform/uniforms", "item/items"],
                sampleLevel1: "A woman in uniform scans items.",
                sampleLevel2: "The worker in a red uniform is scanning grocery items.",
                sampleLevel3: "The store assistant wearing a red uniform is carefully scanning grocery items for a customer.",
                explanation: "Sử dụng 'uniform' trong cụm 'in a ... uniform' / 'wearing a uniform' và 'items' làm tân ngữ."
            },
            {
                qNum: 2,
                image: "images/image13.jpeg",
                keywords: ["several", "package"],
                vietnameseContext: "Có một vài kiện hàng được xếp chồng trong phòng chứa đồ.",
                keyRules: ["several", "package/packages"],
                sampleLevel1: "There are several packages on the floor.",
                sampleLevel2: "Several cardboard packages are stacked inside the storage room.",
                sampleLevel3: "Several large shipping packages are stacked neatly against the wall on the floor.",
                explanation: "Sử dụng 'several' đứng trước danh từ số nhiều 'packages'."
            },
            {
                qNum: 3,
                image: "images/image3.png",
                keywords: ["screen", "look"],
                vietnameseContext: "Người nhân viên đang nhìn vào màn hình máy tính.",
                keyRules: ["screen/screens", "look/looking/looks/is looking"],
                sampleLevel1: "The man is looking at the screen.",
                sampleLevel2: "The employee is looking closely at the computer screen.",
                sampleLevel3: "The professional seated at the office desk is focused on looking at his monitor screen.",
                explanation: "Cụm động từ 'look at' chia tiếp diễn: 'is looking at the computer screen'."
            },
            {
                qNum: 4,
                image: "images/image9.png",
                keywords: ["colleague", "table"],
                vietnameseContext: "Các đồng nghiệp đang tụ họp quanh bàn làm việc.",
                keyRules: ["colleague/colleagues", "table/tables"],
                sampleLevel1: "Colleagues are sitting at a table.",
                sampleLevel2: "Several colleagues are gathered around a conference table to talk.",
                sampleLevel3: "A group of colleagues are seated around a modern wooden table during a collaborative discussion.",
                explanation: "Kết hợp chủ ngữ 'colleagues' với trạng từ nơi chốn 'around/at the table'."
            },
            {
                qNum: 5,
                image: "images/image10.png",
                keywords: ["platform", "train"],
                vietnameseContext: "Mọi người đang đứng trên sân ga đợi chuyến tàu.",
                keyRules: ["platform/platforms", "train/trains"],
                sampleLevel1: "People on the platform wait for a train.",
                sampleLevel2: "Passengers are standing on the railway platform awaiting the train.",
                sampleLevel3: "Several commuters waiting on the open platform are watching for the upcoming train.",
                explanation: "Giới từ đi với platform là 'on the platform', tàu hỏa là 'the train'."
            }
        ]
    },
    {
        testId: 4,
        title: "ETS 2026 - FULL TEST 04",
        description: "Đề thi mô phỏng chuẩn ETS Writing Task 1 - Questions 1 to 5 (Thời gian: 8 phút)",
        durationMinutes: 8,
        questions: [
            {
                qNum: 1,
                image: "images/image12.png",
                keywords: ["checkout", "hold"],
                vietnameseContext: "Nhân viên tại quầy thu ngân đang cầm máy quét.",
                keyRules: ["checkout", "hold/holding/holds/is holding"],
                sampleLevel1: "She is holding a scanner at the checkout.",
                sampleLevel2: "The clerk is holding an electronic scanner at the checkout counter.",
                sampleLevel3: "The retail staff member standing at the checkout area is holding a price scanner in her right hand.",
                explanation: "Động từ 'hold' chia tiếp diễn 'is holding', địa điểm 'at the checkout (counter)'."
            },
            {
                qNum: 2,
                image: "images/image13.jpeg",
                keywords: ["arrange", "storage"],
                vietnameseContext: "Các hộp hàng được sắp xếp trong khu vực lưu trữ.",
                keyRules: ["arrange/arranged/are arranged/is arranged", "storage"],
                sampleLevel1: "Boxes are arranged in the storage area.",
                sampleLevel2: "Many shipping cartons are arranged neatly in the storage facility.",
                sampleLevel3: "Numerous cardboard boxes are carefully arranged in rows across the warehouse storage space.",
                explanation: "Động từ 'arrange' chia bị động 'are arranged', 'storage area / storage room'."
            },
            {
                qNum: 3,
                image: "images/image3.png",
                keywords: ["desk", "sit"],
                vietnameseContext: "Người đàn ông đang ngồi tại bàn làm việc của mình.",
                keyRules: ["desk/desks", "sit/sitting/sits/is sitting"],
                sampleLevel1: "A man is sitting at a desk.",
                sampleLevel2: "An employee is sitting at his wooden desk using a laptop.",
                sampleLevel3: "A male office worker dressed in formal attire is sitting comfortably at his work desk.",
                explanation: "Động từ 'sit' chia tiếp diễn gấp đôi chữ t: 'is sitting at the desk'."
            },
            {
                qNum: 4,
                image: "images/image9.png",
                keywords: ["listen", "presentation"],
                vietnameseContext: "Các nhân viên đang lắng nghe bài thuyết trình trong phòng họp.",
                keyRules: ["listen/listening/listens/are listening", "presentation/presentations"],
                sampleLevel1: "They are listening to a presentation.",
                sampleLevel2: "The team members are attentively listening to a business presentation.",
                sampleLevel3: "All attendees in the meeting room are quietly listening to the ongoing project presentation.",
                explanation: "Cụm động từ 'listen to' chia 'are listening to a presentation'."
            },
            {
                qNum: 5,
                image: "images/image10.png",
                keywords: ["stand", "line"],
                vietnameseContext: "Hành khách đang đứng xếp hàng chờ lên phương tiện.",
                keyRules: ["stand/standing/stands/are standing", "line/lines"],
                sampleLevel1: "People are standing in line.",
                sampleLevel2: "The passengers are standing in a straight line at the station.",
                sampleLevel3: "A row of travelers carrying luggage are standing in line waiting to board the transport.",
                explanation: "Cụm từ chuẩn 'stand in line' (đứng xếp hàng): 'are standing in line'."
            }
        ]
    },
    {
        testId: 5,
        title: "ETS 2026 - FULL TEST 05",
        description: "Đề thi mô phỏng chuẩn ETS Writing Task 1 - Questions 1 to 5 (Thời gian: 8 phút)",
        durationMinutes: 8,
        questions: [
            {
                qNum: 1,
                image: "images/image12.png",
                keywords: ["barcode", "counter"],
                vietnameseContext: "Thiết bị quét mã vạch được sử dụng tại quầy thanh toán.",
                keyRules: ["barcode", "counter/counters"],
                sampleLevel1: "A barcode is scanned at the counter.",
                sampleLevel2: "The worker is scanning a barcode on the item at the counter.",
                sampleLevel3: "The cashier uses a modern scanner to read the barcode of groceries on the counter.",
                explanation: "Kết hợp 'barcode' và 'counter' trong câu mô tả thao tác thanh toán."
            },
            {
                qNum: 2,
                image: "images/image13.jpeg",
                keywords: ["cardboard", "pile"],
                vietnameseContext: "Các thùng bìa cứng được chất thành đống trên sàn.",
                keyRules: ["cardboard", "pile/piled/are piled/piles"],
                sampleLevel1: "Cardboard boxes are piled on the floor.",
                sampleLevel2: "There is a pile of cardboard containers in the center of the room.",
                sampleLevel3: "Several sturdy cardboard boxes are piled up systematically on the concrete floor.",
                explanation: "'cardboard' bổ nghĩa cho boxes (cardboard boxes) và 'pile' chia bị động 'are piled' hoặc 'a pile of'."
            },
            {
                qNum: 3,
                image: "images/image3.png",
                keywords: ["work", "office"],
                vietnameseContext: "Người đàn ông đang làm việc một mình trong văn phòng.",
                keyRules: ["work/working/works/is working", "office/offices"],
                sampleLevel1: "A man is working in an office.",
                sampleLevel2: "The businessman is working on his laptop in a bright office.",
                sampleLevel3: "A dedicated professional is working diligently at his personal computer inside a quiet office.",
                explanation: "'work' chia tiếp diễn 'is working', địa điểm 'in an office' hoặc 'in the office'."
            },
            {
                qNum: 4,
                image: "images/image9.png",
                keywords: ["gather", "conference"],
                vietnameseContext: "Mọi người tụ họp trong phòng hội nghị.",
                keyRules: ["gather/gathered/gathering/are gathered", "conference"],
                sampleLevel1: "They gather in a conference room.",
                sampleLevel2: "A team of managers are gathered inside the conference room.",
                sampleLevel3: "Several corporate executives are gathered around the central table for a crucial conference.",
                explanation: "'gather' chia 'are gathered' (tụ họp) đi với 'in the conference room'."
            },
            {
                qNum: 5,
                image: "images/image10.png",
                keywords: ["traveler", "station"],
                vietnameseContext: "Những người đi lại đang có mặt tại nhà ga.",
                keyRules: ["traveler/travelers", "station/stations"],
                sampleLevel1: "Travelers are at the station.",
                sampleLevel2: "Several travelers with suitcases are walking through the busy station.",
                sampleLevel3: "Many travelers holding their tickets and baggage are gathering near the main platform at the railway station.",
                explanation: "'travelers' làm chủ ngữ số nhiều và 'station' trong cụm 'at the train/railway station'."
            }
        ]
    }
];

if (typeof module !== 'undefined' && module.exports) {
    module.exports = { OVERVIEW_DATA, GRAMMAR_CHAPTERS, UNSCRAMBLE_EXERCISES, UPGRADER_CHALLENGES, ETS_MOCK_TESTS };
}
"""

with open('/Users/nguyetpham/Desktop/TEACHING/TOEIC 2026/BÀI GIẢNG/toeic_writing_web/js/data.js', 'w', encoding='utf-8') as f:
    f.write(data_js_content)

print("Generated data.js successfully with full Overview, Grammar chapters, Unscramble games, Upgrader challenges, and 5 ETS Mock Tests!")
