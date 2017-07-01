(function() {
  var $grid = $('.grid').imagesLoaded(function() {
    $('.site__wrapper').masonry({
      itemSelector: '.grid'
    });
  });
})();