/**
 * St. Joseph College of Arts and Science (SJCAS)
 * Main Interactive Application Script
 */

document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initMobileDrawer();
  initBackToTop();
  initCourseFilters();
  initAccordions();
  initCommitteeSearch();
  initGalleryLightbox();
  initGalleryCategoryFilters();
  initAdmissionForm();
  initEligibilityChecker();
  initNoticeBoardTabs();
});

/**
 * Sticky Header and Scroll Tracking
 */
function initStickyHeader() {
  const header = document.querySelector('.main-header');
  const backToTop = document.querySelector('.back-to-top');

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;

    if (header) {
      if (scrollY > 60) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    }

    if (backToTop) {
      if (scrollY > 400) {
        backToTop.classList.add('show');
      } else {
        backToTop.classList.remove('show');
      }
    }
  });

  if (backToTop) {
    backToTop.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
}

/**
 * Mobile Drawer Menu
 */
function initMobileDrawer() {
  const toggleBtn = document.querySelector('.mobile-toggle');
  const drawer = document.querySelector('.mobile-drawer');
  const overlay = document.querySelector('.mobile-drawer-overlay');
  const closeBtn = document.querySelector('.drawer-close');
  const submenuToggles = document.querySelectorAll('.drawer-submenu-toggle');

  if (!toggleBtn || !drawer || !overlay) return;

  function openDrawer() {
    drawer.classList.add('active');
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    drawer.classList.remove('active');
    overlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  toggleBtn.addEventListener('click', openDrawer);
  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  overlay.addEventListener('click', closeDrawer);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('active')) {
      closeDrawer();
    }
  });

  // Accordion submenus in drawer
  submenuToggles.forEach(toggle => {
    toggle.addEventListener('click', (e) => {
      e.preventDefault();
      const parent = toggle.closest('.drawer-nav-item');
      const submenu = parent.querySelector('.drawer-submenu');
      const icon = toggle.querySelector('i');

      if (submenu) {
        submenu.classList.toggle('open');
        if (icon) {
          icon.style.transform = submenu.classList.contains('open') ? 'rotate(180deg)' : 'rotate(0deg)';
        }
      }
    });
  });
}

/**
 * Back to Top
 */
function initBackToTop() {
  // Handled in initStickyHeader
}

/**
 * Course Category Filtering
 */
function initCourseFilters() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const courseCards = document.querySelectorAll('.course-card');

  if (!filterBtns.length || !courseCards.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filterValue = btn.getAttribute('data-filter');

      courseCards.forEach(card => {
        const category = card.getAttribute('data-category');
        if (filterValue === 'all' || category === filterValue || category?.includes(filterValue)) {
          card.style.display = 'flex';
          card.style.opacity = '0';
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transition = 'opacity 0.3s ease';
          }, 10);
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/**
 * Accordion Component (Committees, FAQs)
 */
function initAccordions() {
  const accordionItems = document.querySelectorAll('.accordion-item');

  accordionItems.forEach(item => {
    const trigger = item.querySelector('.accordion-trigger');
    const content = item.querySelector('.accordion-content');

    if (!trigger || !content) return;

    trigger.addEventListener('click', () => {
      const isActive = item.classList.contains('active');

      // Close all other accordions in the same wrapper if required
      const wrapper = item.closest('.accordion-wrapper');
      if (wrapper && !wrapper.dataset.multiple) {
        wrapper.querySelectorAll('.accordion-item').forEach(other => {
          if (other !== item) {
            other.classList.remove('active');
            const otherContent = other.querySelector('.accordion-content');
            if (otherContent) otherContent.style.maxHeight = null;
          }
        });
      }

      if (isActive) {
        item.classList.remove('active');
        content.style.maxHeight = null;
      } else {
        item.classList.add('active');
        content.style.maxHeight = content.scrollHeight + 'px';
      }
    });
  });
}

/**
 * Committee Live Search
 */
function initCommitteeSearch() {
  const searchInput = document.getElementById('committeeSearch');
  const items = document.querySelectorAll('.committee-item');

  if (!searchInput || !items.length) return;

  searchInput.addEventListener('input', () => {
    const query = searchInput.value.toLowerCase().trim();

    items.forEach(item => {
      const text = item.textContent.toLowerCase();
      if (text.includes(query)) {
        item.style.display = '';
      } else {
        item.style.display = 'none';
      }
    });
  });
}

/**
 * Gallery Lightbox Modal
 */
function initGalleryLightbox() {
  const galleryItems = document.querySelectorAll('.gallery-item');
  const lightbox = document.getElementById('galleryLightbox');
  if (!lightbox) return;

  const lightboxImg = lightbox.querySelector('.lightbox-img');
  const lightboxCaption = lightbox.querySelector('.lightbox-caption');
  const closeBtn = lightbox.querySelector('.modal-close-btn');

  galleryItems.forEach(item => {
    item.addEventListener('click', () => {
      const img = item.querySelector('img');
      const caption = item.getAttribute('data-caption') || img?.alt || 'St. Joseph Campus';

      if (img && lightboxImg) {
        lightboxImg.src = img.src;
        if (lightboxCaption) lightboxCaption.textContent = caption;
        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden';
      }
    });
  });

  function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) closeLightbox();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && lightbox.classList.contains('active')) {
      closeLightbox();
    }
  });
}

