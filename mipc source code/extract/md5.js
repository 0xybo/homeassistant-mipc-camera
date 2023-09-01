function e(e, t) {
	var o = (65535 & e) + (65535 & t);
	return (((e >> 16) + (t >> 16) + (o >> 16)) << 16) | (65535 & o);
}
function t(t, o, r, n, a, i) {
	return (t = e(e(o, t), e(n, i))), e((t << a) | (t >>> (32 - a)), r);
}
function o(e, o, r, n, a, i, l) {
	return t((o & r) | (~o & n), e, o, a, i, l);
}
function r(e, o, r, n, a, i, l) {
	return t((o & n) | (r & ~n), e, o, a, i, l);
}
function n(e, o, r, n, a, i, l) {
	return t(r ^ (o | ~n), e, o, a, i, l);
}
function a(a, i) {
	(a[i >> 5] |= 128 << i % 32), (a[14 + (((i + 64) >>> 9) << 4)] = i);
	var l = 1732584193,
		s = -271733879,
		c = -1732584194,
		d = 271733878,
		_ = 0;
	for (i = a.length; _ < i; _ += 16) {
		var g = l,
			m = s,
			p = c,
			u = d;
		(l = o(l, s, c, d, a[_ + 0], 7, -680876936)),
			(d = o(d, l, s, c, a[_ + 1], 12, -389564586)),
			(c = o(c, d, l, s, a[_ + 2], 17, 606105819)),
			(s = o(s, c, d, l, a[_ + 3], 22, -1044525330)),
			(l = o(l, s, c, d, a[_ + 4], 7, -176418897)),
			(d = o(d, l, s, c, a[_ + 5], 12, 1200080426)),
			(c = o(c, d, l, s, a[_ + 6], 17, -1473231341)),
			(s = o(s, c, d, l, a[_ + 7], 22, -45705983)),
			(l = o(l, s, c, d, a[_ + 8], 7, 1770035416)),
			(d = o(d, l, s, c, a[_ + 9], 12, -1958414417)),
			(c = o(c, d, l, s, a[_ + 10], 17, -42063)),
			(s = o(s, c, d, l, a[_ + 11], 22, -1990404162)),
			(l = o(l, s, c, d, a[_ + 12], 7, 1804603682)),
			(d = o(d, l, s, c, a[_ + 13], 12, -40341101)),
			(c = o(c, d, l, s, a[_ + 14], 17, -1502002290)),
			(s = o(s, c, d, l, a[_ + 15], 22, 1236535329)),
			(l = r(l, s, c, d, a[_ + 1], 5, -165796510)),
			(d = r(d, l, s, c, a[_ + 6], 9, -1069501632)),
			(c = r(c, d, l, s, a[_ + 11], 14, 643717713)),
			(s = r(s, c, d, l, a[_ + 0], 20, -373897302)),
			(l = r(l, s, c, d, a[_ + 5], 5, -701558691)),
			(d = r(d, l, s, c, a[_ + 10], 9, 38016083)),
			(c = r(c, d, l, s, a[_ + 15], 14, -660478335)),
			(s = r(s, c, d, l, a[_ + 4], 20, -405537848)),
			(l = r(l, s, c, d, a[_ + 9], 5, 568446438)),
			(d = r(d, l, s, c, a[_ + 14], 9, -1019803690)),
			(c = r(c, d, l, s, a[_ + 3], 14, -187363961)),
			(s = r(s, c, d, l, a[_ + 8], 20, 1163531501)),
			(l = r(l, s, c, d, a[_ + 13], 5, -1444681467)),
			(d = r(d, l, s, c, a[_ + 2], 9, -51403784)),
			(c = r(c, d, l, s, a[_ + 7], 14, 1735328473)),
			(s = r(s, c, d, l, a[_ + 12], 20, -1926607734)),
			(l = t(s ^ c ^ d, l, s, a[_ + 5], 4, -378558)),
			(d = t(l ^ s ^ c, d, l, a[_ + 8], 11, -2022574463)),
			(c = t(d ^ l ^ s, c, d, a[_ + 11], 16, 1839030562)),
			(s = t(c ^ d ^ l, s, c, a[_ + 14], 23, -35309556)),
			(l = t(s ^ c ^ d, l, s, a[_ + 1], 4, -1530992060)),
			(d = t(l ^ s ^ c, d, l, a[_ + 4], 11, 1272893353)),
			(c = t(d ^ l ^ s, c, d, a[_ + 7], 16, -155497632)),
			(s = t(c ^ d ^ l, s, c, a[_ + 10], 23, -1094730640)),
			(l = t(s ^ c ^ d, l, s, a[_ + 13], 4, 681279174)),
			(d = t(l ^ s ^ c, d, l, a[_ + 0], 11, -358537222)),
			(c = t(d ^ l ^ s, c, d, a[_ + 3], 16, -722521979)),
			(s = t(c ^ d ^ l, s, c, a[_ + 6], 23, 76029189)),
			(l = t(s ^ c ^ d, l, s, a[_ + 9], 4, -640364487)),
			(d = t(l ^ s ^ c, d, l, a[_ + 12], 11, -421815835)),
			(c = t(d ^ l ^ s, c, d, a[_ + 15], 16, 530742520)),
			(s = t(c ^ d ^ l, s, c, a[_ + 2], 23, -995338651)),
			(l = n(l, s, c, d, a[_ + 0], 6, -198630844)),
			(d = n(d, l, s, c, a[_ + 7], 10, 1126891415)),
			(c = n(c, d, l, s, a[_ + 14], 15, -1416354905)),
			(s = n(s, c, d, l, a[_ + 5], 21, -57434055)),
			(l = n(l, s, c, d, a[_ + 12], 6, 1700485571)),
			(d = n(d, l, s, c, a[_ + 3], 10, -1894986606)),
			(c = n(c, d, l, s, a[_ + 10], 15, -1051523)),
			(s = n(s, c, d, l, a[_ + 1], 21, -2054922799)),
			(l = n(l, s, c, d, a[_ + 8], 6, 1873313359)),
			(d = n(d, l, s, c, a[_ + 15], 10, -30611744)),
			(c = n(c, d, l, s, a[_ + 6], 15, -1560198380)),
			(s = n(s, c, d, l, a[_ + 13], 21, 1309151649)),
			(l = n(l, s, c, d, a[_ + 4], 6, -145523070)),
			(d = n(d, l, s, c, a[_ + 11], 10, -1120210379)),
			(c = n(c, d, l, s, a[_ + 2], 15, 718787259)),
			(s = n(s, c, d, l, a[_ + 9], 21, -343485551)),
			(l = e(l, g)),
			(s = e(s, m)),
			(c = e(c, p)),
			(d = e(d, u));
	}
	return [l, s, c, d];
}
function i(e) {
	for (var t = 0, o = [], r = (1 << p) - 1; t < e.length * p; t += p) o[t >> 5] |= (e.charCodeAt(t / p) & r) << t % 32;
	return o;
}
function l(e, t) {
	var o;
	o = 0;
	var r = Array(16),
		n = Array(16),
		l = i(e);
	for (16 < l.length && (l = a(l, e.length * p)); 16 > o; o++) (r[o] = 909522486 ^ l[o]), (n[o] = 1549556828 ^ l[o]);
	return (o = a(r.concat(i(t)), 512 + t.length * p)), a(n.concat(o), 640);
}
function s(e) {
	var t,
		o = "";
	for (t = 0, len = 4 * e.length; t < len; t++) o += _.charAt((e[t >> 2] >> ((t % 4) * 8 + 4)) & 15) + _.charAt((e[t >> 2] >> ((t % 4) * 8)) & 15);
	return o;
}
function c(e) {
	for (var t = 0, o = "", r = (1 << p) - 1; t < 32 * e.length; t += p) o += String.fromCharCode((e[t >> 5] >>> t % 32) & r);
	return o;
}
function d(e) {
	for (var t, o, r = 0, n = ""; r < 4 * e.length; r += 3)
		for (
			t =
				(((e[r >> 2] >> ((r % 4) * 8)) & 255) << 16) |
				(((e[(r + 1) >> 2] >> (((r + 1) % 4) * 8)) & 255) << 8) |
				((e[(r + 2) >> 2] >> (((r + 2) % 4) * 8)) & 255),
				o = 0;
			4 > o;
			o++
		)
			n = 8 * r + 6 * o > 32 * e.length ? n + m : n + g.charAt((t >> (6 * (3 - o))) & 63);
	return n;
}
var _ = "0123456789abcdef",
	g = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",
	m = "=",
	p = 8;
function hex(e) {
	return s(a(i(e), e.length * p));
}
function b64(e) {
	return d(a(i(e), e.length * p));
}
function str(e) {
	return c(a(i(e), e.length * p));
}
function hex_hmac(e, t) {
	return s(l(e, t));
}
function b64_hmac(e, t) {
	return d(l(e, t));
}
function str_hmac(e, t) {
	return c(l(e, t));
}
