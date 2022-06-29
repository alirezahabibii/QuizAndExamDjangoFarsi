const modalBtns = [...document.getElementsByClassName('modal-button')];
const modalBody = document.getElementById('modal-body-confirm');
const statrBtn = document.getElementById('start-button');

const url = window.location.href;
modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', () => {
    const pk = modalBtn.getAttribute('data-pk');
    const name = modalBtn.getAttribute('data-quiz');
    const nameQuestions = modalBtn.getAttribute('data-questions');
    const difficulty = modalBtn.getAttribute('data-difficulty');
    const time = modalBtn.getAttribute('data-time');
    const scoreToPass = modalBtn.getAttribute('data-pass');

    modalBody.innerHTML = `
    <div class="h5 mb-3 text-right" dir="rtl">آیا مطمئن هستید که می خواهید شروع کنید؟ <b>(${name})</b></div>
    <div class="text-muted text-right" dir="rtl">
        <ul>
            <li>دشواری: <b>${difficulty}</b></li>
            <li>تعداد سوالات: <b>${nameQuestions}</b></li>
            <li>امتیاز برای پاس: <b>%${scoreToPass}</b></li>
            <li>زمان: <b>${time} دقیقه</b></li>
        </ul>
    </div>
    `;

    statrBtn.addEventListener('click', () => {
        window.location.href = url + pk + '/';
    }, {once: true});
}));