// use resizeable-js for ability to resize right and left panels by dragging the splitter bar
$(".panel-left").resizable({
  handleSelector: ".splitter",
  resizeHeight: false
});


// load info/modal page when ?/infoButton is clicked
$('#infoButton').click(function(e) {
    e.preventDefault();
    // $.get("info.html", function(h) {
    $.get("static/info.html", function(h) {
      $(h).appendTo('#info').modal();
          });
      }); // end infoButton click function
