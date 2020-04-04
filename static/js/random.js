var jQuery = $('.blog').each(function(i, obj) {
    var randomColor = "#000000".replace(/0/g,function(){return (~~(Math.random()*16)).toString(16);});
    $(obj).css('background-color',randomColor)
});

