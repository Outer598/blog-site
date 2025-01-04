var navigationOptions = $(".navigation-page a");
var editButton = $(".edit");

$(document).ready(function() {
    highlightCurrentPage();

    editButton.on("click", function() {
        $(".edit-blog").removeClass("hidden");
        $("nav, .posts").addClass("blur");
    });
    for (var i = 0; i < 9; i++){
        $(".blog:first").clone().appendTo(".blog-container");
    }

    $(".write-new").on("click", function() {
        $(".new-blog").removeClass("hidden");
        $("nav, .posts").addClass("blur");
    });

    $(".save").on("click", function(event) {
        event.preventDefault();
        $(".edit-blog").addClass("hidden");
        $("nav, .posts").removeClass("blur");
        $(".status").css("background-color", "green");
        $(".status h2").html("Updated successfully");
        $(".status").fadeIn(2000).fadeOut(2000);
    });

    $(".add").on("click", function(event) {
        event.preventDefault();
        $(".new-blog").addClass("hidden");
        $("nav, .posts").removeClass("blur");
        $(".status").css("background-color", "green");
        $(".status h2").html("Added successfully");
        $(".status").fadeIn(2000).fadeOut(2000);
    });

    $(".cancel").on("click", function() {
        $(".edit-blog").addClass("hidden");
        $("nav, .posts").removeClass("blur");
    });

    
    $(".cancel").on("click", function() {
        $(".new-blog").addClass("hidden");
        $("nav, .posts").removeClass("blur");
    });

    $(".delete").on("click", function() {
        $(".delete-post").removeClass("hidden");
        $("nav, .posts").addClass("blur");
    });

    $(".delete-post .yes").on("click", function() {
        $(".delete-post").addClass("hidden");
        $("nav, .posts").removeClass("blur");
        $(".status h2").html("Deleted successfully");
        $(".status").css("background-color", "red");
        $(".status").fadeIn(2000).fadeOut(2000);
    });

    $(".delete-post .no").on("click", function() {
        $(".delete-post").addClass("hidden");
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