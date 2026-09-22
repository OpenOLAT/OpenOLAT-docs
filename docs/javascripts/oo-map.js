/*
 * "What is in OpenOlat": the two-layer map above the cards.
 *
 * A reduced port of the internal concept-map viewer
 * (fxIntelligence/knowledge/openolat/concept-map/index.html, built by
 * scripts/04_build_page.py). The drawing, the motion and the way the reader
 * navigates are that viewer's, kept as close as the two layers allow:
 *
 *   - the night sky: a navy wash, two soft corner glows and a drifting
 *     constellation, drawn in screen space before anything else;
 *   - the hub and its spokes: the focus sits in the middle, the level around
 *     it, one spoke per satellite, as heavy as the satellite it carries;
 *   - the satellite: an orange dot inside a crescent that opens toward the
 *     hub, with its label outboard;
 *   - the way back: pinned to the top-left corner, tied to the hub by a
 *     dotted line that bows and sways;
 *   - the callout: it sits on the free side of the hovered node and points
 *     at it, so dot and label stay visible;
 *   - the breadcrumb on the drawing itself, and the detail panel below it.
 *
 * What the two-layer map does not need, and what is therefore gone: the
 * sphere and the free physics layout, the pan, the zoom and the auto-fit
 * camera, the relation lines, the ghost fan of the next level, the search,
 * the filters, the window mode and the auto tour. The camera is the identity,
 * so a label drawn at 16 px IS 16 px on screen, which is the body size of the
 * manual. Nothing on this map is smaller than the text around it.
 *
 * Levels. Layer 1 are the five groups, layer 2 the areas inside one group.
 * Selecting a node narrows the grid cards below it: a group keeps its areas,
 * an area keeps its single card. The way back, the breadcrumb and Escape
 * widen it again.
 *
 * The model is read from the page itself, so nothing is written twice: the
 * groups are the H2 sections with their colour swatch, the areas are the
 * cards with data-oo-cluster and data-oo-domain, and the sentence and the
 * manual link of an area are the card's own. Only the name in the other
 * language comes from the small JSON block the page carries, because a card
 * holds one language.
 *
 * The page works without this file. The map stays hidden and every card is
 * visible.
 *
 * 2026, frentix GmbH, https://frentix.com
 */
