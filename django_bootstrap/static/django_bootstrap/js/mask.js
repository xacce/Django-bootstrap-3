// jQuery Mask Plugin v0.11.4
// github.com/igorescobar/jQuery-Mask-Plugin

$(function () {
    l = $
    var m = function (g, h, k) {
        var a = this;
        g = l(g);
        a.init = function () {
            k = k || {};
            a.byPassKeys = [8, 9, 37, 38, 39, 40, 46];
            a.maskChars = {":": ":", "-": "-", ".": "\\.", "(": "\\(", ")": "\\)", "/": "/", ",": ",", _: "_", " ": "\\s", "+": "\\+"};
            a.translationNumbers = {0: "\\d", 1: "\\d", 2: "\\d", 3: "\\d", 4: "\\d", 5: "\\d", 6: "\\d", 7: "\\d", 8: "\\d", 9: "\\d"};
            a.translation = {A: "[a-zA-Z0-9]", S: "[a-zA-Z]"};
            a.translation = l.extend({}, a.translation, a.translationNumbers);
            a = l.extend(!0, {}, a, k);
            a.specialChars = l.extend({}, a.maskChars, a.translation);
            g.each(function () {
                h = c.resolveMask();
                h = c.fixRangeMask(h);
                g.attr("maxlength", h.length).attr("autocomplete", "off");
                c.destroyEvents();
                c.keyUp();
                c.paste()
            })
        };
        var c = {paste: function () {
            g.on("paste", function () {
                setTimeout(function () {
                    g.trigger("keyup")
                }, 100)
            })
        }, keyUp: function () {
            g.on("keyup", c.maskBehaviour).trigger("keyup")
        }, destroyEvents: function () {
            g.off()
        }, resolveMask: function () {
            return"function" == typeof h ? h(c.val(), k) : h
        }, val: function (b) {
            var f = "input" === g.get(0).tagName.toLowerCase();
            return 0 < arguments.length ?
                f ? g.val(b) : g.text(b) : f ? g.val() : g.text()
        }, specialChar: function (b, f) {
            return a.specialChars[b.charAt(f)]
        }, maskChar: function (b, f) {
            return a.maskChars[b.charAt(f)]
        }, maskBehaviour: function (b) {
            b = b || window.event;
            var f = b.keyCode || b.which, e = c.applyMask(h);
            if (-1 < l.inArray(f, a.byPassKeys))return c.seekCallbacks(b, e);
            e !== c.val() && c.val(e).trigger("change");
            return c.seekCallbacks(b, e)
        }, applyMask: function (b) {
            if ("" !== c.val()) {
                var f = function (b, a) {
                    for (; a < b.length;) {
                        if (void 0 !== b[a])return!0;
                        a++
                    }
                    return!1
                }, e = function (a) {
                    a =
                        "string" === typeof a ? a : a.join("");
                    a = a.match(RegExp(c.maskToRegex(b))) || [];
                    a.shift();
                    return a
                }, d = c.val();
                b = c.getMask(d, b);
                for (var d = k.reverse ? c.removeMaskChars(d) : d, a = e(d); a.join("").length < c.removeMaskChars(d).length;)a = a.join("").split(""), d = c.removeMaskChars(a.join("") + d.substring(a.length + 1)), b = c.getMask(d, b), a = e(d);
                for (d = 0; d < a.length; d++)if (e = c.specialChar(b, d), c.maskChar(b, d) && f(a, d))a[d] = b.charAt(d); else if (e)if (void 0 !== a[d]) {
                    if (null === a[d].match(RegExp(e)))break
                } else if (null === "".match(RegExp(e))) {
                    a =
                        a.slice(0, d);
                    break
                }
                return a.join("")
            }
        }, getMask: function (a) {
            if (k.reverse) {
                a = c.removeMaskChars(a);
                for (var f = 0, e = 0, d = 0, f = h.length, e = f = 1 <= f ? f : f - 1; d < a.length;) {
                    for (; c.maskChar(h, e - 1);)e--;
                    e--;
                    d++
                }
                e = 1 <= h.length ? e : e - 1;
                a = h.substring(f, e)
            } else a = h;
            return a
        }, maskToRegex: function (a) {
            for (var f, e = 0, d = ""; e < a.length; e++)(f = c.specialChar(a, e)) && (d += "(" + f + ")?");
            return d
        }, fixRangeMask: function (b) {
            return b.replace(/([A-Z0-9])\{(\d+)?,([(\d+)])\}/g, function () {
                var b = arguments, e = [], d = a.translationNumbers[b[1]] ? String.fromCharCode(parseInt("6" +
                    b[1], 16)) : b[1].toLowerCase();
                e[0] = b[1];
                e[1] = Array(b[2] - 1 + 1).join(b[1]);
                e[2] = Array(b[3] - b[2] + 1).join(d).toLowerCase();
                a.specialChars[d] = c.specialChar(b[1]) + "?";
                return e.join("")
            })
        }, removeMaskChars: function (b) {
            l.each(a.maskChars, function (c, e) {
                b = b.replace(RegExp("(" + a.maskChars[c] + ")?", "g"), "")
            });
            return b
        }, seekCallbacks: function (a, c) {
            if (k.onKeyPress && void 0 === a.isTrigger && "function" == typeof k.onKeyPress)k.onKeyPress(c, a, g, k);
            if (k.onComplete && void 0 === a.isTrigger && c.length === h.length && "function" == typeof k.onComplete)k.onComplete(c,
                a, g, k)
        }};
        "boolean" === typeof QUNIT && (a.p = c);
        a.remove = function () {
            c.destroyEvents();
            c.val(c.removeMaskChars(c.val())).removeAttr("maxlength")
        };
        a.getCleanVal = function () {
            return c.removeMaskChars(c.val())
        };
        a.init()
    };
    l.fn.mask = function (g, h) {
        return this.each(function () {
            l(this).data("mask", new m(this, g, h))
        })
    };
    l("input[data-mask]").each(function () {
        l(this).mask(l(this).attr("data-mask"))
    })
})