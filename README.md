# St. Joseph College of Arts and Science (SJCAS) - Official Web Portal

> **Institution:** St. Joseph College of Arts and Science  
> **Location:** JNP Nagar, Vaikalipatti, Mettur (PO), Kadayam, Tenkasi District – 627 808, Tamil Nadu, India  
> **Affiliation:** Affiliated to Manonmaniam Sundaranar University (MSU), Tirunelveli  
> **Management:** Roman Catholic Diocese of Palayamkottai  
> **Motto:** *“To know oneself and To know God”*  
> **Official Website:** [sjcas.edu.in](https://sjcas.edu.in)

---

## 🏛️ Project Overview

This project is a modern, responsive redesign and web portal for **St. Joseph College of Arts and Science (SJCAS)**. Built using authentic institutional data, official photography, leadership profiles, and academic rosters scraped from the college's website.

The redesign resolves the legacy template issues (broken placeholder links, missing responsive support, outdated layout) and delivers a collegiate user experience tailored for students, parents, faculty, and administrative regulators.

---

## ✨ Key Features & Architecture

### 1. 📱 100% Mobile-First & Cross-Device Responsive
- **Fluid Layout**: Seamlessly adapts from small mobile screens (320px–480px), tablets (768px–1024px) to 4K ultra-wide monitors.
- **Off-Canvas Mobile Drawer**: Slide-in touch navigation drawer with collapsible accordion sub-menus.
- **Adaptive Breakpoints**: Smart typography scaling with CSS `clamp()`, flexible grids, and automated image containment.

### 2. 🎓 Academic Course Explorer & Filter
- **Interactive Stream Filter**: Filter programmes between **All**, **Science & Technology**, **Commerce & Management**, and **Arts & Languages**.
- **7 MSU-Affiliated Undergraduate Programmes**:
  1. `B.Sc. Computer Science`
  2. `B.Sc. Mathematics`
  3. `B.Sc. Physics`
  4. `B.Com. (General)`
  5. `B.Com. Corporate Secretaryship`
  6. `B.A. English Literature`
  7. `B.A. Tamil (தமிழ்)`
- Program cards complete with duration, semester breakdown, curriculum tags, eligibility criteria, and direct application triggers.

### 3. 🎯 Instant Stream Eligibility Finder
- Prospective students select their +2 / Higher Secondary stream (Maths/Bio, Commerce, Arts) to instantly view eligible degree programmes.

### 4. 📝 Admissions Portal 2025–2026
- Complete 5-step admission roadmap.
- Form validation with 10-digit mobile number regex check, interactive confirmation modal, and direct integration with the official Google Admission Form.
- Documents checklist and government/diocesan scholarship guidance.

### 5. ⚖️ Statutory Committees & Regulatory Governance
- Searchable directory of **all 17 official institutional committees** (with real coordinators and faculty members from SJCAS):
  - Planning and Monitoring Committee
  - Discipline and Welfare Committee
  - Anti-Ragging Committee (Zero Tolerance policy)
  - Complaints Cum Redressal Committee
  - Women Redressal Committee
  - Internal Complaints Committee (ICC) & Sexual Harassment Prevention
  - Admission Committee
  - Examination Committee
  - Internal Quality Assurance Cell (IQAC)
  - Research Committee
  - Sports and Games Committee
  - Library Committee
  - Fine Arts & Literary Committees
  - Public Relations Committee
  - Anti-Drug Committee
  - Prayer Service & College Website Committees

### 6. 🤝 Extension Wings & Student Life
- Detailed coverage of **NSS (National Service Scheme)**, **YRC (Youth Red Cross)**, **Enviro Club**, **Eat Right Club**, **EDI (Entrepreneurship Development & Innovation)**, and **Placement Cell**.
- Sports facilities & athletic achievements under Physical Education.

### 7. 📸 Campus Photo Gallery & Modal Lightbox
- High-resolution photographs of campus buildings, assemblies, laboratories, and events.
- Full-screen lightbox modal with ESC key dismissal and backdrop click support.

### 8. 🗺️ Location & Transit Guide
- Embedded interactive Google Map for Vaikalipatti, Kadayam, Tenkasi.
- Bus route connections across Tenkasi, Kadayam, Alangulam, Pavoorchatram, and Surandai.

---

## 📂 Site Structure

```
st.joseph.com/
│
├── index.html            # Main Portal Homepage
├── about.html            # Institutional Heritage, Vision, Mission, Governing Body, Organogram
├── academics.html        # Academic Departments, Syllabi, Central Library & Science Labs
├── admissions.html       # Admission Guidelines 2025-2026, Eligibility Matrix, Scholarships
├── governance.html       # 17 Statutory Committees, Anti-Ragging Cell, IQAC & ICC Rosters
├── campus-life.html      # Extension Activities (NSS, YRC, Clubs), Sports & Full Gallery
├── contact.html          # Contact Cards, Interactive Map, Directions & Grievance Desk
│
└── assets/
    ├── css/
    │   └── style.css     # Master responsive stylesheet (CSS variables, modern grid, animations)
    ├── js/
    │   └── main.js       # Client application logic (sticky header, mobile drawer, filters, modals)
    └── images/
        ├── logo.png      # Official College Crest Emblem
        ├── logo-white.png
        ├── campus/       # Campus architecture, libraries, computer labs, assemblies
        ├── leadership/   # Secretary, Principal, Bishop, Governing Body portraits
        └── gallery/      # 8 high-res campus event and student photographs
```

---

## 🚀 How to Run Locally

Because the portal is engineered using pure modern HTML5, CSS3, and Vanilla JavaScript, it requires no heavy runtime dependencies or build steps.

### Method 1: Direct File Opening
Double-click `index.html` to open directly in any modern browser (Chrome, Edge, Firefox, Safari).

### Method 2: Local HTTP Server
Run with Python:
```bash
python -m http.server 8080
```
Then visit:
```
http://localhost:8080/index.html
```

---

## 🎨 Design System

- **Primary Navy:** `#0a1f44` (Oxford academic blue)
- **Secondary Crimson:** `#c2410c` (Regal academic rust)
- **Royal Amber / Gold:** `#d97706` (Accent highlights)
- **Neutral Base:** `#f8fafc` & `#ffffff`
- **Typography:**
  - Display / Headings: `Playfair Display` (Serif elegance)
  - Interface / Body: `Inter` (High-legibility sans-serif)

