function e(c, b) {
	for (var d = 1, e = 0; ; ) {
		if (1 == c) return d;
		if (0 == c) return 0;
		e -= d * Math.floor(b / c);
		b %= c;
		if (1 == b) return e;
		if (0 == b) return 0;
		d -= e * Math.floor(c / b);
		c %= b;
	}
}

function d(a, c, b) {
	var d,
		e = a.length,
		g = c.length;
	k = e + b < g ? e + b : g;
	for (d = g - 1 - b; d < e && 0 <= d; d++) if (0 < a[d]) return 1;
	for (d = e - 1 + b; d < g; d++) if (0 < c[d]) return 0;
	for (d = k - 1; d >= b; d--) {
		if (a[d - b] > c[d]) return 1;
		if (a[d - b] < c[d]) break;
	}
	return 0;
}

function b(a, c) {
	var b,
		d = a.length < c.length ? a.length : c.length;
	for (b = a.length; b < c.length; b++) if (c[b]) return 0;
	for (b = c.length; b < a.length; b++) if (a[b]) return 1;
	for (b = d - 1; 0 <= b; b--) {
		if (a[b] > c[b]) return 1;
		if (a[b] < c[b]) break;
	}
	return 0;
}

function g(c, b, d) {
	b = Math.ceil(b / z) + 1;
	buff = new Array(d > b ? d : b);
	r(buff, c);
	return buff;
}

function h(a, c, b) {
	var d,
		e,
		l,
		h = a.length;
	if (-1 == c) {
		for (l = new Array(0); ; ) {
			c = new Array(l.length + 1);
			for (e = 0; e < l.length; e++) c[e + 1] = l[e];
			c[0] = parseInt(a, 10);
			l = c;
			d = a.indexOf(",", 0);
			if (1 > d) break;
			a = a.substring(d + 1);
			if (0 == a.length) break;
		}
		return l.length < b ? ((c = new Array(b)), s(c, l), c) : l;
	}
	l = g(0, c * h, 0);
	for (e = 0; e < h; e++) {
		d = M.indexOf(a.substring(e, e + 1), 0);
		36 >= c && 36 <= d && (d -= 26);
		if (d >= c || 0 > d) break;
		var m = l,
			r = c,
			q = void 0,
			u = void 0,
			t = void 0,
			C = void 0;
		if (r) {
			u = m.length;
			for (q = t = 0; q < u; q++) (t += m[q] * r), (C = 0), 0 > t && ((C = -(t >> z)), (t += C * N)), (m[q] = t & H), (t = (t >> z) - C);
		}
		m = l;
		t = u = q = r = void 0;
		m[0] += d;
		q = m.length;
		for (r = u = 0; r < q && !((u += m[r]), (t = 0), 0 > u && ((t = -(u >> z)), (u += t * N)), (m[r] = u & H), (u = (u >> z) - t), !u); r++);
	}
	for (h = l.length; 0 < h && !l[h - 1]; h--);
	h = b > h + 1 ? b : h + 1;
	c = new Array(h);
	a = h < l.length ? h : l.length;
	for (e = 0; e < a; e++) c[e] = l[e];
	for (; e < h; e++) c[e] = 0;
	return c;
}

function c(a, c) {
	var b;
	if (a[0] != c) return 0;
	for (b = 1; b < a.length; b++) if (a[b]) return 0;
	return 1;
}

function l(a) {
	var c;
	for (c = 0; c < a.length; c++) if (a[c]) return 0;
	return 1;
}

function m(a, c) {
	var b,
		d = "";
	Ea.length != a.length ? (Ea = q(a)) : s(Ea, a);
	if (-1 == c) {
		for (b = a.length - 1; 0 < b; b--) d += a[b] + ",";
		d += a[0];
	} else for (; !l(Ea); ) (b = u(Ea, c)), (d = M.substring(b, b + 1) + d);
	0 == d.length && (d = "0");
	return d;
}

function q(a) {
	buff = new Array(a.length);
	s(buff, a);
	return buff;
}

function s(a, c) {
	var b,
		d = a.length < c.length ? a.length : c.length;
	for (b = 0; b < d; b++) a[b] = c[b];
	for (b = d; b < a.length; b++) a[b] = 0;
}

function r(a, c) {
	var b, d;
	d = c;
	for (b = 0; b < a.length; b++) (a[b] = d & H), (d >>= z);
}

function t(c, b) {
	var d,
		e = Math.floor(b / z);
	if (e) {
		for (d = 0; d < c.length - e; d++) c[d] = c[d + e];
		for (; d < c.length; d++) c[d] = 0;
		b %= z;
	}
	for (d = 0; d < c.length - 1; d++) c[d] = H & ((c[d + 1] << (z - b)) | (c[d] >> b));
	c[d] >>= b;
}

