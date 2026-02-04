const button_hero_card2 = document.querySelector('#button_hero_card2');
const name = 'button_hero_card2';

button_hero_card2.addEventListener('click', (e) => {
    let clicks = Number(localStorage.getItem(`clicks_${name}`));
    clicks += 1;
    localStorage.setItem(`clicks_${name}`, clicks);

    console.log(`Кнопка ${name}: ${clicks}`);
})