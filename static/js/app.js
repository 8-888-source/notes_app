// подтверждение удаления
function confirmDelete(noteId) {
    return confirm("Удалить заметку?");
}

// плавное исчезновение карточки
function deleteCard(el) {
    el.style.transition = "0.3s";
    el.style.opacity = "0";
    el.style.transform = "scale(0.9)";

    setTimeout(() => {
        el.remove();
    }, 300);
}