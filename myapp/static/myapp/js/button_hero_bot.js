const button_hero_bot = document.querySelector('#button_hero_bot a');
const name = 'button_hero_bot';

button_hero_bot.addEventListener('click', (e) => {
    let clicks = Number(localStorage.getItem(`clicks_${name}`));
    clicks += 1;
    localStorage.setItem(`clicks_${name}`, clicks);

    console.log(`Кнопка ${name}: ${clicks}`);
})