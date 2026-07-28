document.addEventListener('DOMContentLoaded', init);

const allModules = [];
const allProjects = [];
const allTimelineItems = [];

function init() {
  // Initialize modules animations
  const modules = document.querySelectorAll('.module-card');
  allModules.push(...modules);
  setupIntersectionObserver(modules, 'animate-in');

  // Initialize projects animations
  const projects = document.querySelectorAll('.project-card');
  allProjects.push(...projects);
  setupIntersectionObserver(projects, 'project-animate');

  // Initialize timeline animations
  const timelineItems = document.querySelectorAll('.timeline-item');
  allTimelineItems.push(...timelineItems);
  setupIntersectionObserver(timelineItems, 'timeline-reveal');

  // Initialize status dot animation
  const statusDot = document.querySelector('.status-dot');
  statusDot.style.animation = 'status-blink 2s ease-in-out infinite';
}

function setupIntersectionObserver(elements, animationClass) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add(animationClass);
      }
    });
  }, { threshold: 0.5 });

  elements.forEach(element => {
    observer.observe(element);
  });
}

// Project hover effects
document.querySelectorAll('.project-card').forEach(card => {
  card.addEventListener('mouseenter', () => {
    card.style.boxShadow = '0 8px 40px rgba(220,38,38,0.2)';
    card.style.transform = 'translateY(-2px)';
  });

  card.addEventListener('mouseleave', () => {
    card.style.boxShadow = '0 0 30px rgba(220,38,38,0.1)';
    card.style.transform = 'translateY(0)';
  });
});

// Terminal typing effect
const terminal = document.querySelector('.terminal');
if (terminal) {
  const lines = terminal.querySelectorAll('.terminal-line');
  lines.forEach((line, index) => {
    setTimeout(() => {
      line.style.opacity = '1';
      line.style.transform = 'translateX(0)';
    }, index * 300);
  });
}
