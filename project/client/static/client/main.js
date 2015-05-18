$(document).ready(function(){
    $('#go_link').on('click', function(event){
        event.preventDefault();
            $.getJSON('/gvd/play/game', function(data){
                console.log(data);
                var template = $('#template').html();
                var info = Mustache.render(template, data);
                $('.api_calls').html(info);
      });
  });
});
