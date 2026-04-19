/**
 * YC INSULATION GEO 自动跳转
 * 根据访问者IP地理位置自动跳转到对应语言版本
 * 
 * 语言映射：
 * - CN (中国) → index.html (中文)
 * - US/UK/CA/AU/NZ → index-en.html (英文)
 * - KR (韩国) → index-ko.html (韩文)
 * - VN (越南) → index-vi.html (越南文)
 * - TH (泰国) → index-th.html (泰文)
 * - ID (印尼) → index-id.html (印尼文)
 * - TR (土耳其) → index-tr.html (土耳其文)
 * - SA/AE/QA/KW/BH/OM/EG/MA/DZ/TN/LY/IQ/JO/LB/SY/PS/YE → index-ar.html (阿拉伯文)
 * - 其他 → index-en.html (默认英文)
 */

(function() {
    'const GEO_REDIRECT_VERSION = '1.0.0';
    const STORAGE_KEY = 'yc_geo_redirected';
    const GEO_DATA_KEY = 'yc_geo_data';
    const CACHE_DURATION = 24 * 60 * 60 * 1000; // 24小时缓存

    // 语言页面映射
    const COUNTRY_LANGUAGE_MAP = {
        'CN': '',              // 中国 → 默认中文（index.html）
        'TW': '-en',           // 台湾 → 英文
        'HK': '-en',           // 香港 → 英文
        'US': '-en',           // 美国 → 英文
        'GB': '-en',           // 英国 → 英文
        'CA': '-en',           // 加拿大 → 英文
        'AU': '-en',           // 澳大利亚 → 英文
        'NZ': '-en',           // 新西兰 → 英文
        'IE': '-en',           // 爱尔兰 → 英文
        'ZA': '-en',           // 南非 → 英文
        'PH': '-en',           // 菲律宾 → 英文
        'SG': '-en',           // 新加坡 → 英文
        'MY': '-en',           // 马来西亚 → 英文
        'IN': '-en',           // 印度 → 英文
        'KR': '-ko',           // 韩国 → 韩文
        'VN': '-vi',           // 越南 → 越南文
        'TH': '-th',           // 泰国 → 泰文
        'ID': '-id',           // 印尼 → 印尼文
        'TR': '-tr',           // 土耳其 → 土耳其文
        // 阿拉伯语国家
        'SA': '-ar',           // 沙特
        'AE': '-ar',           // 阿联酋
        'QA': '-ar',           // 卡塔尔
        'KW': '-ar',           // 科威特
        'BH': '-ar',           // 巴林
        'OM': '-ar',           // 阿曼
        'EG': '-ar',           // 埃及
        'MA': '-ar',           // 摩洛哥
        'DZ': '-ar',           // 阿尔及利亚
        'TN': '-ar',           // 突尼斯
        'LY': '-ar',           // 利比亚
        'IQ': '-ar',           // 伊拉克
        'JO': '-ar',           // 约旦
        'LB': '-ar',           // 黎巴嫩
        'SY': '-ar',           // 叙利亚
        'PS': '-ar',           // 巴勒斯坦
        'YE': '-ar',           // 也门
        'IR': '-ar',           // 伊朗
    };

    // 当前页面语言（从URL推断）
    function getCurrentLanguage() {
        const path = window.location.pathname;
        if (path.includes('index-en.html') || path.endsWith('/en/')) return 'en';
        if (path.includes('index-ko.html') || path.endsWith('/ko/')) return 'ko';
        if (path.includes('index-vi.html') || path.endsWith('/vi/')) return 'vi';
        if (path.includes('index-th.html') || path.endsWith('/th/')) return 'th';
        if (path.includes('index-id.html') || path.endsWith('/id/')) return 'id';
        if (path.includes('index-tr.html') || path.endsWith('/tr/')) return 'tr';
        if (path.includes('index-ar.html') || path.endsWith('/ar/')) return 'ar';
        return 'zh'; // 默认中文
    }

    // 获取目标语言后缀
    function getTargetLanguageSuffix(countryCode) {
        return COUNTRY_LANGUAGE_MAP[countryCode] || '-en'; // 默认英文
    }

    // 检查是否已重定向过
    function hasRedirected() {
        const redirected = sessionStorage.getItem(STORAGE_KEY);
        return redirected === 'true';
    }

    // 标记已重定向
    function markRedirected() {
        sessionStorage.setItem(STORAGE_KEY, 'true');
    }

    // 获取缓存的地理位置数据
    function getCachedGeoData() {
        const cached = localStorage.getItem(GEO_DATA_KEY);
        if (!cached) return null;

        try {
            const data = JSON.parse(cached);
            const now = Date.now();
            if (now - data.timestamp < CACHE_DURATION) {
                return data;
            }
        } catch (e) {
            console.error('Failed to parse cached geo data:', e);
        }
        return null;
    }

    // 缓存地理位置数据
    function cacheGeoData(countryCode) {
        localStorage.setItem(GEO_DATA_KEY, JSON.stringify({
            countryCode: countryCode,
            timestamp: Date.now()
        }));
    }

    // 执行重定向
    function redirectToLanguage(targetSuffix) {
        const targetPage = targetSuffix === '' ? 'index.html' : `index${targetSuffix}.html`;
        
        // 如果当前已经在目标页面，不重定向
        const currentLang = getCurrentLanguage();
        const targetLang = targetSuffix === '' ? 'zh' : targetSuffix.replace('-', '');
        if (currentLang === targetLang) {
            console.log('[GEO] Already on correct language page:', currentLang);
            return;
        }

        console.log('[GEO] Redirecting to:', targetPage);
        markRedirected();
        window.location.href = targetPage;
    }

    // 使用 ipapi.co 获取地理位置（免费API，1000次/月）
    async function getGeoByIP() {
        try {
            const response = await fetch('https://ipapi.co/json/', {
                method: 'GET',
                headers: {
                    'Accept': 'application/json'
                }
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const data = await response.json();
            return data.country_code;
        } catch (error) {
            console.error('[GEO] Failed to get location by IP:', error);
            return null;
        }
    }

    // 备用方案：使用浏览器语言
    function getLanguageFromBrowser() {
        const browserLang = navigator.language || navigator.userLanguage;
        const langCode = browserLang.split('-')[0].toLowerCase();
        
        console.log('[GEO] Browser language:', browserLang, '→', langCode);
        
        // 浏览器语言映射
        const browserLangMap = {
            'zh': '',      // 中文
            'en': '-en',   // 英文
            'ko': '-ko',   // 韩文
            'vi': '-vi',   // 越南文
            'th': '-th',   // 泰文
            'id': '-id',   // 印尼文
            'tr': '-tr',   // 土耳其文
            'ar': '-ar',   // 阿拉伯文
        };
        
        return browserLangMap[langCode] || '-en';
    }

    // 主函数
    async function initGeoRedirect() {
        console.log('[GEO] Initializing geo redirect v' + GEO_REDIRECT_VERSION);

        // 如果已经重定向过，跳过
        if (hasRedirected()) {
            console.log('[GEO] Already redirected in this session, skipping');
            return;
        }

        // 检查URL参数，如果指定了语言，跳过自动重定向
        const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.has('lang')) {
            console.log('[GEO] Language specified in URL, skipping auto redirect');
            markRedirected();
            return;
        }

        // 尝试使用缓存
        const cachedData = getCachedGeoData();
        if (cachedData) {
            console.log('[GEO] Using cached geo data:', cachedData.countryCode);
            const targetSuffix = getTargetLanguageSuffix(cachedData.countryCode);
            redirectToLanguage(targetSuffix);
            return;
        }

        // 获取IP地理位置
        const countryCode = await getGeoByIP();
        
        if (countryCode) {
            console.log('[GEO] Detected country:', countryCode);
            cacheGeoData(countryCode);
            const targetSuffix = getTargetLanguageSuffix(countryCode);
            redirectToLanguage(targetSuffix);
        } else {
            // 备用方案：使用浏览器语言
            console.log('[GEO] Failed to detect country, using browser language');
            const targetSuffix = getLanguageFromBrowser();
            redirectToLanguage(targetSuffix);
        }
    }

    // 页面加载后执行
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initGeoRedirect);
    } else {
        initGeoRedirect();
    }
})();