(function () {
	"use strict";

	var root = document.querySelector("[data-oo-map]");
	if (!root) return;                       // not this page

	/* ====================================================================
	   1) The model, read off the page
	   ==================================================================== */

	var NAMES = { clusters: {}, domains: {}, ui: {} };
	var store = document.getElementById("oo-map-names");
	if (store) {
		try {
			NAMES = Object.assign(NAMES, JSON.parse(store.textContent) || {});
		} catch (e) { /* keep the defaults */ }
	}
	var UI = NAMES.ui || {};
	function t(key, fallback) {
		return (UI[key] === undefined || UI[key] === null) ? fallback : UI[key];
	}

	function clean(el) {
		/* an H2 carries a colour swatch and Material's headerlink; neither is
		   part of the name */
		var copy = el.cloneNode(true);
		Array.prototype.slice.call(copy.querySelectorAll("span[style], .headerlink"))
			.forEach(function (x) { x.parentNode.removeChild(x); });
		return copy.textContent.replace(/\s+/g, " ").trim();
	}

	/* the cards, and the section each one sits in */
	var cards = Array.prototype.slice.call(
		document.querySelectorAll(".grid.cards [data-oo-domain]")
	).map(function (title) {
		var item = title.closest ? title.closest("li") : null;
		if (!item) return null;
		var link = title.querySelector("a");
		var paras = item.querySelectorAll("p");
		var body = paras.length ? paras[paras.length - 1] : null;
		return {
			item: item,
			cluster: title.getAttribute("data-oo-cluster"),
			domain: title.getAttribute("data-oo-domain"),
			name: clean(title),
			href: link ? link.getAttribute("href") : null,
			desc: (body && body !== title) ? clean(body) : ""
		};
	}).filter(Boolean);
	if (!cards.length) return;

	/* every grid, with the heading block above it: hiding a whole section
	   keeps the page readable when a filter empties it */
	var sections = Array.prototype.slice.call(
		document.querySelectorAll(".grid.cards")
	).map(function (grid) {
		var lead = [], node = grid.previousElementSibling;
		while (node && node.tagName !== "H2") {
			lead.push(node);
			node = node.previousElementSibling;
		}
		if (node) lead.push(node);           // the H2 itself
		return { grid: grid, lead: lead, head: node };
	});

	/* Which language is this page in? The html element is not to be trusted:
	   the manual's i18n plugin leaves lang="en" on the German build. The page
	   itself is the better witness, so the group names in the markup are held
	   against both columns of the name table and the majority decides. */
	var LANG = (function () {
		var vote = { de: 0, en: 0 };
		sections.forEach(function (section) {
			var head = section.head;
			if (!head || !head.id) return;
			var rec = NAMES.clusters[head.id];
			if (!rec) return;
			var name = clean(head);
			if (rec.de === name) vote.de++;
			if (rec.en === name) vote.en++;
		});
		if (vote.de > vote.en) return "de";
		if (vote.en > vote.de) return "en";
		return (document.documentElement.lang || "en").slice(0, 2).toLowerCase();
	})();
	var OTHER = LANG === "de" ? "en" : "de";

	/* the groups, in the order the page states them */
	var clusters = [], byCluster = {};
	sections.forEach(function (section) {
		var head = section.head;
		if (!head || !head.id) return;
		var mine = cards.filter(function (c) { return c.cluster === head.id; });
		if (!mine.length) return;
		var swatch = head.querySelector("span[style]");
		var colour = swatch ? (swatch.style.background || swatch.style.backgroundColor) : "";
		var intro = null, node = head.nextElementSibling;
		while (node && node.tagName !== "H2") {
			if (node.tagName === "P") { intro = node; break; }
			if (node.tagName === "DIV") break;
			node = node.nextElementSibling;
		}
		var cl = {
			id: head.id,
			name: clean(head),
			other: (NAMES.clusters[head.id] || {})[OTHER] || "",
			desc: intro ? clean(intro) : "",
			colour: canvasHue(colour),
			domains: mine
		};
		clusters.push(cl);
		byCluster[cl.id] = cl;
	});
	if (!clusters.length) return;

	/* The viewer paints its nodes in hsl(h 58% 52%): saturated enough to carry
	   on the night sky. The page's own group colours are darker than that, so
	   only their hue is taken over and the viewer's saturation and lightness
	   are applied. The map therefore shows the same five hues as the headings
	   without going muddy on navy. */
	function canvasHue(css) {
		var hex = /^#?([0-9a-f]{6})$/i.exec((css || "").trim());
		var rgb = /rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)/i.exec(css || "");
		var r, g, b;
		if (hex) {
			var v = parseInt(hex[1], 16);
			r = (v >> 16) & 255; g = (v >> 8) & 255; b = v & 255;
		} else if (rgb) {
			r = +rgb[1]; g = +rgb[2]; b = +rgb[3];
		} else {
			return "hsl(181 58% 52%)";       // the OpenOlat teal, as a floor
		}
		r /= 255; g /= 255; b /= 255;
		var mx = Math.max(r, g, b), mn = Math.min(r, g, b), d = mx - mn, h = 0;
		if (d) {
			if (mx === r) h = ((g - b) / d) % 6;
			else if (mx === g) h = (b - r) / d + 2;
			else h = (r - g) / d + 4;
		}
		h = Math.round(h * 60); if (h < 0) h += 360;
		return "hsl(" + h + " 58% 52%)";
	}

	function otherName(kind, id) {
		var rec = NAMES[kind] ? NAMES[kind][id] : null;
		return (rec && rec[OTHER]) || "";
	}

	/* ====================================================================
	   2) The stage
	   ==================================================================== */

	root.innerHTML =
		'<div class="oo-map__stage">' +
		'<div class="oo-map__wrap">' +
		'<canvas class="oo-map__canvas" tabindex="0" role="application"></canvas>' +
		'<p class="oo-map__crumbs"></p>' +
		'<div class="oo-map__tip" hidden></div>' +
		"</div>" +
		'<div class="oo-map__detail"></div>' +
		'<p class="oo-map__status" role="status" aria-live="polite"></p>' +
		"</div>";
	root.hidden = false;

	var cv = root.querySelector(".oo-map__canvas");
	var crumbs = root.querySelector(".oo-map__crumbs");
	var tip = root.querySelector(".oo-map__tip");
	var detail = root.querySelector(".oo-map__detail");
	var status = root.querySelector(".oo-map__status");
	var ctx = cv.getContext("2d");
	cv.setAttribute("aria-label", t("canvas",
		"Map of the subject areas. Arrow keys move, Enter opens, Escape goes back."));

	/* ====================================================================
	   3) State
	   ==================================================================== */

	var GH = {
		focus: null,        // null = the groups, a group id = its areas
		nodes: [],
		hover: null,
		sel: null,          // the selected key, drawn with a ring
		kb: null,           // the keyboard cursor
		pulse: null,
		t: 0, raf: 0, dpr: 1, w: 0, h: 0, wmax: 1, idle: 0, on: true, frames: 0,
		dscale: 1
	};

	var still = false;
	var mq = window.matchMedia
		? window.matchMedia("(prefers-reduced-motion: reduce)") : null;
	if (mq) {
		still = mq.matches;
		if (mq.addEventListener) {
			mq.addEventListener("change", function (e) { still = e.matches; wake(); });
		}
	}

	/* ====================================================================
	   4) Geometry
	   ==================================================================== */

	var NARROW = 620;                        // below this the ring stands up
	var BODY = 16;                           // the body size of the manual

	function shape() {
		var narrow = GH.w < NARROW;
		var lab = narrow
			? Math.min(180, Math.max(118, Math.round(GH.w * 0.40)))
			: Math.min(150, Math.max(96, Math.round(GH.w * 0.20)));
		var xs = narrow ? 0.64 : 1.28;
		/* Wide: the label runs outboard, so its whole width is kept free beside
		   the ring. Narrow: it sits under its dot and is clamped to the frame,
		   so only a margin is needed and the ring may use the width. */
		var bx = ((GH.w / 2) - (narrow ? 30 : lab + 26)) / xs;
		var by = GH.h / 2 - (narrow ? 74 : 46);
		/* the dots step back on a narrow screen, where the ring is tighter */
		GH.dscale = narrow ? 0.78 : 1;
		return { narrow: narrow, labelW: lab, xs: xs, base: Math.max(56, Math.min(bx, by)) };
	}

	/* How present a node is, the viewer's weight: the more a group holds, the
	   bigger its dot, its spoke and its label. Normalised per level. */
	function weigh(list) {
		if (!list.length) return;
		var raw = list.map(function (n) { return Math.sqrt(Math.max(1, n.count || 1)); });
		var lo = Math.min.apply(null, raw), hi = Math.max.apply(null, raw);
		/* A level whose nodes all weigh the same, such as the areas inside one
		   group, would normalise to nothing and draw the smallest dot there is.
		   It gets one middling weight instead, so the level reads. */
		if (hi === lo) { list.forEach(function (n) { n.w = 0.45; }); return; }
		list.forEach(function (n, i) { n.w = (raw[i] - lo) / (hi - lo); });
	}

	function conceptuality(n) { return 0.12 + 0.88 * (n.w !== undefined ? n.w : 0.4); }
	function dotRadius(n) {
		return (7 + 13 * Math.pow(conceptuality(n), 1.25)) * (GH.dscale || 1);
	}

	var SPOKE_MIN = 1.8;
	function spokeWidth(n) {
		var mx = GH.wmax || 1;
		return SPOKE_MIN * (1 + 2 * Math.min(1, (n && n.w !== undefined ? n.w : 0) / mx));
	}
	function centreRing() {
		return Math.max(3.4, GH.nodes.reduce(function (m, n) {
			return (n.isFocus || n.isBack) ? m : Math.max(m, spokeWidth(n));
		}, 0));
	}
	function nodeRadius(n) { return n.isFocus ? 44 : dotRadius(n) + 9; }

	function fnv(s) {
		var h = 2166136261;
		for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
		return h >>> 0;
	}

	/* ====================================================================
	   5) Building a level
	   ==================================================================== */

	var built = false;

	function build() {
		var prev = {};
		GH.nodes.forEach(function (n) { prev[n.key] = n; });
		var N = [];
		function push(o) {
			var p = prev[o.key];
			N.push(Object.assign({
				x: p ? p.x : (Math.random() - 0.5) * 320,
				y: p ? p.y : (Math.random() - 0.5) * 220,
				vx: 0, vy: 0, ph: Math.random() * 6.28, rjit: 1
			}, o));
		}

		if (GH.focus === null) {
			clusters.forEach(function (cl) {
				push({
					key: cl.id, kindOf: "cluster", label: cl.name, sub: cl.other,
					desc: cl.desc, col: cl.colour, count: cl.domains.length,
					childCount: cl.domains.length, isFocus: false
				});
			});
		} else {
			var cl2 = byCluster[GH.focus];
			push({
				key: cl2.id, kindOf: "cluster", label: cl2.name, sub: cl2.other,
				desc: cl2.desc, col: cl2.colour, count: cl2.domains.length,
				childCount: cl2.domains.length, isFocus: true
			});
			cl2.domains.forEach(function (card) {
				push({
					key: cl2.id + "/" + card.domain, domain: card.domain,
					cluster: cl2.id, kindOf: "domain", label: card.name,
					sub: otherName("domains", card.domain), desc: card.desc,
					href: card.href, col: cl2.colour, count: 1, childCount: 0,
					isFocus: false
				});
			});
			N.push({
				key: "BACK", kindOf: "back", isBack: true, target: null,
				label: t("overview", "Overview"), col: "hsl(0 0% 50%)",
				x: -9999, y: -9999, vx: 0, vy: 0, ph: 1.7, rjit: 1.08, w: 0.72
			});
		}

		/* the spoke slots, evenly spread, in the order the page states them */
		var sats = N.filter(function (n) { return !n.isFocus && !n.isBack; });
		sats.forEach(function (n, i) {
			n.slot = -Math.PI / 2 + i * (6.2832 / Math.max(1, sats.length));
		});

		/* Spoke length. A plain hash clumps, so the satellites are ordered by
		   hash and dealt one stratum each across the range: even spread, still
		   stable per node. The viewer's trick, unchanged. */
		var hashed = sats.map(function (n) { return [n, fnv(n.key)]; });
		hashed.sort(function (a, b) { return a[1] - b[1]; });
		var k = hashed.length || 1, LO = 0.82, HI = 1.10;
		hashed.forEach(function (pair, i) {
			var stratum = (i + 0.5) / k;
			var jit = (((pair[1] >>> 11) % 10000) / 10000 - 0.5) * (0.92 / k);
			pair[0].rjit = LO + Math.max(0, Math.min(1, stratum + jit)) * (HI - LO);
		});

		/* The first level is placed where it belongs. Later levels keep the
		   viewer's entrance: the new satellites start scattered and settle
		   into the ring. */
		if (!built) {
			var s0 = shape();
			sats.forEach(function (n) {
				var R = s0.base * (n.rjit || 1);
				n.x = Math.cos(n.slot) * R * s0.xs;
				n.y = Math.sin(n.slot) * R;
				n.vx = n.vy = 0;
			});
			built = true;
		}

		weigh(sats);
		var ws = sats.map(function (n) { return n.w || 0; });
		GH.wmax = ws.length ? Math.max.apply(null, ws) : 1;
		if (!(GH.wmax > 0)) GH.wmax = 1;

		GH.nodes = N;
		GH.kb = sats.length ? sats[0] : null;
		wake();
	}

	/* ====================================================================
	   6) Motion
	   ==================================================================== */

	function step() {
		var s = shape();
		if (!still) GH.t += 0.016;
		var moved = 0;
		for (var i = 0; i < GH.nodes.length; i++) {
			var n = GH.nodes[i];
			n.r = nodeRadius(n);
			if (n.isBack) {
				/* pinned to the corner, not sprung: the eye expects it there */
				n.x = -GH.w / 2 + 68;
				n.y = -GH.h / 2 + (s.narrow ? 84 : 94);
				continue;
			}
			var tx = 0, ty = 0, k = 0.05;
			if (!n.isFocus) {
				var breath = still ? 1 : 1 + Math.sin(GH.t * 0.32 + n.ph) * 0.022;
				var R = s.base * (n.rjit || 1) * breath;
				var a = n.slot + (still ? 0 : GH.t * 0.012);
				tx = Math.cos(a) * R * s.xs;
				ty = Math.sin(a) * R;
				k = 0.028;
			}
			n.vx += (tx - n.x) * k;
			n.vy += (ty - n.y) * k;
			if (!still) {
				n.vx += Math.sin(GH.t * 0.6 + n.ph) * 0.02;
				n.vy += Math.cos(GH.t * 0.5 + n.ph) * 0.02;
			}
			n.vx *= 0.88; n.vy *= 0.88;
			n.x += Math.max(-9, Math.min(9, n.vx));
			n.y += Math.max(-9, Math.min(9, n.vy));
			moved = Math.max(moved, Math.abs(n.vx) + Math.abs(n.vy));
		}
		/* with motion switched off the loop may stop once the level has settled */
		if (still && !GH.hover && !GH.pulse && moved < 0.04) GH.idle++; else GH.idle = 0;
	}

	/* ====================================================================
	   7) The night sky
	   ==================================================================== */

	var STAR_N = 62, STAR_DRIFT = 0.05, STAR_LINK = 128, STARS = null;

	function initStars(w, h) {
		var s = 1234567;
		function rnd() { return (s = (s * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff; }
		STARS = [];
		for (var i = 0; i < STAR_N; i++) {
			var a = rnd() * 6.2832, sp = 0.35 + rnd() * 0.9, u = rnd();
			STARS.push({
				x: rnd() * w, y: rnd() * h,
				vx: Math.cos(a) * sp, vy: Math.sin(a) * sp,
				r: 0.7 + u * u * u * 2.9, tw: rnd() * 6.2832
			});
		}
		STARS.w = w; STARS.h = h;
	}

	function backdrop() {
		var w = GH.w, h = GH.h;
		if (!STARS || STARS.w !== w || STARS.h !== h) initStars(w, h);

		var g = ctx.createLinearGradient(0, 0, w, h);
		g.addColorStop(0, "#0c1526");
		g.addColorStop(0.5, "#0d1a2e");
		g.addColorStop(1, "#0a1220");
		ctx.fillStyle = g; ctx.fillRect(0, 0, w, h);

		var glows = [
			[w * 0.18, h * 0.18, Math.max(w, h) * 0.5, "rgba(46,86,150,0.20)"],
			[w * 0.85, h * 0.80, Math.max(w, h) * 0.45, "rgba(32,157,158,0.13)"]
		];
		for (var i = 0; i < glows.length; i++) {
			var q = glows[i];
			var rg = ctx.createRadialGradient(q[0], q[1], 0, q[0], q[1], q[2]);
			rg.addColorStop(0, q[3]); rg.addColorStop(1, "rgba(0,0,0,0)");
			ctx.fillStyle = rg; ctx.fillRect(0, 0, w, h);
		}

		if (!still) {
			for (var j = 0; j < STARS.length; j++) {
				var st = STARS[j];
				st.x += st.vx * STAR_DRIFT; st.y += st.vy * STAR_DRIFT;
				if (st.x < -20) st.x = w + 20; else if (st.x > w + 20) st.x = -20;
				if (st.y < -20) st.y = h + 20; else if (st.y > h + 20) st.y = -20;
			}
		}
		/* the links first, so the stars sit on top of them */
		ctx.save();
		for (var a2 = 0; a2 < STARS.length; a2++) {
			for (var b2 = a2 + 1; b2 < STARS.length; b2++) {
				var p = STARS[a2], q2 = STARS[b2];
				var dx = p.x - q2.x, dy = p.y - q2.y, d2 = dx * dx + dy * dy;
				if (d2 > STAR_LINK * STAR_LINK) continue;
				var tt = 1 - Math.sqrt(d2) / STAR_LINK;
				var m = (p.r + q2.r) / 2;
				ctx.lineWidth = 0.6 + m * 0.42;
				ctx.strokeStyle = "rgba(150,190,235," +
					(0.075 * tt * tt * (0.8 + m * 0.28)).toFixed(3) + ")";
				ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(q2.x, q2.y); ctx.stroke();
			}
		}
		for (var c = 0; c < STARS.length; c++) {
			var s2 = STARS[c];
			var tw = still ? 1 : 0.88 + Math.sin(GH.t * 0.45 + s2.tw) * 0.12;
			ctx.fillStyle = "rgba(190,215,245," +
				(0.26 * tw * (0.85 + s2.r * 0.16)).toFixed(3) + ")";
			ctx.beginPath(); ctx.arc(s2.x, s2.y, s2.r, 0, 6.2832); ctx.fill();
		}
		ctx.restore();
	}

	/* ====================================================================
	   8) Drawing
	   ==================================================================== */

	var INK = "#f3f4ef";                     // the brand paper, on navy
	var DOT = "#e8622a";
	var HOT = "#ff7a3d";
	var TEAL = "#2fc0c0";
	var FILL = "#0c1526";
	var FONT = 'Roboto, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif';

	/* the mark of the logo: a Gerono lemniscate, y doubled so the proportions
	   match the mark */
	function infinity(cx, cy, a, col) {
		ctx.save();
		ctx.strokeStyle = col; ctx.lineWidth = Math.max(3.2, a * 0.40);
		ctx.lineCap = "round"; ctx.lineJoin = "round";
		ctx.beginPath();
		for (var i = 0; i <= 120; i++) {
			var th = i / 120 * 6.2831853;
			var x = cx + a * Math.cos(th);
			var y = cy + a * 2 * Math.sin(th) * Math.cos(th) * 0.5;
			if (i) ctx.lineTo(x, y); else ctx.moveTo(x, y);
		}
		ctx.closePath(); ctx.stroke(); ctx.restore();
	}

	/* the slack tether to the way back: it bows sideways and sways slowly */
	function bowTo(x0, y0, x1, y1) {
		var dx = x1 - x0, dy = y1 - y0, d = Math.hypot(dx, dy) || 1;
		var px = -dy / d, py = dx / d;
		var amt = 42 + (still ? 0 : Math.sin(GH.t * 0.5) * 12);
		ctx.beginPath(); ctx.moveTo(x0, y0);
		ctx.quadraticCurveTo((x0 + x1) / 2 + px * amt, (y0 + y1) / 2 + py * amt, x1, y1);
	}

	/* Wrapping never goes below the body size of the manual: it adds a line
	   instead. That is the one place this port parts with the viewer, which
	   shrinks a label to 8.5 px to make it fit. */
	function breakText(txt, maxw, size, weight, maxLines) {
		ctx.font = (weight || "500 ") + size + "px " + FONT;
		var words = String(txt).split(" "), lines = [], cur = "";
		for (var i = 0; i < words.length; i++) {
			var cand = cur ? cur + " " + words[i] : words[i];
			if (ctx.measureText(cand).width > maxw && cur) { lines.push(cur); cur = words[i]; }
			else cur = cand;
		}
		if (cur) lines.push(cur);
		if (maxLines && lines.length > maxLines) {
			lines = lines.slice(0, maxLines);
			lines[maxLines - 1] += " …";
		}
		return lines;
	}

	function wrapText(txt, x, y, maxw, size, weight, maxLines) {
		var lines = breakText(txt, maxw, size, weight, maxLines);
		var lh = size + 3, start = y - (lines.length - 1) * lh / 2;
		for (var j = 0; j < lines.length; j++) ctx.fillText(lines[j], x, start + j * lh);
		return lines.length;
	}

	function clampX(v, half) {
		return Math.max(-GH.w / 2 + half + 6, Math.min(GH.w / 2 - half - 6, v));
	}
	function clampY(v, half) {
		return Math.max(-GH.h / 2 + half + 4, Math.min(GH.h / 2 - half - 4, v));
	}

	function draw() {
		var s = shape();
		ctx.setTransform(GH.dpr, 0, 0, GH.dpr, 0, 0);
		ctx.clearRect(0, 0, GH.w, GH.h);
		backdrop();                          // screen space, before the origin moves
		ctx.save();
		ctx.translate(Math.round(GH.w / 2), Math.round(GH.h / 2));

		var hub = GH.nodes.filter(function (n) { return n.isFocus; })[0];
		var hx = hub ? hub.x : 0, hy = hub ? hub.y : 0;
		var hubR = hub ? nodeRadius(hub) : 34;

		/* the spokes */
		ctx.save();
		GH.nodes.forEach(function (n) {
			if (n.isFocus || n.isBack) return;
			var dx = n.x - hx, dy = n.y - hy, d = Math.hypot(dx, dy) || 1;
			var ux = dx / d, uy = dy / d, outer = dotRadius(n) + 7;
			if (d <= hubR + outer + 2) return;
			ctx.strokeStyle = INK;
			ctx.lineWidth = spokeWidth(n);
			ctx.globalAlpha = (GH.pulse && GH.pulse.key !== n.key) ? 0.22 : 1;
			ctx.beginPath();
			ctx.moveTo(hx + ux * (hubR + 2), hy + uy * (hubR + 2));
			ctx.lineTo(n.x - ux * (outer + 1), n.y - uy * (outer + 1));
			ctx.stroke();
		});
		/* the way back is tied to the centre too, but dotted, so it reads as a
		   return rather than another spoke */
		var bk = GH.nodes.filter(function (n) { return n.isBack; })[0];
		if (bk) {
			var bdx = bk.x - hx, bdy = bk.y - hy, bd = Math.hypot(bdx, bdy) || 1;
			var bux = bdx / bd, buy = bdy / bd, bouter = dotRadius(bk) + 7;
			var on = GH.hover === bk || GH.kb === bk;
			ctx.globalAlpha = on ? 0.95 : 0.55;
			ctx.strokeStyle = on ? DOT : INK;
			ctx.setLineDash([2, 5]); ctx.lineWidth = on ? 2.4 : 1.6;
			bowTo(hx + bux * (hubR + 2), hy + buy * (hubR + 2),
				bk.x - bux * (bouter + 1), bk.y - buy * (bouter + 1));
			ctx.stroke(); ctx.setLineDash([]);
		}
		ctx.restore();

		/* the hub: the product mark on the overview, the group on layer 2 */
		if (!hub) {
			ctx.save();
			ctx.fillStyle = FILL;
			ctx.beginPath(); ctx.arc(0, 0, hubR, 0, 6.2832); ctx.fill();
			ctx.lineWidth = centreRing(); ctx.strokeStyle = INK; ctx.globalAlpha = 0.95;
			ctx.stroke();
			ctx.globalAlpha = 1; infinity(0, 0, hubR * 0.52, TEAL);
			ctx.restore();
		}

		/* the soft bodies: additive, so overlaps read as one body of liquid */
		ctx.save();
		ctx.globalCompositeOperation = "lighter";
		GH.nodes.forEach(function (n) {
			if (n.isBack) return;
			var GR = dotRadius(n) * 3.4;
			var g = ctx.createRadialGradient(n.x, n.y, 0, n.x, n.y, GR);
			g.addColorStop(0, n.col.replace(")", " / " + (n.isFocus ? 0.62 : 0.52) + ")"));
			g.addColorStop(1, "transparent");
			ctx.fillStyle = g;
			ctx.beginPath(); ctx.arc(n.x, n.y, GR, 0, 6.2832); ctx.fill();
		});
		ctx.restore();

		/* the cores */
		GH.nodes.forEach(function (n) {
			var dim = (GH.pulse && GH.pulse.key !== n.key) ? 0.32 : 1;
			ctx.globalAlpha = dim;

			if (n.isFocus) {
				ctx.save();
				ctx.fillStyle = FILL;
				ctx.beginPath(); ctx.arc(n.x, n.y, n.r, 0, 6.2832); ctx.fill();
				ctx.lineWidth = centreRing(); ctx.strokeStyle = INK;
				ctx.globalAlpha = 0.95; ctx.stroke();
				ctx.restore();
				return;
			}
			if (n.isBack) {
				/* the way back to the overview IS the product: the same mark */
				var rr = dotRadius(n) + 7;
				ctx.save();
				ctx.globalAlpha = 1; ctx.fillStyle = FILL;
				ctx.beginPath(); ctx.arc(n.x, n.y, rr, 0, 6.2832); ctx.fill();
				ctx.lineWidth = Math.max(centreRing() * 0.8,
					(GH.hover === n || GH.kb === n) ? 3.6 : 2.8);
				ctx.strokeStyle = INK; ctx.globalAlpha = 0.95; ctx.stroke();
				ctx.globalAlpha = 1; infinity(n.x, n.y, rr * 0.52, TEAL);
				ctx.restore();
				return;
			}

			var ang = Math.atan2(n.y, n.x), dr = dotRadius(n);
			ctx.save();
			/* the crescent opens toward the hub and encloses the dot; it is as
			   heavy as the spoke that reaches it */
			ctx.globalAlpha = 0.92 * dim;
			ctx.lineWidth = spokeWidth(n); ctx.strokeStyle = INK; ctx.lineCap = "round";
			ctx.beginPath(); ctx.arc(n.x, n.y, dr + 7, ang + 0.66, ang - 0.66); ctx.stroke();

			/* the dot IS the node, at the centre of the crescent */
			ctx.globalAlpha = dim;
			ctx.fillStyle = DOT;
			ctx.beginPath(); ctx.arc(n.x, n.y, dr, 0, 6.2832); ctx.fill();

			if (GH.pulse && GH.pulse.key === n.key) {
				/* two rings, half a cycle apart, slow enough to read */
				var e = (GH.t - GH.pulse.t0) * 0.85;
				[0, 0.5].forEach(function (off) {
					var ph = (e + off) % 1;
					ctx.globalAlpha = (1 - ph) * (1 - ph) * 0.9;
					ctx.lineWidth = 3.2; ctx.strokeStyle = DOT;
					ctx.beginPath(); ctx.arc(n.x, n.y, dr + 6 + ph * 34, 0, 6.2832); ctx.stroke();
				});
				var sw = 1 + Math.sin(e * 6.2832) * 0.18;
				ctx.globalAlpha = 1; ctx.fillStyle = HOT;
				ctx.beginPath(); ctx.arc(n.x, n.y, dr * sw + 2.2, 0, 6.2832); ctx.fill();
			}
			if (GH.hover === n || GH.sel === n.key || GH.kb === n) {
				ctx.lineWidth = 2; ctx.strokeStyle = DOT;
				ctx.globalAlpha = (GH.sel === n.key) ? 0.9 : 0.55;
				ctx.beginPath(); ctx.arc(n.x, n.y, dr + 4, 0, 6.2832); ctx.stroke();
			}
			ctx.restore();

			/* a dashed ring hints that there is something inside */
			if (n.childCount) {
				ctx.save();
				ctx.beginPath(); ctx.arc(n.x, n.y, dr + 12, 0, 6.2832);
				ctx.globalAlpha = 0.45 * dim; ctx.lineWidth = 1;
				ctx.strokeStyle = INK; ctx.setLineDash([3, 4]); ctx.stroke();
				ctx.restore();
			}
		});

		/* the labels, last, and never below the body size of the manual */
		var boxes = [];
		/* the dots are obstacles too: a label may not be laid over a node that
		   is not its own */
		var discs = GH.nodes.map(function (n) {
			var r = (n.isFocus ? n.r : dotRadius(n) + 9) + 3;
			return { n: n, x: n.x - r, y: n.y - r, w: r * 2, h: r * 2 };
		});
		/* on the overview the hub is the product mark, which is drawn rather
		   than held as a node, so it is added here by hand */
		if (!hub) {
			discs.push({ n: null, x: -hubR - 3, y: -hubR - 3,
				w: (hubR + 3) * 2, h: (hubR + 3) * 2 });
		}
		function blocked(box, self) {
			var hit = function (b) {
				return !(box.x > b.x + b.w || box.x + box.w < b.x ||
					box.y > b.y + b.h || box.y + box.h < b.y);
			};
			return boxes.some(hit) || discs.some(function (d) {
				return d.n !== self && hit(d);
			});
		}
		GH.nodes.forEach(function (n) { n._lb = null; });
		GH.nodes.forEach(function (n) {
			var dim = (GH.pulse && GH.pulse.key !== n.key) ? 0.32 : 1;
			ctx.globalAlpha = dim;
			ctx.fillStyle = (GH.pulse && GH.pulse.key === n.key) ? HOT : INK;
			ctx.textBaseline = "middle";

			if (n.isFocus) {
				/* keep the name inside the circle where it fits at body size,
				   and put it below the circle where it does not */
				ctx.textAlign = "center";
				var box = n.r * 1.62, size = 0, lines = null;
				for (var i = 0; i < 2; i++) {
					var cand = i ? BODY : 20;
					var ls = breakText(n.label, box, cand, "600 ");
					var widest = ls.reduce(function (m, l) {
						return Math.max(m, ctx.measureText(l).width);
					}, 0);
					/* it goes inside only when every line fits the circle and the
					   block does not reach past its rim */
					if (widest <= box && ls.length * (cand + 3) <= n.r * 1.5) {
						size = cand; lines = ls; break;
					}
				}
				if (lines) wrapText(n.label, n.x, n.y, box, size, "600 ");
				else wrapText(n.label, n.x, n.y + n.r + 20, s.labelW * 1.7, BODY, "600 ", 2);
				ctx.globalAlpha = 1;
				return;
			}

			var lbl = n.label;
			var dr2 = n.isBack ? dotRadius(n) + 7 : dotRadius(n);
			var lx, ly, box, w, bh;

			if (s.narrow && !n.isBack) {
				/* the standing ring: the label sits under its dot, centred */
				ctx.textAlign = "center";
				ctx.font = "500 " + BODY + "px " + FONT;
				w = Math.min(s.labelW, ctx.measureText(lbl).width) + 8;
				lx = n.x; ly = n.y + dr2 + 14 + BODY * 0.7;
				bh = BODY * 2.6;
				box = { x: lx - w / 2, y: ly - bh / 2, w: w, h: bh };
				for (var k2 = 0; k2 < 7; k2++) {
					if (!blocked(box, n)) break;
					ly += BODY * 1.1; box.y += BODY * 1.1;
				}
				/* never let a label run off the drawing */
				lx = clampX(lx, w / 2); ly = clampY(ly, bh / 2);
				box.x = lx - w / 2; box.y = ly - bh / 2;
				boxes.push(box); n._lb = box;
				wrapText(lbl, lx, ly, s.labelW, BODY,
					conceptuality(n) > 0.7 ? "600 " : "500 ", 2);
				ctx.globalAlpha = 1;
				return;
			}

			/* the outboard label, aligned away from the hub and pushed further
			   out until its box clears the ones already drawn */
			var ang2 = n.isBack ? 0.55 : Math.atan2(n.y, n.x);
			var ca = Math.cos(ang2), sa = Math.sin(ang2);
			ctx.textAlign = ca < -0.25 ? "right" : (ca > 0.25 ? "left" : "center");
			ctx.font = "500 " + BODY + "px " + FONT;
			var out = dr2 + (Math.abs(ca) < 0.35 ? dr2 * 0.9 + 18 : 26);
			for (var tries = 0; tries < 5; tries++) {
				lx = n.x + ca * out; ly = n.y + sa * out;
				w = Math.min(s.labelW, ctx.measureText(lbl).width || s.labelW) + 8;
				bh = BODY * 2.8;
				var bx = lx + (ctx.textAlign === "left" ? w / 2
					: ctx.textAlign === "right" ? -w / 2 : 0);
				box = { x: bx - w / 2, y: ly - bh / 2, w: w, h: bh };
				if (!blocked(box, n)) break;
				out += BODY * 1.2;
			}
			var shift = clampX(box.x + box.w / 2, box.w / 2) - (box.x + box.w / 2);
			lx += shift; box.x += shift;
			shift = clampY(ly, bh / 2) - ly;
			ly += shift; box.y += shift;
			boxes.push(box); n._lb = box;
			wrapText(lbl, lx, ly, s.labelW, BODY,
				conceptuality(n) > 0.7 ? "600 " : "500 ", 3);
			ctx.textAlign = "center";
			ctx.globalAlpha = 1;
		});

		ctx.restore();
		if (GH.pulse && GH.t - GH.pulse.t0 > 2.4) GH.pulse = null;
	}

	/* ====================================================================
	   9) The callout
	   ==================================================================== */

	function placeTip() {
		var n = GH.hover;
		if (tip.hidden || !n) return;
		var ox = GH.w / 2, oy = GH.h / 2, r = (n.r || 14) + 4;
		var x0 = n.x - r, y0 = n.y - r, x1 = n.x + r, y1 = n.y + r;
		if (n._lb) {
			x0 = Math.min(x0, n._lb.x); y0 = Math.min(y0, n._lb.y);
			x1 = Math.max(x1, n._lb.x + n._lb.w); y1 = Math.max(y1, n._lb.y + n._lb.h);
		}
		var L = ox + x0, R = ox + x1, T = oy + y0, B = oy + y1;
		var cx = ox + n.x, cy = oy + n.y;
		var tw = tip.offsetWidth, th = tip.offsetHeight, gap = 12;
		var room = { right: GH.w - R, left: L, below: GH.h - B, above: T };
		var need = { right: tw + gap, left: tw + gap, below: th + gap, above: th + gap };
		var order = ["right", "left", "below", "above"].sort(function (a, b) {
			return room[b] - room[a];
		});
		var side = order.filter(function (k) { return room[k] >= need[k]; })[0] || order[0];
		var x, y;
		if (side === "right") { x = R + gap; y = cy - th / 2; }
		else if (side === "left") { x = L - gap - tw; y = cy - th / 2; }
		else if (side === "below") { x = cx - tw / 2; y = B + gap; }
		else { x = cx - tw / 2; y = T - gap - th; }
		if (side === "right" || side === "left") y = Math.max(4, Math.min(GH.h - th - 4, y));
		else x = Math.max(4, Math.min(GH.w - tw - 4, x));
		tip.style.left = x + "px"; tip.style.top = y + "px";
		tip.dataset.side = side;
		var ap = (side === "right" || side === "left")
			? Math.max(12, Math.min(th - 12, cy - y))
			: Math.max(12, Math.min(tw - 12, cx - x));
		tip.style.setProperty("--ap", ap + "px");
	}

	function showTip(n) {
		if (!n) { tip.hidden = true; return; }
		var kind;
		if (n.isBack) kind = t("back", "Back to the overview");
		else if (n.kindOf === "cluster") {
			kind = t("group", "Group") + " · " + n.count + " " +
				(n.count === 1 ? t("area", "area") : t("areas", "areas"));
		} else kind = t("area_one", "Subject area");
		tip.innerHTML = '<span class="t"></span><b></b><span class="d"></span>';
		tip.querySelector(".t").textContent = kind;
		tip.querySelector("b").textContent = n.label;
		tip.querySelector(".d").textContent = (n.desc || "").slice(0, 190);
		tip.hidden = false;
		placeTip();
	}

	/* ====================================================================
	   10) Navigation
	   ==================================================================== */

	function go(key) {
		GH.focus = key;
		GH.sel = null;
		GH.pulse = null;
		tip.hidden = true;
		GH.hover = null;
		detail.textContent = "";
		build();
		renderCrumbs();
		if (key !== null) {
			showDetail(GH.nodes.filter(function (n) { return n.isFocus; })[0]);
		}
		apply();
		settleIfUnpainted();
	}

	function renderCrumbs() {
		crumbs.textContent = "";
		if (GH.focus === null) {
			var cur = document.createElement("span");
			cur.className = "cur";
			cur.textContent = t("overview", "Overview");
			crumbs.appendChild(cur);
			return;
		}
		var b = document.createElement("button");
		b.type = "button";
		b.textContent = t("overview", "Overview");
		b.addEventListener("click", function () { go(null); cv.focus(); });
		crumbs.appendChild(b);
		var sep = document.createElement("span");
		sep.className = "sep"; sep.textContent = "›";
		crumbs.appendChild(sep);
		var cur2 = document.createElement("span");
		cur2.className = "cur";
		cur2.textContent = (byCluster[GH.focus] || {}).name || GH.focus;
		crumbs.appendChild(cur2);
	}

	function showDetail(n) {
		detail.textContent = "";
		if (!n || n.isBack) return;
		var wrap = document.createElement("div");
		wrap.className = "detail";

		var title = document.createElement("div");
		title.className = "dtitle";
		var main = document.createElement("span");
		main.className = "de"; main.textContent = n.label;
		title.appendChild(main);
		if (n.sub && n.sub !== n.label) {
			var alt = document.createElement("span");
			alt.className = "en"; alt.textContent = n.sub;
			alt.setAttribute("lang", OTHER);
			title.appendChild(alt);
		}
		wrap.appendChild(title);

		if (n.desc) {
			var d = document.createElement("div");
			d.className = "desc";
			var p = document.createElement("p");
			p.textContent = n.desc;
			d.appendChild(p);
			wrap.appendChild(d);
		}

		if (n.kindOf === "domain" && n.href) {
			var a = document.createElement("a");
			a.className = "mlink";
			a.href = n.href;
			a.textContent = t("open", "Open the manual page");
			var ext = document.createElement("span");
			ext.className = "ext"; ext.textContent = "›";
			a.appendChild(ext);
			wrap.appendChild(a);
		} else {
			var hint = document.createElement("p");
			hint.className = "oo-map__hint";
			hint.textContent = (n.kindOf === "cluster")
				? t("hint_area", "Select a subject area to see its manual page.")
				: t("hint_none", "This subject area has no manual page yet.");
			wrap.appendChild(hint);
		}
		detail.appendChild(wrap);
	}

	function activate(n) {
		if (!n) return;
		if (n.isBack) { go(n.target); return; }
		if (n.isFocus) { showDetail(n); return; }
		if (n.kindOf === "cluster") { go(n.key); return; }
		GH.sel = n.key;
		GH.pulse = { key: n.key, t0: GH.t };
		showDetail(n);
		apply();
		wake();
	}

	/* ====================================================================
	   11) The cards follow the selection
	   ==================================================================== */

	function apply() {
		var chosen = GH.sel
			? GH.nodes.filter(function (n) { return n.key === GH.sel; })[0]
			: null;
		var mode = chosen ? "domain" : (GH.focus ? "cluster" : "all");
		var domain = chosen ? chosen.domain : null;
		var shown = 0;

		cards.forEach(function (card) {
			var visible = mode === "all"
				|| (mode === "cluster" && card.cluster === GH.focus)
				|| (mode === "domain" && card.domain === domain);
			card.item.hidden = !visible;
			if (visible) shown++;
		});
		sections.forEach(function (section) {
			var any = cards.some(function (card) {
				return section.grid.contains(card.item) && !card.item.hidden;
			});
			section.grid.hidden = !any;
			section.lead.forEach(function (el) { el.hidden = !any; });
		});

		var label = mode === "all"
			? t("all", "All subject areas")
			: (chosen ? chosen.label : (byCluster[GH.focus] || {}).name || "");
		status.textContent = label + " — " + shown + " " +
			(shown === 1 ? t("card", "card") : t("cards", "cards"));
	}

	/* ====================================================================
	   12) The loop
	   ==================================================================== */

	function resize() {
		var dpr = Math.min(2, window.devicePixelRatio || 1);
		var r = cv.getBoundingClientRect();
		if (!r.width) return;
		GH.dpr = dpr; GH.w = r.width; GH.h = r.height;
		var w = Math.round(r.width * dpr), h = Math.round(r.height * dpr);
		if (cv.width !== w || cv.height !== h) {
			/* Assigning the backing size wipes the canvas, so the drawing is
			   put back at once rather than waiting for the next frame: a
			   browser suspends requestAnimationFrame for a hidden window and
			   the map would stay blank. */
			cv.width = w; cv.height = h;
			draw();
		}
		wake();
	}

	function frame() {
		GH.raf = 0;
		if (!GH.on) return;
		GH.frames++;
		step(); draw(); placeTip();
		if (still && GH.idle > 20) return;   // settled, and the reader asked for calm
		GH.raf = requestAnimationFrame(frame);
	}

	function wake() {
		GH.idle = 0;
		if (GH.on && !GH.raf) GH.raf = requestAnimationFrame(frame);
	}

	/* A browser delivers no frames to a hidden or background window, and the
	   entrance of a new level would then never be drawn. If nothing has been
	   painted shortly after a move, the level is settled in one go and drawn
	   once, so the map is never left showing the level before it. */
	function settleIfUnpainted() {
		var mark = GH.frames;
		setTimeout(function () {
			if (GH.frames !== mark || !GH.w) return;
			for (var i = 0; i < 80; i++) step();
			draw();
		}, 180);
	}

	/* ====================================================================
	   13) Input
	   ==================================================================== */

	function at(ev) {
		var r = cv.getBoundingClientRect();
		var x = ev.clientX - r.left - GH.w / 2;
		var y = ev.clientY - r.top - GH.h / 2;
		var best = null, bd = 1e9;
		GH.nodes.forEach(function (n) {
			var d = Math.hypot(n.x - x, n.y - y);
			var reach = (n.r || 14) + 8;
			if (n._lb && x >= n._lb.x && x <= n._lb.x + n._lb.w &&
				y >= n._lb.y && y <= n._lb.y + n._lb.h) { d = 0; }
			if (d < reach && d < bd) { bd = d; best = n; }
		});
		return best;
	}

	cv.addEventListener("pointermove", function (ev) {
		var n = at(ev);
		if (n !== GH.hover) { GH.hover = n; showTip(n); wake(); }
		cv.style.cursor = n ? "pointer" : "default";
	});
	cv.addEventListener("pointerleave", function () {
		GH.hover = null; tip.hidden = true; wake();
	});
	cv.addEventListener("click", function (ev) {
		var n = at(ev);
		if (!n) return;
		GH.kb = n;
		activate(n);
	});

	cv.addEventListener("keydown", function (ev) {
		var ring = GH.nodes.filter(function (n) { return !n.isFocus; });
		if (!ring.length) return;
		var i = ring.indexOf(GH.kb);
		if (ev.key === "ArrowRight" || ev.key === "ArrowDown") {
			GH.kb = ring[(i + 1 + ring.length) % ring.length];
		} else if (ev.key === "ArrowLeft" || ev.key === "ArrowUp") {
			GH.kb = ring[(i - 1 + ring.length) % ring.length];
		} else if (ev.key === "Enter" || ev.key === " ") {
			activate(GH.kb);
		} else if (ev.key === "Escape" || ev.key === "Backspace") {
			if (GH.sel) {
				GH.sel = null;
				showDetail(GH.nodes.filter(function (n) { return n.isFocus; })[0]);
				apply();
			} else if (GH.focus !== null) {
				go(null);
			} else return;
		} else if (ev.key === "Home") {
			go(null);
		} else return;
		ev.preventDefault();
		if (GH.kb) { GH.hover = GH.kb; showTip(GH.kb); }
		wake();
	});
	cv.addEventListener("blur", function () {
		GH.hover = null; tip.hidden = true; wake();
	});

	if (window.ResizeObserver) new ResizeObserver(resize).observe(cv);
	else window.addEventListener("resize", resize);

	/* a docs page is long: the loop runs only while the map is on screen */
	if (window.IntersectionObserver) {
		new IntersectionObserver(function (entries) {
			GH.on = entries[0].isIntersecting;
			if (GH.on) wake();
			else if (GH.raf) { cancelAnimationFrame(GH.raf); GH.raf = 0; }
		}, { rootMargin: "120px" }).observe(cv);
	}

	/* ====================================================================
	   14) Start
	   ==================================================================== */

	resize();
	build();
	renderCrumbs();
	apply();
	/* A browser suspends requestAnimationFrame for a hidden or background
	   window. The first frame is therefore painted here, not waited for. */
	if (GH.w) draw();
	wake();
})();
