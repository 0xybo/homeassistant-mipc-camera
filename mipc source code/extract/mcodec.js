var mcodec = null;
function f(a, c) {
	return (a ? a : "%") + v.charAt(c >> 4) + v.charAt(c & 15);
}

function e(a) {
	return 48 <= a && 57 >= a ? a - 48 : 65 <= a && 71 >= a ? a - 55 : 97 <= a && 102 >= a ? a - 87 : 0;
}

function d(a, c) {
	var b,
		d,
		g,
		f = "",
		l = "" + a;
	if (0 == l.indexOf("0x"))
		for (b = l.length - 1; 1 < b; ) {
			for (d = g = 0; 8 > d && 1 < b; --b, d += 4) g += e(l.charCodeAt(b)) << d;
			f = s(g) + f;
		}
	else for (b = 24; 0 <= b; b -= 8) a >= 1 << b && (f += s((a >> b) & 255));
	for (; f.length < c; ) f = "\x00" + f;
	return f;
}

function b(a, c) {
	for (var b, d, e, g, f = 0, l = "", h = a.length, m = c ? A : u; f < h; ) {
		for (d = 0; 24 > d && f < h; d += 8, ++f) b = (b << 8) + a.charCodeAt(f);
		for (g = 0; 24 > g; g += 6, b &= (1 << (d - g)) - 1) (e = d - g - 6), (l += g < d ? m.charAt(0 > e ? b << -e : b >> e) : "");
	}
	return l;
}

function g(a, c) {
	var b,
		d,
		e,
		g,
		l,
		h,
		m,
		r = "";
	e = 0;
	for (h = a.length; e < h; ++e)
		if (127 >= (d = a.charCodeAt(e))) r += C[(b = a.charAt(e))] ? f(c, d) : b;
		else {
			m = "";
			for (g = l = 128 > d ? 0 : 2048 > d ? 1 : 65536 > d ? 2 : 4194304 > d ? 3 : 134217728 > d ? 4 : 5; 0 < g; --g, d >>= 6)
				m = f(c, 128 | (d & 63)) + m;
			d |= t[l];
			r += f(c, d) + m;
		}
	return r;
}

function h(a, c) {
	var b,
		d,
		g,
		f = a.length,
		l,
		h,
		m,
		r = "",
		c = c || "%";
	for (g = 0; g < f; )
		if (c != a.charAt(g) || g + 3 > f) (r += a.charAt(g)), ++g;
		else {
			b = (e(a.charCodeAt(g + 1) & 255) << 4) + e(a.charCodeAt(g + 2) & 255);
			l = t.length;
			for (d = 0; 1 < l; --l)
				if (b >= t[l - 1]) {
					if ((m = g + 3 * l) <= f) {
						d = b - t[l - 1];
						for (h = g + 3; h < m && c == a.charAt(h); h += 3)
							d = (d << 6) + (((e(a.charCodeAt(h + 1) & 255) << 4) + e(a.charCodeAt(h + 2) & 255)) & 95);
						h == m && ((r += s(d)), (g += 3 * l));
					}
					break;
				}
			0 == d && ((r += s(b)), (g += 3));
		}
	return r;
}

function c(c, b) {
	function d(c, b) {
		var h,
			m,
			r,
			u,
			t = c.constructor == Array ? b + "__x_countz_" + e + c.length : "";
		for (h in c)
			if (void 0 != (m = c[h]) && null != m) {
				if ((r = "%" == ("" + h).charAt(0))) h = h.substr(1);
				u = b + (0 != h ? ("" == b ? "d" : "_") + h : "");
				"function" != typeof m &&
					(t =
						typeof m == q
							? t + (("" == t ? "" : f) + (m.constructor == Array ? "" : u + e + "1" + f) + d(m, u))
							: t + (("" == t ? "" : f) + u + e + (r ? m : g("" + m, l))));
			}
		return t;
	}
	var e = "-" == b ? "-" : "=",
		f = "=" == e ? "&" : "-",
		l = "-" == b ? "_" : "%";
	return d(c, "", b);
}

function l(c, b) {
	function d(c, b, e) {
		var g,
			f,
			l,
			h,
			m = c.constructor == Array,
			r = m ? '<input type="hidden" name="' + b + '__x_countz_" value="' + c.length + '"/>\r\n' : "";
		for (g in c)
			if (void 0 != (f = c[g]) && null != f)
				(l = b + (0 != g ? ("" == b ? "d" : "_") + g : "")),
					(h = "" + e + (m ? "[" + g + "]" : ("" == e ? "" : ".") + g)),
					(r =
						typeof f == q
							? r +
							  ('<div style="border:1px solid #00ffff;padding:2px;"><br/>\r\n' +
									(0 == g ? "" : '<input type="hidden" name="' + l + '" value="1"/>\r\n') +
									d(f, l, h) +
									"</div>\r\n")
							: r + ("<label>" + h + ':</label><input type="text" name="' + l + '" value="' + f + '"/><br/>'));
		return r;
	}
	return (
		'<form action="' +
		b +
		'" method="get" style="border:2px solid blue;padding:1px;"><button id="submit" type="submit">\u63d0\u4ea4</button><br/>' +
		d(c, "", "") +
		"</form>"
	);
}

