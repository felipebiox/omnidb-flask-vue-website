import Vue from 'vue';

Vue.directive('omnidb-scroll', {
  // Quando o elemento vinculado é inserido no DOM...
  inserted: function (el) {

    let jEl = $(el),
        target = $( "#" + jEl.attr('attr-scroll-target') ),
        scrollTriggerPosition = jEl.offset().top - 200,
        scrollTriggerBottom   = scrollTriggerPosition + jEl.height(),
        classAppliedOnTrigger = ( jEl.attr('attr-scroll-class') ) ? jEl.attr('attr-scroll-class') : 'omnidb-fixed';

    target.on('scroll', function(e) {

      let scrollTop = this.scrollTop();

      if ( scrollTop >= scrollTriggerPosition && scrollTop <= scrollTriggerBottom ) {
          jEl.addClass( classAppliedOnTrigger );
      }
      else
          jEl.removeClass( classAppliedOnTrigger );

    }.bind( target ));

  }
});
