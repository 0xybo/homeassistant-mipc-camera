/*
 ** 参数对应注释
 ** '域名': {
 **    title: '标签页展示的title值',
 **    brand: '请求项目包的品牌名称',
 **    address: '固定的请求地址(访问dcm上的固定位置的静态资源时添加该属性)',
 **    versionType: '请求的项目类型(main: 正式版, test: 线上测试版, debug: 开发测试版)'
 ** }
 */

var host_choose = {
	"www.vimtag.com": {
		title: "Vimtag",
		brand: "vimtag",
		address: "/dcm/home/",
	},
	"www.vimtag.com/device": {
		title: "Vimtag",
		brand: "vimtag",
		versionType: "main",
	},
	"test.vimtag.com": {
		title: "Vimtag",
		brand: "vimtag",
		versionType: "test",
	},
	"debug.vimtag.com": {
		title: "Vimtag",
		brand: "vimtag",
		versionType: "debug",
	},
	"www.ebitcam.com": {
		title: "Ebitcam",
		brand: "ebitcam",
		address: "/dcm/home/",
	},
	"www.ebitcam.com/device": {
		title: "Ebitcam",
		brand: "ebitcam",
		versionType: "main",
	},
	"test.ebitcam.com": {
		title: "Ebitcam",
		brand: "ebitcam",
		versionType: "test",
	},
	"debug.ebitcam.com": {
		title: "Ebitcam",
		brand: "ebitcam",
		versionType: "debug",
	},
	"www.mipcm.com": {
		title: "MIPC",
		brand: "mipcm",
		versionType: "main",
	},
	"test.mipcm.com": {
		title: "MIPC",
		brand: "mipcm",
		versionType: "test",
	},
	"debug.mipcm.com": {
		title: "MIPC",
		brand: "mipcm",
		versionType: "debug",
	},
	"www.vsmahome.com": {
		title: "vsmahome",
		brand: "vsmahome",
		versionType: "main",
	},
	"test.vsmahome.com": {
		title: "vsmahome",
		brand: "vsmahome",
		versionType: "test",
	},
	"debug.vsmahome.com": {
		title: "vsmahome",
		brand: "vsmahome",
		versionType: "debug",
	},
	"www.mininginfotech.com": {
		title: "mininginfotech",
		address: "/dcm/mininginfotech.com/home/",
	},
	"www.myannke.com": {
		title: "ANNKE",
		// address: '/dcm/static/http_v4.5.2.1705271554/index.html?m=www.myannke.com&ta=&tp='
	},
	"www.prolabcloud.com": {
		title: "PROLAB CLOUD",
		// address: '/dcm/static/http_v4.5.2.1705271554/index.html?m=www.prolabcloud.com&ta=&tp='
	},
	"ehawk.hootoo.com": {
		title: "E-HAWK",
		// address: '/dcm/static/http_v4.5.2.1705271554/index.html?m=ehawk.hootoo.com&ta=&tp='
	},
	"cloud.serenelifehome.com": {
		title: "SereneViewer",
		address: "/dcm/http/v4.2.1.1702201430/v2n/main.v2n.htm?1v4.2.1.1702201430&amp;m=cloud.serenelifehome.com&amp;ta=&amp;tp=",
	},
	"www.eazieplus.com": {
		title: "eazieplus",
		address: "http://162.254.149.214:12180/product/v4.8.2.1709151058/main.htm?v4.8.2.1709151058&m=www.eazieplus.com&ta=&tp=&sign=ezps",
	},
	"www.fujikam.com": {
		title: "Fujikam",
		address: "/dcm/fujikam.com/home/",
	},
	"test.fujikam.com": {
		title: "Fujikam",
		address: "/dcm/fujikam.com/home/",
	},
	"v1.mipcm.com": {
		title: "MIPC",
		brand: "mipcm",
		versionType: "test",
	},
	"v2.mipcm.com": {
		title: "MIPC",
		brand: "mipcm",
		versionType: "test",
	},
	"v3.vimtag.com": {
		title: "Vimtag",
		brand: "vimtag",
		versionType: "test",
	},
	"v4.vimtag.com": {
		title: "Vimtag",
		brand: "vimtag",
		versionType: "test",
	},
	"mall.vimtag.com": {
		title: "Vimtag",
		brand: "vimtag",
		versionType: "test",
	},
	"mall.vsmahome.com": {
		title: "vsmahome",
		brand: "vsmahome",
		versionType: "test",
	},
	"product.vsmahome.com": {
		title: "vsmahome",
		brand: "vsmahome",
		versionType: "test",
	},
	"45.113.201.4": {
		title: "vimtag",
		brand: "vimtag",
		// brand: 'mipc',
		versionType: "test",
		// address: '/dcm/fujikam.com/home/'
	},
};