function m(c) {
	if (c) {
		var b,
			d,
			e,
			g,
			f = 0,
			l,
			h = c.constructor == Array,
			r = h ? "[" : "{";
		for (b in c)
			switch (((d = c[b]), (r += (0 == f++ ? "" : ",") + (h ? "" : b + ":")), typeof d)) {
				case "number":
					r += d;
					break;
				case "object":
					r += m(d);
					break;
				case "string":
					r += '"';
					e = 0;
					for (l = d.length; e < l; ++e)
						(g = d.charAt(e)), (r += '"' != g && "\\" != g ? ("\n" == g ? "\\n" : "\r" == g ? "\\r" : g) : "\\" + g);
					r += '"';
			}
		return r + (h ? "]" : "}");
	}
	return "";
}
var q = "object",
	s = String.fromCharCode,
	r = function (a) {
		try {
			return eval("(" + a + ")");
		} catch (c) {
			return null;
		}
	},
	t = [0, 192, 224, 240, 248, 252],
	v = "0123456789abcdef",
	u = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
	A = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_.-",
	C = {},
	B = [
		["&", "&amp;"],
		["\\n", "&#10;"],
		["\\r", "&#13;"],
		["\\t", "&#9;"],
		["`", "&#96;"],
		["'", "&#39;"],
		['"', "&quot;"],
		[" ", "&nbsp;"],
		["<", "&lt;"],
		[">", "&gt;"],
	],
	K = [
		{
			s: /\[img\]([^\]]*)\[\/img\]/gi,
			d: '<img src="$1" border="0"/>',
		},
		{
			s: /\[flash\]([^\]]*)\[\/flash\]/gi,
			d:
				'<embed type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/shockwave/download/index.cgi?P1_Prod_Version=ShockwaveFlash" quality="heigh" src="$1"/></embed>',
		},
		{
			s: /\[url=([^\]]*)\]([^\]]*)\[\/url\]/gi,
			d: '<a href="$1" target="_blank">$2</a>',
		},
		{
			s: /\[url\]([^\]]*)\[\/url\]/gi,
			d: '<a href="$1" target="_blank">$1</a>',
		},
		{
			s: /\[email=([^\]]*)\]([^\]]*)\[\/email\]/gi,
			d: '<a href="mailto:$1">$2</a>',
		},
		{
			s: /\[email\]([^\]]*)\[\/email\]/gi,
			d: '<a href="mailto:$1">$1</a>',
		},
		{
			s: /\[color=([^\]]*)\]([^\]]*)\[\/color\]/gi,
			d: '<font color="$1">$2</font>',
		},
		{
			s: /\[face=([^\]]*)\]([^\]]*)\[\/face\]/gi,
			d: '<font face="$1">$2</font>',
		},
		{
			s: /\[size=1\]([^\]]*)\[\/size\]/gi,
			d: '<font size="1">$1</font>',
		},
		{
			s: /\[size=2\]([^\]]*)\[\/size\]/gi,
			d: '<font size="2">$1</font>',
		},
		{
			s: /\[size=3\]([^\]]*)\[\/size\]/gi,
			d: '<font size="3">$1</font>',
		},
		{
			s: /\[size=4\]([^\]]*)\[\/size\]/gi,
			d: '<font size="4">$1</font>',
		},
		{
			s: /\[align=([^\]]*)\]([^]]*)\[\/face\]/gi,
			d: '<align="$1">$2</align>',
		},
		{
			s: /\[fly\]([^\]]*)\[\/fly\]/gi,
			d: "<marquee>$1</marquee>",
		},
		{
			s: /\[b\]([^\]]*)\[\/b\]/gi,
			d: "<b>$1</b>",
		},
		{
			s: /\[i\]([^\]]*)\[\/i\]/gi,
			d: "<i>$1</i>",
		},
		{
			s: /\[u\]([^\]]*)\[\/u\]/gi,
			d: "<u>$1</u>",
		},
		{
			s: /\[code\]([^\]]*)\[\/code\]/gi,
			d: '<pre><font size="2" face="Verdana,Arial">$1</font></pre>',
		},
		{
			s: /\[list\]([^\]]*)\[\/list\]/gi,
			d: "<ul>$1</ul>",
		},
		{
			s: /\[list=1\]([^\]]*)\[\/list\]/gi,
			d: '<ol type="1">$1</ol>',
		},
		{
			s: /\[list=a\]([^\]]*)\[\/list\]/gi,
			d: '<ol type="a">$1</ol>',
		},
		{
			s: /\[\*\]([^\]]*)\[\/\*\]/gi,
			d: "<li>$1</li>",
		},
		{
			s: /\[quote\]([^\]]*)\[\/quote\]/gi,
			d: "<blockquote>$1</blockquote>",
		},
	],
	F;
