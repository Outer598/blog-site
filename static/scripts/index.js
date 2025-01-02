var navigationOptions = $(".navigation-page a");
var editButton = $(".edit");

$(document).ready(function() {
    highlightCurrentPage();

    editButton.on("click", function() {
        $(".edit-blog").removeClass("hidden");
        $("nav, .posts").addClass("blur");
    });

    $(".cancel").on("click", function() {
        $(".edit-blog").addClass("hidden");
        $("nav, .posts").removeClass("blur");
    });
    
});

function highlightCurrentPage(){
    var currentPage = window.location.pathname;
    
    if (currentPage === '/templates/about.html') {
        navigationOptions[3].classList.add("bold");
    } else if (currentPage === '/templates/contact.html') {
        navigationOptions[2].classList.add("bold");
    } else if (currentPage === '/templates/post.html') {
        navigationOptions[1].classList.add("bold");
    }
}