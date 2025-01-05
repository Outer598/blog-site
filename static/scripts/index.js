var navigationOptions = $(".navigation-page a");
var editButton = $(".edit");

var currentPage = window.location.pathname;

$(document).ready(function() {
    highlightCurrentPage();

    editButton.on("click", function() {
        $(".edit-blog").removeClass("hidden");
        $("nav, .posts").addClass("blur");
    });
    
    homePage();

    if (currentPage === '/blog'){
        blogPage();
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

function homePage(){
    $.ajax({
        url: '/api/blogs',
        type: 'GET',
        contentType: 'application/json',
        success: function(response){
            responseLength = response.length;

            $(".blog h2").text(response[0].title);
            $(".blog summary").text(response[0].synopsis);
            $(".blog a").attr('id', `${response[0].id}`);
            for (var i = 1; i < responseLength; i++){
                let latestBlog = $(".blog").clone();

                $('.blog h2').text(response[i].title);
                $(".blog summary").text(response[i].synopsis);
                $(".blog a").attr('id', `${response[i].id}`);
                $(".blog-container").append(latestBlog);
            }
            $('.blog a').on('click', function(e) {
                e.preventDefault();
                var blog_id = this.id;
                window.location.href = `/blog?id=${blog_id}`;
            });

        },
        error: function(xhr, status, error){
            console.log("Error: " + error)
        }
    });
}

function blogPage(){
    var blogId = new URLSearchParams(window.location.search).get('id');

    $.ajax({
        url: `/api/blog?id=${blogId}`,
        type: 'GET',
        contentType: 'application/json',
        success: function(response){
            $(".content h1").text(response.title);
            $(".content time").text(response.created_at);
            $(".content p").text(response.content);
            $(".about h4").text(`Author - ${response.Author}`);
        },
        error: function(xhr, status, error){
            console.log('error: ' + error)
        }
    });
}