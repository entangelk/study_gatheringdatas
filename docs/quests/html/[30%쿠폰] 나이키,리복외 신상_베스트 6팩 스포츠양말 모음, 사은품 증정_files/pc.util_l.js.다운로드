(function(){
	// IE버전확인 후 업그레이드 안내 노출
  var useragent = navigator.userAgent.toLowerCase();
  var isIE6 = useragent.indexOf('msie 6') != -1;
  var isIE7 = useragent.indexOf('msie 7') != -1;
  var isIE8 = useragent.indexOf('msie 8') != -1;

	if(isIE6 || isIE7 || isIE8){
		// css 동적으로 추가하기
		var link = document.createElement('link');
		link.setAttribute('rel', 'stylesheet');
		link.setAttribute('type', 'text/css');
		link.setAttribute('href', '//c.011st.com/css/event/upgrade_explorer.css');
		document.getElementsByTagName('head')[0].appendChild(link);

		document.body.innerHTML = '<div id="layBodyWrap">\
		<div id="layBody">\
			\<div class="upgrade_explorer">\
					<div class="spot spot_v2">\
							<h2 class="skip">Microsoft Edge 다운로드 받고 더 안전하고 빠르게 11번가를 사용해보세요!</h2>\
							<p class="skip">최신 버전으로 업그레이드 받고 안전하게 쓰세요.</p>\
							<div class="detail_box">\
									<a href="https://www.microsoft.com/en-us/download/internet-explorer.aspx" class="sp_upgrade lk_upgrade">\
											<span class="skip">최신 버전으로 업그레이드 하러가기</span>\
									</a>\
									<p class="txt_noti"><em class="t_noti">\
											<span class="sp_upgrade ico_noti"></span>주의 :</em>\
											<span class="t_desc">Microsoft에서 구 버전 Internet Explorer 보안 업데이트 지원을 중단함에 따라<br>악성코드 및 내 PC의 중요 정보 노출로 보안이 취약해질 수 있습니다.</span>\
									</p>\
							</div>\
					</div>\
					<div class="content">\
							<div class="other_box">\
									<h3 class="tit">“다른 브라우저 사용도 가능해요!”</h3>\
									<p class="txt_desc">11번가는 Internet Explorer 외 Chrome, Firefox 등의 브라우저에서도 안전하고 편리하게 이용하실 수 있습니다.</p>\
									<div class="lk_box">\
											<a href="https://www.google.com/intl/ko/chrome" class="sp_upgrade lk_chrome"><span class="skip">Chrome 설치하기</span></a>\
											<a href="https://www.mozilla.org/ko/firefox/new" class="sp_upgrade lk_firefox"><span class="skip">Firefox 설치하기</span></a>\
									</div>\
							</div>\
					</div>\
			</div>\
			</div>\</div>';
	}
})();

function logUsedFunction(fn){
	fetch('//www.11st.co.kr/luf.st?name='+fn+'&timestamp='+(+new Date()));
}

var HeaderComm = {};
var appVer=navigator.appVersion.substring(25,22);

function FF_changeFlashSize(movieid, w, h){
	setDivSize(movieid, w,h);
    var swfmovie = document.getElementById(movieid);
	if(swfmovie)
	{
		if(w != null)
			swfmovie.setAttribute("width", w);

		if(h != null)
			swfmovie.setAttribute("height", h);
	}
}
function FF_gotoPage(pageUrl, target){
	// 해당 pageUrl 경로로 target 이동합니다.
	if(target == "_blank"){
		window.open(pageUrl);
	}else if(target == "_top"){
		top.location.href = pageUrl;
	}else if(target){
		var newWindow = window.open(pageUrl, target);
		newWindow.focus();
	}else{
		location.href = pageUrl;
	}
}
function FF_getCookie(key){
	return getCookie(key);
}

function layerView(idName){
	Obj = $ID(idName);
	Obj.style.display="block";
}

function layerHidden(idName)	{
	Obj = $ID(idName);
	Obj.style.display="none";
}

function optionTab(){}
function tab(id,su,n){
	for(var i = 1; i <= su; i++){
		obj_Con = $ID(id+i);
		if(n == i){
			obj_Con.style.display = "block";
		}else{
			obj_Con.style.display = "none";
		}
	}
}

function funcCheckIsLogin(){
	var arg = "TMALL_AUTH=";
	var alen = arg.length;
	var clen = document.cookie.length;
	var i = 0;
	var isLogin = false;

	while(i < clen){
		var j = i + alen;
		if(document.cookie.substring(i, j) == arg)
			isLogin = true;
			i = document.cookie.indexOf(" ", i) + 1;
		if(i == 0) break;
	}

	return isLogin;
}
HeaderComm.funcCheckIsLogin = function(){
	return funcCheckIsLogin();
}

// 미성년자 여부(true이면 미성년자임)
function funcCheckIsMinor(){
	var tmallIsMinor = false;
	authkey = getCookieTmall("TMALL_STATIC");
	if(authkey == "N"){
		// authkey가 N이면 미성년자임
		tmallIsMinor = true;
	}
	return tmallIsMinor;
}

var CP_IS_AUTH;

if(!funcCheckIsLogin())
	CP_IS_AUTH =  false;
else
	CP_IS_AUTH =  true;

function doCommonTrim(str)	{
	try	{
		return str.replace(/(^ *)|( *$)/g, "");
	}	catch (ex)	{
		return str;
	}
}

function $ID(d, w){
	if(w == null)	w = window;
	return w.document.getElementById(d);
}

function $NM(m, w){
	if(w == null)	w = window;
	return w.document.getElementsByName(m);
}

var $URL = function()	{
	return {
		prd: function(n,pr)	{
			if(pr)
				return _GNB_CONTEXT_PATH_ + "/products/" + n + pr.replace(/^&/, '?');
			else
				return _GNB_CONTEXT_PATH_ + "/products/" + n;
		},
		ctgr: function(d,n,c){
			var ct = "";
			if(d == 3){
				ct = "S";
			}else if(d == 4){
				ct = "M";
			}
			return _GNB_CONTEXT_PATH_
			+ "/browsing/DisplayCategory.tmall?method=getDisplayCategory"+d+"Depth&dispCtgrNo="+n+"&dispCtgrCd="+c
			+ (ct != "" ? "&cateType=" + ct : "");
		}
	}
}();

/* Cookie */
function getCookieTmall(str){
	var binfo=document.cookie.split(";");
	var tmp="";
	for (var i=0; i<binfo.length; i++){
		// Do Not find TMCookie
		var cKey = trim(binfo[i].substring(0,binfo[i].indexOf("=")));
		if(cKey == "TP" || cKey == "TD" || cKey == "TT" || cKey == "TM"  || cKey == "TW") continue;

		if(binfo[i].indexOf(str)>=0){
			tmp=binfo[i].substring(binfo[i].indexOf("=")+1,binfo[i].length);
			break;
		}
	}
	return tmp;
}

function getCookie(name){
	return getCookieTmall(name);
}

function getCookieVal(){}

function setCookie (name, value, expires){
  document.cookie = name + "=" + escape (value) + "; path=/; domain=.11st.co.kr; expires=" + expires.toGMTString();
}


/**
 * !! cookie form is shown below
 * cookieId=cookieName[|cookieValue]#cookieName[|cookieValue] !! cookie samples
 * TD=FOO1#FOO2|BAR2#FOO3|BAR3 TP=FOO|BAR#FOO_A|BAR_A#FOO_B#FOO_C
 * TT=TOAST_MKT_OBJNO_HIST|FALSE<*>F^5702091<@>[F^5702092<@>]
 *
 * Field Description ----- 1. COOKIE_ID_ARR - Array which contains string of
 * cookie id TP : Temporary TD : A Day TT : Ten Year 2. ckIdIndex - Index of
 * COOKIE_ID_ARR 0 : TP 1 : TD 2 : TT 3. cookieName : The Name of Cookie 4.
 * cookieValue : Value for the cookie 5. !! DO NOT INCLUDE "#" or "|" IN THE
 * NAME OR THE VALUE OF COOKIE
 *
 * Modified on 2nd Apr. 2010. jhjung
 */
