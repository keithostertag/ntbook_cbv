/* use resizeable-js for ability to resize top panels by dragging the splitter bar
checks media query to see if the flex-direction is set to column, if yes then
we need resizeWidth: false for a vertical column format, else we need the top
panels to be in the row configutation. In either case the splitter bar will
enable changing the relative sizes of those two panels */

$(document).ready(function()  {
  checkSize();  // run test on initial page load
});

// Function to check css rule
function checkSize(){
  if ($(".panel-container").css("flex-direction") == "column"){
    $(".panel-one").resizable({
      handleSelector: ".splitter",
      resizeWidth: false
    })}
  else {
    $(".panel-one").resizable({
      handleSelector: ".splitter",
      resizeHeight: false
      }); // end resizeable
  } // end else
} // end function checkSize

$(window).resize(checkSize);  // check to determine panel col or row format

// load info/modal page when ?/infoButton is clicked
$('#infoButton').click(function(e) {
    e.preventDefault();
    // $.get("info.html", function(h) {
    $.get("static/info.html", function(h) {
      $(h).appendTo('#info').modal();
          });
      }); // end infoButton click function
