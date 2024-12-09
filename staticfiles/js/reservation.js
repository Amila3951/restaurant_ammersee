document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const redirectTo = urlParams.get('next');
  
    if (redirectTo) {
      window.location.href = redirectTo;
    }
  });