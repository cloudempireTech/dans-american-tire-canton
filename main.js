// Dan's American Tire - Precision Auto Care Engine
document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Menu Toggle
  const mobileToggle = document.querySelector('.mobile-toggle');
  const mobileDrawer = document.querySelector('.mobile-menu-drawer');

  if (mobileToggle && mobileDrawer) {
    mobileToggle.addEventListener('click', () => {
      mobileDrawer.classList.toggle('open');
      const isOpen = mobileDrawer.classList.contains('open');
      mobileToggle.setAttribute('aria-expanded', isOpen);
    });
  }

  // 2. Dynamic Typewriter Headline
  const typewriterEl = document.querySelector('.typewriter-text');
  if (typewriterEl) {
    const phrases = [
      'All-Season & Performance Tires',
      'Hunter Laser 4-Wheel Alignments',
      'Ceramic Brake & Rotor Services',
      'Steering & Suspension Overhauls',
      'Commercial Fleet Truck Support'
    ];
    let phraseIdx = 0;
    let charIdx = 0;
    let isDeleting = false;
    let typingSpeed = 100;

    function typeLoop() {
      const currentPhrase = phrases[phraseIdx];
      if (isDeleting) {
        typewriterEl.textContent = currentPhrase.substring(0, charIdx - 1);
        charIdx--;
        typingSpeed = 50;
      } else {
        typewriterEl.textContent = currentPhrase.substring(0, charIdx + 1);
        charIdx++;
        typingSpeed = 110;
      }

      if (!isDeleting && charIdx === currentPhrase.length) {
        typingSpeed = 2200;
        isDeleting = true;
      } else if (isDeleting && charIdx === 0) {
        isDeleting = false;
        phraseIdx = (phraseIdx + 1) % phrases.length;
        typingSpeed = 500;
      }

      setTimeout(typeLoop, typingSpeed);
    }
    typeLoop();
  }

  // 3. Animated Number Counters
  const counterEls = document.querySelectorAll('.stat-number');
  if (counterEls.length > 0) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const target = parseInt(el.getAttribute('data-target'), 10);
          const prefix = el.getAttribute('data-prefix') || '';
          const suffix = el.getAttribute('data-suffix') || '';
          let count = 0;
          const duration = 1800;

          const timer = setInterval(() => {
            count += Math.ceil(target / 45);
            if (count >= target) {
              el.textContent = `${prefix}${target.toLocaleString()}${suffix}`;
              clearInterval(timer);
            } else {
              el.textContent = `${prefix}${count.toLocaleString()}${suffix}`;
            }
          }, 35);

          observer.unobserve(el);
        }
      });
    }, { threshold: 0.2 });

    counterEls.forEach(el => observer.observe(el));
  }

  // 4. Interactive Tire & Maintenance Triage Widget
  const triageBtn = document.getElementById('btnCalculateTriage');
  if (triageBtn) {
    triageBtn.addEventListener('click', (e) => {
      e.preventDefault();
      const checkboxes = document.querySelectorAll('input[name="car_symptom"]:checked');
      const vehicleType = document.getElementById('vehicleType') ? document.getElementById('vehicleType').value : '';
      const tireSeason = document.getElementById('tireSeason') ? document.getElementById('tireSeason').value : '';
      const resultTitle = document.getElementById('triageResultTitle');
      const resultDesc = document.getElementById('triageResultDesc');
      const resultUrgency = document.getElementById('triageResultUrgency');

      if (checkboxes.length === 0) {
        resultTitle.textContent = "Complimentary Tire & Alignment Safety Check";
        resultDesc.textContent = "Bring your vehicle by our 4570 Tuscarawas St W shop in Canton for a free optical tread depth measurement, tire pressure check, and visual brake inspection.";
        resultUrgency.innerHTML = "<strong>Shop Status:</strong> No appointment needed for quick tread inspections.";
        return;
      }

      let symptoms = Array.from(checkboxes).map(cb => cb.value);

      if (symptoms.includes('pulling') || symptoms.includes('wear')) {
        resultTitle.textContent = "Hunter Hawkeye 4-Wheel Alignment & Rotation";
        resultDesc.textContent = `Uneven shoulder wear or drift to one side indicates camber/toe misalignment. Our laser optical alignment restores true tracking, saving hundreds in premature tire wear.`;
        resultUrgency.innerHTML = "<strong>Urgency: Moderate.</strong> Driving out of alignment cuts tire lifespan by over 50%.";
      } else if (symptoms.includes('vibration')) {
        resultTitle.textContent = "Hunter Road Force Balancing & Rim Trueing";
        resultDesc.textContent = `Steering wheel shaking above 50-60 mph signals dynamic wheel imbalance or radial tire runout. Road Force balancing eliminates hidden vibrations standard balancers miss.`;
        resultUrgency.innerHTML = "<strong>Recommendation:</strong> Schedule Road Force balance on all 4 wheels.";
      } else if (symptoms.includes('brakes')) {
        resultTitle.textContent = "Ceramic Brake Service & Rotor Inspection";
        resultDesc.textContent = `High-pitched squealing or pedal pulsation indicates worn friction pads or rotor thickness variation. We install low-dust ceramic pads and precision-machine rotors.`;
        resultUrgency.innerHTML = "<strong>Safety Priority: High.</strong> Brake lining inspection recommended immediately.";
      } else if (symptoms.includes('clunking')) {
        resultTitle.textContent = "Suspension & Steering Component Triage";
        resultDesc.textContent = `Clunking over Canton road bumps points to worn sway bar links, ball joints, or leaking struts. Comprehensive front-end chassis inspection included.`;
        resultUrgency.innerHTML = "<strong>Status: Complete Chassis Evaluation.</strong> ASE-certified inspection.";
      } else {
        resultTitle.textContent = "New Tire Package & Installation";
        resultDesc.textContent = `Select from top-rated ${tireSeason} tires for your ${vehicleType}. Package includes computerized mounting, new rubber valve stems, and lifetime rotations.`;
        resultUrgency.innerHTML = "<strong>Stock Ready:</strong> Major brands in stock at our Canton location.";
      }
    });
  }
});