for (F = 0; 21 > F; ++F) C["\x00\t\n\r\"\\' #%&+-_./:;=?@".charAt(F)] = 1;
mcodec = {
	magic: "mcodec",
	str_2_b64: b,
	b64_2_binary: function (a) {
		if (a) {
			for (var c = [], b = 0; b < A.length; b++) c[A.charAt(b)] = b;
			var d,
				e,
				g,
				f,
				l = a.length,
				h = l;
			"-" == a.charAt(l - 1) && (h -= 4);
			for (var m = [], b = 0; b < h; b += 4)
				(d = c[a.charAt(b)]),
					(e = c[a.charAt(b + 1)]),
					(g = c[a.charAt(b + 2)]),
					(f = c[a.charAt(b + 3)]),
					(d = (d << 2) | (e >> 4)),
					(e = (e << 4) | (g >> 2)),
					(g = (g << 6) | f),
					m.push(d & 255),
					m.push(e & 255),
					m.push(g & 255);
			h != l &&
				((d = c[a.charAt(b)]),
				(e = c[a.charAt(b + 1)]),
				(g = a.charAt(b + 2)),
				m.push(((d << 2) | (e >> 4)) & 255),
				"-" != g && ((g = c[g]), m.push(((e << 4) | (g >> 2)) & 255)));
			return m;
		}
	},
	binary_2_b64: function (a, c) {
		for (var b, d, e, g, f = 0, l = "", h = a.length, m = c ? A : u; f < h; ) {
			for (d = 0; 24 > d && f < h; d += 8, f++) b = (b << 8) + a[f];
			for (g = 0; 24 > g; g += 6, b &= (1 << (d - g)) - 1) (e = d - g - 6), (l += g < d ? m.charAt(0 > e ? b << -e : b >> e) : "");
		}
		return l;
	},
	str_2_uri_param: g,
	uri_param_2_str: h,
	uri_2_obj: function (a) {
		var c = {},
			b,
			d,
			e,
			g,
			f,
			l,
			m = a.length,
			r = 0 < m && "-" == a.charAt(0) ? "-" : "=",
			q = "-" == r ? "-" : "&",
			u = "-" == q ? "_" : "%";
		for (l = 1; l < m; ++l) {
			for (d = l; l < m && r != (b = a.charAt(l)) && b != q; ++l);
			g = l - d;
			for (e = l += l < m && r == b ? 1 : 0; l < m && q != a.charAt(l); ++l);
			f = l - e;
			0 < g && 0 < f && (c[a.substr(d, g)] = h(a.substr(e, f), u));
		}
		return c;
	},
	obj_2_url: c,
	json_txt_2_url: function (a, b) {
		var d = a.indexOf("("),
			e = a.lastIndexOf(")");
		0 < d && e > d && (a = a.substring(d + 1, e));
		return c(r(a), b);
	},
	obj_2_form: l,
	json_txt_2_form: function (a, c) {
		var b = a.indexOf("("),
			d = a.lastIndexOf(")");
		0 < b && d > b && (a = a.substring(b + 1, d));
		return l(r(a), c);
	},
	obj_2_str: m,
	str_2_html: function (a) {
		for (var c = 0; c < B.length; ++c) a = a.replace(RegExp(B[c][0], "g"), B[c][1]);
		return a;
	},
	html_2_str: function (a) {
		for (var c = B.length - 1; 0 <= c; --c) a = a.replace(RegExp(B[c][1], "g"), B[c][0]);
		return a;
	},
	ubb_2_html: function (a) {
		for (var c, b = K.length; 0 <= b; --b) (c = K[b]), (a = a.replace(c.s, c.d));
		return a;
	},
	hex_2_uri_param: function (a) {
		var c,
			b = "";
		for (c = 0; c < a.length; ++c) b += (0 == (1 & c) ? "%" : "") + a.charAt(c);
		return b;
	},
	nid: function (a, c, e, g, f, l, h, m) {
		var a = d(a),
			r = c ? d(c) : "",
			c = c ? d(g) : "",
			l = l ? d("0x" + h[m](l)) : "",
			f =
				(a ? s(64 + a.length) + a : "") +
				(r ? s(96 + r.length) + r : "") +
				(c ? s(128 + c.length) + c : "") +
				(f ? s(160 + f.length) + f : ""),
			e = f + (e ? s(0 + e.length) + e : "") + (l ? s(0 + l.length) + l : "");
		s_md5 = d("0x" + h[m](e));
		return b(s(32 + s_md5.length) + s_md5 + f, 1);
	},
};
