 
// 
  const phrases = document.querySelector('#phrases');

  phrases.addEventListener('click', function(event) {
    if (event.target.tagName === 'LI') { // LI要素がクリックされたか確認
      const selectedPhrase = event.target.textContent.trim();
      const outputBox = document.querySelector("#copyBodyTarget");

      // 現在のカーソル位置を取得
      const cursorPosition = outputBox.selectionStart;

      // テキストを分割して挿入
      const textBeforeCursor = outputBox.value.substring(0, cursorPosition);
      const textAfterCursor = outputBox.value.substring(cursorPosition);

      // 新しい値を設定
      outputBox.value = textBeforeCursor + selectedPhrase + textAfterCursor;

      // カーソル位置を調整（挿入したフレーズの後ろに設定）
      outputBox.selectionStart = outputBox.selectionEnd = cursorPosition + selectedPhrase.length;

      // テキストエリアにフォーカスを戻す
      outputBox.focus();
    }
  });

const toggleButton = document.getElementById("toggleDetailsButton");
const detailsSection = document.getElementById("detailsSection");
toggleButton.addEventListener("click", () => {
    if (detailsSection.style.display === "none") {
        detailsSection.style.display = "block";
        toggleButton.textContent = "詳細設定を閉じる";
    } else {
        detailsSection.style.display = "none";
        toggleButton.textContent = "詳細設定を開く";
    }
});


// 本文コピー部分
  function copyBodyToClipboard() {
    const copyBodyTarget = document.getElementById("copyBodyTarget");
    copyBodyTarget.select();
    document.execCommand("Copy");
    alert("コピーできました！ : " + copyBodyTarget.value);
  }
// AI添削コピー部分
  function copyToClipboard() {
    const copyTarget = document.getElementById("copyTarget");
    copyTarget.select();
    document.execCommand("Copy");
    alert("コピーできました！ : " + copyTarget.value);
  }

