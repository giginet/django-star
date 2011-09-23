(function(){
	jQuery.fn.djangoStar = function(config){
		config = $.extend(true, {
			'url' : '', 
			'add' : {
				'caption' : 'add star'
			},
			'popup' : {
				'quote' : {
					'begin' : "\'",
					'end' : "\'"
				}
			},
			'del' : {
				'message' : 'Are you sure you want to delete this star?',
				'delay' : 2000
			}
		}, config);
		var addButton = $('<div>').addClass('django-star-add-button').append($('<a>')
		.attr('href', 'javascript:void(0)').bind('click', function(){
			// this code may not work well on IE.
			var comment = document.getSelection();
			$.post(config.url, {comment : comment}, function(data){
				$container.append(createStar(data).fadeIn('slow'))
			}, 'json');
		}).attr('title', config.add.caption));
		$(this).append(addButton);
		var $container = $('<ul>').addClass('django-star-container');
		
		var createStar = function(data){
			var username = data.author.username;
			var comment = data.comment;
			var $star = $('<li>');
			var $popup = $('<div>').addClass('django-star-popup');
			$popup.append(username);
			if(comment){
				$popup.append($('<blockquote>').append(config.popup.quote.begin + comment + config.popup.quote.end));	
			}
			$star.attr({
				'comment' : comment,
				'username' : username,
				'star-id' : data.pk
			}).bind('mouseover', function(event){
				$star.append($popup.fadeIn('fast'));
				$popup.css({
					'top' : event.pageY + 20,
					'left' : event.pageX + 20
				})
				$(this).delay(config.del.delay).queue(function(){
					if(confirm(config.del.message)){
						var id = $(this).attr('star-id');
						$.ajax({
							'url' : '/api/star/delete/' + id + '/', 
							'data' : {star_id : id},
							'type' : 'DELETE',
							'success' : function(data){
								$star.clearQueue();
								$star.toggle('slow', function(){
									$(this).remove();
								});
							}
						})
					}
				});
			}).bind('mouseout', function(event){
				$(this).clearQueue();
				$popup.fadeOut('fast', function(){
					$(this).remove();
				});
			});
			return $star;
		}
		
		$.getJSON(config.url, function(data){
			$(data).each(function(){
				$container.append(createStar(this));
			});
		});
		$(this).append($container);
	};
})();