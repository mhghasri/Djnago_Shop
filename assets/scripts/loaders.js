(function () {
  var overlay = document.getElementById("x__ldr_9f3c_overlay");
  if (!overlay) return;
  var startedAt = performance.now();

  window.addEventListener("load", function () {
    var elapsed = performance.now() - startedAt;
    var minDuration = 1000; // حداقل ۱ ثانیه
    var wait = Math.max(minDuration - elapsed, 0);

    setTimeout(function () {
      // محو نرم
      overlay.classList.add("x-hide");

      // بعد از اتمام ترنزیشن، کامل حذف می‌شود
      var removeIt = function () {
        overlay && overlay.removeEventListener("transitionend", removeIt);
        if (overlay && overlay.parentNode)
          overlay.parentNode.removeChild(overlay);
      };
      overlay.addEventListener("transitionend", removeIt, { once: true });

      // فالبک اگر transitionend رخ نداد
      setTimeout(removeIt, 700);
    }, wait);
  });
})();