/**
 * Interactive Gallery Category Filter
 */
function initGalleryCategoryFilters() {
  const filterBtns = document.querySelectorAll('.gallery-filter-btn');
  const galleryItems = document.querySelectorAll('.gallery-item');

  if (!filterBtns.length || !galleryItems.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const category = btn.getAttribute('data-category');

      galleryItems.forEach(item => {
        const itemCat = item.getAttribute('data-category');
        if (category === 'all' || itemCat === category || itemCat?.includes(category)) {
          item.style.display = 'block';
          item.style.opacity = '0';
          setTimeout(() => {
            item.style.opacity = '1';
            item.style.transition = 'opacity 0.3s ease';
          }, 10);
        } else {
          item.style.display = 'none';
        }
      });
    });
  });
}

/**
 * Admission Enquiry & Instant Form Handler
 */
function initAdmissionForm() {
  const form = document.getElementById('admissionEnquiryForm');
  const confirmationModal = document.getElementById('confirmationModal');

  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = form.querySelector('[name="studentName"]')?.value;
    const phone = form.querySelector('[name="studentPhone"]')?.value;
    const course = form.querySelector('[name="preferredCourse"]')?.value;

    if (!name || !phone || !course) {
      alert('Please complete all required fields.');
      return;
    }

    // Save lead in localStorage for demo resilience
    const enquiries = JSON.parse(localStorage.getItem('sjcas_enquiries') || '[]');
    enquiries.push({
      name,
      phone,
      course,
      date: new Date().toISOString()
    });
    localStorage.setItem('sjcas_enquiries', JSON.stringify(enquiries));

    // Show confirmation modal
    if (confirmationModal) {
      const studentNameDisplay = confirmationModal.querySelector('.student-name-display');
      if (studentNameDisplay) studentNameDisplay.textContent = name;
      confirmationModal.classList.add('active');
    } else {
      alert(`Thank you, ${name}! Your admission enquiry for ${course} has been registered. Our admissions office will contact you at ${phone}.`);
    }

    form.reset();
  });

  // Modal dismiss buttons
  const modalCloses = document.querySelectorAll('.close-modal');
  modalCloses.forEach(btn => {
    btn.addEventListener('click', () => {
      const modal = btn.closest('.modal-overlay');
      if (modal) modal.classList.remove('active');
    });
  });
}

/**
 * Quick Course Eligibility Checker
 */
function initEligibilityChecker() {
  const checkerBtn = document.getElementById('checkEligibilityBtn');
  const streamSelect = document.getElementById('checkerStream');
  const resultDiv = document.getElementById('eligibilityResult');

  if (!checkerBtn || !streamSelect || !resultDiv) return;

  checkerBtn.addEventListener('click', () => {
    const stream = streamSelect.value;
    if (!stream) {
      resultDiv.innerHTML = '<div style="color: #ea580c; font-weight: 600;">Please select your +2 Stream.</div>';
      resultDiv.style.display = 'block';
      return;
    }

    let recommendations = [];
    if (stream === 'maths-bio' || stream === 'maths-cs') {
      recommendations = [
        'B.Sc. Computer Science',
        'B.Sc. Mathematics',
        'B.Sc. Physics',
        'B.Com (General)',
        'B.Com (Corporate Secretaryship)',
        'B.A. English Literature',
        'B.A. Tamil'
      ];
    } else if (stream === 'commerce') {
      recommendations = [
        'B.Com (General)',
        'B.Com (Corporate Secretaryship)',
        'B.A. English Literature',
        'B.A. Tamil'
      ];
    } else if (stream === 'arts') {
      recommendations = [
        'B.A. English Literature',
        'B.A. Tamil',
        'B.Com (Corporate Secretaryship)'
      ];
    }

    let html = `<div style="background-color: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 8px; padding: 1rem; margin-top: 1rem;">
      <h5 style="color: #065f46; font-size: 0.95rem; margin-bottom: 0.5rem; font-weight: 700;">
        <i class="fas fa-check-circle"></i> Eligible Courses for Your Stream:
      </h5>
      <ul style="padding-left: 1.25rem; list-style-type: disc; color: #047857; font-size: 0.9rem;">
        ${recommendations.map(r => `<li style="margin-bottom: 0.25rem;"><strong>${r}</strong></li>`).join('')}
      </ul>
      <p style="font-size: 0.8rem; color: #047857; margin-top: 0.5rem;">
        *All courses are affiliated to Manonmaniam Sundaranar University (MSU).
      </p>
    </div>`;

    resultDiv.innerHTML = html;
    resultDiv.style.display = 'block';
  });
}

/**
 * Notice Board Dual-Tab Switcher
 */
function initNoticeBoardTabs() {
  const tabBtns = document.querySelectorAll('.notice-tab-btn');
  const panes = document.querySelectorAll('.notice-pane');

  if (!tabBtns.length || !panes.length) return;

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetPaneId = btn.getAttribute('data-target');
      if (!targetPaneId) return;

      tabBtns.forEach(b => b.classList.remove('active'));
      panes.forEach(p => p.classList.remove('active'));

      btn.classList.add('active');
      const targetPane = document.getElementById(targetPaneId);
      if (targetPane) {
        targetPane.classList.add('active');
      }
    });
  });
}


