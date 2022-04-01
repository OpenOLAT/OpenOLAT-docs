/*
 * Some extra JS code for the OpenOlat-docs project to extend mkdocs and the material theme. 
 * Missing pieces such as figure or lightbox support
 *
 * 15.03,2021, gnaegi@frentix.com, https://frentix.com
 */
try {	
	/* 
		Convert images to figures if they have a title element
	*/
	document.querySelectorAll("img").forEach(function(item) {
		var title = item.getAttribute('title');
		if (title && title != '' && !title.startsWith(':')) {
			const newItem = document.createElement('figure');
			newItem.innerHTML = item.outerHTML + '<figcaption>' + title + '</figcaption>';
			item.parentNode.replaceChild(newItem, item);			
		}
	});

	/* 
		Open downloads in new window
	*/
	document.querySelectorAll("a").forEach(function(item) {
		const types = ['pdf', 'odt', 'xlsx', 'docx'];
		var href = item.getAttribute('href');		
		if (href && href != '' && (href.lastIndexOf('.') > 0)) {
			type = href.substring(href.lastIndexOf('.') + 1);
			if (types.includes(type)) {
				item.setAttribute('target','_blank');			
			}			
		}
	});
	
	/* 
		Initialize the lighbox on ever image with the marker css class "lightbox" 
	*/
	document.querySelectorAll("img.lightbox").forEach(function(item) {
		item.addEventListener("click", function(event) {
			const instance = basicLightbox.create('<img src="' + event.target.src + '" width="1024" height="768">');
			instance.show();
		});
	});

	
	
} catch(e) {
	if (console) {
		console.log(e.msg)
	}	
}