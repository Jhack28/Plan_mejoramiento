// Botones para abrir los modals
const openRegistroBtn = document.getElementById('openRegistroBtn');
const openLoginBtn = document.getElementById('openLoginBtn');

// Modals
const registroModal = document.getElementById('registro-modal');
const loginModal = document.getElementById('login-modal');

// Botones de cerrar
const closeButtons = document.querySelectorAll('.close');

// Abrir modal de registro
openRegistroBtn.addEventListener('click', () => {
    registroModal.style.display = 'flex';
});

// Abrir modal de login
openLoginBtn.addEventListener('click', () => {
    loginModal.style.display = 'flex';
});

// Cerrar modals al hacer click en la 'x'
closeButtons.forEach(btn => {
    btn.addEventListener('click', () => {
        btn.closest('.login-modal').style.display = 'none';
    });
});

// Cerrar modal si se hace click fuera del contenido
window.addEventListener('click', (e) => {
    if (e.target === registroModal) {
        registroModal.style.display = 'none';
    }
    if (e.target === loginModal) {
        loginModal.style.display = 'none';
    }
});

