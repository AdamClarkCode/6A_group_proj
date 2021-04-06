$(document).ready(function() {
	$('#like_btn').click(function() {
		var storySlugVar;
		storySlugVar = $(this).attr('data-storyslug');
		
		$.get('/oneWordStory/like_story/',
			{'story_slug': storySlugVar},
			function(data) {
				$('#like_count').html(data);
				$('#like_btn').hide();
			})
	});
});