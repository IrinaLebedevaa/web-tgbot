const button_hero_card3 = document.querySelector('#button_hero_card3');
const name = 'button_hero_card3';

button_hero_card3.addEventListener('click', (e) => {
    let clicks = Number(localStorage.getItem(`clicks_${name}`));
    clicks += 1;
    localStorage.setItem(`clicks_${name}`, clicks);

    console.log(`Кнопка ${name}: ${clicks}`);
})