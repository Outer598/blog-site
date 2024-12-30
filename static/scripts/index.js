var navigationOptions = document.querySelectorAll(".navigation-page a");
document.addEventListener('DOMContentLoaded', function() {
    var currentPage = window.location.pathname;

    if (currentPage === '/templates/about.html') {
        navigationOptions[3].classList.add("bold");
    } else if (currentPage === '/templates/contact.html') {
        navigationOptions[2].classList.add("bold");
    } else if (currentPage === '/templates/post.html') {
        navigationOptions[1].classList.add("bold");
    }
});
