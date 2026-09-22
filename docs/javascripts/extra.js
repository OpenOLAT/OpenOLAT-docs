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


	/*
		Start page: the "Ask Sophia" button submits the same field under the name
		the Sophia widget reads. Material's bundle opens its search overlay on
		?q=, sophia.js opens the chat on ?sophia=. One field, two names.
		Without JavaScript the second button degrades to a normal search.
	*/
	document.querySelectorAll("form [data-oo-ask-sophia]").forEach(function(btn) {
		var form = btn.form;
		if (!form) return;
		/* When Material's search has been moved into the page (see below), the
		   reader types into that field, not into the fallback one. Carry the
		   text over before the form is submitted. */
		function carryText(form) {
			var live = document.querySelector(".oo-home-searchslot .md-search__input");
			var field = form.querySelector("input[name='q'], input[name='sophia']");
			if (live && field) field.value = live.value;
			return field;
		}
		btn.addEventListener("click", function() {
			var field = carryText(form);
			if (field) field.name = "sophia";
		});
		form.querySelectorAll("button[type='submit']:not([data-oo-ask-sophia])").forEach(function(other) {
			other.addEventListener("click", function() {
				var field = carryText(form);
				if (field) field.name = "q";
			});
		});
	});

	/*
		Start page: the results belong under the big field, not under the header.

		Material resolves its search elements by selector when it mounts, on
		DOMContentLoaded. This file runs earlier, while the document is still
		parsing, so moving .md-search into the page here is invisible to
		Material: it finds the element wherever it sits and binds to it as
		usual. Only the theme CSS cares about the old position, because every
		open-state rule is written as
		  [data-md-toggle=search]:checked ~ .md-header .md-search__...
		Those rules simply stop matching, which is why extra.scss carries its
		own, much smaller set for the relocated field.

		The open state is driven here rather than by the theme's checkbox, so
		the dropdown does not depend on the header markup at all. Escape and a
		click outside close it; Material's own Escape handling stays untouched.

		Without JavaScript nothing moves: the slot stays empty, the fallback
		form keeps its own field and the ?q= submit still works.
	*/
	(function() {
		var slot = document.querySelector("[data-oo-search-slot]");
		var search = document.querySelector(".md-header [data-md-component=search]");
		if (!slot || !search) return;

		slot.appendChild(search);
		document.documentElement.classList.add("oo-home-live-search");

		var form = search.querySelector(".md-search__form");
		var input = search.querySelector(".md-search__input");
		if (!form || !input) return;

		/* the magnifier of the fallback field, so both look the same */
		var icon = document.createElement("i");
		icon.className = "o_icon o_icon_search oo-home-searchslot__icon";
		icon.setAttribute("aria-hidden", "true");
		form.insertBefore(icon, form.firstChild);

		var row = slot.closest ? slot.closest(".oo-home-ask__row") : null;
		var fallback = document.querySelector(".oo-home-ask__form input[name='q']");
		if (fallback && fallback.placeholder) input.placeholder = fallback.placeholder;

		function open(state) {
			if (row) row.classList.toggle("oo-home-ask__row--open", !!state);
		}
		input.addEventListener("focus", function() { open(true); });
		input.addEventListener("input", function() { open(true); });
		document.addEventListener("keydown", function(event) {
			if (event.key === "Escape") open(false);
		});
		document.addEventListener("click", function(event) {
			if (row && !row.contains(event.target)) open(false);
		});
		/* ?q=... : Material fills and focuses the field, which opens the panel */
	})();

	/*
		Start page: the example questions come from assets/sophia-questions.json,
		the file the docs team maintains. The page ships a static set as markup,
		so a failed or missing fetch simply leaves those in place.
	*/
	/*
		The chips stay on one line: every chip that would wrap onto a second
		line is removed. The full set is kept on the box, so a resize can
		re-fit the row from scratch.
	*/
	function fitChips(box) {
		var all = box.oooChips;
		if (!all) return;
		all.forEach(function(chip) { box.appendChild(chip); });
		var first = all[0];
		if (!first) return;
		var top = first.offsetTop;
		all.forEach(function(chip) {
			if (chip.offsetTop > top) box.removeChild(chip);
		});
	}
	var chipBoxes = document.querySelectorAll("[data-oo-questions]");
	chipBoxes.forEach(function(box) {
		box.oooChips = Array.prototype.slice.call(box.querySelectorAll(".oo-home-chip"));
		fitChips(box);
	});
	if (chipBoxes.length) {
		var chipTimer = null;
		window.addEventListener("resize", function() {
			clearTimeout(chipTimer);
			chipTimer = setTimeout(function() { chipBoxes.forEach(fitChips); }, 150);
		});
	}
	chipBoxes.forEach(function(box) {
		var lang = box.getAttribute("data-oo-questions");
		var src = box.getAttribute("data-oo-questions-src");
		if (!src || !window.fetch) return;
		fetch(src).then(function(response) {
			return response.ok ? response.json() : null;
		}).then(function(data) {
			var questions = data && data[lang];
			if (!questions || !questions.length) return;
			var label = box.querySelector(".oo-home-chips__label");
			box.textContent = "";
			if (label) box.appendChild(label);
			box.oooChips = questions.map(function(question) {
				var chip = document.createElement("a");
				chip.className = "oo-home-chip";
				chip.href = "?sophia=" + encodeURIComponent(question);
				chip.textContent = question;
				return chip;
			});
			fitChips(box);
		}).catch(function() { /* keep the static questions */ });
	});

	
	
} catch(e) {
	if (console) {
		console.log(e.msg)
	}	
}