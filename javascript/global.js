// Base javascript
(function(){
    $(function(){
        $('article').click(function(){
            var href=$(this).data('href');
            if (0 < href.length){
                window.location.href = href;
            }
        })
    });
})();