function v(c, b) {
	var d,
		e = Math.floor(b / z);
	if (e) {
		for (d = c.length; d >= e; d--) c[d] = c[d - e];
		for (; 0 <= d; d--) c[d] = 0;
		b %= z;
	}
	if (b) {
		for (d = c.length - 1; 0 < d; d--) c[d] = H & ((c[d] << b) | (c[d - 1] >> (z - b)));
		c[d] = H & (c[d] << b);
	}
}

function u(c, b) {
	var d,
		e = 0;
	for (d = c.length - 1; 0 <= d; d--) (e = e * N + c[d]), (c[d] = Math.floor(e / b)), (e %= b);
	return e;
}

function A(a, c, b, d) {
	var e, g, f, l;
	f = a.length < d + c.length ? a.length : d + c.length;
	l = a.length;
	g = 0;
	for (e = d; e < f; e++) (g += a[e] + b * c[e - d]), (a[e] = g & H), (g >>= z);
	for (e = f; g && e < l; e++) (g += a[e]), (a[e] = g & H), (g >>= z);
}

function C(c, b) {
	pb.length != c.length ? (pb = q(c)) : s(pb, c);
	qb.length != c.length && (qb = q(c));
	var e = qb,
		g,
		f,
		l,
		h,
		m,
		u;
	s(c, pb);
	for (f = b.length; 0 == b[f - 1]; f--);
	g = b[f - 1];
	for (u = 0; g; u++) g >>= 1;
	u = z - u;
	v(b, u);
	v(c, u);
	for (g = c.length; 0 == c[g - 1] && g > f; g--);
	for (r(e, 0); !d(b, c, g - f); ) {
		l = c;
		h = b;
		m = g - f;
		for (
			var p = void 0, C = void 0, B = void 0, F = void 0, B = l.length < m + h.length ? l.length : m + h.length, F = l.length, C = 0, p = m;
			p < B;
			p++
		)
			(C += l[p] - h[p - m]), (l[p] = C & H), (C >>= z);
		for (p = B; C && p < F; p++) (C += l[p]), (l[p] = C & H), (C >>= z);
		e[g - f]++;
	}
	for (g -= 1; g >= f; g--) {
		for (e[g - f] = c[g] == b[f - 1] ? H : Math.floor((c[g] * N + c[g - 1]) / b[f - 1]); ; )
			if (
				((h = (1 < f ? b[f - 2] : 0) * e[g - f]),
				(m = h >> z),
				(h &= H),
				(l = m + e[g - f] * b[f - 1]),
				(m = l >> z),
				(l &= H),
				m == c[g] ? (l == c[g - 1] ? h > (1 < g ? c[g - 2] : 0) : l > c[g - 1]) : m > c[g])
			)
				e[g - f]--;
			else break;
		A(c, b, -e[g - f], g - f);
		if ((c[c.length - 1] >> (z - 1)) & 1) {
			l = c;
			h = b;
			m = g - f;
			F = B = C = p = void 0;
			B = l.length < m + h.length ? l.length : m + h.length;
			F = l.length;
			C = 0;
			for (p = m; p < B; p++) (C += l[p] + h[p - m]), (l[p] = C & H), (C >>= z);
			for (p = B; C && p < F; p++) (C += l[p]), (l[p] = C & H), (C >>= z);
			e[g - f]--;
		}
	}
	t(b, u);
	t(c, u);
}

function B(a, c, b) {
	var d;
	T.length != 2 * a.length && (T = new Array(2 * a.length));
	r(T, 0);
	for (d = 0; d < c.length; d++) c[d] && A(T, a, c[d], d);
	C(T, b);
	s(a, T);
}

function K(a, c) {
	var b;
	for (b = a.length; 0 < b && !a[b - 1]; b--);
	b = new Array(b + c);
	s(b, a);
	return b;
}

