const button_main_bot = document.querySelector('#button_main_bot a');
const name = 'button_main_bot';

button_main_bot.addEventListener('click', (e) => {
    let clicks = Number(localStorage.getItem(`clicks_${name}`));
    clicks += 1;
    localStorage.setItem(`clicks_${name}`, clicks);

    console.log(`Кнопка ${name}: ${clicks}`);
})