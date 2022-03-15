/*
 * Some extra JS code for the OpenOlat-docs project to extend mkdocs and the material theme. 
 * Missing pieces such as figure or lightbox support
 *
 * 15.03,2021, gnaegi@frentix.com, https://frentix.com
 */
try {	
	/* 
		Convert images to figures if they have a title element specified
	*/
	document.querySelectorAll("img").forEach(function(item) {
		var title = item.getAttribute('title');
		if (title && title != '') {
			const newItem = document.createElement('figure');
			newItem.innerHTML = item.outerHTML + '<figcaption>' + title + '</figcaption>';
			item.parentNode.replaceChild(newItem, item);			
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