function F(a, c, d, e) {
	var g,
		l,
		h,
		m,
		q,
		u,
		t = d.length,
		C = c.length;
	I.length != t && (I = new Array(t));
	for (r(I, 0); 0 < t && 0 == d[t - 1]; t--);
	for (; 0 < C && 0 == c[C - 1]; C--);
	u = I.length - 1;
	for (g = 0; g < t; g++) {
		q = I[0] + a[g] * c[0];
		m = ((q & H) * e) & H;
		h = (q + m * d[0]) >> z;
		q = a[g];
		for (l = 1; l < C - 4; )
			(h += I[l] + m * d[l] + q * c[l]),
				(I[l - 1] = h & H),
				(h >>= z),
				l++,
				(h += I[l] + m * d[l] + q * c[l]),
				(I[l - 1] = h & H),
				(h >>= z),
				l++,
				(h += I[l] + m * d[l] + q * c[l]),
				(I[l - 1] = h & H),
				(h >>= z),
				l++,
				(h += I[l] + m * d[l] + q * c[l]),
				(I[l - 1] = h & H),
				(h >>= z),
				l++,
				(h += I[l] + m * d[l] + q * c[l]),
				(I[l - 1] = h & H),
				(h >>= z),
				l++;
		for (; l < C; ) (h += I[l] + m * d[l] + q * c[l]), (I[l - 1] = h & H), (h >>= z), l++;
		for (; l < t - 4; )
			(h += I[l] + m * d[l]),
				(I[l - 1] = h & H),
				(h >>= z),
				l++,
				(h += I[l] + m * d[l]),
				(I[l - 1] = h & H),
				(h >>= z),
				l++,
				(h += I[l] + m * d[l]),
				(I[l - 1] = h & H),
				(h >>= z),
				l++,
				(h += I[l] + m * d[l]),
				(I[l - 1] = h & H),
				(h >>= z),
				l++,
				(h += I[l] + m * d[l]),
				(I[l - 1] = h & H),
				(h >>= z),
				l++;
		for (; l < t; ) (h += I[l] + m * d[l]), (I[l - 1] = h & H), (h >>= z), l++;
		for (; l < u; ) (h += I[l]), (I[l - 1] = h & H), (h >>= z), l++;
		I[l - 1] = h & H;
	}
	if (!b(d, I)) {
		c = I;
		l = c.length < d.length ? c.length : d.length;
		for (e = g = 0; e < l; e++) (g += c[e] - d[e]), (c[e] = g & H), (g >>= z);
		for (e = l; g && e < c.length; e++) (g += c[e]), (c[e] = g & H), (g >>= z);
	}
	s(a, I);
}
for (
	var z = 0, H = 0, N = H + 1, M = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_=!@#$%^&*()[]{}|;:,.<>/?`~ \\'\"+-", z = 0;
	1 << (z + 1) > 1 << z;
	z++
);
var z = z >> 1,
	H = (1 << z) - 1,
	N = H + 1,
	G = g(1, 1, 1),
	L = [],
	T = L,
	ha = L,
	pb = L,
	qb = L,
	Ea = L,
	Xa = L,
	I = L,
	Cb = {
		Base: 10,
		PowMod: function (a, b, d) {
			var a = h(a, this.Base),
				b = h(b, this.Base),
				d = h(d, this.Base),
				l = a,
				a = d.length,
				a = g(0, (l.length > a ? l.length : a) * z, 0);
			s(a, l);
			var b = K(b, 2),
				d = K(d, 2),
				t,
				v;
			Xa.length != d.length && (Xa = q(d));
			if (0 == (d[0] & 1)) {
				s(Xa, a);
				for (r(a, 1); !c(b, 0); ) {
					b[0] & 1 && B(a, Xa, d);
					u(b, 2);
					l = Xa;
					v = d;
					var A = void 0,
						L = void 0,
						M = void 0,
						A = (t = void 0);
					for (t = l.length; 0 < t && !l[t - 1]; t--);
					A = t > v.length ? 2 * t : 2 * v.length;
					T.length != A && (T = new Array(A));
					r(T, 0);
					for (A = 0; A < t; A++) {
						M = T[2 * A] + l[A] * l[A];
						T[2 * A] = M & H;
						M >>= z;
						for (L = A + 1; L < t; L++) (M = T[A + L] + 2 * l[A] * l[L] + M), (T[A + L] = M & H), (M >>= z);
						T[A + t] = M;
					}
					C(T, v);
					s(l, T);
				}
			} else {
				r(Xa, 0);
				for (l = d.length; 0 < l && !d[l - 1]; l--);
				v = N;
				A = 0;
				for (t = d.length - 1; 0 <= t; t--) A = (A * N + d[t]) % N;
				v -= e(A, N);
				Xa[l] = 1;
				B(a, Xa, d);
				ha.length != a.length ? (ha = q(a)) : s(ha, a);
				for (l = b.length - 1; (0 < l) & !b[l]; l--);
				if (0 == b[l]) r(a, 1);
				else {
					for (t = 1 << (z - 1); t && !(b[l] & t); t >>= 1);
					for (;;) {
						if (!(t >>= 1)) {
							l--;
							if (0 > l) {
								F(a, G, d, v);
								break;
							}
							t = 1 << (z - 1);
						}
						F(a, a, d, v);
						t & b[l] && F(a, ha, d, v);
					}
				}
			}
			a = K(a, 1);
			return (a = m(a, this.Base));
		},
		RandomInt: function (c) {
			var b;
			b = Math.floor((c - 1) / z) + 2;
			b = g(0, 0, b);
			var d, e;
			for (d = 0; d < b.length; d++) b[d] = 0;
			e = Math.floor((c - 1) / z) + 1;
			for (d = 0; d < e; d++) b[d] = Math.floor(Math.random() * (1 << (z - 1)));
			b[e - 1] &= (2 << (c - 1) % z) - 1;
			return m(b, this.Base);
		},
	};
mdh = {
	prime: "791658605174853458830696113306796803",
	g: "5",
	gen_private: function () {
		return Cb.RandomInt(64);
	},
	gen_public: function (a) {
		return Cb.PowMod("5", a, "791658605174853458830696113306796803");
	},
	gen_shared_secret: function (a, c) {
		return Cb.PowMod(c, a, "791658605174853458830696113306796803");
	},
};
