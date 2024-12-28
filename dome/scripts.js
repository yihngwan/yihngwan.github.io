function toggleSidebar(side) {
    const sidebar = document.querySelector(`.${side}-sidebar`);
    const toggleBtn = document.querySelector(`.${side}-toggle-btn`);
    const content = document.querySelector('.content');
    sidebar.classList.toggle('collapsed');
    toggleBtn.classList.toggle('collapsed');
    if (side === 'left') {
        content.style.marginLeft = sidebar.classList.contains('collapsed') ? '0' : '200px';
    } else {
        content.style.marginRight = sidebar.classList.contains('collapsed') ? '0' : '200px';
    }
}