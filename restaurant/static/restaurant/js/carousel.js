$(document).ready(function() {
    $('.carousel-control-prev, .carousel-control-next').hide();
  
    $('.carousel-indicators li').click(function() {
      var target = $(this).data('bs-slide-to');
      if (target > $('.carousel-item.active').index()) {
        $('.carousel-control-next').click(); 
      } else {
        $('.carousel-control-prev').click(); 
      }
    });
  });