var TMCookieUtil = function(){
    var COOKIE_ID_ARR = ["TP", "TD", "TT", "TM", "TW"]; // !DO NOT CHANGE SORT ORDER
    var HOST_DOMAIN = ".11st.co.kr";
    var TD_PERIOD = 1; // 1Day
    var TT_PERIOD = 365 * 10; // 10Year
    var TM_PERIOD = TD_PERIOD * 30; // 1Month
    var TW_PERIOD = TD_PERIOD * 7; // 1Week
    var CK_SP = "#"; // seperator for each sub cookies
    var VL_SP = "|"; // seperator for bewteen name of cookies and there value

    // strip sharp(#) on begining of string and end of string, also trim white
	// space
    String.prototype.stripSharp = function(){
        return this.replace(/^[\#\s]+|[\#\s]+$/g, "");
    }

    // trim white space
    String.prototype.trim = function(){
        return this.replace(/^\s+|\s+$/g, "");
    }

    /* Estimate whether the param value is empty or not */
    function isEmpty(param){
        if(!isNaN(param)){
					param = param.toString();
        }
        if(param == null || param.trim() == "" || param.trim() == "undefined" || (typeof param == "undefined")){
            return true;
        }else{
            return false;
        }
    }

    /**
	 * get expire date. period -> day
	 */
    function getExpireDate(period){
        var date = new Date();
        date.setDate(date.getDate() + period);
        var nextDay = new Date(date.getFullYear(),date.getMonth(),date.getDate(), 0, 0, 0);
        return nextDay.toGMTString();
    }

    /*
	 * Create cookie with string value of sub cookie samples of newCookieStr
	 * "foo1|bar1#foo2#foo3#foo4|bar2" !! Cookie name and value string must be
	 * encode !! use encodeURIComponent()
	 */
    function createNewCookie(ckIdIndex, newCookieStr){
        var cookieStr = "";
        var expireDate = "";
        if(!isEmpty(newCookieStr)){
            cookieStr += COOKIE_ID_ARR[ckIdIndex] + "=" + encodeURIComponent(newCookieStr.stripSharp()) + ";";
            if(ckIdIndex == 1){
                expireDate = getExpireDate(TD_PERIOD);
            }else if(ckIdIndex == 2){
                expireDate = getExpireDate(TT_PERIOD);
            }else if(ckIdIndex == 3){
                expireDate = getExpireDate(TM_PERIOD);
            }else if(ckIdIndex == 4){
                expireDate = getExpireDate(TW_PERIOD);
            }
            if(!isEmpty(expireDate)){
                cookieStr += " expires=" + expireDate + ";"
            }
            cookieStr += " domain=" + HOST_DOMAIN + "; path=/;"
            document.cookie = cookieStr;
        }else{
            // remove cookie, when there is no sub cookie at all
            document.cookie = COOKIE_ID_ARR[ckIdIndex] + "= " + "; expires=" + getExpireDate(-1) + "; domain=" + HOST_DOMAIN + "; path=/";
        }
    }

    /**
	 * get matched value from arr with specified seperator
	 */
    function getMatchedStr(strArr, searchStr, seperator){
        if(strArr != null && strArr.length > 0 && !isEmpty(searchStr)){
            for(var index = 0; index < strArr.length; index++){
                var tempArr = strArr[index].trim().split(seperator);
                if(tempArr[0] == searchStr){
                    return decodeURIComponent(tempArr[1].trim());
                }
            }
        }
        return "";
    }

    return {
        add : function(ckIdIndex, cookieName, cookieValue){
            /* add cookie */
            if(isEmpty(cookieName)){ return false; }
            var newCookieArr;
            if(isEmpty(cookieValue)){
                // remove '#' from cookieName
                var regExsp = new RegExp("\\" + CK_SP, "g"); // RegExp =>
																// /\#/g
                newCookieArr = cookieName.replace(regExSp, "").trim().split(VL_SP);
            }else{
                // remove '#', '|' from cookieName and cookieValue
                var regExSp = new RegExp("\\" + CK_SP + "|" + "\\" + VL_SP, "g"); // RegExp
																					// =>
																					// /\#|\|/g
                newCookieArr = [cookieName.replace(regExSp, "").trim(), cookieValue.replace(regExSp, "").trim()];
            }
            var classCookieStr = ""; // whole cookie string (ex>
										// foo1#foo2|bar2)
            var newCookieStr = "";
            if(TMCookieUtil.isExistCookie(COOKIE_ID_ARR[ckIdIndex])){
                // remove exists cookie and add new cookie with value if
				// possible
                classCookieStr = TMCookieUtil.getCookie(COOKIE_ID_ARR[ckIdIndex]);
                var subCookieArr = classCookieStr.split(CK_SP);
                for(var index = subCookieArr.length - 1; index >= 0; index--){
                    if(subCookieArr[index].split(VL_SP)[0] == newCookieArr[0]){
                        subCookieArr.splice(index, 1);
                    }
                }
                subCookieArr.push(newCookieArr.join(VL_SP));
                newCookieStr = subCookieArr.join(CK_SP);
            }else{
                // create new cookie with cookie class
                newCookieStr = newCookieArr.join(VL_SP);
            }
            // The value of newCookieStr will be encoded in function
			// 'createNewCookie'
            createNewCookie(ckIdIndex, newCookieStr);
        },
        clear : function(ckIdIndex){
            /* clear cookie - remove TD, TP, TT */
            createNewCookie(ckIdIndex, "");
        },
        remove : function(ckIdIndex, cookieName){
            /* remove name, value pair of sub cookie */
            if(isEmpty(cookieName)){ return false; }
            var CkCdValues = "";
            var delFlag = false;
            var classCookies = TMCookieUtil.getCookie(COOKIE_ID_ARR[ckIdIndex]); // TD=foo|bar#foo2|bar2#foo3#foo4|bar4...
            var subCookies = classCookies.split(CK_SP); // ["cookieName|cookieValue",
														// "foo|bar", "foo2",
														// ...]
            if(subCookies != null && subCookies.length > 0){
                // remove matched cookie in reverse order
                for(var index = subCookies.length - 1; index >= 0; index--){
                    if(subCookies[index].split(VL_SP)[0] == cookieName){
                         subCookies.splice(index, 1);
                    }
                }
            }
            var splicedCookieStr = subCookies.join(CK_SP);
            // The value of newCookieStr will be encoded in function
			// 'createNewCookie'
            createNewCookie(ckIdIndex, splicedCookieStr);
            if(!TMCookieUtil.isExist(ckIdIndex, cookieName)){
                delFlag = true;
            }
            return delFlag;
        },
        isExistCookie : function(ckId){
            /* Estimate whether exists or not with inserted parameter */
            if(!isNaN(ckId)){
                ckId = COOKIE_ID_ARR[ckId];
            }
            var cookieArr = document.cookie.split(";");
            if(cookieArr != null && cookieArr.length > 0){
                for(var index = 0; index < cookieArr.length; index++){
                    var tempArr = cookieArr[index].trim().split("=");
                    if(tempArr[0] == ckId){
                        return true;
                    }
                }
            }
            return false;
        },
        isExist : function(ckIdIndex, cookieName){
            /* Find sub cookie name, if exist then return true */
            if(isEmpty(cookieName)){ return false; }
            var classCookieValues = TMCookieUtil.getCookie(COOKIE_ID_ARR[ckIdIndex]);
            var subCookieArr = classCookieValues.split(CK_SP);
            if(subCookieArr != null && subCookieArr.length > 0){
                for(var index = 0; index < subCookieArr.length; index++){
                    if(subCookieArr[index].split(VL_SP)[0] == cookieName){
                        return true;
                    }
                }
            }
            return false;
        },
        getCookie : function(ckId){
            /* get string of sub cookies name,value pair */
            if(!isNaN(ckId)){
                ckId = COOKIE_ID_ARR[ckId];
            }
            var cookieString = "";
            if(!isEmpty(ckId)){
                var cookieArr = document.cookie.split(";");
                cookieString = getMatchedStr(cookieArr, ckId, "=").stripSharp();
            }
            return cookieString;
        },
        getSubCookie : function(ckIdIndex, cookieName){
            /* get value of sub cookie */
            if(isEmpty(cookieName)){ return false; }
            var classCookies = TMCookieUtil.getCookie(COOKIE_ID_ARR[ckIdIndex]);
            var subCookieValue = "";
            var subCookies = classCookies.split(CK_SP);
            if(subCookies != null && subCookies.length > 0){
                for(var index = 0; index < subCookies.length; index++){
                    if(subCookies[index].split(VL_SP)[0] == cookieName){
                        var subCookie = subCookies[index].split(VL_SP);
                        if(subCookie.length > 1){
                            subCookieValue = subCookie[1];
                            return subCookieValue;
                        }
                    }
                }
            }
            return subCookieValue;
        },
        allShowCookie : function(ckIdIndex){
            /* DO NOT USE THIS METHOD, USE 'getCookie' INSTEAD */
            var cookie = TMCookieUtil.getCookie(eval(ckIdIndex));
            return cookie;
        }
    };
}();

function callAjax(url, params, callBack){
	var pageRequest = false ; // ajax object를 위한 변수.
	if(window.XMLHttpRequest){ // IE 이외
		pageRequest = new XMLHttpRequest();
	}else if(window.ActiveXObject){ // IE에서
		pageRequest = new ActiveXObject("Microsoft.XMLHTTP");
	}
	if(!pageRequest && typeof XMLHttpRequest != 'undefined')
		pageRequest = new XMLHttpRequest();

	if(pageRequest){ // pageRequest가 true인 경우만.
		try{
			var isAsynch = false;
			if(params != ''){
				pageRequest.open('POST', url, isAsynch);
				pageRequest.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
				pageRequest.setRequestHeader("Content-length", params.length);
				pageRequest.setRequestHeader("Connection", "close");
				pageRequest.send(params);
			}else{
				pageRequest.open('GET', url, isAsynch);
				pageRequest.send(null);
			}
			if(pageRequest.status==200){
		 		var returnVal = pageRequest.responseText;
				if(callBack != ''){
					eval(callBack+"('"+returnVal+"')");
				}else{
					return returnVal;
				}
	   		}else{
	   			var returnVal = 'FAIL';
			    if(callBack != ''){
						eval(callBack+"('"+returnVal+"')");
					}else{
						return returnVal;
					}
	   		}
		} catch (e){
			var returnVal = 'FAIL' ;
			if(callBack != ''){
				eval(callBack+"('"+returnVal+"')");
			}else{
				return returnVal;
			}
		}
	}
}

/* Url */
// 공통 이미지 처리
function getCommonImgUrl(imgUrl){
	try	{
		var protocol = window.document.location.protocol;
		if(protocol == 'https:'){
			if(_UPLOAD_IMG_PATH_!= '' && imgUrl.indexOf(_UPLOAD_IMG_PATH_) > -1){
				return imgUrl.replace(_UPLOAD_IMG_PATH_, _SSL_UPLOAD_IMG_PATH_);
			}else if(_IMG_PATH_ != '' && imgUrl.indexOf(_IMG_PATH_) > -1){
				return imgUrl.replace(_IMG_PATH_, _SSL_IMG_PATH_);
			}else if(_IMG_URL_ != '' && imgUrl.indexOf(_IMG_URL_) > -1){
				return imgUrl.replace(_IMG_URL_, _SSL_IMG_URL_);
			}else if(_UPLOAD_URL_ != '' && imgUrl.indexOf(_UPLOAD_URL_) > -1){
				return imgUrl.replace(_UPLOAD_URL_, 'https://image.11st.co.kr');
			}else if(_CSS_URL_ != '' && imgUrl.indexOf(_CSS_URL_) > -1){
				return imgUrl.replace(_CSS_URL_, _SSL_CSS_URL_);
			}else if(imgUrl.indexOf('http:') > -1){
				return imgUrl.replace('http:', protocol);
			}
		}	else if(protocol == 'http:'){
			if(_SSL_UPLOAD_IMG_PATH_ != '' && imgUrl.indexOf(_SSL_UPLOAD_IMG_PATH_) > -1){
				return imgUrl.replace(_SSL_UPLOAD_IMG_PATH_, _UPLOAD_IMG_PATH_);
			}else if(_SSL_IMG_PATH_ != '' && imgUrl.indexOf(_SSL_IMG_PATH_) > -1){
				return imgUrl.replace(_SSL_IMG_PATH_, _IMG_PATH_);
			}else if(_SSL_IMG_URL_ != '' && imgUrl.indexOf(_SSL_IMG_URL_) > -1){
				return imgUrl.replace(_SSL_IMG_URL_, _IMG_URL_);
			}else if(_SSL_UPLOAD_URL_ != '' && imgUrl.indexOf(_SSL_UPLOAD_URL_) > -1){
				return imgUrl.replace(_SSL_UPLOAD_URL_, _UPLOAD_URL_);
			}else if(_SSL_CSS_URL_ != '' && imgUrl.indexOf(_SSL_CSS_URL_) > -1){
				return imgUrl.replace(_SSL_CSS_URL_, _CSS_URL_);
			}else if(imgUrl.indexOf('https:') > -1){
				return imgUrl.replace('https:', protocol);
			}
		}
	} catch (e)	{}
	return imgUrl;
}
//섬네일 이미지 SSL 분리
function getThumbnailImgUrl(imgUrl)	{
	try	{
		var protocol = window.document.location.protocol;
		if(protocol == "https:")	{
			//상품이미지
			if(imgUrl.indexOf(_UPLOAD_URL_) > -1){
				return imgUrl.replace(_UPLOAD_URL_, "https://image.11st.co.kr");
			//그 외 이미지
			}else if(imgUrl.indexOf(_IMG_URL_) > -1){
				return imgUrl.replace(_IMG_URL_, _SSL_IMG_URL_);
			}

		}	else if(protocol == "http:")	{
			//상품이미지
			if(imgUrl.indexOf("https://image.11st.co.kr") > -1){
				return imgUrl.replace("https://image.11st.co.kr", _UPLOAD_URL_);
			//그 외 이미지
			}else if(imgUrl.indexOf(_SSL_IMG_URL_) > -1){
				return imgUrl.replace(_SSL_IMG_URL_, _IMG_URL_);
			}
		}
	} catch (e)	{}
	return imgUrl;
}

/* Product List */
// 클릭한 상품 노출
function dispClickedPrdBestSeller(style){
	dispClickedPrdNew(null, 26, style, 1);
}
function dispClickedPrd(style){
	dispClickedPrdNew(null, 26, style, 0);
}
function dispClickedPrdRnk(rnk, style){
	dispClickedPrdNew(null, rnk, style, 0);
}
function dispClickedPrdImage(){
	dispClickedPrdNew(true, null, null, 0);
}

/* 벨로시티 상품리스팅용 유틸 */
var vm = {
	desc: "velocity product listing utility",

	// 클릭한 상품 강조 이미지형
	clickedPrd: function(noMove){
		try	{
			var docHref = document.location.href;
			var prdNo = TMCookieUtil.getSubCookie(0, "CLICKED_PRDNO");
			if((prdNo != null) && (prdNo != "")){
				TMCookieUtil.remove(0, "CLICKED_PRDNO");

			}else{
				var index = docHref.indexOf("clickedPrdNo=");
				if(index != -1)
				{
					var temp = docHref.substring(index + 13);
					index = temp.indexOf("&");
					if(index != -1)
						prdNo = temp.substring(0, index);
					else
						prdNo = temp;
				}
			}

			var $dispObj = jQuery("#thisClick_" + prdNo);

			if($dispObj.length > 0){
				$dispObj.html("<div class=\"click_wrap\"><div class=\"click_in\"><div class=\"c_hgroup\"><h4><span>클릭한 상품</span></h4></div></div></div>");
				if(noMove == null){
					document.location.href = "#thisClick_" + prdNo;
				}
			}
		} catch(e){}
	},

	// 클릭한 상품 강조 리스트형
	clickedPrdList: function(noMove){
		try	{
			var docHref = document.location.href;
			var prdNo = TMCookieUtil.getSubCookie(0, "CLICKED_PRDNO");
			if((prdNo != null) && (prdNo != "")){
				TMCookieUtil.remove(0, "CLICKED_PRDNO");

			}else{
				var index = docHref.indexOf("clickedPrdNo=");
				if(index != -1)
				{
					var temp = docHref.substring(index + 13);
					index = temp.indexOf("&");
					if(index != -1)
						prdNo = temp.substring(0, index);
					else
						prdNo = temp;
				}
			}

			var $dispObj = jQuery("#thisClick_" + prdNo);

			if($dispObj.length > 0){

				$dispObj.addClass("click_box");

				var $dispObj2 = jQuery("#box_title_" + prdNo);

				if($dispObj2.length > 0){
					$dispObj2.addClass("click_product");
					$dispObj2.html("클릭한 상품");
					if(noMove == null){
						document.location.href = "#thisClick_" + prdNo;
					}
				}
			}
		} catch(e){}
	}
};

function dispClickedPrdNew(image, rnk, style, type){
	try {
		var prdNo = TMCookieUtil.getSubCookie(0, "CLICKED_PRDNO");
		if((prdNo != null) && (prdNo != ""))
			TMCookieUtil.remove(0, "CLICKED_PRDNO");
		else{
			if(document.location.href.indexOf("click=Y") == -1)
				return;

			var index = document.location.href.indexOf("prdNo=");
			if(index != -1){
				var temp = document.location.href.substring(index + 6);
				index = temp.indexOf("&");
				if(index != -1)
					prdNo = temp.substring(0, index);
				else
					prdNo = temp;
			}
		}

		if(setClickedPrdData(prdNo, image))
			return;
		if(image == true)
			return;

		if(rnk == undefined)
			rnk = 26;

		// 클릭한 상품이 없으면 상품정보 가져와서 innerHtml로 넣어준다.
		var param = "&prdNo=" + prdNo + "&index=" + rnk + "&style=" + style + "&type=" + type;

		var str = callAjax("/browsing/MainAjax.tmall?method=getMainClickPrd150ImgHTML", param, "");

		// 클릭한 상품이 없으면 상품정보 가져와서 innerHtml로 넣어준다.
		var clickedPrd = $ID("rank_" + rnk);

		if((clickedPrd != undefined) && (clickedPrd != null))
		{
			var clickPrdElement = clickedPrd.parentNode;
			if((str != "FALE") && (str != "FAIL") && (str != ""))
			{
				clickPrdElement.innerHTML = str.replace("<li>", "").replace("</li>", "");
				setClickedPrdData(prdNo, image);
			}
		}
	}
	catch(e){}
}

HeaderComm.setClickedPrd = {
	prdNo : ''
};

HeaderComm.ClickedPrd = {
	prdNo : '',
	$wrapObj : '',
	existPrd : false, //상품존재여부
	options : {
		wrapPrefix : 'thisClick_',
		wrapClassNm : 'click_wrap',
		borderHtml : '<div class="click_in"><div class="c_hgroup"><h4><span>클릭한 상품<\/span><\/h4><\/div><\/div>',
		moveMotion : true,
		callBackFnc : ''
	},
	setParameters : function(options){
		for(var key in options){
			this.options[key] = options[key];
		}

		this.prdNo = HeaderComm.getParameter('clickedPrdNo');
		if(this.prdNo == undefined){
			this.prdNo = HeaderComm.getParameter('prdNo');
		}
		this.$wrapObj = jQuery("#" + this.options.wrapPrefix + this.prdNo);
		if(this.$wrapObj.size() > 0){
			this.existPrd = true;
		}
	},
	init : function(options){
		var _this = this;
		_this.setParameters(options);

		if(_this.existPrd){
			_this.setStyle();
			_this.moveVertical();
		}

		if(typeof(_this.options.callBackFnc) === 'function'){
			_this.options.callBackFnc(_this.existPrd);
		}
	}
};

HeaderComm.getParameter = function(key){
	try {
		var _param = document.location.search;
		if(typeof _param !== 'undefined' && _param !== ''){
			_param = _param.substr(1);

			var _chkKey = key+'=';
			var _arrParam =  _param.split('&');

			for (var idx = 0; idx < _arrParam.length; idx++){
				if(_arrParam[idx].indexOf(_chkKey) === 0){
					return _arrParam[idx].replace(_chkKey, '');
				}
			}
		}else{
			return '';
		}
	} catch (ex){
		return '';
	}
};

// goCommonUrl
function goCommonUrl(url, target)	{
	try {
		if(target == null || target == "")	{
			target = top;
		}
		if(url != null && url != "")	{
			if(target == '_blank') window.open(url,target);
			else target.location.href = url;
		}
	} catch (ex){
		window.top.location.href = url;
	}
}

// stat
function doCommonStat(code){
	try	{
		if(code != null && code != "")	{
			var	i =	new	Image();
			var protocol = window.document.location.protocol;
			var statDomain = _GNB_CONTEXT_PATH_;

			if(protocol == "http:"){
				statDomain = statDomain.replace("https:", protocol);
			}
			i.src =	statDomain + "/a.st?url=" + code;
			s_objectID = code;
		}
	} catch (ex){}
}

function doCommonStatCtgrNo(code, ctgrNo)	{
	try	{
		if(code != null && code != "")	{
			var	i =	new	Image();
			var protocol = window.document.location.protocol;
			var statDomain = _GNB_CONTEXT_PATH_;

			if(protocol == "http:")	{
				statDomain =  statDomain.replace("https:", protocol);
			}

			i.src =	statDomain + "/a.st?url=" + code + "&ctgrNo=" + ctgrNo;
			s_objectID = code;

		}
	} catch (ex)	{}
}

var StringBuffer = function(){
    this.buffer = new Array();
};
StringBuffer.prototype.append = function(str){
    this.buffer[this.buffer.length] = str;
};
StringBuffer.prototype.toString = function(){
    return this.buffer.join("");
};
function goCommonPrdDtl(prdNo,target){
	goCommonUrl(_PRODUCT_DETAIL_URL_ + prdNo, target);
}
function goStatUrl(url, code, target)	{
	goCommonUrl(url, target);
}
var targetPopup;
function goStatPopUp(url, code, popupNm){
	if(targetPopup == null || targetPopup == undefined){
		targetPopup = window.open(url, popupNm);
	}else{
		targetPopup = window.open(url, popupNm);
		targetPopup.focus();
	}
}

// ms.song, 2011.09.29
// 클릭통계 (spceNo를 가지고 클릭통계를 잡는다.)
var stat = {
	desc : {
		 DC: "전시카테고리 구좌 통계",
		 AC: "추가전시카테고리 구좌 통계",
		 BC: "브랜드전문관 카테고리 구좌 통계(추후 추가 요청 예정)",
		 EP: "페이지/코너(메인, 서비스/이벤트 페이지 등 나머지 페이지용)",
		 DT: "DT 전문관(dt_disp_ctgr 테이블을 사용하는 페이지)"
	},

	track : function(spceNo, type, ctgrNo){
		var strCtgrParam =  ctgrNo ? "&CNO=" + ctgrNo : "";
		doCommonStat(spceNo + "&TP=" + type + strCtgrParam);
	},

	Impression : function(param){
		try {
			param = param.replace(/&amp;/gi,"&");
			var url = "https://st.11st.co.kr/a.st?type=I"+param;
			var img = new Image();
			img.src = url;
		} catch (e){}
	}
};

/* 광고 Tracking Code */
var isValidTrcStrLength = function(str){
	// 길이 체크
	var result = true;
	if(str.length < 6){
		result = false;
	}
	return result;
}
var isValidTrcStrChar = function(str){
	var result = true;
	var tempVal;
	for(var i=0; i < str.length; i++){
		tempVal = str.charCodeAt(i);

		if(tempVal < 48 || 122 < tempVal){
			result = false;
			break;
		}

		if(57 < tempVal && tempVal < 65){
			result = false;
			break;
		}

		if(90 < tempVal && tempVal < 97){
			result = false;
			break;
		}
	}
	return result;
}
var isValidTrcStrTrcCode = function(str){
	var result = true;
	if(str.substr(5, 2) == "-1" || str.substr(5, 1) == "0"){
		result = false;
	}

	return result;
}
var isValidTrcCode = function(code){
	var result = true;
	if(code.length < 1 || code.substr(0, 2) == "-1" || code.substr(0, 1) == "0"){
		result = false;
	}

	if(!isValidTrcStrChar(code)){
		result = false;
	}

	try{
		if(isNaN(code)){
			result = false;
		}
	} catch(exp){
		result = false;
	}
	return result;
}
/**
 * 광고서버 스위치
 */
var _dsSeverMode = true;

// 공통 이동 함수
// 상품상세
function goPrd(prdNo, target,pr){
	var url = $URL.prd(prdNo,pr);
	goCommonUrl(url, target);
}
function newPrd(prdNo,pr){
	goPrd(prdNo,'_blank',pr);
}
// Cache 방지를 위해 원 문자열 끝에 TimeStamp를 붙여서 반환한다.
function appendTimeStamp(source){
	var delimiter = "&";
	if(typeof(source) === "undefined" || source === ""){
		delimiter = "?", source = "";
	}

	return source + delimiter + "noCache=" + (new Date()).getTime();
}

// gnb.js
/* 1. 함수 */
function deleteCookie(cookieName){
	var expireDate = new Date();
	var domain = "www.11st.co.kr";
	if(cookieName != null && cookieName == "TMALL_MY_IMGSTOP"){
		domain = "11st.co.kr";
	}
	expireDate.setDate(expireDate.getDate()-1);
	document.cookie = cookieName + "= " + "; path=/; domain="+domain+";  expires=" + expireDate.toGMTString() + ";";
}
/* 2. 회원/로그인 관련 링크/액션 */
function goMemberInfoPages(){
	var loc = top.location ;
	loc.href = "https://www.11st.co.kr/register/memInfoEditForm.tmall?method=getMemberInfo&protocol=https" ;
}
function goMemberWithdrawPages(){
	var loc = top.location ;
	loc.href = "https://www.11st.co.kr/register/withdrawLimitCondChk.tmall?method=withdrawLimitCondChk&CHOICEMENU=F03&isSSL=Y&protocol=https" ;
}
function goFrontMemberInfoPage(code){
	goStatUrl("https://www.11st.co.kr/register/memInfoEditForm.tmall?method=getMemberInfo&protocol=https",code);
}
// 로그인
function login(code, url)	{
	var retUrl = encodeURIComponent(document.location.href);
	var xFrom = "";
	if(retUrl == _GNB_CONTEXT_PATH_ + "/html/main.html"){
		xFrom = "main^gnb";
	}
	if(url != undefined && url != null && url != ""){
		retUrl = encodeURIComponent(url);
	}
	goStatUrl(_LOGIN_TARGET_URL_+"/login/Login.tmall?returnURL=" + retUrl + "&xfrom=" + xFrom, code);
}
// 로그아웃
function logout(code, url){
	var retUrl 	= encodeURIComponent(document.location.href);
	var xFrom 	= "";
	if(retUrl == _GNB_CONTEXT_PATH_ + "/html/main.html"){
		xFrom = "main^gnb";
	}
	if(url != undefined && url != null && url != ""){
		retUrl = encodeURIComponent(url);
	}
	try{SCP_INIT.stop();}catch(e){};
	goStatUrl(_GNB_CONTEXT_PATH_+"/login/Logout.tmall?xfrom=" + xFrom + "&returnURL=" + retUrl, code);
}
function item(){}
function f_search(){
	var gnbFormObj = document.forms["GNBSearchForm"];
     var keyword = gnbFormObj.naturalKwd.value;

     if(keyword == ""){
           alert("검색어를 입력하세요.");
     }else{
  	   goStatUrl("https://search.11st.co.kr/SearchEmotionAction.tmall?method=getSearchEmotion&targetTab=P&isGnb=Y&kwd=" + keyword);
     }
}

function directLogin(){
    var url = 'https://www.11st.co.kr/toc/bridge.tmall?method=chatPage';
        window.open(url, 'open11Talk', 'width=482, height=800, toolbar=no, location=no, status=no, menubar=no, scrollbars=no, status=no, resizable=yes');
}

/* 3. UI 설정 */
function setGnbLogInArea(){}
function headSel(no,optionV){
	obj_sel=$ID("headSel_" + no);
	obj_opt=$ID("headSelO_" + no)
	obj_sel.value=optionV;
	obj_opt.style.display="none";
}
/* 5. GNB 카테고리 */
function getGnbCtgr(level, ctgrNo, ctgrNm, ctgrCd, selClass, renew, ctgrUrl){
	level = parseInt(level);

	var url = "";
	var flag = true;
	var ctgrHtml = "";

	var ocb	= [
		"", 
		"/browsing/CashbagStreet.tmall?method=showCashbagStreetMain", 
		"/browsing/CashbagStreet.tmall?method=showCashbagStreetSub&dispCtgrNo=", 
		"/browsing/CashbagStreet.tmall?method=getBrandPage&dispCtgrNo=", 
		"/browsing/CashbagStreet.tmall?method=getBrandPage&dispCtgrNo="
	];

	if(ctgrCd.indexOf("371") > -1){
		url = ocb[level];
	}	else{
		url = $URL.ctgr(level, ctgrNo, ctgrCd);
		flag = false;
	}

	if(flag && level > 1){
		if(level == 2){
			url += ctgrNo + "&dispCtgrCd=" + ctgrCd;
		}	else if(level == 3){
			url += ctgrNo + "&dispCtgrCd=" + ctgrCd + "&cateType=S";
		}	else{
			url += ctgrNo + "&dispCtgrCd=" + ctgrCd + "&cateType=M";
		}
	}

	if(ctgrUrl && ctgrUrl != "null"){
		url = ctgrUrl;
	}
	
	if(renew){
		ctgrHtml = "<a href=\"" + url + "\" data-log-actionid-label=\"category\" data-log-body=\"{'btn_name':'" + ctgrNm + "','content_no':'" + ctgrNo + "','category_no':'" + ctgrNo + "','content_type':'CATEGORY'}\" onClick=\"rakeLog.sendRakeLog(this);headSel('" + level + "','" + ctgrNm + "');ga('send', 'event', '중소세카테고리', '중/소/세분류 리스팅', '카테고리 네비게이션');\" >";
		if(selClass=="on"){
			ctgrHtml += "<em>"+ctgrNm+"</em>";
		}else{
			ctgrHtml += ctgrNm;
		}
		ctgrHtml += "</a>";
	}else{
		ctgrHtml ="<a href=\"" + url + "\" onClick=\"headSel('" + level + "','" + ctgrNm + "');ga('send', 'event', '중소세카테고리', '중/소/세분류 리스팅', '카테고리 네비게이션');\" class=\"" + selClass + "\">" + ctgrNm + "</a>";
	}

	return ctgrHtml;
}
function getGnbCtgrG(level, ctgrNo, ctgrNm, ctgrCd, selClass)	{
	level = parseInt(level);

	var url = "";
	var flag = true;

	var ocb	= [
		"", 
		"/browsing/CashbagStreet.tmall?method=showCashbagStreetMain", 
		"/browsing/CashbagStreet.tmall?method=showCashbagStreetSub&dispCtgrNo=", 
		"/browsing/CashbagStreet.tmall?method=getBrandPage&dispCtgrNo=", 
		"/browsing/CashbagStreet.tmall?method=getBrandPage&dispCtgrNo="
	 ];

		if(ctgrCd.indexOf("192") == 0 && ctgrCd.length > 3){
			url = $URL.ctgr(2, ctgrNo, ctgrCd);
		}	else if(ctgrCd.indexOf("371") > -1)	{
			url = ocb[level];
		}	else{
			url = $URL.ctgr(level, ctgrNo, ctgrCd);
			flag = false;
		}

	if(flag && level > 1)	{
		if(level == 2){
			url += ctgrNo + "&dispCtgrCd=" + ctgrCd;
		}	else if(level == 3){
			url += ctgrNo + "&dispCtgrCd=" + ctgrCd + "&cateType=S";
		}else{
			url += ctgrNo + "&dispCtgrCd=" + ctgrCd + "&cateType=M";
		}
	}
	return "<div class='InCateTxt'><a href=\"" + url + "\" class=\"" + selClass + "\">" + ctgrNm + "</a></div>";
}

function getGnbCtgrUrl(level, ctgrNo, ctgrCd)	{
	level = parseInt(level);

	var url = "";
	var flag = true;

	var ocb = [
		"", 
		"/browsing/CashbagStreet.tmall?method=showCashbagStreetMain", 
		"/browsing/CashbagStreet.tmall?method=showCashbagStreetSub&dispCtgrNo=", 
		"/browsing/CashbagStreet.tmall?method=getBrandPage&dispCtgrNo=", 
		"/browsing/CashbagStreet.tmall?method=getBrandPage&dispCtgrNo="
	];

	if(ctgrCd.indexOf("192") == 0 && ctgrCd.length > 3){
		url = $URL.ctgr(2, ctgrNo, ctgrCd);
	}	else if(ctgrCd.indexOf("371") > -1){
		url = ocb[level];
	}	else{
		url = $URL.ctgr(level, ctgrNo, ctgrCd);
		flag = false;
	}

	if(flag && level > 1){
		if(level == 2){
			url += ctgrNo + "&dispCtgrCd=" + ctgrCd;
		}else if(level == 3){
			url += ctgrNo + "&dispCtgrCd=" + ctgrCd + "&cateType=S";
		}else{
			url += ctgrNo + "&dispCtgrCd=" + ctgrCd + "&cateType=M";
		}
	}

	return url;
}

/* 7. inc_footer_data.js 에서 이동 */
/* header 선언 부분 */
if(typeof(isLeftBnnr) == "undefined") var isLeftBnnr = false;
if(typeof(isWingBnnr) == "undefined") var isWingBnnr = false;
if(typeof(isToastBnnr) == "undefined") var isToastBnnr = false;
if(typeof(isToastBnnrAct) == "undefined") var isToastBnnrAct = false;
if(typeof(isPopUnder) == "undefined") var isPopUnder = false;
/* header 선언 부분 */
var toastBnnrState = 0;
var totCnt = 7; // 2011.12.12 토스트배너 : total count(토스트배너 최대 노출 횟수를 지정해줍니다. 5개에서 7개로 변경) - 김태현
var _browser = navigator.userAgent.toLowerCase();
var isIE = false;
var isIE6 = false;
var isIE7 = false;
var isIE8 = false;
var isIE9 = false;
var isIE10 = false;
var isFireFox = false;
var isOpera = false;
var isSafari = false;
var isChrome = 0;

var IS_OVER_1024 = false;
var WBMINUS=0;

var WBTopPosition=180;	// Default Top Position
var WBTopPosition2=0;
var WBHeight=0;
var WBWidth=0;
var SwfWidth=270;

if(screen.width > 1024){
	IS_OVER_1024 = true;
	WBMINUS = 0;
}

if(_browser.indexOf('msie') != -1)	{
	isIE = true;
	if(_browser.indexOf('msie 9') != -1)
		isIE9 = true;
	else if(_browser.indexOf('msie 8') != -1)
		isIE8 = true;
	else if(_browser.indexOf('msie 7') != -1)
		isIE7 = true;
	else if(_browser.indexOf('msie 10') != -1)
		isIE10 = true;
	else if(_browser.indexOf('msie 6') != -1)
		isIE6 = true;
}	else	{
	if(_browser.indexOf('firefox') != -1)
		isFireFox = true;
	else if(_browser.indexOf('opera') != -1)
		isOpera = true;
	else if(_browser.indexOf('chrome') != -1)
		isChrome = 1;	
	else if(_browser.indexOf('safari') != -1)
		isSafari = true;
}

// 비회원 로그인여부
function funcIsNonAuth(){
	var arg = "TMALL_NON_AUTH=";
	var alen = arg.length;
	var clen = document.cookie.length;
	var i = 0;

	while(i < clen){
		var j = i + alen;
		if(document.cookie.substring(i, j) == arg){
			return true;
		}
		i = document.cookie.indexOf(" ", i) + 1;
		if(i == 0) break;
	}
	return false;
}

function openLogin(type, formName, targetUrl, width, height, scroll, refresh, noNonMem){
	// targetUrl =
	// '/community/AuthShoppingInfoAction.tmall?method=getContentsReporting&contNo=11303&contDclObjClfC=D01&memNM=한글'

	var url = "";
	try {
		url = _LOGIN_TARGET_URL_;
	} catch (ex)	{
		url = "https://www.11st.co.kr";
	}
	url += '/login/PopupLogin.tmall?type='+type+'&formName='+formName+'&width='+width+'&height='+height+'&scroll='+scroll+'&refresh='+refresh+'&targetUrl='+encodeURIComponent (encodeURIComponent(targetUrl))+'&domain='+document.domain+'&noNonMem='+noNonMem;
	// 비회원 로그인 상태일 경우에는 parameter 를 추가한다
	if(funcIsNonAuth()){
		url += '&authMethod=nonAuth';
	}

	var protocol = window.document.location.protocol;

  // Header JS Include
  if(protocol == "https:"){
  	url += '&protocol=https';
  }

	/*
	 * if(type == '4') str =
	 * 'width=400,height=550,resizable=no,scrollbars=no,left=100,top=20'; else
	 * str = 'width=400,height=350,resizable=no,scrollbars=no,left=100,top=20';
	 * return window.open(url, 'login', str);
	 */
	cw=screen.availWidth; // 화면 너비
	ch=screen.availHeight; // 화면 높이
	if(type == '4'){
		sw=750;// 띄울 창의 너비
		sh=515;// 띄울 창의 높이
	}else if(type == '6'){
		sw=750;// 띄울 창의 너비
		sh=515;// 띄울 창의 높이
	}else{
		sw=750;// 띄울 창의 너비
		sh=515;// 띄울 창의 높이
	}

	ml=(cw-sw)/2;// 가운데 띄우기위한 창의 x위치
	mt=(ch-sh)/2;// 가운데 띄우기위한 창의 y위치

	return window.open(url, 'login', 'width='+sw+',height='+sh+',top='+mt+',left='+ml+',scrollbars=yes,status=no');
}

function openLoginAdults(type, formName, targetUrl, width, height, scroll, refresh, noNonMem){
	var url = "";
	try {
		url = _LOGIN_TARGET_URL_;
	} catch (ex)	{
		url = "https://login.11st.co.kr";
	}
	url += '/login/PopupLogin.tmall?age19=Y&type='+type+'&formName='+formName+'&width='+width+'&height='+height+'&scroll='+scroll+'&refresh='+refresh+'&targetUrl='+encodeURIComponent (encodeURIComponent(targetUrl))+'&domain='+document.domain+'&noNonMem='+noNonMem;
	// 비회원 로그인 상태일 경우에는 parameter 를 추가한다
	if(funcIsNonAuth()){
		url += '&authMethod=nonAuth';
	}

	cw=screen.availWidth; // 화면 너비
	ch=screen.availHeight; // 화면 높이
	if(type == '4'){
		sw=750;// 띄울 창의 너비
		sh=515;// 띄울 창의 높이
	}else if(type == '6'){
		sw=750;// 띄울 창의 너비
		sh=515;// 띄울 창의 높이
	}else{
		sw=750;// 띄울 창의 너비
		sh=515;// 띄울 창의 높이
	}

	ml=(cw-sw)/2;// 가운데 띄우기위한 창의 x위치
	mt=(ch-sh)/2;// 가운데 띄우기위한 창의 y위치

	return window.open(url, 'login', 'width='+sw+',height='+sh+',top='+mt+',left='+ml+',scrollbars=yes,status=no');
}

function checkNum(obj, value){
  var regExp = /[^0-9]+/g;

  if(regExp.test(value)){
		alert("'숫자' 만 입력 가능합니다.");
		var returnStr = "";

		for(var i = 0; i < value.length; i++){
			if(value.charAt(i) >= '0' && value.charAt(i) <= '9'){
				returnStr += value.charAt(i);
			}
		}

		obj.value = returnStr;
		obj.focus();
  }
}

// partnerHeaderInfo.js
function getPartnerCookieVal(offset){
	var endstr = document.cookie.indexOf(";", offset);
	if(endstr == -1) endstr = document.cookie.length;
	return unescape(document.cookie.substring(offset, endstr));
}

// 제휴사 코드 획득
function getPartnerCookie(){
	var arg = "PARTNER_CD=";
	var alen = arg.length;
	var clen = document.cookie.length;
	var i = 0;

	while(i < clen){
		var j = i + alen;
		if(document.cookie.substring(i, j) == arg)
			return getPartnerCookieVal(j);
			i = document.cookie.indexOf(" ", i) + 1;
		if(i == 0) break;
	}
	return null;
}


// 제휴사 코드 획득
function getXsiteDetailCookie(){
	var arg = "XSITE_DETAIL=";
	var alen = arg.length;
	var clen = document.cookie.length;
	var i = 0;

	while(i < clen){
		var j = i + alen;
		if(document.cookie.substring(i, j) == arg)
			return getPartnerCookieVal(j);
			i = document.cookie.indexOf(" ", i) + 1;
		if(i == 0) break;
	}
	return null;
}

var partnerHeaderInfo = '';
var partnerHeaderHeight = 0;

var nPartnerCookieValue = getPartnerCookie();
var benepiaDomain;

var encode = "euckr";
if(document.URL.indexOf("buy.11st.co.kr/cart") > -1 || document.URL.indexOf("buy.11st.co.kr/pay") > -1 || document.URL.indexOf("login.11st.co.kr/auth") > -1){
	encode = "utf";
}

var protocol = window.location.protocol + '//';

try {
	if(nPartnerCookieValue != '' && window._VIEW_PARTNER_HEADER != false){
		if(nPartnerCookieValue == '1023' || nPartnerCookieValue == '1038' || nPartnerCookieValue == '1153'
				|| nPartnerCookieValue == '1154' || nPartnerCookieValue == '1155'){ // OCB(SK에너지) Header 처리
            var today = new Date();
		  partnerHeaderInfo = '<script language="javascript" src="//cashbagmall.okcashbag.com/mall/cTop411st.js?noCache=' + today.getFullYear() + (today.getMonth()+1) + today.getDate() + today.getHours() + '" charset="EUC-KR"></script>';
		  partnerHeaderHeight = 67;
		}else if(nPartnerCookieValue == '1073' || nPartnerCookieValue == '1151' || nPartnerCookieValue == '1152'){ // 현대카드
		  partnerHeaderInfo = '<script type="text/javascript" src="//www.hyundaicard.com/js/common/outlink_header_hc.js"></script> ';
		  partnerHeaderHeight = 75;
		}else if(nPartnerCookieValue == '1205' || nPartnerCookieValue == '1222'){ // 아시아나
			// 무조건 utf-8로 부르도록 한다.
			partnerHeaderInfo = '<script type="text/javascript" src="'+protocol+'flyasiana.com/C/pc/js/partnerHeader/partnerHeader_utf.js?mn=11ST&code=SKM&logoYn=Y" charset="UTF-8"></script>';
			partnerHeaderHeight = 50;
		}else if(nPartnerCookieValue == '1214' || nPartnerCookieValue == '1252'){ // 신한카드
			partnerHeaderInfo = '<script src="//allthatcdn.aws.shinhancard.com/conts/partners/header/allthat.js"></script>'
			+ '<div id = "allthat"></div>';
			partnerHeaderHeight = 97;
		}else if(nPartnerCookieValue == '1226' && encode == "euckr"){ // 삼성카드
			partnerHeaderInfo = '<script type="text/javascript" src="//static12.samsungcard.com/js/mallinmall/cml/partner/fo/cooper_e_11st.js" charset="EUC-KR"></script>';
			partnerHeaderHeight = 81;
		}else if(nPartnerCookieValue == '1261'){ // 동양종합금융증권
			partnerHeaderInfo = '<script type="text/javascript" src="//www.myasset.com/js/11st/tongyang_header.js" charset="EUC-KR"></script>';
			partnerHeaderHeight = 81;
		}else if(nPartnerCookieValue == '1342'){ // 하나SK카드
			partnerHeaderInfo = '<script type="text/javascript" src="//www.hanacard.co.kr/js/shopping_wa.js" charset="EUC-KR"></script>';
			partnerHeaderHeight = 68;
		}else if(nPartnerCookieValue == '1008'){ // 베스트바이어
			partnerHeaderInfo = '<script type="text/javascript" src="//www.bb.co.kr/js/bb/bb.front.simpleheader.js"></script>';
			partnerHeaderHeight = 65;
		}else if(nPartnerCookieValue == '1371' || nPartnerCookieValue == '1383' || nPartnerCookieValue == '1384'){ // 한국교총
			partnerHeaderInfo = '<iframe id="tmall_partner_k" src="//www.kftaplus.com/common/top0.asp" frameborder="0" scrolling="no" style="width:100%;height:40px;margin:0 0;padding:0 0;"></iframe>';
			partnerHeaderHeight = 40;
		}else if(nPartnerCookieValue == '1404' || nPartnerCookieValue == '1405' || nPartnerCookieValue == '1472'
			 || nPartnerCookieValue == '1527' || nPartnerCookieValue == '1528' || nPartnerCookieValue == '1614' || nPartnerCookieValue == '1615'){ // 베네피아
			// Benepia 파트너 헤더 내부에서 부르는 자원이 http 일 경우 https 로 오버라이드 하기 위함이므로 https 로 정규식을 변경하면 안됨
            var regExp = new RegExp("https?:[/]{2}[0-9a-zA-Z.;\-]*", "");
            var benepiaDomain = TMCookieUtil.getSubCookie(0, "PARTNER_REFERER");

            benepiaDomain = benepiaDomain.replace(/%3A/gi, ":").replace(/%2F/gi, "/").replace(/%3F/gi, "?").replace(/%3D/gi, "=").replace(/%26/gi, "&");
			benepiaDomain = (benepiaDomain).match(regExp);
			if(benepiaDomain && benepiaDomain[0]) {
				benepiaDomain = benepiaDomain[0].replace('http://', '//');
			}
			// End: Benepia 파트너 헤더 프로토콜 오버라이드
            partnerHeaderInfo = '<script type="text/javascript" src="//test01.benepia.co.kr/bene11st.jsp?benepiaDomain='+benepiaDomain+'"></script>';
            partnerHeaderHeight = 56;
		}else if(nPartnerCookieValue == '1442'){ // KB국민카드
			partnerHeaderInfo = '<iframe src="//lifes.kbcard.com/CXLRICOC0006.cms" width="100%" height="90" scrolling="no" marginwidth="0" marginheight="0" overflow:auto;overflow-x:no;=""></iframe>';
			partnerHeaderHeight = 90;
		}else if(nPartnerCookieValue == '1707' && encode == "euckr"){	//하나로드림
        	partnerHeaderInfo = '<script type="text/javascript" src="//shop.dreamx.com/html/cpGNB/redir_ssl.js" charset="EUC-KR"></script>';
			partnerHeaderHeight = 64;
		}
	}
} catch (e){}

if(partnerHeaderInfo != '') {
	window.addEventListener('DOMContentLoaded', function() {
		var iframeElem = document.createElement('iframe');
		iframeElem.setAttribute('width', '100%'); 
		iframeElem.setAttribute('height', partnerHeaderHeight);
		iframeElem.setAttribute('frameborder', 0);
		iframeElem.setAttribute('scrolling', 'no');
		document.body.insertBefore(iframeElem, document.body.firstChild)
		var iframeDoc = iframeElem.contentDocument;
		var iframeWindow = iframeElem.contentWindow;
		iframeDoc.open();
		iframeDoc.write('<body style="margin:0">');
		if(nPartnerCookieValue === '1342') {
			iframeDoc.write('<script src="//c.011st.com/js/lib/jquery/jquery-3.1.1.min.js"></script>');
		}
		iframeDoc.write(partnerHeaderInfo);
		iframeDoc.write('</body>');
		iframeDoc.close();
	
		iframeElem.onload = function() {
			iframeElem.setAttribute('height', iframeDoc.body.scrollHeight);
			var a, aTags = iframeDoc.querySelectorAll('a');
	
			for(var i = 0, l = aTags.length; i < l; i++) {
				a = aTags[i];
				if(!/^javascript:/.test(a.href)){
					a.setAttribute('target', '_blank');
				}
			}
		}
	})
}

/* searchCommon.js */
 /*
 * 검색 GNB javascript
 * /js/common/type_check.js 필요!! 
 */
/* GNB 콤보박스별 대상 action, method 설정 */
function setSearchTarget(code, gubun){
	var gnbFormObj = document.forms["GNBSearchForm"];
	if(gubun == "f"){
		gnbFormObj = document.forms["FooterSearchForm"];
	}
	var actionStr = "https://search.11st.co.kr/SearchPrdAction.tmall";
	var method = "getTotalSearchSeller";

	if(gnbFormObj.semanticFromGNB){
		gnbFormObj.semanticFromGNB.value = "";
	}

	//통계코드 영역 접두코드
	var areaCodePre = HeaderGnb.makeGnb.areaCodePre;
	// Start 2010.11.24 검색 조건 별 선택 횟수 집계
	if(gnbFormObj.gnbTag){
		if(code == "MO"){	 // 도서11번가
			gnbFormObj.gnbTag.value = "MO";
		}else if(code == "SC"){	 // 입체검색
			gnbFormObj.gnbTag.value = "SC";
		}else if(code == "SL"){	 // 판매자 검색
			gnbFormObj.gnbTag.value = "SL";
		}else if(code == "TOUR11ST"){// 여행 11번가
			gnbFormObj.gnbTag.value = "TR";
		}else if(code == "SEMANTIC"){// 시맨틱 검색
			gnbFormObj.gnbTag.value = "SE";
		}else if(code == "TICKET"){// 티켓 검색
			gnbFormObj.gnbTag.value = "TK";
		}else if(code == "MODEL"){// 가격비교
			gnbFormObj.gnbTag.value = "MD";
		}else if(code == "CONTENTS"){//쇼핑리뷰
			gnbFormObj.gnbTag.value = "CT";
		}else{ // 통합검색 (T)
			gnbFormObj.gnbTag.value = "TO";
		}
	}

	if(code == "M"){	// 대표상품
		actionStr = "https://search.11st.co.kr/SearchPrdAction.tmall";
		gnbFormObj.prdType.value = "M";
		method = "getMasterPrd";
	}else if(code == "S"){	// 가게
		actionStr = "https://search.11st.co.kr/SearchSellerShopAction.tmall";
		method = "getSearchSellerShop";
		gnbFormObj.pageSize.value = "5";
	}else if(code == "D"){
		actionStr = "https://search.11st.co.kr/SearchInvoiceNoAction.tmall";	// 운송장번호검색
		// action
		// 연동
		method = "";
	}else if(code == "CH"){ // 뷰티 11번가
		actionStr = "https://beauty.11st.co.kr/TotalSearch.do";
		method = "";
		gnbFormObj.category.value = "cherrya";
		gnbFormObj.cmd.value = "productList";
	}else if(code == "MO"){ // 도서 11번가
		actionStr = "https://book.11st.co.kr/TotalSearch.do";
		method = "";
		gnbFormObj.category.value = "morning365";
		gnbFormObj.cmd.value = "productList";
	}else if(code == "SC"){ // 즐겨운 쇼핑
		actionStr = "https://www.11st.co.kr/browsing/specialcorner/enjoyShopping.tmall";
		method = "tSearch";
	}else if(code == "TOUR11ST"){// 여행 11번가
		actionStr = "https://tour.11st.co.kr/tour/TourSearchAction.tmall";
		method = "search";
	}else if(code == "TOUR"){// 여행
		actionStr = "https://tour.11st.co.kr/tour/TourSearchAction.tmall";
		method = "search";
	}else if(code == "OVERSEAS"){// 해외호텔
		actionStr = "https://tour.11st.co.kr/tour/TourSearchAction.tmall";
		method = "search";
	}else if(code == "DOMESTIC"){// 국내숙박
		actionStr = "https://tour.11st.co.kr/tour/TourSearchAction.tmall";
		method = "search";
	}else if(code == "SEMANTIC"){// 시맨틱검색
		actionStr = "https://search.11st.co.kr/SemanticSearchAction.tmall";
		method = "getSemanticSearch";
		gnbFormObj.semanticFromGNB.value="Y";
	}else if(code == "MT11"){	// 마트 11번가
		actionStr = "https://www.11st.co.kr/mart11st/Mart11stSearchAction.tmall";
		method = "goMart11stSearch";
	}else if(code == "BRAND"){// 브랜드검색
		actionStr = "https://search.11st.co.kr/BrandSearchAction.tmall";
		method = "getBrandSearch";
	}else if(code == "TICKET"){// 티켓11번가
        actionStr="https://search.11st.co.kr/TicketSearchAction.tmall";
        method="getTicketSearchProduct";
	}else if(code == "MODEL"){// 가격비교
		actionStr = "https://search.11st.co.kr/ModelSearchAction.tmall";
		method = "getModelSearch";
	}else if(code == "CONTENTS"){//쇼핑리뷰
		actionStr = "https://search.11st.co.kr/ContentsSearchAction.tmall";
		method = "getContentsSearch";
		gnbFormObj.pageSize.value = "30";
	}else{ // T/P/NP/SL
		if(code == "BT"){ // 뷰티11번가 통합검색 추가
			actionStr = "https://beauty.11st.co.kr/newBeauty/newBeautyAction.tmall";
			method = "newBeautySearch";
			//gnbFormObj.pageSize.value = "25";
		}else if(code == "SIC"){ // 싸이닉 통합검색 추가
			actionStr = "https://scinic.11st.co.kr/beauty/BeautySearchAction.tmall";
			method = "getBeautyTotalSearch";
			gnbFormObj.pageSize.value = "10";
		}else{
			actionStr = "https://search.11st.co.kr/SearchPrdAction.tmall";
			method = "getTotalSearchSeller";
		}
	}
	if(trim(code) == "" || trim(code) == "P") code = "T";
	gnbFormObj.targetTab.value = code;
	gnbFormObj.action = actionStr;
	gnbFormObj.target = "_top";
	gnbFormObj.method.value = method;
}

/* 키워드 클릭 검색처리 */
function searchKwd(kwd){
	var gnbFormObj = document.forms["GNBSearchForm"];
	var keyword = kwd;

	if(keyword == ""){
		alert("검색어를 입력하세요.");
	}
	else{ /* OM/MM 통합검색(targetTab=T)에서 관련/추천 검색어는 11번가 통합검색으로 보낸다 - 이지연 추가 */
		if(gnbFormObj.targetTab.value == "T") gnbFormObj.targetTab.value = "P";
		gnbFormObj.kwd.value = keyword;
		gnbFormObj.target = "_top";
		gnbFormObj.adUrl.value = "";
		gnbFormObj.adKwdTrcNo.value = "";
		gnbFormObj.adPrdNo.value = "";
		gnbFormObj.submit();
	}
}

function funcSetCookieSearchKey(){}
function fucnSetSearchKey(){}
/* 키워드 광고 수동 처리 시작 */
function KeywordEvent(keywordList, stDate, enDate, url, isReserve){
	// /components/Gnb/Search/useSearch.ts 에서 사용
	this.args = [keywordList, stDate, enDate, url];
	var isUse = false;
	var targetUrl = "";

	// Today
	var td = new Date();
	var yyyy = new String(td.getFullYear());
	var mm = new String(td.getMonth()+1);
	var dd = new String(td.getDate());
	if(mm.length == 1){
		mm = "0" + mm;
	}

	if(dd.length == 1){
		dd = "0" + dd;
	}

	var curDate = parseInt(new String(yyyy + mm + dd));

	if(curDate >= parseInt(stDate) &&  curDate <= parseInt(enDate)){
		isUse = true;
		targetUrl = url;
	}

	this.goEventUrl = function(keyword)	{
		if(isUse && (keywordList.toUpperCase()).indexOf("/" + new String(keyword.toUpperCase()) + "/") > -1)	{
			if(isReserve){ 
				var	i =	new	Image();
				i.src =	"https://st.11st.co.kr/srch.st?action=gnb_event_redirect&kwd=" + encodeURIComponent(keyword);
			}
			top.location.href = targetUrl;
			return true;
		}
		return false;
	}
}

function getInnocentWord(keyword){
	var reg = /[^\uAC00-\uD7AF\u1100-\u11FF\u3130-\u318f a-zA-Z0-9]+/;
	while(keyword.match(reg)){
		keyword = keyword.replace(reg,"");
	}

	while(keyword.match(/\s/)){
		keyword = keyword.replace(/\s/,"");
	}

	return keyword;
}

var arrEvents = new Array(new KeywordEvent("","", "", ""));

try{
	if(isUTF8 == true);
}catch(e){
	isUTF8 = false;
}

function encodeKwd(keyword)	{
	if(getHtmlCharset() == "utf-8")	{
		keyword = encodeURIComponent(keyword);
	}

	return keyword;
}

function encodeKwdNew(keyword){
	keyword = encodeURIComponent(encodeURIComponent(keyword));
	return keyword;
}

function searchReset(){
	var form = jQuery("[name=GNBSearchForm]");

	//Anchor 이동용 값 추가
	if(form.find("[name=targetAnchor]").length == 0){
		var input = jQuery("<input type='hidden' name='targetAnchor' value='#searchlist' />").appendTo(form);
	};

	goSearch();
}
function goSearchFromGNB(){
	var gaParam = {};
	gaParam.actionName = 'PC_GNB_통합검색>키워드검색';
	goSearch('', gaParam);
}
function goSearch(code, gaParam, area){
	if(code != undefined && code != null){
		doCommonStat(code);
	}else{
		//통계코드 영역 접두코드
		var areaCodePre = HeaderGnb.makeGnb.areaCodePre;
		doCommonStat(areaCodePre + "GN0314");
	}
	
	var gnbFormObj = document.forms["GNBSearchForm"];
	var keyword = trim(gnbFormObj.kwd.value);
	if(typeof(area) != 'undefined' && area != ''){
		if(area == 'BT' || area == 'SIC'){
			gnbFormObj = document.forms["BeautyGNBSearchForm"];
		}
	}
	
	if(ga && gaParam){
		var actionName = gaParam.actionName;
		var categoryNameLocation = gaParam.categoryNameLocation;
		var gaCustomValue = {};
		
		if(categoryNameLocation){
			gaCustomValue.dimension21 = categoryNameLocation;
			ga('send', 'event', actionName, document.title, keyword, gaCustomValue);
		}else{
			ga('send', 'event', actionName, document.title, keyword);
		}
	}
	
	if(gnbFormObj.targetTab.value == "SL"){	 //판매자 검색
		gnbFormObj.action = "https://search.11st.co.kr/Search.tmall";
		gnbFormObj.method.value = "";
	}else if(gnbFormObj.targetTab.value == "S"){ // 가게
		gnbFormObj.action = "https://search.11st.co.kr/SearchSellerShopAction.tmall";
	}else if(gnbFormObj.targetTab.value == "CH"){	// 뷰티11번가
		gnbFormObj.action = "https://beauty.11st.co.kr/TotalSearch.do";
		gnbFormObj.category.value = "cherrya";
		gnbFormObj.cmd.value = "productList";
	}else if(gnbFormObj.targetTab.value == "MO"){	// 도서11번가
		gnbFormObj.action = "https://books.11st.co.kr/booksmall/BooksAction.tmall";
		gnbFormObj.ID.value = "BOOKS";
		gnbFormObj.ctgrNo.value = "63517";
		gnbFormObj.srCtgrNo.value = "63516";
	}else if(gnbFormObj.targetTab.value == "TOUR11ST"){//여행 11번가
		gnbFormObj.action = "https://tour.11st.co.kr/tour/TourSearchAction.tmall";
		gnbFormObj.keyword.value = gnbFormObj.kwd.value;
	}else if(gnbFormObj.targetTab.value == "TOUR"){//여행
		gnbFormObj.action = "https://tour.11st.co.kr/tour/TourSearchAction.tmall";
		gnbFormObj.keyword.value = gnbFormObj.kwd.value;
	}else if(gnbFormObj.targetTab.value == "OVERSEAS"){//해외호텔
		gnbFormObj.action = "https://tour.11st.co.kr/tour/TourSearchAction.tmall";
		gnbFormObj.keyword.value = gnbFormObj.kwd.value;
	}else if(gnbFormObj.targetTab.value == "DOMESTIC"){//국내숙박
		gnbFormObj.action = "https://tour.11st.co.kr/tour/TourSearchAction.tmall";
		gnbFormObj.keyword.value = gnbFormObj.kwd.value;
	}else if(gnbFormObj.targetTab.value == "SEMANTIC"){//시맨틱 검색
		gnbFormObj.action = "https://search.11st.co.kr/SemanticSearchAction.tmall";
		gnbFormObj.method.value = "getSemanticSearch";
	}else if(gnbFormObj.targetTab.value == "MODEL"){//가격비교
		gnbFormObj.action = "https://search.11st.co.kr/ModelSearchAction.tmall";
		gnbFormObj.method.value = "getModelSearch";
	}else if(gnbFormObj.targetTab.value == "CONTENTS"){//쇼핑리뷰
		gnbFormObj.action = "https://search.11st.co.kr/ContentsSearchAction.tmall";
		gnbFormObj.method.value = "getContentsSearch";
		gnbFormObj.pageSize.value = 30;
	}else if(gnbFormObj.targetTab.value == "BT"){//신뷰티11번가
		gnbFormObj = document.forms["BeautyGNBSearchForm"];
		gnbFormObj.action = "https://beauty.11st.co.kr/newBeauty/newBeautyAction.tmall";
		gnbFormObj.method.value = "newBeautySearch";
		keyword = trim(gnbFormObj.kwd.value);
	}else if(gnbFormObj.targetTab.value == "SIC"){//싸이닉
		gnbFormObj = document.forms["BeautyGNBSearchForm"];
		gnbFormObj.action = "https://scinic.11st.co.kr/beauty/BeautySearchAction.tmall";
		gnbFormObj.method.value = "getBeautyTotalSearch";
		keyword = trim(gnbFormObj.kwd.value);
	}else if(gnbFormObj.targetTab.value == "TICKET"){//티켓11번가
		actionStr="https://search.11st.co.kr/TicketSearchAction.tmall";
		method="getTicketSearchProduct";
	}

	var ad_banner_url = gnbFormObj.adUrl.value;
	if(ad_banner_url == ""){
		if(keyword == ""){
			alert("검색어를 입력하세요.");
			gnbFormObj.kwd.focus();
			// return false;
		}else if(chkKeywordEvent(keyword)){
			return;
		}else if(gnbFormObj.targetTab.value == "D" && !IsNumeric(keyword)){
			alert("운송번호 조회는 숫자(정수)만 가능합니다.");
			gnbFormObj.kwd.focus();
		}else if(gnbFormObj.targetTab.value == "D" && keyword.length < 10){
			alert("운송번호 10자리 이상 입력하세요.");
			gnbFormObj.kwd.focus();
		}else if(gnbFormObj.targetTab.value == "N"){
			if(!IsNumeric(keyword)){
				alert("상품번호는 숫자(정수)만 가능합니다.");
				gnbFormObj.kwd.focus();
			}else{
				var prdNoUrl = _GNB_CONTEXT_PATH_ + "/products/" + keyword;
				// Start 2010.11.24 검색 조건 별 선택 횟수 집계
				prdNoUrl += "&gnbTag=NO";
				// End   2010.11.24 검색 조건 별 선택 횟수 집계
				document.location.href = prdNoUrl;
			}
		 }else if(gnbFormObj.targetTab.value == "SL"){

			 if(gnbFormObj.targetAnchor)
					gnbFormObj.action += gnbFormObj.targetAnchor.value; // add anchor name

			//fucnSetSearchKey(keyword); //내 검색 기록 쿠키 남기기
			//gnbFormObj.kwd.value = encodeKwd(keyword);
			gnbFormObj.kwd.value = encodeKwdNew(keyword);
			gnbFormObj.action = protocolCheckAndUpdate(gnbFormObj);
			gnbFormObj.submit();
		}else{ // T/P/NP/M/I/S
			if(gnbFormObj.targetAnchor)
				gnbFormObj.action += gnbFormObj.targetAnchor.value; // add anchor name
			
			keyword = keyword.replace(/&/g, ' ');

			gnbFormObj.kwd.value = encodeKwd(keyword);
			gnbFormObj.action = protocolCheckAndUpdate(gnbFormObj);
			gnbFormObj.submit();
		}

	}else{
		//검색창 텍스트링크 광고
		var trcNo = gnbFormObj.adKwdTrcNo.value;
		var typGubn = 'M';
		var areaGubn = 'A01';
		var prdNo = gnbFormObj.adPrdNo.value;

		stck(typGubn, areaGubn, trcNo);
		if(prdNo > 0){
			ad_headerCommonJs.util.instance.ConversionCookieQueue.add(trcNo, prdNo, (typGubn + '' + areaGubn));
		}

		top.location.href = ad_banner_url;
	}
}

function getListPage(rows,pageNumber,tots,pageRows,onlyPremPrd){
	var argLength = arguments.length;
	var rowsPerPage = rows;
	var currentPage = pageNumber;
	var totalCount = tots;

	var totalPage = "";
	if(totalCount % rowsPerPage)
		totalPage =  (Math.floor(totalCount / rowsPerPage) + 1);
	else
		totalPage = Math.floor(totalCount / rowsPerPage);

	var pageGroupStart = Math.floor(((currentPage-1) / pageRows)) * pageRows + 1;
	var pageGroupEnd = (pageGroupStart + pageRows -1 >= totalPage) ? totalPage : (pageGroupStart + pageRows - 1);
	if(totalPage <= 0)
		totalPage = 1;

	var sbuf = "<div class=\"pagingV2_wrap\"><div class=\"paging_Align_FreeW\"><div class=\"paging_v4\">";

	sbuf += "<a href=\"javascript:goToFirstPage(" + currentPage + ", 1);\" class=\"first\" title=\"첫페이지\"></a>";

	if(currentPage - rowsPerPage > 0 || currentPage > pageRows)
		sbuf += "<a href=\"#\" onClick=\"javascript:navigatePage('"+ (pageGroupStart - 1)+ "');return false;\" class=\"pre\" title=\"앞페이지10개\"></a>";
	else
		sbuf += "<a class=\"pre\" title=\"앞페이지10개\"></a>";

	sbuf += "<span class=\"pagingList\">";
	sbuf += "<ul>";

	for (var i = pageGroupStart; i <= pageGroupEnd; i++){
		if(i == currentPage)
			sbuf += "<li><a href=\"#\" onClick=\"javascript:navigatePage('" + i + "');return false;\" class=\"on\">" + i + "</a></li>\n";
		else
			sbuf += "<li><a href=\"#\" onClick=\"javascript:navigatePage('" + i + "');return false;\">"+i+"</a></li>\n";
	}

	if(totalCount == 0)
		sbuf += "<li><a href=\"#\" onClick=\"javascript:navigatePage('1');return false;\">1</a></li>\n";

	sbuf += "</ul>";
	sbuf += "</span>";

	if(pageGroupEnd < totalPage)
		sbuf += "<a href=\"#\" onClick=\"javascript:navigatePage('"+ (pageGroupStart + pageRows)+ "');return false;\" class=\"next\" title=\"다음페이지10개\"></a>";
	else
		sbuf += "<a class=\"next\" title=\"다음페이지10개\"></a>";

	sbuf += "<a href=\"javascript:goToLastPage(" + currentPage + ", " + totalPage + ");\" class=\"end\" title=\"마지막페이지\"></a>";

	sbuf += "</div></div>";
/*
 * if(argLength == 5){ sbuf += "<div class=\"info_v2\">"; if(onlyPremPrd){
 * sbuf += "<a href=\"javascript:goNormPrdPage_Ctgr();\"
 * class=\"btn_viewList_2\"></a>"; }else{ sbuf += "<a
 * href=\"javascript:goPremiumPrdPage();\" class=\"btn_viewList_1\"></a>"; }
 * sbuf += "</div>"; }
 */
	sbuf += "<div class=\"page_GotoWrap\">";
	sbuf += "<span class=\"page\"><input type=\"text\" name=\"directPage\" id=\"directPage\" value=\"" + currentPage + "\" onclick=\"this.value=''\" style=\"ime-mode:disabled\" onkeypress=\"inputOnlyNumber(event)\"></span>";
	sbuf += "<span class=\"InLineWrap\">";

	sbuf += "<div class=\"total\">&nbsp;/ 총 <span>" + totalPage + "</span>페이지</div>";
	sbuf += "<a href=\"javascript:goToPageDirect(" + totalPage + ");\" class=\"btn_pagego\"></a>";

	sbuf += "</span>";
	sbuf += "</div></div>";

	return sbuf;
}
function getNewListPage(rows,pageNumber,tots,pageRows){
	var argLength = arguments.length;
	var rowsPerPage = rows;
	var currentPage = pageNumber;
	var totalCount = tots;

	var totalPage = "";
	if(totalCount % rowsPerPage)
		totalPage =  (Math.floor(totalCount / rowsPerPage) + 1);
	else
		totalPage = Math.floor(totalCount / rowsPerPage);

	var pageGroupStart = Math.floor(((currentPage-1) / pageRows)) * pageRows + 1;
	var pageGroupEnd = (pageGroupStart + pageRows -1 >= totalPage) ? totalPage : (pageGroupStart + pageRows - 1);
	if(totalPage <= 0)
		totalPage = 1;



	var sbuf = "<div class=\"pagingV2_wrap\"><div class=\"paging_Align_FreeW\"><div class=\"paging_v4\">";

	var prePage = 0;

	// sbuf += "<a href=\"javascript:goToFirstPage(" + currentPage + ", 1);\"
	// class=\"first\" title=\"첫페이지\"></a>";
	sbuf += "<a href=\"javascript:navigatePage('"+ (currentPage - 1)+ "');\" class=\"pre\" title=\"앞페이지10개\"></a>";


	sbuf += "<span class=\"pagingList\"><ul>";

	for (var i = pageGroupStart; i <= pageGroupEnd; i++){
		if(i == currentPage)
			sbuf += "<li><a href=\"javascript:navigatePage('" + i + "');\" class=\"on\">" + i + "</a></li>";
		else
			sbuf += "<li><a href=\"javascript:navigatePage('" + i + "');\">"+i+"</a></li>";
	}

	if(totalCount == 0)
		sbuf += "<li><a href=\"javascript:navigatePage('1');\">1</a></li>";

	sbuf += "</ul></span>";

	sbuf += "<a href=\"javascript:navigatePage('"+ (currentPage + 1)+ "');\" class=\"next\" title=\"다음페이지10개\"></a>";
	// sbuf += "<a href=\"javascript:goToLastPage(" + currentPage + ", " +
	// totalPage + ");\" class=\"end\" title=\"마지막페이지\"></a>";

	sbuf += "</div>";

	sbuf += "</div>";

	sbuf += "</div>";

	return sbuf;
}
function goToFirstPage(cur, move){
	if(cur == move)
		alert("처음 페이지 입니다");
	else
		navigatePage(move);
}
// type_check.js
function isBlank(obj){
	if(typeof(obj) == "object"){
		if(obj.value == ""){
			return true;
		}else{
			return false;
		}
	}else{
		alert("Object 가 아닙니다.");
		return false;
	}
}

function IsNumeric(checkStr){
	if(checkStr == undefined){
		return false;
	}else{
		for (var i = 0; i < checkStr.length; i++){
			ch = checkStr.charAt(i);
			if(ch < "0" || ch > "9")
				return false;
		}
		return true;
	}
}

function trim(str){
  var count = str.length;
  var len = count;
  var st = 0;

  while ((st < len) && (str.charAt(st) <= ' ')){
	 st++;
  }
  while ((st < len) && (str.charAt(len - 1) <= ' ')){
	 len--;
  }
  return ((st > 0) || (len < count)) ? str.substring(st, len) : str ;
}

function checkNumber(value, isNeed){
	// value 값이 있을경우만 체크한다.
	if(value != ""){
		var x = value;

		var anum =/(^\d+$)|(^\d+\.\d+$)|(^[-]\d+$)|(^[-]\d+\.\d+$)/;

		if(anum.test(x)){
			return true;
		}else{
			return false;
		}
	}else{
		return true;
	}
}

function numberCheck(obj, msg, limit_num1, limit_num2, isNeed){
	if(typeof(obj) == "object")
	{
		if(isNeed){
			if(isBlank(obj)){
				alert(msg);
				alertInput(obj);

				return false;
			}
		}

		if(!isBlank(obj)){
			if(!checkNumber(obj.value, isNeed)){
				alert(msg);
				alertInput(obj);

				return false;
			}
			else if(!checkFigure(obj.value, limit_num1, limit_num2)){
				if(limit_num1 != limit_num2){
					alert(limit_num1 + "~" + limit_num2 + " 자리까지 입력해주십시오.");
				}else{
					alert(limit_num1 +" 자리까지 입력해주십시오.");
				}
				alertInput(obj);
				return false;
			}
		}
		return true;
	}else{
		alert("Object 가 아닙니다.");
		return false;
	}
}

var NUM = "0123456789";
var SALPHA = "abcdefghijklmnopqrstuvwxyz";
var ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"+SALPHA;
var EMAIL = "!#$%&*+-./=?@^_`{|}"+NUM+ALPHA;

function isNumber(obj, title, isNeed){
	return numberCheck(obj, title + '은(는) 반드시 숫자로 입력하셔야 합니다.', 0, 14, isNeed);	// 10
}
function getRanNum(v){
	return Math.floor(Math.random()*v) + 1;
}

/*
 * 가중치에 따른 랜덤 카운트 arrWeight : 가중치 배열 return : 가중치에 따른 배열 Index
 */
function getRanNumWeight(arrWeight){
	var totalWeight = 0; // 총가중치
	var ranWegithNum; // 랜덤생성번호
	var returnIndex = 0;

	try {
		if(arrWeight == "undefined") return;

		for(var i=0 ; i<arrWeight.length ; i++){
			totalWeight += arrWeight[i];
		}

		ranWegithNum = Math.random()*totalWeight;

		// 가중치에 해당하는 index 조회
		var beforeWeight = 0;
		var thisWeight = 0;
		for(var i=0 ; i<arrWeight.length ; i++){
			thisWeight = thisWeight + arrWeight[i];

			if(i != 0){
				beforeWeight = beforeWeight + arrWeight[i-1];
			}

			// 랜덤 가중치가 전 가중치와 현재 index 가중치 사이에 있을시 해당 index번호 축출
			if(ranWegithNum >= beforeWeight && ranWegithNum <= thisWeight){
				returnIndex = i;
				break;
			}
		}

	} catch (e){}

	return returnIndex;
}

// 검색창 레이어 숨김처리
var _objSrchRunFlag;
var _objSrchRun;
var _mouseSrchStatus;
/**
 * 2011.02.25 - 송명수 검색관련 function은 searchManager에 모아 추후 분리한다.
 */
var searchManager = {
	isAkcLoaded : false,
	akcObj : "",
	getSSLParam: function(){
		var rtnParamString = "";
		if(document.location.protocol === "https:"){
			rtnParamString = "isSSL=Y";
		}
		return rtnParamString;
	}
};

var townSearchManager = {
	isAkcLoaded : false,
	akcObj : ""
};

/* Web Javascript Error Logging Start */
var Logger = new Logger();

function Logger(){
	this.Filters = new Array();

	this.IsFiltered = function(){
		var iter;
		for (var iter = 0; iter < Logger.Filters.length; iter++){
			var filter = Logger.Filters[iter];
			if(filter())
				return true;
		}
		return false;
	}

	this.ErrorHandler = function(pMsg, pURL, pLines){
		Logger.LoggingMsg("msg:" + pMsg + " / url:" + pURL + " / lines:" + pLines);
	}

	this.LoggingMsg = function(description){
		if(Logger.IsFiltered())
			return;
		var hostname = document.location.hostname;
		var errPageURL = GetLoggingPoint(hostname);
		var queryString = "";
		queryString = AddErrorQuery(queryString, "Source", document.location.pathname);
		queryString = AddErrorQuery(queryString, "Description", description);
		queryString = AddErrorQuery(queryString, "Query", document.location.search);
		queryString = AddErrorQuery(queryString, "Server", document.location.hostname);
		errPageURL += queryString;
		var imgObj = document.createElement('img');
		imgObj.setAttribute("src", errPageURL);
		imgObj.setAttribute("height", 0);
		imgObj.setAttribute("width", 0);
		document.body.appendChild(imgObj);
	}

	GetLoggingPoint = function(domainName){
		var retTag = document.location.protocol;
		return retTag + "//err.11st.co.kr/e.st";
	}

	AddErrorQuery = function(query, key, value){
		if(query != "") query += "&";
		else query += "?";
		query += escape(key) + "=" + escape(value);
		return query;
	}
}

/* Web Javascript Error Logging End */

/**
 * 상품 이미지 더보기
 */
var ImageSplit_headerCommonJs = function(){
	var imgUrl = "";
	var imgList = new Array();
	var imgSize = "";

	var $object = "";
	var orgImg = "";
	var $aTagObj = "";

	var timer = "";

	function getImageCutUrl(){
		var url = "https://search.11st.co.kr/SearchPrdAction.tmall?callBack=?";

		var data = {
				"method" : "getProductImageSplit",
				"imgUrl" : imgUrl,
				"imgSize" : imgSize
				};
		try{
			jQuery.getJSON(url, data, function(data){
				if(data.success){
					imgList = data.LARGE_IMG_LIST;
					if(imgList.length > 0){
						drawSplitImage();
					}
				}
			})
		} catch(e){}
	}

	function drawSplitImage(){
		try{
			if(timer != ""){
				var errorImg = jQuery(orgImg).attr("onError");
				var className = jQuery(orgImg).attr("class");

				for(var i=0 ; i < imgList.length && i < 5 ; i++){
					var cutImg = new Image();
					var imgUrl = imgList[i].replace('/280x280/', '/80x80/');
					if(imgUrl.indexOf(_UPLOAD_URL_) <  0)
					{
						imgUrl = _UPLOAD_URL_ + imgUrl;
					}
					cutImg.src = imgUrl;

					cutImg.width = orgImg.width;
					cutImg.height = orgImg.height;
					jQuery(cutImg).addClass(className);
					jQuery(cutImg).error(function(){
						jQuery(this).attr("src", errorImg); // No Image
					})

					$aTagObj.append(cutImg);
				}

				$object.data("SPLIT_IMG",jQuery("img", $aTagObj));

				showAnimate();
			}
		} catch(e){}
	}

	function showAnimate(){
		try{
			$object.addClass("numwrap");
			$object.animate({width: (imgSize +1)*imgList.length + 1}, 200);
			jQuery(orgImg).remove();
		} catch(e){}
	}

	return {}
}();

/*
 * JSONP CALL
 */
var getJsonpData = function(){
	var url = "";
	var callbackName = "";
	var charset = "utf-8";
	var useTrace = false;
	var errorCallbackName = "";
	var errorCallbackCalledCnt = 0;
	var trace = function(msg){
		if(useTrace && window.console){
			console.log("[headerCommonJs.getJsonData] " + msg);
		}
	};

	return {
		setUseTrace: function(bolVal){
			useTrace = bolVal;
		},
		getUrl: function(){
			return url;
		},
		setUrl : function(pUrl){
			url = pUrl;
		},
		setCallbackName : function(nm){
			callbackName = nm;
		},
		setCharSet : function(char){
			charset = char;
		},
		setErrorCallbackName : function(cbnm){
			errorCallbackName = cbnm;
		},
		init : function(){
			jQuery.ajax({
				url: url,
				dataType: "jsonp",
				jsonp: false,
				scriptCharset: charset ,
				jsonpCallback: callbackName,
				success: function(data){
					trace("success: " + data);
				},
				complete: function(jqXHR, textStatus){
					trace("complete: jqXHR " + jqXHR.status);
					trace("complete: textStatus " + textStatus);
				},
				error: function(jqXHR, textStatus, errorThrown){
					try {
						errorCallbackCalledCnt++;
						if(errorCallbackCalledCnt <= 2){ // 예외 발생시 최대 2번까지 error시 콜백함수 호출
							eval("("+ errorCallbackName + ")()");
						}
					} catch(error){}
					trace("error: status - " + jqXHR.status);
					trace("error: textStatus - " + textStatus);
					trace("error: errorThrown - " + errorThrown);
				}
			});
		}
	}
}

Date.prototype.toYYYYMMDD = function(delim){
	if(!delim) delim = "";
	var year = this.getFullYear().toString();
	var month = this.getMonth() + 1;
	var day = this.getDate();

	month = (month < 10 ? "0" : "") + month;
	day = (day < 10 ? "0" : "") + day;

	return year + delim + month + delim + day;
}

function getNitmusParam(existParam){
	var param = TMCookieUtil.getSubCookie(0,'nitmus');
	var result = "";

	if(param !== ""){
		var delimiter = existParam ? "&" : "?";
		result = delimiter + decodeURIComponent(param);
	}

	return appendTimeStamp(result);
}

if(typeof jQuery !== "undefined"){
	jQuery.ajaxPrefilter(function(options){
		if((options.url).indexOf("ds.11st.co.kr") !== -1){
			options.cache = true;
		}
	});
}

(function(){
	var cookieValue = getCookie("PRODUCT_CHECK_PRDNO");
	if(cookieValue && cookieValue != undefined && cookieValue != null && cookieValue != ""){
		cookieValue = cookieValue.replace(/:/gi,"?@");
		TMCookieUtil.add(3,"MH_PRD",cookieValue);
		setCookie("PRODUCT_CHECK_PRDNO","",new Date("2011"));
	}
})();

/* IP 국가별 시작 페이지 관리 */
var StartPageManager=function (){
    var ENTERANCE="11ST_ENTERANCE";
    var ENTERANCE_EN="EN";
    var ENTERANCE_KR="KR";

    var CONN_IP_LOC="CONN_IP_LOC";
    var CONN_IP_DOM="DOM";
    var CONN_IP_FOR="FOR";

    var VIEW_DLV_LAYER="VIEW_DLV_LAYER";

    var initialize=function (){
				var result = new RegExp("isGlobal=([^&]*)", "i").exec(window.location.search);
        if(result && result[1] =="Y"){
        	setCookie(CONN_IP_LOC, CONN_IP_FOR);
            //showLayer();
            //toastBanner(false);
        }else{

        	// 접속아이피 지역 정보
        	var cookieValConnIpLoc=TMCookieUtil.getSubCookie(2, CONN_IP_LOC).toUpperCase();

        	if(cookieValConnIpLoc==null || cookieValConnIpLoc=="" || cookieValConnIpLoc=="EMPTY"){
        		getDomesticAccessYn();
        	}

        	cookieValConnIpLoc=TMCookieUtil.getSubCookie(2, CONN_IP_LOC).toUpperCase();

        	// 해외접속 IP 인경우
        	if(cookieValConnIpLoc==CONN_IP_FOR){
        		//toastBanner(false);
        		//showLayer();
        	}else{
        		//toastBanner(true);
        	}
        }
    };

    // 국내 접속여부
    var getDomesticAccessYn=function(){
        try{
            jQuery.ajax({
							url:"//www.11st.co.kr/browsing/Main.tmall?method=getDomesticAccessYnAjax",
							type:"post",
							dataType:"jsonp",
							scriptCharset:"UTF-8",
							crossDomain:true,
							success:function(data){
								if(data.result=="N"){//해외 접속 IP
									setCookie(CONN_IP_LOC, CONN_IP_FOR);
								}else{//국내 접속 IP
									setCookie(CONN_IP_LOC, CONN_IP_DOM);
								}
							},
							error :function (xhr, status, error){}
						});
					}catch(e){}
    };

    var showLayer=function (){
    	var cookieVal=TMCookieUtil.getSubCookie(2, ENTERANCE).toUpperCase();
        if(cookieVal==null || cookieVal=="" || cookieVal=="EMPTY"){
        	jQuery("#global_top_cntr").show();
        }else{
        	showDlvInfoLayer();
        }
    };

    var showDlvInfoLayer=function (){
    	var cookieVal=TMCookieUtil.getSubCookie(2, VIEW_DLV_LAYER).toUpperCase();

        if(cookieVal==null || cookieVal=="" || cookieVal=="EMPTY"){
        	jQuery("#global_deliv_top").show();
        }
    };

    var hideDlvInfoLayer=function (noMoreView){

   		jQuery("#global_deliv_top").hide();

    	if(noMoreView){
    		setCookie(VIEW_DLV_LAYER, "N");
    	}
    };

    var hideLayer=function (){
        jQuery("#global_top_cntr").hide();
    };

    var goEnglish11st=function (){
        location.href="https://global.11st.co.kr";
    };

    var goKorean11st=function (){
        location.href="https://www.11st.co.kr/main";
    };

    var setCookie=function (cookieName, cookieValue){
        TMCookieUtil.add(2, cookieName, cookieValue);
    };

    // 쿠키에 저정되었으니, footerJsData_v6.js(inc_footer_data_v6.js 에서 호출한다.)
    /*
    var toastBanner=function (isKor){
    	return;
        if(typeof(toastBnnr)!="undefined"){
        	try{
        		FooterData.toastBnnr.init(isKor, toastBnnrState);
        	} catch(e){}
        }
    };
    */

    return {
        init:function (){
            initialize();
        },
        show:function (){
            showLayer()
        },
        hide:function (){
            hideLayer();
        },
        hideDlvInfoLayer :function (noMoreView){
        	hideDlvInfoLayer(noMoreView);
        },
        korean  :function (){
            setCookie(ENTERANCE, ENTERANCE_KR);
            goKorean11st();
        },
        english :function (){
            setCookie(ENTERANCE, ENTERANCE_EN);
            goEnglish11st();
        }
    }
}();

//바닥 페이지에서 성인 본인인증하기 버튼
function adultCrtf(code)	{
	var retUrl 	= encodeURIComponent(document.location.href);
	var referer = "";

	if(retUrl.indexOf("www.11st.co.kr") != -1){ //11번가
		referer = "www.11st.co.kr";
		var xFrom 	= "";
		if(retUrl == _GNB_CONTEXT_PATH_ + "/html/main.html")	{
			xFrom = "main^gnb";

		}
		retUrl + "&xfrom=" + xFrom;
	}
	else if(retUrl.indexOf("town.11st.co.kr") != -1){ //타운11번가
		referer = "town.11st.co.kr";
	}

	goStatUrl(_LOGIN_TARGET_URL_+"/login/AdultCrtf.tmall?returnUrl=" + retUrl +"&referer="+ referer , code);
}

/**
 * @author celestialmoon
 * @reason 광고전환통계개선(P1206004) PJ로 추가
 */
// ----- 광고전환통계개선용 모듈 시작 -----
var ad_headerCommonJs = ad_headerCommonJs || {};
ad_headerCommonJs.util = ad_headerCommonJs.util || {};
ad_headerCommonJs.util.cookie = ad_headerCommonJs.util.cookie || {};
ad_headerCommonJs.util.instance = ad_headerCommonJs.util.instance || {};

ad_headerCommonJs.util.cookie.CookieUtil = function(){
	this.defaultCookieOptions = {
		expires: 1,
		path: '/',
		domain: ".11st.co.kr"
	};
};
ad_headerCommonJs.util.cookie.CookieUtil.prototype = {
	isExistCookie: function(key){
		var result = null;

		if(result = new RegExp(key + "=(.*?)(?:;|$)").exec(document.cookie)) return true;
		return false;
	},
	cookie: function(key, value, options){
		if(arguments.length > 1){
			options = options || this.defaultCookieOptions;

			if(value === null || value === undefined || value == '') return;

	        if(options.expires.constructor != Date){
	        	var expireDate = new Date();
	        	expireDate.setDate(expireDate.getDate() + options.expires);
	        	options.expiresDate = expireDate;
	        }

	        var cookieOptionsValue = key + '=' + value +
	        	(options.expires == -1 ? '' : '; expires=' + options.expiresDate.toUTCString()) +
	        	(options.path ? '; path=' + (options.path) : '') +
	        	(options.domain ? '; domain=' + (options.domain) : '') +
	        	(options.secure ? '; secure' : '');

	        document.cookie = cookieOptionsValue;
		}
		else{
			var result = null;

			if(result = new RegExp(key + "=(.*?)(?:;|$)").exec(document.cookie))
				return result[1];
		}
	}
};

ad_headerCommonJs.util.cookie.ConversionCookieQueue = function(parameter){
	parameter = parameter || {};

	this.cookieUtil = new ad_headerCommonJs.util.cookie.CookieUtil();
	this.isDebugEnabled = false;

	var thisObj = this;
	var cookieKey = parameter.cookieKey || 'adC';
	var maximumQueueSize = parameter.size || 10;
	var eachItemMatchedKeyIndex = parameter.eachItemMatchedKeyIndex || 2;
	var eachValueDelimiter = '^', eachQueueValueDelimiter = '!';
	var queue = null;
	var requstStackArray = null;
	var validAction = null;

	this.add = function(trcNo, prdNo, typeAreaGubun, actionType){
		if(arguments.length == 0 || isNaN(trcNo) || parseFloat(trcNo) <= 0) return;
		if(eachItemMatchedKeyIndex > arguments.length) eachItemMatchedKeyIndex = -1;
		var values = Array.prototype.slice.call(arguments, 0, 3);

		removeUnnecessaryValue(values);
		this.trimQueue();

		var nowDate = new Date();
		queue.push(values.join(eachValueDelimiter) + eachValueDelimiter + nowDate.getDay() + '' + nowDate.getHours());

		if(this.isDebugEnabled) this.log(queue.join(eachQueueValueDelimiter) + " ==> " + values.join(', '));

		this.cookieUtil.cookie(cookieKey, queue.join(eachQueueValueDelimiter));

		if(arguments.length > 3) this.requestToServer(prdNo, actionType);
	};
	this.take = function(){
		if(this.isEmpty()) return null;
		return queue.splice(0, 1).join('');
	};
	this.isEmpty = function(){
		return (queue.length == 0);
	};
	this.getSize = function(){
		return (queue.length);
	};
	this.find = function(value){
		if(!this.isEmpty() && value){
			var targetValue = (value instanceof Array ? (eachItemMatchedKeyIndex != -1 ? value[(eachItemMatchedKeyIndex - 1)] : value.join('')) : value);
			var existsMatchedTarget = false;

			for (var i = 0; i < thisObj.getSize.call(thisObj); ++i){
				if((eachItemMatchedKeyIndex != -1 ? queue[i].split(eachValueDelimiter)[(eachItemMatchedKeyIndex - 1)] : queue[i].join('')) == targetValue){
					existsMatchedTarget = true;
					break;
				}
			}

			return {has: existsMatchedTarget, index: i};
		}

		return {has: false};
	};
	this.hasValue = function(value){
		return (this.find(value)).has;
	};
	this.trimQueue = function(){
		if(queue.length >= maximumQueueSize)
			for (var j = 0, arrayLength = queue.length; j <= arrayLength - maximumQueueSize; ++j) thisObj.take.call(thisObj);
	};
	this.requestToServer = function(prdNo, actionType){
		if(this.hasValue(prdNo) && isValidAction(actionType)){
			if(!requstStackArray) requstStackArray = [];
			var requestImg = new Image();
			requstStackArray[0] = requestImg;

			requestImg.src = 'https://www.11st.co.kr/ad11st/Ad11stAction.tmall?method=saveConversionLog' +
				'&prdNo=' + prdNo + '&actionType=' + actionType + '&noCache=' + (new Date()).getTime();
		}
	};
	this.log = function(value){
		var divElm = document.getElementById("_$_logArea_$_");

		if(!divElm){
			divElm = document.createElement("div");
			divElm.setAttribute("id", "_$_logArea_$_");

			if(document.body) document.body.appendChild(divElm);
			else if(document.documentElement) document.documentElement.appendChild(divElm);
		}

		divElm.innerHTML = divElm.innerHTML + value + "<br />";
	};
	function removeUnnecessaryValue(value){
		var matchedInfo = thisObj.find.call(thisObj, value);
		if(matchedInfo.has) queue.splice(matchedInfo.index, 1);

		if(!thisObj.isEmpty.call(thisObj)){
			var nowDate = new Date();
			var compareDate = new Date(Date.parse(nowDate) - (1 * 1000 * 60 * 60 * 24));
			var dayInfo = null, timeInfo = null;
			var isRemoveElement = false;

			nowDate.setMinutes(0, 0, 0);

			for (var i = (thisObj.getSize.call(thisObj) - 1); i >= 0; --i){
				dayInfo = queue[i].split(eachValueDelimiter)[3].split('');
				timeInfo = (dayInfo.splice(1, (dayInfo.length - 1))).join('');

				if(nowDate.getDay() != dayInfo){
					if(Math.abs(((nowDate.getDay() - dayInfo) % 5)) > 1) isRemoveElement = true;
					else{
						compareDate.setHours(timeInfo, 0, 0, 0);
						if(((nowDate.getTime() - compareDate.getTime()) / (1000 * 60 * 60)) > 24) isRemoveElement = true;
					}

					if(isRemoveElement) queue.splice(i, 1); isRemoveElement = false;
				}
			}
		}
	};
	function buildQueueUsingCookieValue(){
		cookieValue = thisObj.cookieUtil.cookie.call(thisObj.cookieUtil, cookieKey);
		return cookieValue.split(eachQueueValueDelimiter);
	};
	function isValidAction(actionType){
		if(!validAction) validAction = ['order', 'basket', 'jjim', 'buy'];
		for (var i = 0; i < validAction.length; ++i)
				if(validAction[i] === actionType) return true;
		return false;
	};

	try {
		queue = (this.cookieUtil.isExistCookie(cookieKey) ? buildQueueUsingCookieValue() : []);
		removeUnnecessaryValue();
	}
	catch (error){
		queue = [];
	}

	this.cookieUtil.cookie(cookieKey, queue.join(eachQueueValueDelimiter));
};

(function(){
	ad_headerCommonJs.util.instance.ConversionCookieQueue = new ad_headerCommonJs.util.cookie.ConversionCookieQueue({
		cookieKey: 'adC',
		size: 10,
		eachItemMatchedKeyIndex: 2
	});
})();
// ----- 광고 전환 통계 개선용 모듈 끝 -----
var headSelOFocusflag = false;
HeaderComm.SimpleFIOUtil = (function(){
	var lastObj;
	var desc = {ver: 1.3, appNick: "SimpleFocusInOutUtil", desc: "It makes keyboard focus events automatically."};
	var outFnObj, execSkip, eventHandler = {
		setEvent: function(st){
			var inFnObj, _this = this;
			// put a last focusable object.
			this.setLastObj(st);
			jQuery(st).bind({
				"focusin" : function(evt){
					inFnObj = fnExtractor.getFn(evt, this, "mouseover");
					_this.exec(outFnObj, this);	// 이전객체의 out event먼저 실행
					_this.exec(inFnObj, this);	// 현재 객체의 in evet 실행
				}
				,"focusout": function(evt){
					var target = evt.target;
					var tmpOutFnObj = fnExtractor.getFn(evt, this, "mouseout");
					if(tmpOutFnObj.fn !== "NaF"){
						outFnObj = tmpOutFnObj;
					}
					_this.execForLastObj(outFnObj, this, target); // focusin이 될 항목이 없을 경우, out을 실행시킨다.
				}
			});
		},
		exec: function(fn, obj){
			try {
				var _fn = fn.fn;
				if(_fn && !execSkip && _fn !== "NaF"){  // check for an executable function
					_fn(fn.evt, obj);
				}
			} catch(e){}
		},
		execForLastObj: function(fn, obj, target){
			if(lastObj[0] === target){
				this.exec(fn, obj);
			}
		},
		setLastObj : function(st){	// save a last focusable object.
			var obj = jQuery(st).parent().find("a").filter(":last");
			if(obj.length > 0){
				lastObj = obj;
			}
		}
	};
	var fnExtractor = {
		relatedEvt: { mouseover: "mouseenter", mouseout: "mouseleave"}
		,getFn: function(evt, obj, strEvt){
			evt.stopPropagation(); // bubble blocking
			var target = evt.target;
			var rtnFn = this.extractFn(evt, target, strEvt);// a tag fn
			if(rtnFn === "NaF"){
				var parentsObj = jQuery(target).parents();
				rtnFn = this.extractFn(evt, parentsObj, strEvt);// parents fn
			}

			return {fn: rtnFn, evt: evt};
		}
		,extractFn: function(evt, obj, strEvt){
			var rtnFn, fn, evtObj, eventsObj, $obj = jQuery(obj);
			execSkip = false;
			try {
				if($obj.get(0).tagName !== "A" && $obj.siblings("a").length > 0){
					evt.stopImmediatePropagation();
					execSkip = true;
					return "NaF";
				}else if($obj.get(0).tagName !== "BUTTON" && $obj.siblings("button").length > 0){
					evt.stopImmediatePropagation();
					execSkip = true;
					return "NaF";
				}
			} catch(e){}

			fn = $obj.attr("on" + strEvt);
			rtnFn = this.chkFn(fn, evt);
			//this.swapEvtType(evt, {focusin:"mouseover", focusout:"mouseout"});

			if(rtnFn === "NaF"){ // for jQuery bined events
				eventsObj = $obj.data("events");
				if(eventsObj && typeof(eventsObj) !== "undefined"){ // exists binded events by jQuery
					evtObj = eventsObj[this.relatedEvt[strEvt]];
					rtnFn = this.chkFn(evtObj, evt);
					this.swapEvtType(evt, {focusin:"mouseenter", focusout:"mouseleave"});

					if(rtnFn === "NaF"){
						evtObj = eventsObj[strEvt];
						rtnFn = this.chkFn(evtObj, evt);
						this.swapEvtType(evt, {focusin:"mouseover", focusout:"mouseout"});
					}
				}
			}
			return rtnFn;
		}
		/* focus in, out을 mouseenter, mouseleavel, mouseover, mouseout으로 변경 */
		,swapEvtType: function(evt, swapObj){
			var type = evt.type, evtType = swapObj[type];

			if("focusin,focusout".indexOf(type) >= 0){
				evt.type = swapObj[type];
			}
		}
		,chkFn: function(fn, evt){
			var rtnVal = "NaF", objType = typeof(fn);
			if(objType === "function"){
				rtnVal = fn;

			}else if(fn !== null && objType === "object"){
				try {
					rtnVal = fn[0].handler;
				}catch (e){}
			}
			return rtnVal;
		}
	};
	return {
		setSelector: function(st){
			eventHandler.setEvent(st);
		}
	};
})();
HeaderComm.flexibleResize = (function(){
	try {

		var $html = jQuery("html");

		if(jQuery.browser.version=="6.0"){
			$html.removeClass("fiexible_resize");
		}else{

			var adjustSize = function(){
				var isFlexible = true, lastB = true, tmp;
				var _class = $html.attr("class");
				if(jQuery(window).width() > 1220){
					if(_class === ""){
						$html.addClass("fiexible_resize");
					}
				}else{
					if(_class !== ""){
						$html.removeClass("fiexible_resize");
					}
				};
			}

			adjustSize();

			jQuery(window).bind("resize", function(){
				adjustSize();
			});
		}
	} catch(e){}
})();
function getCommaString(val){
	var pVal = val + "";
	if(val == undefined || val == "" || !IsNumeric(val)) return 0;
	if(pVal.length > 3){
		var result = "";
		for (var i = pVal.length, j = 0; i >= 0; i--, j++){
			if(i != pVal.length && i%3 == 0 && i != 0){
				result += ",";
			}
			result += pVal.charAt(j);
		}
		return result;
	}else{
		return pVal;
	}
}

HeaderComm.hashControler = (function(){

	//무조건 추가
	var insert = function(value){
		if(document.location.hash){
			if(document.location.hash === "#$$"){
				document.location.hash += value;
			}else{
				document.location.hash += "$$" + value;
			}
		}else{
			document.location.hash = "#" + value;
		}

	};

	//기존에 key로 등록된 값이 있으면 제거 후 추가
	var upsert = function(key, value){
		if(document.location.hash){
			var historyText = document.location.hash.replace("#","");
			if(historyText.indexOf(key) > -1){
				var historyArr = historyText.split("$$");
				var changeText = "";
				for(var index=0; index < historyArr.length; index++){
					if(historyArr[index].indexOf(key) > -1){
						if(index == 0){
							changeText += key + "%%" + value;
						}else{
							changeText += "$$" + key + "%%" + value;
						}
					}else{
						if(index == 0){
							changeText += historyArr[index];
						}else{
							changeText += "$$" + historyArr[index];
						}
					}
				}
				document.location.hash = "#" + changeText;
			}else{
				document.location.hash += "$$" + key + "%%" + value;
			}
		}else{
			document.location.hash = "#" + key + "%%" + value;
		}
	};

	var remove = function(value){
		if(document.location.hash){
			var hashVal = document.location.hash;
			var valueArray = hashVal.split("$$");
			var replaceArray = new Array();
			if(valueArray.length > 1){
				for(var idx=0; idx < valueArray.length; idx++){
					if(valueArray[idx] != value){
						replaceArray.push(valueArray[idx]);
						continue;
					}
				}
				document.location.hash = "#" + replaceArray.join("$$");
			}else{
				document.location.hash = "";
			}
		}
	};

	var check = function(){

		if(document.location.hash){
			var hashVal = document.location.hash.replace(/#/g, "");
			var objArr = hashVal.split("$$");
			if(hashVal != "searchlist" && objArr.length > 0){
				var lnbSearch = false;
				for(var idx=0; idx < objArr.length; idx++){
					var data = objArr[idx];
					var dataArr = data.split("%%");
					if(dataArr.length > 1){
						if(dataArr[0] === "id"){
							jQuery("#" + dataArr[1]).parent("label").addClass("checked");
							jQuery("#" + dataArr[1]).attr("checked", true);
							var selectedText = jQuery("#" + dataArr[1]).parent("label").text();
							var selectedValue = jQuery("#" + dataArr[1]).val();
							var selectedSbj = jQuery("#" + dataArr[1]).closest("div.def_schconts", "#smartfilter_wrap").find("h3").text();
							jQuery("#selectedAttrDiv").show();
							jQuery("button[name=clearBtn]").before("<span class=\"ch_attr\" name=\"selectedAttr\" value=\"" + selectedValue + "\" key=\"" + dataArr[1] + "\" kwd=\"N\">" + selectedSbj + "-" + selectedText + "<button type=\"button\" name=\"deleteBtn\">삭제</button></span>");
							lnbSearch = true;
						}else if(dataArr[0] === "smtId"){
							jQuery("#" + dataArr[1]).parent("label").addClass("checked");
							jQuery("#" + dataArr[1]).attr("checked", true);
							jQuery("#" + dataArr[1]).parents("li[name=smtItem]").removeClass("selected").addClass("selected");
							var selectedText = jQuery("#" + dataArr[1]).parent("label").text();
							var selectedValue = jQuery("#" + dataArr[1]).val();
							var selectedSbj = jQuery("#" + dataArr[1]).closest("div.def_schconts", "#smartfilter_wrap").find("h3").text();
							jQuery("#selectedAttrDiv").show();
							jQuery("button[name=clearBtn]").before("<span class=\"ch_attr\" name=\"selectedAttr\" value=\"" + selectedValue + "\" key=\"" + dataArr[1] + "\" kwd=\"N\">" + selectedSbj + "-" + selectedText + "<button type=\"button\" name=\"deleteBtn\">삭제</button></span>");
							lnbSearch = true;
						}else{
							jQuery("input[name=" + dataArr[0] + "]", "form").val(dataArr[1]);

							if(dataArr[0] === "sortCd"){
								var $sortCdBtnArr = jQuery("[name=sortCdBtn]", "#searchCondition_wrap");
								$sortCdBtnArr.removeClass("selected");
								$sortCdBtnArr.each(function(){
									if(jQuery(this).attr("code") == dataArr[1]){
										jQuery(this).addClass("selected");
									}
								});

							}else if(dataArr[0] === "viewType"){
								var $viewTypeBtnArr = jQuery("a[name=viewTypeBtn]");
								$viewTypeBtnArr.each(function(){
									var listType = jQuery(this).text();

									if(listType == "리스트형" && dataArr[1] == "L"){
										jQuery(this).attr("className", "list_type_selected");
									}else if(listType == "리스트형" && dataArr[1] != "L"){
										jQuery(this).attr("className", "list_type");
									}else if(listType == "이미지형" && dataArr[1] == "I"){
										jQuery(this).attr("className", "image_type_selected");
									}else if(listType == "이미지형" && dataArr[1] != "I"){
										jQuery(this).attr("className", "image_type");
									}else if(listType == "큰 이미지형" && dataArr[1] == "B"){
										jQuery(this).attr("className", "bigimage_type_selected");
									}else if(listType == "큰 이미지형" && dataArr[1] != "B"){
										jQuery(this).attr("className", "bigimage_type");
									}
								});
							}else if(dataArr[0] === "pageSize"){
								jQuery("span[name=curPageSize]").text(dataArr[1] + "개씩");
							}else if(dataArr[0] === "prdState"){
								jQuery("li[name=prd_state]").removeClass("selected");
								jQuery("input:radio","li[name=prd_state]").attr("checked", false);
								jQuery("#" + dataArr[1]).attr("checked", true);
								jQuery("#" + dataArr[1]).parents("li[name=prd_state]").addClass("selected");
							}else if(dataArr[0] === "pageNum"){
								jQuery("input[name=pageNum]").val(dataArr[1]);
							}else if(dataArr[0] === "partnerFilterHeader"){
							    var $partnerFilterArr = jQuery("#filterdivPartnerBnnr").find("a[class=partnerBnnrFilter]");
								$partnerFilterArr.parents("li[name=ptnrBnnrLi]").removeClass("selected");
								jQuery("div[class=partner_filter]").find("a[name=ptnrBnnrAall]").removeClass("selected");
								
								if("all"==dataArr[1]){// 제휴사필터 전체
									jQuery("div[class=partner_filter]").find("a[name=ptnrBnnrAall]").addClass("selected");
									jQuery("input[name=partnerSellerNos]", "form").val("");
									jQuery("input[name=partnerFilterYN]", "form").val("N");
								}else if("deal"==dataArr[1]){
									jQuery("input[name=partnerSellerNos]", "form").val("");
									jQuery("input[name=partnerFilterYN]", "form").val("Y");
									jQuery("input[name=dealPrdYN]", "form").val("Y");
									
									$partnerFilterArr.parents("li[name=ptnrBnnrLi]").removeClass("selected");
									jQuery("div[class=partner_filter]").find("a[name=dealBnnr]").parent().addClass("selected");
								}else{
									jQuery("input[name=partnerSellerNos]", "form").val(dataArr[1]);
									jQuery("input[name=partnerFilterYN]", "form").val("Y");
									jQuery("#filterdivPartnerBnnr").find("ul[name=ptnrBnnrUlname]").css("display", "none");
									$partnerFilterArr.parents("li[name=ptnrBnnrLi]").removeClass("selected");
								}
								$partnerFilterArr.each(function(){
									if(jQuery(this).attr("value") == dataArr[1]){
										jQuery(this).parents("li[name=ptnrBnnrLi]").addClass("selected");
										jQuery(this).parents("li[name=ptnrBnnrLi]").parents("ul[name=ptnrBnnrUlname]").css("display", "block");
										jQuery("#refreshYn").val("Y");
										jQuery(this).trigger("click");
										jQuery("#refreshYn").val("N");
									}
								});
							}
						}
					}
				}

				//lnb선택해제버튼
				if(lnbSearch){
					jQuery("div[name=deselect_wrap]").show();
				}

				//검색
				try{
					smartFilter.setIsPageMove("Y");
					smartFilter.searchPrd();
				}catch(e){}
			}else{
				document.location.hash = "#$$";
			}
		}
	};

	var clear = function(){
		document.location.href = "#$$";
	};

	return {
		addHash : function(value){
			insert(value);
		},
		updateHash : function(key, value){
			upsert(key, value);
		},
		removeHash : function(value){
			remove(value);
		},
		checkHash : function(){
			setTimeout(function(){
				check();
			}, 500);
		}
	}
})();


HeaderComm.callPvSt = function(code){
	try {
		var uvImg = new Image();
		uvImg.src = '//www.11st.co.kr/pv.st?url=' + code;
	} catch (e){}
}

HeaderComm.isEmpty = function(val){
	if(val === null || typeof val === 'undefined'){
		return true;
	}

	if(typeof val === 'string'){
		if(val.trim() === 'undefined'){
			return true;
		}

		if(val.trim() === ''){
			return true;
		}
	}

	return false;
}

/**
 * targetId : 타켓이 되는 <div>의 id값
 * rows : 한 화면에 나오는 데이터 개수
 * pageNumber : 현재 페이지 번호
 * tots : 전체 데이터 수
 * pageRows : 한 화면에 나오는 페이지 단
*/
HeaderComm.getListPage = function(targetId, formName, rows, pageNumber, tots, pageRows){
	var rowsPerPage = rows;
	var currentPage = pageNumber;
	var totalCount = tots;

	var totalPage = '';
	if(totalCount % rowsPerPage)
		totalPage =  (Math.floor(totalCount / rowsPerPage) + 1);
	else
		totalPage = Math.floor(totalCount / rowsPerPage);

	var pageGroupStart = Math.floor(((currentPage-1) / pageRows)) * pageRows + 1;
	var pageGroupEnd = (pageGroupStart + pageRows -1 >= totalPage) ? totalPage : (pageGroupStart + pageRows - 1);
	if(totalPage <= 0)
		totalPage = 1;

	var prePage = 0;

	var sbuf = '';

	if(pageGroupStart - pageRows > 0){
		sbuf += '<a href="#" onclick="HeaderComm.navigatePage(\'' + formName + '\',1);return false;" class="first"><span>처음목록</span></a>\n';
		sbuf += '<a href="#" onclick="HeaderComm.navigatePage(\'' + formName + '\','+ (pageGroupStart - pageRows)+ ');return false;" class="prev"><span>이전목록</span></a>\n';
	}

	sbuf += '<span>\n';

	for (var i = pageGroupStart; i <= pageGroupEnd; i++)
	{
		if(i == currentPage)
			sbuf += '<strong>' + i + '</strong>\n';
		else
			sbuf += '<a href="#" onclick="HeaderComm.navigatePage(\'' + formName + '\',' + i + ');return false;">' + i + '</a></li>\n';
	}

	sbuf += '</span>\n';

	if(pageGroupStart + pageRows <= totalPage){
		sbuf += '<a href="#" onclick="HeaderComm.navigatePage(\'' + formName + '\','+ (pageGroupStart + pageRows)+ ');return false;" class="next"><span>다음목록</span></a>\n';
		sbuf += '<a href="#" onclick="HeaderComm.navigatePage(\'' + formName + '\','+ (totalPage)+ ');return false;" class="last"><span>마지막목록</span></a>\n';
	}

	jQuery('#' + targetId).removeClass('s_paging').addClass('s_paging').html(sbuf);
}

HeaderComm.navigatePage = function(formNm, pageNumber){
	var formObj = document.forms[formNm];
	formObj.pageNum.value= pageNumber;
	formObj.submit();
}

HeaderComm.directVisitCookie = {};
HeaderComm.setDirectVisitCookie = function(jsonObj){
	// footer data JS에서 주입
	HeaderComm.directVisitCookie = jsonObj;
}

HeaderComm.isDirectVisit = function(){
	try {
		var _xsiteList = HeaderComm.directVisitCookie.XSITE;
		var _xsite = getCookieTmall('XSITE');

		if(_xsite && typeof(_xsiteList) == 'object'){
			_xsite = _xsite.split('^')[0];

			for(var idx = 0; idx < _xsiteList.length; idx++){
				if(_xsite == _xsiteList[idx]){
					return true;
				}
			}
		}
	} catch (ex){}

	try {
		var _partnerCdList = HeaderComm.directVisitCookie.PARTNER_CD;
		var _partnerCd = getCookieTmall('PARTNER_CD');

		if(_partnerCd && typeof(_partnerCdList) == 'object'){
			for(var idx = 0; idx < _partnerCdList.length; idx++){
				if(_partnerCd == _partnerCdList[idx]){
					return true;
				}
			}
		}
	} catch (ex){}
	return false;
}

function getBookMarkYn(){
	var bBookMarkYn = false;
	try{
		if(HeaderComm.isDirectVisit())
			bBookMarkYn = true;
	}catch(e){
		bBookMarkYn = false;
	}finally{
		return bBookMarkYn;
	}
}

/*
 * 링크 속성 정의
 */
HeaderComm.link = {
	target : {
		self : 'self', 
		top : 'top', 
		parent : 'parent', 
		blank : 'blank', 
		newWindow : 'newWindow'
	}
};

/*
 * 미니몰 함수 정의
 */
HeaderComm.MiniMall = {
	gatewayPath : 'gateway', 
	goUrl : function (url, target){
		var tgtUrl = 'https://shop.11st.co.kr/' + url;

		switch (target){
			case HeaderComm.link.target.top :
				top.location.href = tgtUrl;
				break;
			case HeaderComm.link.target.parent :
				parent.location.href = tgtUrl;
				break;
			case HeaderComm.link.target.blank :
			case HeaderComm.link.target.newWindow :
				window.open(tgtUrl);
				break;
			default :
				try {
					if(typeof(target) == 'object'){
						target.location.href = tgtUrl;
					}else{
						window.location.href = tgtUrl;
					}
				} catch (ex){
					window.location.href = tgtUrl;
				}
				break;
		}
	}, 
	goGateway : function(pagePath, paramKey, paramValue, target){
		this.goUrl(this.gatewayPath+'/'+pagePath+'/'+paramKey+'/'+paramValue, target);
	}, 
	getGoPage : function(page){
		var instance = {
			pagePath : page, 
			url :  function (homeUrl, target){
				HeaderComm.MiniMall.goUrl(homeUrl, target);
			}, 
			prdNo : function (prdNo, target){
				HeaderComm.MiniMall.goGateway(this.pagePath, 'prdNo', prdNo, target);
			}, 
			nckNmSeq : function (nckNmSeq, target){
				HeaderComm.MiniMall.goGateway(this.pagePath, 'nckNmSeq', nckNmSeq, target);
			}, 
			memNo : function (memNo, target){
				HeaderComm.MiniMall.goGateway(this.pagePath, 'memNo', memNo, target);
			}
		}
		return instance;
	}
};

// 결과적으로는 shop 으로 redirect 되지만 다른 페이지들에서 onclick 핸들러로 HeaderComm.MiniMall 이 사용되고 있으므로 지우면 안됨
HeaderComm.MiniMall.goHome = HeaderComm.MiniMall.getGoPage('home');
HeaderComm.MiniMall.goDelivery = HeaderComm.MiniMall.getGoPage('delivery');


HeaderComm.callHotClick = function(action, method, prdNoList, ctgrNoList, callback){
	var _conf = {};
	try{
		if(arguments.length ==  1){
			_conf = arguments[0];
		}else{
			_conf.action = action;
			_conf.method = method;
			_conf.prdNoList = prdNoList;
			_conf.ctgrNoList = ctgrNoList;
			_conf.callback = callback;
		}
		_conf.uid = TMCookieUtil.getSubCookie(0, "uid");

		if(!_conf.ctgrNoList){
			jQuery.ajax({
				//todo : url 변경
				url : "//www.11st.co.kr/commons/HeaderAjaxAction.tmall?method=getPrdInfoList&prdNoList=" + _conf.prdNoList+"&callback=?",
				dataType : 'jsonp',
				scriptCharset : 'utf-8',
				success : function(data){
					if(typeof(data) != 'undefined'){
						_conf.prdNoList = data.sPrdNo;
						_conf.ctgrNoList = data.sCtgrNo;
						if(_conf.action =='rm'){
							var img2 = new Image();
							img2.src = "https://ad.hotclick.netinsight.co.kr/hotclick/" 
								+ _conf.action + "-cuki?"
								+ "method=" + _conf.method 
								+ "&prod_no=" + _conf.prdNoList 
								+ "&ctgr_no=" + _conf.ctgrNoList;
						}else{
							var _html = '<iframe title="hotClick" src="//c.hotclick.netinsight.co.kr/hotclick/'
								+ _conf.action + '-cuki#'
								+ 'method=' + _conf.method
								+ '&prod_no=' + _conf.prdNoList
								+ '&ctgr_no=' + _conf.ctgrNoList
								+ '" width="0" height="0" frameborder="0"></iframe>';
							jQuery('body').append(_html);
						}
					}//end if
				}, 
				complete : function (){
					if(typeof(_conf.callback) != 'undefined'){
						_conf.callback();
					}
				}
			});
		}else{
			if(_conf.action =='rm'){
				var img2 = new Image();
				img2.src = "https://ad.hotclick.netinsight.co.kr/hotclick/" 
					+ _conf.action + "-cuki?"
					+ "method=" + _conf.method 
					+ "&prod_no=" + _conf.prdNoList 
					+ "&ctgr_no=" + _conf.ctgrNoList;
			}else{
				var _html = '<iframe title="hotClick" src="//c.hotclick.netinsight.co.kr/hotclick/'
                     + _conf.action + '-cuki#'
                     + 'method=' + _conf.method
                     + '&prod_no=' + _conf.prdNoList
                     + '&ctgr_no=' + _conf.ctgrNoList
                     + '" width="0" height="0" frameborder="0"></iframe>';
				jQuery('body').append(_html);
			}
			if(typeof(_conf.callback) != 'undefined'){
				_conf.callback();
			}
		}

	}catch(ex){
		if(typeof(_conf.callback) != 'undefined'){
			_conf.callback();
		}
	}
}

HeaderComm.Product = {
	doTracking : function(prdNo, trcNo, typCd, areaCd, isCPC, clickCd, clickObj, minorSelCnYn){
		if(typeof (trcNo) != 'undefined' && typeof (typCd) != 'undefined' && typCd != '' && typeof (areaCd) != 'undefined' && areaCd != ''){
			HeaderComm.Product.doAdTracking(prdNo, trcNo, typCd, areaCd, isCPC, clickObj, minorSelCnYn);
		}
		
		HeaderComm.Product.doInflowTracking(prdNo);
		
		if(clickObj){
            HeaderComm.Product.doColosseoClickLink(clickObj);

			//if(typeof rakeLog !== 'undefined')
                //rakeLog.sendRakeLog(clickObj);
			HeaderComm.Product.goElementTargetUrl(clickObj);
		}
	},
	doAdTracking : function(prdNo, trcNo, typCd, areaCd, isCPC, clickObj, minorSelCnYn){
		ad_headerCommonJs.util.instance.ConversionCookieQueue.add(trcNo,prdNo, typCd + areaCd);
		stck(typCd, areaCd, trcNo);

		if(isCPC){
			if(minorSelCnYn === 'N'){
				if(funcCheckIsLogin() && !funcCheckIsMinor()){
					adSave.ins.clickCPC(typCd, areaCd, trcNo);
				}
			}else{
				adSave.ins.clickCPC(typCd, areaCd, trcNo);
			}
		}
	},
	goElementTargetUrl : function(clickObj){
		var url = '';
		var target = '';
		if(clickObj){
			var tmpObjUrl = clickObj.getAttribute('href');
			var tmpTarget = clickObj.getAttribute('target');
			if(tmpObjUrl != null && tmpObjUrl != '' && tmpObjUrl.indexOf('javascript:') < 0 && tmpObjUrl.indexOf('#') < 0){
				url = tmpObjUrl;
			}
			
			if(tmpTarget != null && tmpTarget != '' && tmpTarget.indexOf('_') > -1){
				target = tmpTarget;
			}
			if(url != ''){
				if(typeof (target) != 'undefined' && target == '_parent'){
					setTimeout(function(){ parent.location.href = url; } , 100);
				}else if(typeof (target) != 'undefined' && target == '_top'){
					setTimeout(function(){ top.location.href = url; } , 100);
				}else if(typeof (target) != 'undefined' && target == '_blank'){	
					setTimeout(function(){ 
						var prdWidnow = window.open(url,target); 
						prdWidnow.focus(); 
					} , 100);
				}else{
					setTimeout(function(){ window.location.href = url; } , 100);
				}
			}
		}
	},
	doInflowTracking : function(prdNo){
		if(HeaderComm.Product.isTotalSearchPage() && HeaderComm.Product.getSearchKeyword()){
			var url = 'https://st.11st.co.kr/srch.st?kwd='+HeaderComm.Product.getSearchKeyword()+'&prdNo='+prdNo+'&ch=pc&noCache='+(new Date()).getTime();
			var img = new Image();
			img.src = url;
		}
	},
	isTotalSearchPage : function(){
		var url = document.URL;
		return url.indexOf("https://search.11st.co.kr/SearchPrdAction.tmall?method=getTotalSearchSeller") != -1;
	},
    doColosseoClickLink : function(clickObj){
        var clickLinkUrl = clickObj.getAttribute('data-colosseo-clickLog');
        if(clickLinkUrl != null){
            var img = new Image();
            img.src = clickLinkUrl;
        }
    }
}

HeaderComm.CommonLog = {
	doClick : function(inflowClfCd, trcNo, dispObjNo, areaClfCd, areaSubClfCd, listSortSeq, pageSize, pageNum, listSortClfCd, dispObjClfCd){
		var inflowKeyVal = '';
		
		if(inflowClfCd == '01'){ //카테고리
			inflowKeyVal = jQuery('input[name="dispCtgrNo"]').val();
		}else if(inflowClfCd == '02'){ //검색
			inflowKeyVal = encodeURIComponent(document.searchForm.kwd.value);
		}

		if(areaSubClfCd == 'Y') areaSubClfCd = '01';
		else if(areaSubClfCd == 'N') areaSubClfCd = '02';
		
		if(areaSubClfCd == '01' || areaSubClfCd == '02' || areaSubClfCd == '05'){
			listSortClfCd = (typeof listSortClfCd  === 'undefined' || listSortClfCd === '') ? jQuery("input[name='sortCd']").val() : listSortClfCd;
		}
		
		listSortSeq = (pageNum-1) * pageSize + listSortSeq;
		
		if(typeof dispObjClfCd === 'undefined'){
			dispObjClfCd = '01';
		}
		
		jQuery.ajax({
			url : '/log/CommonLogAjaxAction.tmall?method=clickInfoLog',
			type: 'GET',
			timeout: 2000,
			dataType : 'json',
			data: {
				  'inflowKeyVal' : inflowKeyVal	// 대상번호 : 카테고리 번호 / 키워드명
				, 'inflowClfCd' : inflowClfCd	// 대상구분코드(카테고리/키워드 구분 코드)
				, 'trcNo' : trcNo			// TRC_NO
				, 'dispObjNo' : dispObjNo			// 전시대상번호(상품번호)
				, 'dispObjClfCd' : dispObjClfCd		// 전시대상구분코드 : 01(상품)
				, 'svcClfCd' : '01'			// 서비스구분코드   : [DI254] pc 01 / 모바일 02 / app 03
				, 'pageClfCd' : inflowClfCd	// 페이지구분코드   : [DI255] 카테고리 리스팅 / 검색결과 리스팅
				, 'areaClfCd' : areaClfCd		// 영역구분코드     : [DI258] 일반리스팅 / 통합리스팅
				, 'areaSubClfCd' : areaSubClfCd	// 영역상세구분코드 : [DI256] 플러스상품 01 / 일반상품 02 / 추천상품 03 / HOT클릭상품 04 / 파워상품 05
				, 'listSortClfCd' : listSortClfCd	// 리스트정렬구분코드
				, 'listSortSeq' : listSortSeq	// 리스트정렬순번
			}
		});
		
	}
}

HeaderComm.checkFromMobile = function(){
	try {
		var _userAgent 	= navigator.userAgent;
		var _arrPassHeaderStrck = [
			'SAMSUNG-', 'SHW-', 'SCH-', 'SPH-', 'SGH-', 'LG-', 'CANU', 'IM-', 'EV-', 'iPhone', 'Nokia', 'BlackBerry', 
			'lgtelecom', 'NATEBrowser', 'SonyEricsson', 'Mobile' ,'Server_KO_SKT' ,'POLARIS', 'Sony', 'Android'
		];
		for (var idx = 0; idx < _arrPassHeaderStrck.length; idx++){
			if(_userAgent.indexOf(_arrPassHeaderStrck[idx]) != -1){
				return true;
			}
		}
		return false;
	} catch (ex){
		return false;
	}
}

//var isMobile = HeaderComm.checkFromMobile();
var isMobile = false;
if(_browser.indexOf('mobile') != -1)	{
	isMobile = true;
}

(function(skp11){
	'use strict';
	skp11.common = skp11.common || {};
	skp11.common = {
		blankImage: function(imageObj, imageInfo){
			imageObj.onerror = null; // To avoid endless loop.
			imageObj.src = this.getImagePath(imageInfo);
		},
		getImagePath: function(imageInfo){
			var rect, imagePath;
			
			if(typeof imageInfo === 'number'){
				rect = imageInfo + 'x' + imageInfo;
				imagePath = '//i.011st.com/ex_t/R/' + rect + '/1/85/1/src/img/product/no_image.gif';
			}else{
				imagePath = imageInfo;
			}
			
			return imagePath;
		}
	};
})(window.skp11 = window.skp11 || {});

HeaderComm.rake = {
		eventId : {PRODUCT: 'PRODUCT', CATALOG: 'CATALOG'},
		action : {VIEW : 'view', CLICK :'click'}
	}

/********* inc_header_v7.js *********/
/**
 * @deprecated
 * gnb 로직 삭제
 * */
var HeaderGnb = {};

HeaderGnb.getChannel = function(){
	var url = document.URL;
	if(url.indexOf('//www.11st.co.kr/browsing/BrandHomeAction') != -1 || url.indexOf('//www.11st.co.kr/browsing/BrandSearchAction') != -1 || url.indexOf('&gnbType=brand11') != -1){
		return 'BRAND11';
	}else if(url.indexOf('www.11st.co.kr/mart/') != -1 || url.indexOf('&gnbType=mart') != -1){
		return 'MART';
	}else if(url.indexOf('deal.11st.co.kr') != -1){
	 	return 'DEAL';
	}else if(url.indexOf('soho.11st.co.kr') != -1){
	 	return 'SOHO';
	}else if(url.indexOf('DTAction.tmall?ID=STARSOHO') != -1 || url.indexOf('DTAction.tmall?ID=TOPSOHO') != -1 || url.indexOf('DTAction.tmall?ID=FASHIONDNA') != -1 || url.indexOf('DTAction.tmall?ID=KOREASPA') != -1 ||url.indexOf('DTAction.tmall?ID=MISSY') != -1){
		return 'SOHO';
	}else if(url.indexOf('tour.11st.co.kr/html/vertical/tourMain.html') != -1 || url.indexOf('tour.11st.co.kr/tour/') != -1 || typeof(TOUR_HEADER) != 'undefined'){
	 	return 'TOUR';
	}else if(url.indexOf('www.11st.co.kr/html/HyundaiDepart.html') != -1 || url.indexOf('HyundaiDeptAction.tmall') != -1){
	 	return 'DEPARTHD';
	}else if(url.indexOf('FashionDept') != -1){
	 	return 'DEPARTFS';
	}else if(url.indexOf('shop.11st.co.kr') != -1){
	 	return 'SHOP';
	}else if(url.indexOf('ticket.11st.co.kr') != -1){
	 	return 'TICKET';
	}else if(url.indexOf('books.11st.co.kr') != -1){
	 	return 'BOOKS';
	}else{
		return '11ST';
	}
};
HeaderGnb.search = function(){};
HeaderGnb.makeGnb = {
	area : '',
	gnbDealIntroduceBnr : {'count':0,'items':[]},
	gnbDealEmergencyBnrPrd : {'count':0,'items':[]},
	gnbNowIntroduceBnr : {'count':0,'items':[]},
	gnbNowOnSalePrd : {'count':0,'items':[]},
	gnbNowExhiBnr : {'count':0,'items':[]},
	gnbNowCtgr : {'count':0,'items':[]},
	templateType : 'sub',
	isLogin : funcCheckIsLogin(),
	channel : HeaderGnb.getChannel(),
	areaCodePre : 'MAINS',
    grand_11Days_Gnb_Yn : 'N',
    grand_11Days_Festival_Gnb_Yn : 'N',
    grand_11Days_Gnb_link_url : "https://www.11st.co.kr/browsing/MallPlanDetail.tmall?method=getMallPlanDetail&planDisplayNumber=2018694",
	grand_11Days_Gnb_Festival_link_url : "https://www.11st.co.kr/browsing/MallPlanDetail.tmall?method=getMallPlanDetail&planDisplayNumber=2018551",

	setData : function(){

		var self = this;

        var protocol = document.location.protocol;
        var url = "https://www.11st.co.kr/commons/HeaderAjaxAction.tmall?method=get11DaysYn";
        if(protocol == "https:"){
            url = "https://www.11st.co.kr/commons/HeaderAjaxAction.tmall?method=get11DaysYn";
        }

		jQuery.ajax({
            url : url,
            type : 'post',
            dataType : 'json',
            async : false,
            timeout: 1000,
            success : function (data){
            	if(data != null || data != '' || typeof(data) != 'undefined'){
                    self.grand_11Days_Gnb_Yn = data.grand_11Days_Gnb_Yn;
            		self.grand_11Days_Festival_Gnb_Yn = data.grand_11Days_Festival_Gnb_Yn;
                    self.grand_11Days_Gnb_link_url = data.grand_11Days_Gnb_link_url;
                    self.grand_11Days_Gnb_Festival_link_url = data.grand_11Days_Gnb_Festival_link_url;
                }
            }
        });

		if(typeof(gnbDealIntroduceBnr) != 'undefined' && gnbDealIntroduceBnr != ''){
			this.gnbDealIntroduceBnr = gnbDealIntroduceBnr; 
		}
		if(typeof(gnbDealEmergencyBnrPrd) != 'undefined' && gnbDealEmergencyBnrPrd != ''){
			this.gnbDealEmergencyBnrPrd = gnbDealEmergencyBnrPrd; 
		}
		if(typeof(gnbNowIntroduceBnr) != 'undefined' && gnbNowIntroduceBnr != ''){
			this.gnbNowIntroduceBnr = gnbNowIntroduceBnr; 
		}
		if(typeof(gnbNowOnSalePrd) != 'undefined' && gnbNowOnSalePrd != ''){
			this.gnbNowOnSalePrd = gnbNowOnSalePrd; 
		}
		if(typeof(gnbNowExhiBnr) != 'undefined' && gnbNowExhiBnr != ''){
			this.gnbNowExhiBnr = gnbNowExhiBnr; 
		}
		if(typeof(gnbNowCtgr) != 'undefined' && gnbNowCtgr != ''){
			this.gnbNowCtgr = gnbNowCtgr; 
		}
	},

	headerUtilDraw: function(){},
	headerThemeNaviOn: function(){},
	init: function(){},
}

function getAltTxt(etcText, titleText){
    if(!isNaN(etcText)){
    	etcText = etcText.toString();
    }
    if(etcText == null || etcText.trim() == '' || etcText.trim() == 'undefined' || (typeof etcText == 'undefined')){
        return titleText;
    }else{
        return etcText;
    }
}

/**
 * @deprecated
 * HeaderGnb 로직 삭제
 * */
HeaderGnb.categoryNavi_v2 = {
	$allLayerWrap :  '',
	$allLayerCont : '',
	allLayerLoaded : false,
	area : 'main',
	areaCodePre : 'MAINS',

	//메타 그룹별 레이어
	makeGrpCtgrLayer : function(grpIdx){
		var _this = this;
		var $layerWrap = jQuery('#lnb_cate_layer' + (grpIdx+1));
		var $layerCont = jQuery('.box_category', $layerWrap);
		var $layerCont2 = jQuery('<div class="box_rel"></div>');
		var $layerCont3 = jQuery('<div class="cate_visbox" data-log-actionid-area="lnb_banner" data-log-actionid-label="banner"></div>');
		var categoryContents = [];
		var categoryContents2 = [];
		var categoryContents3 = [];

		var codeIdx = (grpIdx+2) >= 10 ?(grpIdx+2) : '0' + (grpIdx+2);
		
		var metaCtgrGroupCount = 0;
		
		var $firstGroup = jQuery('<div/>');
		
		//카테고리
		var grpData = eval('FooterData.lCtgrGrp2016_' + (grpIdx+1));
		if((grpIdx+1) == 12){
			grpData = FooterData.globalLCtgrList2016;
		}
		if(grpData != undefined){
			var lv1CtgrCnt = 0;
			var lv1CtgrDisp1LineMaxCnt = 13;	//1줄에 보여줄수 있는 대카 최고 개수.
			var lv2CtgrCnt = 0;
			var lv2CtgrDisp1LineMaxCnt = 15;	//1줄에 보여줄수 있는 중카 최고 개수.
			
			var lnbMenuLi = jQuery('#lnbMenu > ul > li');
			var isForeign = false;
			if(jQuery(lnbMenuLi[grpIdx]).hasClass('foreign')){
				isForeign = true;
			}
			
			var lv1CtgrLinkUrl = '';
			var $content = jQuery('<strong class="tit_sort">카테고리</strong>');
			categoryContents.push($content);
			$content = jQuery('<ul class="list_category"/>');
			var subCateId;
			var subCateUlId;
			for(var idx = 0 ; idx < grpData.length ; idx++){
				var data = grpData[idx];
				var ctgrLv;
				if(data.CtgrLv){
					ctgrLv = data.CtgrLv;
				}else if(data.Level){
					ctgrLv = data.Level;
				}
				
				var ctgrNo;
				var ctgrNm;
				if(ctgrLv === 1){
					if(data.CtgrNo){
						ctgrNo = data.CtgrNo;
					}else if(data.DispCtgrNo){
						ctgrNo = data.DispCtgrNo
					}

					if(data.CtgrNm){
						ctgrNm = data.CtgrNm;
					}else if(data.DispCtgrNm){
						ctgrNm = data.DispCtgrNm
					}
					
					if(lv1CtgrCnt == lv1CtgrDisp1LineMaxCnt){
						categoryContents.push($content);
						$content = jQuery('<ul class="list_category"/>');
					}
					var displayStyle = ''; 
					if(isForeign == false){
						lv1CtgrLinkUrl = 'https://www.11st.co.kr/html/category/' + ctgrNo + '.html';
					}else if(isForeign == true){
						if(ctgrNo == 476017){//DLUXURY11 처리
							lv1CtgrLinkUrl = 'https://www.11st.co.kr/disp/DTAction.tmall?ID=DLUXURY11';
						}else if(ctgrNo == 8286){//DLUXURY11 처리
							lv1CtgrLinkUrl = 'https://www.11st.co.kr/html/category/' + ctgrNo + '.html';
							displayStyle = 'display:none;';
						}else{
							lv1CtgrLinkUrl = 'https://www.11st.co.kr/browsing/DisplayCategory.tmall?method=getDisplayCategory2Depth&dispCtgrNo=' + ctgrNo;
						}
					}
					
					subCateId = (ctgrNo+'_sub_cate');
					subCateUlId = (ctgrNo+'_sub_cate_'+0);
					$content.append('<li data-log-actionid-area="lnb_nav" data-log-actionid-label="large_category"><a href="' + lv1CtgrLinkUrl + '" class="link_cont" data-ga-event-category="PC_LNB 카테고리 탐색" data-ga-event-action="대카테고리" data-ga-event-label="' + ctgrNm + '" data-ga-Dimension84="PCLNB_TEST_B" data-log-body="{\'content_no\':\''+ ctgrNo +'\', \'content_name\':\''+ ctgrNm +'\', \'content_type\':\'CATEGORY\'}" data-log-index="' +(lv1CtgrCnt+1)+ '">' + ctgrNm + '</a><div class="sub_cate" id="' + subCateId + '" style="width:140px;' + displayStyle + '"><ul class="list_sub_cate" id="' + subCateUlId + '"/></div></li>');
					lv1CtgrCnt++;
					lv2CtgrCnt = 0;

				}else if(ctgrLv === 2){
					if(lv2CtgrDisp1LineMaxCnt <= lv2CtgrCnt){
						subCateUlId = (ctgrNo+'_sub_cate_' + parseInt(lv2CtgrCnt/lv2CtgrDisp1LineMaxCnt))
						if(jQuery('#'+subCateUlId, $content).length == 0){
							jQuery('#'+subCateId, $content).append('<ul class="list_sub_cate" id="' + subCateUlId + '"/>');
						}
						jQuery('#'+subCateId, $content).css({ width :  140 * (parseInt(lv2CtgrCnt/lv2CtgrDisp1LineMaxCnt)+1)});
					}
					jQuery('#'+subCateUlId, $content).append(this.setCtgrNmStyle(data, isForeign));
					jQuery('#'+subCateUlId+' > li:last-child > a', $content).attr('data-log-index', lv2CtgrCnt+1);
					lv2CtgrCnt++;
				}
			}
			
			categoryContents.push($content);
			
			//통계코드
			jQuery('ul > li', $content).bind('click', function(){
				doCommonStat(_this.areaCodePre + 'CG'+codeIdx+'02');
			});
			
			//추천카테고리
			var dispCnt = 6;
			var remainExtraDispCnt = 6;	//"추천카테고리+전문관/브랜드"의 남는 공간에 추가 노출되는 카테고리 수
			var recommendCtgr = eval('FooterData.recommendCtgrGrp2016_' + (grpIdx+1));
			if(recommendCtgr != undefined && recommendCtgr.length != 0){
				var $recommandArea = jQuery('<div class="cate_related">');
				$recommandArea.append('<strong class="tit_sort">테마 편집샵</strong>').append('<ul class="list_recommend"/>');
				for(var idx = 0 ; idx < recommendCtgr.length && idx < dispCnt ; idx++){
					var data = recommendCtgr[idx];
					
					jQuery('ul:last-child', $recommandArea).append('<li data-log-actionid-area="lnb_nav" data-log-actionid-label="theme_category"><a href="https://www.11st.co.kr/browsing/DisplayCategory.tmall?method=getThemeCategory&dispCtgrNo=' + data.RefCtgrNo + '" data-ga-event-category="PC_LNB 카테고리 탐색" data-ga-event-action="추천카테고리" data-ga-event-label="' + data.CtgrNm + '" data-ga-Dimension84="PCLNB_TEST_B" data-log-body="{\'content_no\':\''+ data.RefCtgrNo +'\', \'content_name\':\''+ data.CtgrNm +'\', \'content_type\':\'CATEGORY\'}" data-log-index="' + (idx+1) + '">' + data.CtgrNm + '</a></li>');
					remainExtraDispCnt--;
				}
				categoryContents2.push($recommandArea);
				
				//통계코드
				jQuery('ul > li', $specialShopArea).bind('click', function(){
					doCommonStat(_this.areaCodePre + 'CG'+codeIdx+'06');
				});
				
			}
			
			//전문관/브랜드
			var gnbCtgrMallList = eval('FooterData.gnbCtgrMallList' + (grpIdx+1));
			if(gnbCtgrMallList != undefined && gnbCtgrMallList.length != 0){
				var $specialShopArea = jQuery('<div class="cate_related">');
				var ctgrListLength = 0;
				for(var idx = 0 ; idx < gnbCtgrMallList.length ; idx++){
					var data = gnbCtgrMallList[idx];
					var ctgrList = data.ctgrList;
					ctgrListLength = ctgrList.length;
					$specialShopArea.append('<strong class="tit_sort">'+ data.title.DispObjNm +'</strong>').append('<ul class="list_specialshop"/>');
					for(var ctgrIdx = 0 ; ctgrIdx < ctgrList.length && ctgrIdx < (dispCnt + remainExtraDispCnt) ; ctgrIdx++){
						jQuery('ul:last-child', $specialShopArea).append('<li data-log-actionid-area="lnb_nav" data-log-actionid-label="special_category"><a href="'+ctgrList[ctgrIdx].DispObjLnkUrl+'" data-ga-event-category="PC_LNB 카테고리 탐색" data-ga-event-action="전문관/브랜드" data-ga-event-label="' + ctgrList[ctgrIdx].DispObjNm + '" data-ga-Dimension84="PCLNB_TEST_B" data-log-body="{\'content_no\':\''+ ctgrList[ctgrIdx].DispObjNo +'\', \'content_name\':\''+ ctgrList[ctgrIdx].DispObjNm +'\', \'content_type\':\'CATEGORY\'}" data-log-index="' + (ctgrIdx+1) + '">' + ctgrList[ctgrIdx].DispObjNm + '</a></li>');
					}
				}
				if(ctgrListLength > 0){
					categoryContents3.push($specialShopArea);
				}
				
				//통계코드
				jQuery('ul > li', $specialShopArea).bind('click', function(){
					doCommonStat(_this.areaCodePre + 'CG'+codeIdx+'06');
				});
				
			}
			
			if(categoryContents && categoryContents.length > 0){
				metaCtgrGroupCount = categoryContents.length;
				
				for(var metaIdx = 0; metaIdx < metaCtgrGroupCount; metaIdx++){
					$firstGroup.append(categoryContents[metaIdx]);
				}
				
				if($firstGroup.children().length > 0){
					$layerCont.append($firstGroup);
				}
			}
			if(categoryContents2 && categoryContents2.length > 0){
				metaCtgrGroupCount = categoryContents2.length;
				
				for(var metaIdx = 0; metaIdx < metaCtgrGroupCount; metaIdx++){
					$layerCont2.append(categoryContents2[metaIdx]);
				}
				
				if(metaCtgrGroupCount > 0){
					$layerWrap.append($layerCont2);
				}
			}
			if(categoryContents3 && categoryContents3.length > 0){
				metaCtgrGroupCount = categoryContents3.length;
				
				for(var metaIdx = 0; metaIdx < metaCtgrGroupCount; metaIdx++){
					$layerCont2.append(categoryContents3[metaIdx]);
				}
				
				if(metaCtgrGroupCount > 0){
					$layerWrap.append($layerCont2);
				}
			}
			
			if((categoryContents2.length + categoryContents3.length) >= 1 && lv1CtgrCnt > 13){
				$layerWrap.css({ width : 510 });
			}

			//LNB 배너
			var lnbBannerDisplaySpaceNos = [521257982, 521257983, 521257984, 521257985, 521257986, 521257987, 521257988, 521257989, 521257990, 521257991, 521257992, 521257993];
			var lnbBannerDisplaySpaceNo = lnbBannerDisplaySpaceNos[grpIdx];
			var mainLnbBanner = eval('FooterData.mainLnbBanner' + (grpIdx+1));
			if(mainLnbBanner != undefined && mainLnbBanner.length != 0){
				var data = mainLnbBanner[0];
				var metaCtgrNm = jQuery('strong.tit_category', $layerWrap).text();
				var linkUrl = data.banner.DispObjLnkUrl;
				var n = linkUrl.indexOf('planDisplayNumber');
				var rakeLogBody = "{'content_type':'BANNER', 'content_no':'" + linkUrl.substring(n+18) + "', 'link_url':'" + linkUrl + "', 'trc_no':'" + lnbBannerDisplaySpaceNo + "', 'position_l1':'" + (grpIdx+1) + "'}";
				$layerCont3.append('<a href="' + linkUrl + '" class="cate_link" data-ga-event-category="PC_LNB 카테고리 탐색" data-ga-event-action="메타별 배너" data-ga-event-label="' + metaCtgrNm + '_' + data.banner.DispObjNm + '" data-ga-Dimension84="PCLNB_TEST_B" data-log-body="' + rakeLogBody + '"><img src="' + _SSL_UPLOAD_URL_ + data.banner.LnkBnnrImgUrl + '" alt="' + data.banner.DispObjNm + '"></a>');
				$layerWrap.append($layerCont3);
			}
		}else{	//전시카테고리가 없을 경우. 메타 추천카테고리.
			var lnbMenuLi = jQuery('#lnbMenu > ul > li');
			if(jQuery(lnbMenuLi[grpIdx]).hasClass('recommand')){
				$layerWrap = jQuery('#lnbMenu > ul > li.recommand > div');
				jQuery('.tit_category', $layerWrap).hide();
				$layerCont = jQuery('.set_recommand', $layerWrap);
				var boxListCnt = 0;
				var themeEditShopList = eval('FooterData.themeEditShopList');
				if(themeEditShopList != undefined){
					var $recommendCtgrArea = jQuery('<div class="box">');
					for(var idx = 0 ; idx < themeEditShopList.length ; idx++){
						$recommendCtgrArea = jQuery('<div class="box">');
						var data = themeEditShopList[idx];
						var ctgrList = data.list;
						$recommendCtgrArea.append('<strong class="subject">' + data.title + '</strong>').append('<div class="cont"/>');
						var recommendDispIndex = 0;
						for(var ctgrIdx = 0 ; ctgrIdx < ctgrList.length ; ctgrIdx++){
							if(ctgrList[ctgrIdx].linkUrl2 != ''){
								if(recommendDispIndex % 10 == 0){
									jQuery('.cont:last-child', $recommendCtgrArea).append('<ul class="box_list"/>');
									boxListCnt++;
								}
								recommendDispIndex++;
								
								jQuery('ul:last-child', $recommendCtgrArea).append('<li data-log-actionid-area="lnb_nav" data-log-actionid-label="alltheme_category"><a href="'+ctgrList[ctgrIdx].linkUrl2+'" data-ga-event-category="PC_LNB 카테고리 탐색" data-ga-event-action="추천카테고리_전시구좌" data-ga-event-label="' + ctgrList[ctgrIdx].title1 + '" data-ga-Dimension84="PCLNB_TEST_B" data-log-body="{\'content_no\':\''+ ctgrList[ctgrIdx].dispObjNo +'\', \'content_name\':\''+ ctgrList[ctgrIdx].title1 +'\', \'content_type\':\'CATEGORY\'}" data-log-index="' +(ctgrIdx+1)+ '"><span class="thumb"><img src="'+ctgrList[ctgrIdx].imageUrl1+'" onError="javascript:this.src=\'' +_IMG_URL_+ '/img/prd_size/noimg_100.gif\';" alt=""></span>' + ctgrList[ctgrIdx].title1 + '</a></li>');
							}
						}
						categoryContents.push($recommendCtgrArea);
					}
					
					//통계코드
					jQuery('ul > li', $recommendCtgrArea).bind('click', function(){
						doCommonStat(_this.areaCodePre + 'CG'+codeIdx+'06');
					});
					
				}
				if(categoryContents && categoryContents.length > 0){
					metaCtgrGroupCount = categoryContents.length;
					
					for(var metaIdx = 0; metaIdx < metaCtgrGroupCount; metaIdx++){
						$firstGroup.append(categoryContents[metaIdx]);
					}
					
					if($firstGroup.children().length > 0){
						$layerCont.append($firstGroup);
						$layerWrap.append($layerCont);
					}
				}
				
				$layerWrap.css({ width : (180 * boxListCnt) + (metaCtgrGroupCount - 1) });
			}
		}

        window.rakeLog && window.rakeLog.scrollHandler();
		
		jQuery(document).ready(function(){
			try {
				jQuery("a", $layerWrap).each(function(idx, obj){
					jQuery(obj).bind('click', function(){
						catchAnchorGAToEvent();
					});
				});
			} catch(e){
			}
		});
	}
}

if(typeof Handlebars !== 'undefined'){
	// HeaderGnb.drawTemplate 함수 내부에서 선언하는 Handlebars.registerHelper 살리기
	Handlebars.registerHelper('last', function (index, count, options){
		if(index+1 == count){
			return options.fn(this);
		}else{
			return options.inverse(this);
		}
	});
	Handlebars.registerHelper('pageNum', function (index, pagePerCnt){
		var page = parseInt(parseInt(index) / parseInt(pagePerCnt)) + 1;
		return page;
	});
	Handlebars.registerHelper('pageDot', function (index, pagePerCnt, options){
		var page = parseInt(parseInt(index) / parseInt(pagePerCnt)) + 1;
		var pageOri = parseInt(index) / parseInt(pagePerCnt) + 1;
		if(page == pageOri){
			return options.fn(this);
		}else{
			return options.inverse(this);
		}
	});
}

// StartPageManager.init 에서 쿠키 TT 에 CONN_IP_LOC|(FOR or DOM) 쿠키를 생성한다.
StartPageManager.init();

var FooterComm = {};
if(typeof(FooterData) === "undefined") FooterData = {};

// recopick
FooterComm.recopick = function(){
	var process = {
		like : 'like', 
		search : 'search'
	}

	var domain = {
		common : '11st.co.kr', 
		deal : 'deal.11st.co.kr'
	}

	var sendData = function(paramObj){
		if(paramObj && paramObj.process && paramObj.process == "view"){
				return;
		}

		var data = {
			url: document.location.href, 
			ref: document.referrer
		}

		if(paramObj.mid){
			data.b = getRecopickUserInfo(paramObj.mid);
		}

		if(paramObj.items){
			data.items = paramObj.items;
		}

		if(paramObj.q){
			data.q = paramObj.q;
		}

		jQuery.ajax({
			url: 'https://api.recopick.com/v1/logs/' + paramObj.process + '/' + paramObj.domain + '/' + TMCookieUtil.getCookie('PCID'), 
			method: 'POST', 
			dataType: 'jsonp', 
			data: data
		});
	}

	return {
		'process' : process, 
		'domain' : domain, 
		'execute' : function(paramObj){
			sendData(paramObj);
		}
	}
}();

// Nethru
function isIEBrowser(){
	var agent = navigator.userAgent.toLowerCase();
	return (navigator.appName === 'Netscape' && agent.indexOf('trident') !== -1) || (agent.indexOf("msie") !== -1);
}


function genUUID(){
	return 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'.replace(/[x]/g, function(c){
		var r = Math.random() * 16 | 0;
		var v = ((c === 'x') ? r : (r & 0x3 | 0x8));

		return v.toString(16);
});
}

var uuid = genUUID();

function Nethru_getCookieVal(offset){
	var endstr = document.cookie.indexOf (";", offset);
	if(endstr == -1)
		endstr = document.cookie.length;
	return unescape(document.cookie.substring(offset, endstr));
}

function Nethru_SetCookie(name, value){
	var argv = Nethru_SetCookie.arguments;
	var argc = Nethru_SetCookie.arguments.length;
	var expires = (2 < argc) ? argv[2] : null;
	var path = (3 < argc) ? argv[3] : null;
	var domain = (4 < argc) ? argv[4] : null;
	var secure = (5 < argc) ? argv[5] : false;

	expires = ((expires == null) ?
			(isIEBrowser() ? "" : "; expires=0") : ("; expires=" + expires.toGMTString()));
	path = ((path == null) ? "" : ("; path=" + path));
	domain = ((domain == null) ? "" : ("; domain=" + domain));
	secure = ((secure == true) ? "; secure" : "");

	document.cookie = name + "=" + escape (value) + expires  + path + domain + secure;
}

function Nethru_GetCookie(name){
	var arg = name + "=";
	var alen = arg.length;
	var clen = document.cookie.length;
	var i = 0;

	while (i < clen){
 		var j = i + alen;
 		if(document.cookie.substring(i, j) == arg)
    			return Nethru_getCookieVal (j);

 		i = document.cookie.indexOf(" ", i) + 1;
 		if(i == 0)
    			break;
 	}

	return null;
}

function Nethru_makePersistentCookie(name,length,path,domain){
	var today = new Date();
	var expiredDate = new Date(new Date().getTime() + 20 * 365 * 24 * 3600 * 1000);
	var cookie;
	var value;

	cookie = Nethru_GetCookie(name);
	if(cookie){		//이미 존재하는지 확인
   		return 1;
	}

	var values = new Array();
	for (i=0; i < length ; i++){
		values[i] = "" + Math.random();
	}

	value = today.getTime();

	// use first decimal
	for (i=0; i < length ; i++){
		value += values[i].charAt(2);
	}

	Nethru_SetCookie(name,value,expiredDate,path,domain);
}

function Nethru_getDomain(){
	var _host   = document.domain;
	var so = _host.split('.');
	var dm  = so[so.length-2] + '.' + so[so.length-1];

	return (so[so.length-1].length == 2) ? so[so.length-3] + '.' + dm : dm;
}

function Nethru_makeSessionCookie(name, value, path, domain){
	var cookie = Nethru_GetCookie(name);

	if(cookie)
			return 1;

	Nethru_SetCookie(name, value, null, path, domain);
}

var Nethru_domain  = Nethru_getDomain();
Nethru_makePersistentCookie("PCID",10,"/",Nethru_domain);
Nethru_makeSessionCookie("XSRF-TOKEN", uuid, "/", Nethru_domain);