(function(){
	jQuery.fn.djangoStar = function(config){
		config = $.extend({
			'url' : {
				'get' : '',
				'create' : '',
				'delete' : ''
			}, 
		}, config);
		console.log(config.url.get);
		var addButton = $('<div>').addClass('django-star-add-button').append($('<a>')
		.attr('href', 'javascript:void(0)').html('add').bind('click', function(){
			$.post(config.url.create, function(data){
				console.log(data);
			}, 'json');
		}));
		$(this).append(addButton);
		var $container = $('<ul>').addClass('django-star-container');
		$.getJSON(config.url.get, function(data){
			console.log(data);
			$(data).each(function(){
				console.log(this);
				var $star = $('<li>').html('star');
				$container.append($star);
			});
		});
		$(this).append($container);
	};
})();