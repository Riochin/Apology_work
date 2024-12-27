const picker = document.querySelector('#picker');

const setBgColor = () => {
  document.body.style.backgroundColor = picker.value;
 }

picker.addEventListener('input', setBgColor)