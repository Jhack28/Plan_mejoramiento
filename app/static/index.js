        
        // manejo del cierre y apertura del modal de login  
        // Obtener elementos
        const openModalBtn = document.getElementById('openModalBtn');
        const loginModal = document.getElementById('login-modal');
        const closeModal = document.querySelector('.close');

        // Abrir modal
        openModalBtn.addEventListener('click', () => {
            loginModal.style.display = 'flex';
        });

        // Cerrar modal al hacer click en la 'x'
        closeModal.addEventListener('click', () => {
            loginModal.style.display = 'none';
        });

        // También cerrar modal si se hace click fuera del contenido
        window.addEventListener('click', (e) => {
            if (e.target === loginModal) {
                loginModal.style.display = 'none';
            }
        });

        document.getElementById('openModalBtn').onclick = function() {
            document.getElementById('modalRegistro').style.display = 'block';
        };      